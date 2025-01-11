from django.shortcuts import render
from .forms import UserRegister

users = ["Ann", "Ksiu", "Masha", "Kate"]  # Псевдо-список существующих пользователей


def sign_up_by_django(request):
    info = {}
    if request.method == "POST":
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            repeat_password = form.cleaned_data["repeat_password"]
            age = form.cleaned_data["age"]

            if password == repeat_password and age >= 18 and username not in users:
                info["message"] = f"Приветствуем, {username}!"
            else:
                if password != repeat_password:
                    info["error"] = "Пароли не совпадают"
                elif age < 18:
                    info["error"] = "Вы должны быть старше 18"
                elif username in users:
                    info["error"] = "Пользователь уже существует"
        else:
            info["error"] = "Форма не валидна. Пожалуйста, проверьте введенные данные."

    else:
        form = UserRegister()  # Создаем пустую форму

    return render(request, "fifth_task/registration_page.html", {'form': form, **info})


def sign_up_by_html(request):
    info = {}
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        repeat_password = request.POST.get("repeat_password")
        age = int(request.POST.get("age"))
        if password == repeat_password and age >= 18 and username not in users:
            info = {"message": f"Приветствуем, {username}!"}
            return render(request, "fifth_task/registration_page.html", info)
        else:
            if password != repeat_password:
                info["error"] = "Пароли не совпадают"
            elif age < 18:
                info["error"] = "Вы должны быть старше 18"
            elif username in users:
                info["error"] = "Пользователь уже существует"
    return render(request, "fifth_task/registration_page.html", info)

