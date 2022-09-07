import re
import sys
from django.utils.timezone import localtime, now, timedelta, localdate,  get_default_timezone_name
from django.shortcuts import render, redirect, HttpResponse
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from .models import CustomUser, Competition, Determined, Task
from django.contrib.auth.hashers import check_password
from .forms import CustomUserCreationFrom, CustomUserChangeFrom, PasswordChangeForm, CreateCompetitionForm
from django.contrib.auth import login, logout
from django.views.generic import DetailView, UpdateView

import subprocess

from pathlib import Path
import os
BASE_DIR = Path(__file__).resolve().parent.parent

silence = False

#------------------------internal functions------------------------#
def check_changes(request):
    # Проверяем пустые ли поля или заняты они или имеют пробелы
    # УДАЛИТЬ
    if re.search('[а-яА-Я]', request.POST.get('username')):
        error = "Кирилицу нельзя"
        return error
    elif (request.POST.get('username').strip() == "") and (request.POST.get('email').strip()  == ""):
        error = "Поля пустые"
        return error
    # Переделать что бы ошибки были отдельно ПЕРЕДЕЛАТЬ
    elif (CustomUser.objects.filter(username=request.POST.get('username')).exists() and request.POST.get('username') != request.user.username) or (CustomUser.objects.filter(email=request.POST.get('email')).exists() and request.POST.get('email') != request.user.email):
        error = "Такое имя или почта уже занято"
        return error
        # email = request.POST.get('email')
        # nickname = request.POST.get('username')
        # # нужно ли мне эти ероры спросить артема
        # if CustomUser.objects.filter(username=nickname).exists():
        #     error_username = "Данное имя уже занято"
        # if CustomUser.objects.filter(email=email).exists():
        #     error_email = "Данный адрес электронной почты уже занято"
    # УДАЛИТЬ
    elif (" " in request.POST.get('username').strip()) or (" " in request.POST.get('email').strip()):
        error = "Пробелов не должно быть в полях"
        return error
    error = ""
    return error
#------------------------------------------------------------------#

def Index (request):
    return render(request, 'main/home.html')

def Account_REDIR (request):
    if not request.user.is_authenticated:
        return redirect('login')
    return redirect('account', request.user.slug)

def Rating (request):
    user = CustomUser.objects.order_by('rating')
    user = user.reverse()[:len(user)-1]
    return render(request, 'main/top.html', {'user': user})

class AccountDetailView(DetailView):
    model = CustomUser
    template_name = 'main/user_page.html'
    context_object_name = 'form'

def CreateCompetition (request):
    error = ''
    if not request.user.is_authenticated:
        return redirect('login')
    if request.method == 'POST':
        form = CreateCompetitionForm(request.POST)
        print('hi')
        if form.is_valid():
            print('hi')
            form.save()
        else:
            print('hi22')
            error = '1'
    form = CreateCompetitionForm()
    content = {
        'error': error
    }
    return render(request, 'main/create_competition.html', content)
    
def Competition_page(request, id):
    error = ''
    if not request.user.is_authenticated:
        return redirect('login')
    comp = Competition.objects.get(id = id)
    if comp.start_time > now():
        return redirect('home')
    content = {
        'error': error,
        'comp': comp
    }
    print(comp.tasks.all())
    return render(request, 'main/сompetition.html', content)

def Task_page(request, id, task):
    error = ''
    comp = Competition.objects.get(id = id)
    if comp.start_time > now():
        return redirect('home')
    task = comp.tasks.get(id = task)
    print(Determined.objects.filter(successfully = True).order_by('points').filter(determined_users = request.user))
    if request.user in task.determined_users.all():
        print("reshil")
    else:
        print('loh')
    if not request.user.is_authenticated:
        return redirect('login')
    if request.method == 'POST':
        if comp.actual:
            # Если отправлена задание
            if "test" in request.POST:
                # Если отправили файл
                if request.FILES:
                    # Если отключена погрешность пробелов
                    if task.soft:
                        # Получаем загруженный файл
                        file = request.FILES['file']
                        fs = FileSystemStorage()
                        # Сохраняем на файловой системе, решаем и удаляем
                        filename = fs.save(file.name, file)
                        # Функция которая будет декодировать ответ файла в нормальный
                        encoding = sys.getdefaultencoding()
                        # Если прописано много запусков, то создаем списки с различными запусками
                        if '/br' in task.input_values:
                            inptvals = task.input_values.strip().split("/br")
                            ouptvals = task.output_values.strip().split("/br")
                            more = True
                            b = False
                        # Создаем "текст" который будем подовать в полученую программу
                        else:
                            target = task.input_values.strip()
                            more = False
                        # Запускаем циклом если несколько запусков
                        if more:
                            for i in range(len(inptvals)):
                                try:
                                    checkruncode = subprocess.run(['python.exe', f"{BASE_DIR}/main{fs.url(filename)}"], input=bytes(inptvals[i].strip(), encoding='utf8'), timeout=1)
                                    if checkruncode.returncode == 0:
                                        runcode = subprocess.check_output(['python.exe', f"{BASE_DIR}/main{fs.url(filename)}"], input=bytes(inptvals[i].strip(), encoding='utf8'))
                                        if ouptvals[i].strip() == runcode.decode(encoding).strip():
                                            print('fff')
                                        else:
                                            DUser = Determined.objects.create(time = now(), points = 0, successfully = False, error = f'Не верный ответ, запуск {i+1}')
                                            DUser.determined_users.add(request.user)
                                            task.determined_users.add(DUser)
                                            print('error, run', i+1, 'of', len(inptvals))
                                            b = True
                                            break
                                    else:
                                        DUser = Determined.objects.create(time = now(), points = 0, successfully = False, error = 'Не удалось получить ответ от программы')
                                        DUser.determined_users.add(request.user)
                                        task.determined_users.add(DUser)
                                        print('returncode != 0')
                                except subprocess.TimeoutExpired as e:
                                    DUser = Determined.objects.create(time = now(), points = 0, successfully = False, error = 'Время испольнения превышело ограничение')
                                    DUser.determined_users.add(request.user)
                                    task.determined_users.add(DUser)
                                    print('Gg')
                                    break
                            else:
                                if not b:
                                    DUser = Determined.objects.create(time = now(), points = 0, successfully = True, error = '-')
                                    DUser.determined_users.objects.set(request.user)
                                    task.determined_users.add(DUser)
                        # Иначе запускаем одним разом
                        elif not more:
                            try:
                                checkruncode = subprocess.run(['python.exe', f"{BASE_DIR}/main{fs.url(filename)}"], input=bytes(target, encoding='utf8'), timeout=1)
                                if checkruncode.returncode == 0:
                                    runcode = subprocess.check_output(['python.exe', f"{BASE_DIR}/main{fs.url(filename)}"], input=bytes(target, encoding='utf8'))
                                    if task.output_values.strip() == runcode.decode(encoding).strip():
                                        DUser = Determined.objects.create(time = now(), points = 0, successfully = True, error = '-')
                                        DUser.determined_users.objects.set(request.user)
                                        task.determined_users.add(DUser)
                                        print(True)
                                    else:
                                        DUser = Determined.objects.create(time = now(), points = 0, successfully = False, error = f'Не верный ответ, запуск 1')
                                        DUser.determined_users.add(request.user)
                                        task.determined_users.add(DUser)
                                        print(print('error, run one'))
                                else:
                                    DUser = Determined.objects.create(time = now(), points = 0, successfully = False, error = 'Не удалось получить ответ от программы')
                                    DUser.determined_users.add(request.user)
                                    task.determined_users.add(DUser)
                                    print('returncode != 0')
                            except subprocess.TimeoutExpired as e:
                                DUser = Determined.objects.create(time = now(), points = 0, successfully = False, error = 'Время испольнения превышело ограничение')
                                DUser.determined_users.add(request.user)
                                task.determined_users.add(DUser)
                                print('Gg')
                        # Если ошибка
                        else:
                            print("error")
                        # Удаляем файл
                        # ПЕРЕМЕННАЯ
                        fs.delete(file.name)
                    else:
                        # Получаем загруженный файл
                        file = request.FILES['file']
                        fs = FileSystemStorage()
                        # Сохраняем на файловой системе, решаем и удаляем
                        filename = fs.save(file.name, file)
                        # Функция которая будет декодировать ответ файла в нормальный
                        encoding = sys.getdefaultencoding()
                        # Если прописано много запусков, то создаем списки с различными запусками
                        if '/br' in task.input_values:
                            inptvals = task.input_values.strip().split("/br")
                            ouptvals = task.output_values.strip().split("/br")
                            listoutput = []
                            for i in range(len(ouptvals)):
                                listoutput.append(list(map(str, ouptvals[i].strip().split())))
                            more = True
                            b = False
                        # Создаем "текст" который будем подовать в полученую программу
                        else:
                            target = task.input_values.strip()
                            answer = list(map(str, task.output_values.strip().split()))
                            more = False
                        # Запускаем циклом если несколько запусков
                        if more:
                            for i in range(len(listoutput)):
                                try:
                                    checkruncode = subprocess.run(['python.exe', f"{BASE_DIR}/main{fs.url(filename)}"], input=bytes(inptvals[i].strip(), encoding='utf8'), timeout=1)
                                    if checkruncode.returncode == 0:
                                        runcode = subprocess.check_output(['python.exe', f"{BASE_DIR}/main{fs.url(filename)}"], input=bytes(inptvals[i].strip(), encoding='utf8'))
                                        if listoutput[i] == list(map(str, runcode.decode(encoding).strip().split())):
                                            print('fff')
                                        else:
                                            DUser = Determined.objects.create(time = now(), points = 0, successfully = False, error = f'Не верный ответ, запуск {i+1}')
                                            DUser.determined_users.add(request.user)
                                            task.determined_users.add(DUser)
                                            print('error, run', i+1, 'of', len(inptvals))
                                            b = True
                                            break
                                    else:
                                        DUser = Determined.objects.create(time = now(), points = 0, successfully = False, error = 'Не удалось получить ответ от программы')
                                        DUser.determined_users.add(request.user)
                                        task.determined_users.add(DUser)
                                        print('returncode != 0')
                                except subprocess.TimeoutExpired as e:
                                    DUser = Determined.objects.create(time = now(), points = 0, successfully = False, error = 'Время испольнения превышело ограничение')
                                    DUser.determined_users.add(request.user)
                                    task.determined_users.add(DUser)
                                    print('Gg')
                                    break
                            else:
                                if not b:
                                    DUser = Determined.objects.create(time = now(), points = 0, successfully = True, error = '-')
                                    DUser.determined_users.objects.set(request.user)
                                    task.determined_users.add(DUser)
                        # Иначе запускаем одним разом
                        elif not more:
                            try:
                                checkruncode = subprocess.run(['python.exe', f"{BASE_DIR}/main{fs.url(filename)}"], input=bytes(target, encoding='utf8'), timeout=1)
                                if checkruncode.returncode == 0:
                                    runcode = subprocess.check_output(['python.exe', f"{BASE_DIR}/main{fs.url(filename)}"], input=bytes(target, encoding='utf8'))
                                    if answer == list(map(str, runcode.decode(encoding).strip().split())):
                                        DUser = Determined.objects.create(time = now(), points = 0, successfully = True, error = '-')
                                        DUser.determined_users.add(request.user)
                                        task.determined_users.add(DUser)
                                        print(True)
                                    else:
                                        DUser = Determined.objects.create(time = now(), points = 0, successfully = False, error = 'Не верный ответ, запуск 1')
                                        DUser.determined_users.add(request.user)
                                        task.determined_users.add(DUser)
                                        print('error, run one')
                                else:
                                    DUser = Determined.objects.create(time = now(), points = 0, successfully = False, error = 'Не удалось получить ответ от программы')
                                    DUser.determined_users.add(request.user)
                                    task.determined_users.add(DUser)
                                    print('returncode != 0')
                            except subprocess.TimeoutExpired as e:
                                DUser = Determined.objects.create(time = now(), points = 0, successfully = False, error = 'Время испольнения превышело ограничение')
                                DUser.determined_users.add(request.user)
                                task.determined_users.add(DUser)
                                print('Gg')
                        # Если не верно
                        else:
                            print("neverno")
                        # Удаляем файл
                        fs.delete(file.name)
                # УДАЛИТЬ
                else:
                    pass
        else:
            pass
    content = {
        'error': error,
        'comp': comp,
        'task': task,
    }
    return render(request, 'main/task.html', content)

def Reg_page (request):
    if request.user.is_authenticated:
        return redirect('account', request.user.slug)
    error = ""
    error_username = ""
    error_email = ""
    if request.method == 'POST':
        form = CustomUserCreationFrom(request.POST)
        email = request.POST.get('email')
        nickname = request.POST.get('username')
        # нужно ли мне эти ероры спросить артема
        if CustomUser.objects.filter(username=nickname).exists():
            error_username = "Данное имя уже занято"
        if CustomUser.objects.filter(email=email).exists():
            error_email = "Данный адрес электронной почты уже занято"
        # Потом это надо будет удалить УДАЛИТЬ
        if (request.POST.get('username').strip() == "") or (request.POST.get('email').strip()  == ""):
            error = "Заполните все поля"
        # УДАЛИТЬ
        if re.search('[а-яА-Я]', nickname):
            error_username = "Кирилицу нельзя"
        # Если форма коректна, то она сохраняется
        elif form.is_valid():
            formsv = form.save()
            login(request, formsv)
            request.user.slug = request.user.username
            request.user.save()
            return redirect('accountREDIR')
        # УДАЛИТЬ
        elif error_email == "" and error_username == "":
            error = "Неизвестная нам ошибка"

    form = CustomUserCreationFrom()
    content = {
        'error': error,
        'error_username': error_username,
        'error_email': error_email
    }
    return render(request, 'main/registration_form.html', content)

def AccountUpdate (request):
    if not request.user.is_authenticated:
        return redirect('login')
    # Вывод ошибки
    error = ''
    # Если метод пост 
    if request.method == 'POST':
        # Если отправлена форма редактирования пользователя
        if "editbtn" in request.POST:
            # Если отправили изображение
            if request.FILES:
                # Не помню
                formaccedit = CustomUserChangeFrom(request.POST, request.FILES)
                error = check_changes(request)
                # ПЕРЕДЕЛАТЬ
                if error != '':
                    pass
                # Если все ок сохраняем
                else:
                    # Проверяем пустые ли поля что бы не сохранить пустое поле
                    if request.POST.get('username').strip() == "":
                        pass
                    else:
                        request.user.username = request.POST.get('username').strip()
                        request.user.slug = request.user.username
                    if request.POST.get('email').strip() == "":
                        pass
                    else:
                        request.user.email = request.POST.get('email').strip()
                    # Получаем загруженный файл
                    file = request.FILES['image']
                    fs = FileSystemStorage()
                    # Сохраняем на файловой системе
                    filename = fs.save(file.name, file)
                    # Получение адреса по которому лежит файл
                    request.user.image = file_url = fs.url(filename)
                    # Сохраняем изменения
                    request.user.save()
                    # Редиректим
                    return redirect('account', request.user.slug)
            # Если не отправили изображение
            else:
                # Не помню
                formaccedit = CustomUserChangeFrom(request.POST)
                error = check_changes(request)
                # ПЕРЕДЕЛАТЬ
                if error != '':
                    pass
                # Если все ок сохраняем
                else:
                    # Проверяем пустые ли поля что бы не сохранить пустое поле
                    if request.POST.get('username').strip() == "":
                        pass
                    else:
                        request.user.username = request.POST.get('username').strip()
                        request.user.slug = request.user.username
                    if request.POST.get('email').strip() == "":
                        pass
                    else:
                        request.user.email = request.POST.get('email').strip()
                    # Сохраняем изменения
                    request.user.save()
                    # Редиректим
                    return redirect('account', request.user.slug)
        # Если нажали кнопку редактирования пароля
        elif "changepswd" in request.POST:
            # Не помню
            formpswdedit = PasswordChangeForm(request.POST)
            # Получаем пароли
            old_password = request.POST.get("old_password")
            pswd1 = request.POST.get("new_password")
            pswd2 = request.POST.get("new_password_repeat")
            # Если все совпадает устанвливаем новый пароль и редиректим
            if check_password(old_password,request.user.password) and pswd1 == pswd2:
                request.user.set_password(pswd1)
                request.user.save()
                return redirect('login')
            # Различные ошибки если форма не верная ПЕРЕДЕЛАТЬ
            elif not check_password(old_password,request.user.password):
                if not silence:
                    error = "Не верный старый пароль"
                else:
                    pass
            elif pswd1 != pswd2:
                error = "Новые пароли не совпадают"
            # УДАЛИТЬ
            else:
                error = "Не известная нам проблема"
        # Если нажали кнопку удалить
        elif "deletbtn" in request.POST:
            request.user.delete()
            return redirect('home')

    content = {
        'error': error
    }
    return render(request, 'main/custom_profile_form.html', content)