from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from .models import CustomUser
from django.contrib.auth.hashers import check_password
from .forms import CustomUserCreationFrom, CustomUserChangeFrom, PasswordChangeForm
from django.contrib.auth import login, logout
from django.views.generic import DetailView, UpdateView 

#------------------------internal functions------------------------#
def test_and_changes(request):
    if (request.POST.get('username').strip() == "") and (request.POST.get('email').strip()  == ""):
        error = "Поля пустые"
    elif (CustomUser.objects.filter(username=request.POST.get('username')).exists() and request.POST.get('username') != request.user.username) or (CustomUser.objects.filter(email=request.POST.get('email')).exists() and request.POST.get('email') != request.user.email):
        error = "Такое имя или почта уже занято"
    elif (" " in request.POST.get('username')) or (" " in request.POST.get('email').strip()):
        error = "Пробелов не должно быть в полях"
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
#------------------------------------------------------------------#

def index (request):
    return render(request, 'main/home.html')

def accountREDIR (request):
    if not request.user.is_authenticated:
        return redirect('login')
    return redirect('account', request.user.slug)

class AccountDetailView(DetailView):
    model = CustomUser
    template_name = 'main/user_page.html'
    context_object_name = 'form'

def reg_page (request):
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
        'form': form,
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
                # Проверяем пустые ли поля или заняты они или имеют пробелы
                # Потом это надо будет удалить УДАЛИТЬ
                if (request.POST.get('username').strip() == "") and (request.POST.get('email').strip()  == ""):
                    error = "Поля пустые"
                # Переделать что бы ошибки были отдельно ПЕРЕДЕЛАТЬ
                elif (CustomUser.objects.filter(username=request.POST.get('username')).exists() and request.POST.get('username') != request.user.username) or (CustomUser.objects.filter(email=request.POST.get('email')).exists() and request.POST.get('email') != request.user.email):
                    error = "Такое имя или почта уже занято"
                    # email = request.POST.get('email')
                    # nickname = request.POST.get('username')
                    # # нужно ли мне эти ероры спросить артема
                    # if CustomUser.objects.filter(username=nickname).exists():
                    #     error_username = "Данное имя уже занято"
                    # if CustomUser.objects.filter(email=email).exists():
                    #     error_email = "Данный адрес электронной почты уже занято"

                # Это надо будет удалить УДАЛИТЬ
                elif (" " in request.POST.get('username')) or (" " in request.POST.get('email').strip()):
                    error = "Пробелов не должно быть в полях"
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
                # Проверяем пустые ли поля или заняты они или имеют пробелы 
                # УДАЛИТЬ
                if (request.POST.get('username').strip() == "") and (request.POST.get('email').strip()  == ""):
                    error = "Поля пустые"
                # Переделать что бы ошибки были отдельно ПЕРЕДЕЛАТЬ
                elif (CustomUser.objects.filter(username=request.POST.get('username')).exists() and request.POST.get('username') != request.user.username) or (CustomUser.objects.filter(email=request.POST.get('email')).exists() and request.POST.get('email') != request.user.email):
                    error = "Такое имя или почта уже занято"
                    # email = request.POST.get('email')
                    # nickname = request.POST.get('username')
                    # # нужно ли мне эти ероры спросить артема
                    # if CustomUser.objects.filter(username=nickname).exists():
                    #     error_username = "Данное имя уже занято"
                    # if CustomUser.objects.filter(email=email).exists():
                    #     error_email = "Данный адрес электронной почты уже занято"
                # УДАЛИТЬ
                elif (" " in request.POST.get('username')) or (" " in request.POST.get('email').strip()):
                    error = "Пробелов не должно быть в полях"
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
            # Различные ошибки если форма не верная
            elif not check_password(old_password,request.user.password):
                error = "Не верный старый пароль"
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