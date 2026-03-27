from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from .forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required

# Kayıt Olma Görünümü
def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "CustomUser olarak kaydınız tamamlandı!")
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'auth/register.html', {'form': form})

# Giriş Yapma Görünümü
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            # Form zaten authenticate yaptı, kullanıcıyı direkt içinden çekelim
            user = form.get_user()
            login(request, user)
            messages.info(request, f"Tekrar hoş geldin, {user.username}!")
            return redirect('home')
        else:
            # Hata varsa terminale yazdıralım ki ne olduğunu görelim
            print("Form hataları:", form.errors)
            messages.error(request, "Kullanıcı adı veya şifre hatalı.")
    else:
        form = AuthenticationForm()
    return render(request, 'auth/login.html', {'form': form})

# Çıkış Yapma
def logout_view(request):
    logout(request)
    messages.warning(request, "Başarıyla çıkış yaptınız.")
    return redirect('home')

def home_view(request):
    return render(request, 'home.html')

@login_required
def profile_view(request):
    # Giriş yapan kullanıcının bilgileri zaten 'request.user' içinde hazır gelir
    return render(request, 'profile.html')