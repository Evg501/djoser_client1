import requests
from django.shortcuts import render, redirect
from django.contrib import messages

DJOSER_API_URL = "http://127.0.0.1:8088/auth/"

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Отправляем запрос на Djoser для получения токена
        #response = requests.post(f"{DJOSER_API_URL}jwt/create/", data={
        #    'username': username,
        #    'password': password
        #})
        response = requests.post(f"{DJOSER_API_URL}token/login/", data={
            'username': username,
            'password': password
        })        

        if response.status_code == 200:
            #token = response.json()['access']
            token = response.json()["auth_token"]
            request.session['auth_token'] = token
            messages.success(request, "Вы вошли в систему.")
            return redirect('profile')
        else:
            messages.error(request, "Неверные учетные данные.")

    return render(request, 'login.html')


def profile_view(request):
    token = request.session.get('auth_token')
    print(token)
    if not token:
        return redirect('login')

    headers = {'Authorization': f'Token {token}'}
    response = requests.get(f"{DJOSER_API_URL}users/me/", headers=headers)
    
    if response.status_code != 200:
        messages.error(request, "Ошибка при получении данных пользователя.")
        return redirect('login')

    user_data = response.json()
    return render(request, 'profile.html', {'user': user_data})


def logout_view(request):
    request.session.flush()
    messages.info(request, "Вы вышли из системы.")
    return redirect('login')