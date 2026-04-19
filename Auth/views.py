from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate , login as auth_login, logout ,get_user_model  
from django.contrib.auth.models import User
from django.contrib import messages
import logging
logger = logging.getLogger(__name__)  
User = get_user_model()

def register(request):
    
    if request.method == 'POST':
        email = request.POST.get("email")
        username = request.POST.get("username")
        password = request.POST.get("parol")
        parolni_tasdiqlang = request.POST.get("parolni_tasdiqlang")

        if password != parolni_tasdiqlang:
            messages.error(request, "Parol birhil emas!")
            return redirect('register')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Bu emeil alaqochon mavjud! ")
            return redirect('register')

        user = User.objects.create_user(email=email, username=username, password=password)
        user.save()

        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            messages.success(request, "Siz muvafaqiyatli ro'yhatan o'tdingiz")
            return redirect('home')

        messages.error(request, "Authenticationda xatolik yuz berdi")
        return redirect('register')

    return render(request, 'register.html')
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        next_url = request.GET.get('next', 'home') 

        if not username:
            logger.warning('Foydalanuvchi nomi kiritilmadi.') 
            return render(request, 'login.html', {'error': 'Iltimos, foydalanuvchi nomini kiriting.'})
        
        try:
            user = User.objects.get(username=username)  # Foydalanuvchini username bo‘yicha tekshirish
            if user.is_superuser:  # Agar u admin boladigon bolsa
                auth_login(request, user)
                logger.info(f"Superuser {username} tizimga kirdi.")
                return redirect(next_url)
            else:
                if not password:
                    logger.warning(f"{username} parolni kiritmadi.")
                    return render(request, 'login.html', {'error': 'Iltimos, parolni kiriting.'})
                
                user = authenticate(request, username=username, password=password)  # Oddiy foydalanuvchi uchun autentifikatsiya
                if user:
                    auth_login(request, user)
                    messages.success(request, "!Siz autentificationdan o‘tdingiz") 
                    return redirect('/home/')
                else:
                    logger.warning(f"Login urunishda xatolik: {username}")
                    return render(request, 'login.html', {'error': 'Foydalanuvchi nomi yoki parol noto‘g‘ri.'})
        except User.DoesNotExist:
            logger.warning(f"Foydalanuvchi topilmadi: {username}")
            return render(request, 'login.html', {'error': 'Bunday foydalanuvchi mavjud emas.'})

    return render(request , 'login.html')

def logouts(request):
    logout(request)
    messages.success(request, "Siz tizimdan muvafaqiyatli chiqib ketingiz")
    return render(request, 'logout.html')
