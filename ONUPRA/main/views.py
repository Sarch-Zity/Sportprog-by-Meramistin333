import re
import sys
from django.utils.timezone import localtime, now, timedelta, localdate,  get_default_timezone_name
from django.shortcuts import render, redirect, HttpResponse
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from .models import CustomUser, Competition, Task, Attempt, AttemptTask, Determined, File, Article
from django.contrib.auth.hashers import check_password
from .forms import CustomUserCreationFrom, CustomUserChangeFrom, PasswordChangeForm, CreateCompetitionForm, CustomUserImageChangeFrom, CustomUserUsernameChangeFrom, CreateTaskForm, ArticleForm, FileForm
from django.contrib.auth import login, logout
from django.views.generic import DetailView, UpdateView
from django.db.models import Max

import subprocess

from pathlib import Path
import os
BASE_DIR = Path(__file__).resolve().parent.parent

#------------------------internal functions------------------------#
def check_changes(request, formaccedit):
    # Проверяем пустые ли поля или заняты они или имеют пробелы
    # УДАЛИТЬ
    if re.search('[а-яА-Я]', request.POST.get('username')):
        error = "Кирилицу нельзя"
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
    # elif (" " in request.POST.get('username').strip()) or (" " in request.POST.get('email').strip()):
    #     error = "Пробелов не должно быть в полях"
    #     return error
    if formaccedit.is_valid():
        print("o net")
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

def AccountPage(request, slug):
    try:
        user = CustomUser.objects.get(slug = slug)
    except CustomUser.DoesNotExist as e:
        return redirect('home')
    # если решили обновить аватарку
    if request.method == 'POST' and request.user.is_authenticated:
        if 'reset image' in request.POST:
            request.user.image = 'default.png'
            request.user.save()
            # Редиректим
            return redirect('account', request.user.slug)
        elif 'update image' in request.POST and request.FILES:
            # В форму добавляем инфу которую пользователь добавил
            form = CustomUserImageChangeFrom(request.POST, request.FILES, instance=request.user)
            print(form.errors)
            if form.is_valid():
                form.save()
                return redirect('account', request.user.slug)
        elif 'new post' in request.POST:
            form = ArticleForm(request.POST)
            form2 = FileForm(request.POST, request.FILES)
            if form.is_valid():
                if form2.is_valid(): 
                    article = form.save(commit=False)
                    article.user = request.user
                    article.save()
                    form2.save(commit=False)
                    for i in request.FILES.getlist('files'):
                        File.objects.create(files=i, article=article)
                else:
                    article = form.save(commit=False)
                    article.user = request.user
                    article.save()
                return redirect('account', request.user.slug)
        elif 'change username' in request.POST:
            form = CustomUserUsernameChangeFrom(request.POST, instance=request.user)
            print(form.is_valid())
            if form.is_valid():
                user = form.save(commit=False)
                user.slug = user.username
                user.save()
                return redirect('account', request.user.slug)
    content = {
        'user': user,
        'form': ArticleForm(),
        'form2': FileForm(),
        'articles': Article.objects.filter(user = user)
    }
    return render(request, 'main/user_page.html', content)

def CreateCompetition (request):
    if request.method == 'POST':
        if 'task' in request.POST:
            task_form = CreateTaskForm(request.POST)
            print(request.POST)
            if task_form.is_valid():
                print("eeeee")
                task_form.save()
            else:
                print(task_form.errors)
                print("Nooooo")
        if 'competition' in request.POST:
            comp_form = CreateCompetitionForm(request.POST)
            print(request.POST)
            if comp_form.is_valid():
                print("eeeee")
                comp_form.save()
            else:
                print(comp_form.errors)
                print("Nooooo")
    comp_form = CreateCompetitionForm()
    task_form = CreateTaskForm()
    content = {
        'comp_form': comp_form,
        'task_form': task_form
    }
    return render(request, 'main/create_competition.html', content)

def Competition_view(request):
    if not request.user.is_authenticated:
        return redirect('login')
    comp = Competition.objects.filter(actual = True).order_by('start_time')
    print(comp)
    print(comp[0].id)
    content = {
        'comp': comp,
    }
    return render(request, 'main/competition_view.html', content)


def Competition_page(request, id):
    if not request.user.is_authenticated:
        return redirect('login')
    comp = Competition.objects.get(id = id)
    if comp.start_time > now():
        return redirect('home')
    content = {
        'comp': comp,
    }
    return render(request, 'main/competition.html', content)

def Task_page(request, id, task):
    error = ''
    comp = Competition.objects.get(id = id)
    if comp.start_time > now():
        return redirect('home')
    task = comp.tasks.get(id = task)
    # if request.user in task.determined_users.all():
    #     print("reshil")
    # else:
    #     print('loh')
    if not request.user.is_authenticated:
        return redirect('login')
    if request.method == 'POST':
        if comp.actual:
            # Если отправлена задание
            if "test" in request.POST:
                # Если отправили файл
                if request.FILES:
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
                                    runcode = subprocess.check_output(['python.exe', f"{BASE_DIR}/main{fs.url(filename)}"], input=bytes(inptvals[i].strip(), encoding='utf8'), timeout=1)
                                    if listoutput[i] == list(map(str, runcode.decode(encoding).strip().split())):
                                        print('fff')
                                    else:
                                        atmpt = Attempt.objects.create(time = now(), points = 0, successfully = False, error = f'Не верный ответ, запуск {i+1}', hidden = False)
                                        detuser = comp.determined_users.filter(user=request.user)
                                        print(detuser.exists())
                                        print(detuser)
                                        if detuser.exists():
                                            detuserx = detuser[0].task.filter(task=task)
                                            print(detuserx.exists())
                                            print(detuserx)
                                            if detuserx.exists():
                                                print('dobavil')
                                                detuserx[0].attempts.add(atmpt)
                                            else:
                                                print('sozdal i dobavil')
                                                atmpttsk = AttemptTask.objects.create()
                                                atmpttsk.task.add(task)
                                                atmpttsk.attempts.add(atmpt)
                                                detuser[0].task.add(atmpttsk)
                                        else:
                                            print('nebilo')
                                            atmpttsk = AttemptTask.objects.create()
                                            atmpttsk.task.add(task)
                                            atmpttsk.attempts.add(atmpt)
                                            dtmd = Determined.objects.create()
                                            dtmd.user.add(request.user)
                                            dtmd.task.add(atmpttsk)
                                            comp.determined_users.add(dtmd)
                                        break
                                else:
                                    atmpt = Attempt.objects.create(time = now(), points = 0, successfully = False, error = 'Не удалось получить ответ от программы', hidden = False)
                                    detuser = comp.determined_users.filter(user=request.user)
                                    print(detuser.exists())
                                    print(detuser)
                                    if detuser.exists():
                                        detuserx = detuser[0].task.filter(task=task)
                                        print(detuserx.exists())
                                        print(detuserx)
                                        if detuserx.exists():
                                            print('dobavil')
                                            detuserx[0].attempts.add(atmpt)
                                        else:
                                            print('sozdal i dobavil')
                                            atmpttsk = AttemptTask.objects.create()
                                            atmpttsk.task.add(task)
                                            atmpttsk.attempts.add(atmpt)
                                            detuser[0].task.add(atmpttsk)
                                    else:
                                        print('nebilo')
                                        atmpttsk = AttemptTask.objects.create()
                                        atmpttsk.task.add(task)
                                        atmpttsk.attempts.add(atmpt)
                                        dtmd = Determined.objects.create()
                                        dtmd.user.add(request.user)
                                        dtmd.task.add(atmpttsk)
                                        comp.determined_users.add(dtmd)
                            except subprocess.TimeoutExpired as e:
                                atmpt = Attempt.objects.create(time = now(), points = 0, successfully = False, error = 'Время испольнения превышело ограничение', hidden = False)
                                detuser = comp.determined_users.filter(user=request.user)
                                print(detuser.exists())
                                print(detuser)
                                if detuser.exists():
                                    detuserx = detuser[0].task.filter(task=task)
                                    print(detuserx.exists())
                                    print(detuserx)
                                    if detuserx.exists():
                                        print('dobavil')
                                        detuserx[0].attempts.add(atmpt)
                                    else:
                                        print('sozdal i dobavil')
                                        atmpttsk = AttemptTask.objects.create()
                                        atmpttsk.task.add(task)
                                        atmpttsk.attempts.add(atmpt)
                                        detuser[0].task.add(atmpttsk)
                                else:
                                    print('nebilo')
                                    atmpttsk = AttemptTask.objects.create()
                                    atmpttsk.task.add(task)
                                    atmpttsk.attempts.add(atmpt)
                                    dtmd = Determined.objects.create()
                                    dtmd.user.add(request.user)
                                    dtmd.task.add(atmpttsk)
                                    comp.determined_users.add(dtmd)
                                break
                        else:
                            if not b:
                                # Считаем сколько получилось поинтов за задание
                                timeLeft = comp.duration - int((now() - comp.start_time).total_seconds() // 60)
                                x = timeLeft / comp.duration
                                h = 1
                                k = 0.4
                                y = h * x
                                if y > 1:
                                    y = 1
                                elif y < k:
                                    y = k
                                # Добавляем попытку в бд
                                atmpt = Attempt.objects.create(time = now(), points = task.score*y, successfully = True, error = '-', hidden = False)
                                detuser = comp.determined_users.filter(user=request.user)
                                print(detuser.exists())
                                print(detuser)
                                if detuser.exists():
                                    detuserx = detuser[0].task.filter(task=task)
                                    print(detuserx.exists())
                                    print(detuserx)
                                    if detuserx.exists():
                                        print('dobavil')
                                        detuserx[0].attempts.add(atmpt)
                                    else:
                                        print('sozdal i dobavil')
                                        atmpttsk = AttemptTask.objects.create()
                                        atmpttsk.task.add(task)
                                        atmpttsk.attempts.add(atmpt)
                                        detuser[0].task.add(atmpttsk)
                                else:
                                    print('nebilo')
                                    atmpttsk = AttemptTask.objects.create()
                                    atmpttsk.task.add(task)
                                    atmpttsk.attempts.add(atmpt)
                                    dtmd = Determined.objects.create()
                                    dtmd.user.add(request.user)
                                    dtmd.task.add(atmpttsk)
                                    comp.determined_users.add(dtmd)
                                print(True)
                    # Иначе запускаем одним разом
                    elif not more:
                        try:
                            checkruncode = subprocess.run(['python.exe', f"{BASE_DIR}/main{fs.url(filename)}"], input=bytes(target, encoding='utf8'), timeout=1)
                            if checkruncode.returncode == 0:
                                runcode = subprocess.check_output(['python.exe', f"{BASE_DIR}/main{fs.url(filename)}"], input=bytes(target, encoding='utf8'), timeout=1)
                                if answer == list(map(str, runcode.decode(encoding).strip().split())):
                                    # Считаем сколько получилось поинтов за задание
                                    timeLeft = comp.duration - int((now() - comp.start_time).total_seconds() // 60)
                                    x = timeLeft / comp.duration
                                    h = 1
                                    k = 0.4
                                    y = h * x
                                    if y > 1:
                                        y = 1
                                    elif y < k:
                                        y = k
                                    # Добавляем попытку в бд
                                    atmpt = Attempt.objects.create(time = now(), points = task.score*y, successfully = True, error = '-', hidden = False)
                                    detuser = comp.determined_users.filter(user=request.user)
                                    print(detuser.exists())
                                    print(detuser)
                                    if detuser.exists():
                                        detuserx = detuser[0].task.filter(task=task)
                                        print(detuserx.exists())
                                        print(detuserx)
                                        if detuserx.exists():
                                            print('dobavil')
                                            detuserx[0].attempts.add(atmpt)
                                        else:
                                            print('sozdal i dobavil')
                                            atmpttsk = AttemptTask.objects.create()
                                            atmpttsk.task.add(task)
                                            atmpttsk.attempts.add(atmpt)
                                            detuser[0].task.add(atmpttsk)
                                    else:
                                        print('nebilo')
                                        atmpttsk = AttemptTask.objects.create()
                                        atmpttsk.task.add(task)
                                        atmpttsk.attempts.add(atmpt)
                                        dtmd = Determined.objects.create()
                                        dtmd.user.add(request.user)
                                        dtmd.task.add(atmpttsk)
                                        comp.determined_users.add(dtmd)
                                    print(True)
                                else:
                                    atmpt = Attempt.objects.create(time = now(), points = 0, successfully = False, error = 'Не верный ответ, запуск 1', hidden = False)
                                    detuser = comp.determined_users.filter(user=request.user)
                                    print(detuser.exists())
                                    print(detuser)
                                    if detuser.exists():
                                        detuserx = detuser[0].task.filter(task=task)
                                        print(detuserx.exists())
                                        print(detuserx)
                                        if detuserx.exists():
                                            print('dobavil')
                                            detuserx[0].attempts.add(atmpt)
                                        else:
                                            print('sozdal i dobavil')
                                            atmpttsk = AttemptTask.objects.create()
                                            atmpttsk.task.add(task)
                                            atmpttsk.attempts.add(atmpt)
                                            detuser[0].task.add(atmpttsk)
                                    else:
                                        print('nebilo')
                                        atmpttsk = AttemptTask.objects.create()
                                        atmpttsk.task.add(task)
                                        atmpttsk.attempts.add(atmpt)
                                        dtmd = Determined.objects.create()
                                        dtmd.user.add(request.user)
                                        dtmd.task.add(atmpttsk)
                                        comp.determined_users.add(dtmd)
                                        for l in comp.objects.all():
                                            if l == task:
                                                continue
                                            else:
                                                atmpt1 = Attempt.objects.create(time = now(), points = 0, successfully = False, error = '-', hidden = True)
                                                user = comp.determined_users.get(user = request.user)
                                                atmpttsk1 = AttemptTask.objects.create()
                                                atmpttsk1.task.add(l)
                                                atmpttsk1.attempts.add(atmpt1)
                                                user.task.add(atmpttsk)
                            else:
                                atmpt = Attempt.objects.create(time = now(), points = 0, successfully = False, error = 'Не удалось получить ответ от программы', hidden = False)
                                detuser = comp.determined_users.filter(user=request.user)
                                print(detuser.exists())
                                print(detuser)
                                if detuser.exists():
                                    detuserx = detuser[0].task.filter(task=task)
                                    print(detuserx.exists())
                                    print(detuserx)
                                    if detuserx.exists():
                                        print('dobavil')
                                        detuserx[0].attempts.add(atmpt)
                                    else:
                                        print('sozdal i dobavil')
                                        atmpttsk = AttemptTask.objects.create()
                                        atmpttsk.task.add(task)
                                        atmpttsk.attempts.add(atmpt)
                                        detuser[0].task.add(atmpttsk)
                                else:
                                    print('nebilo')
                                    atmpttsk = AttemptTask.objects.create()
                                    atmpttsk.task.add(task)
                                    atmpttsk.attempts.add(atmpt)
                                    dtmd = Determined.objects.create()
                                    dtmd.user.add(request.user)
                                    dtmd.task.add(atmpttsk)
                                    comp.determined_users.add(dtmd)
                        except subprocess.TimeoutExpired as e:
                            atmpt = Attempt.objects.create(time = now(), points = 0, successfully = False, error = 'Время испольнения превышело ограничение', hidden = False)
                            detuser = comp.determined_users.filter(user=request.user)
                            print(detuser.exists())
                            print(detuser)
                            if detuser.exists():
                                detuserx = detuser[0].task.filter(task=task)
                                print(detuserx.exists())
                                print(detuserx)
                                if detuserx.exists():
                                    print('dobavil')
                                    detuserx[0].attempts.add(atmpt)
                                else:
                                    print('sozdal i dobavil')
                                    atmpttsk = AttemptTask.objects.create()
                                    atmpttsk.task.add(task)
                                    atmpttsk.attempts.add(atmpt)
                                    detuser[0].task.add(atmpttsk)
                            else:
                                print('nebilo')
                                atmpttsk = AttemptTask.objects.create()
                                atmpttsk.task.add(task)
                                atmpttsk.attempts.add(atmpt)
                                dtmd = Determined.objects.create()
                                dtmd.user.add(request.user)
                                dtmd.task.add(atmpttsk)
                                comp.determined_users.add(dtmd)
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
    error_username = False
    error_email = False
    if request.method == 'POST':
        form = CustomUserCreationFrom(request.POST)
        email = request.POST.get('email')
        nickname = request.POST.get('username')
        if CustomUser.objects.filter(username=nickname).exists():
            error_username = True
        if CustomUser.objects.filter(email=email).exists():
            error_email = True
        if re.search('[а-яА-Я]', nickname):
            pass
        # Если форма коректна, то она сохраняется
        elif form.is_valid():
            formsv = form.save()
            login(request, formsv)
            return redirect('accountREDIR')

    form = CustomUserCreationFrom()
    content = {
        'error_username':error_username,
        'error_email':error_email
    }
    return render(request, 'main/registration.html', content)

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
                error = check_changes(request, formaccedit)
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
                error = check_changes(request, formaccedit)
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