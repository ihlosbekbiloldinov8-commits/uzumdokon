from django.shortcuts import render, get_object_or_404, redirect
from django.utils import translation
from django.conf import settings
from .models import Mahsulot, Main_banner

LANGUAGE_SESSION_KEY = getattr(translation, 'LANGUAGE_SESSION_KEY', 'django_language')

def set_language(request, lang_code):
    if lang_code in ['uz', 'ru', 'en']:
        translation.activate(lang_code)
        request.session[LANGUAGE_SESSION_KEY] = lang_code
    referer = request.META.get('HTTP_REFERER', '/')
    return redirect(referer)
def base(request):
    lang = request.session.get(LANGUAGE_SESSION_KEY, 'uz')
    translation.activate(lang)
    return render(request, "base.html")

def home(request):
    lang = request.session.get(LANGUAGE_SESSION_KEY, 'uz')
    translation.activate(lang)
    mahsulotlar = Mahsulot.objects.all()
    main_banner = Main_banner.objects.all()
    return render(request, "home.html", 
        {"mahsulotlar": mahsulotlar,
         "main_banner": main_banner,
         "current_lang": lang,
        }
    )


def nav(request):
    lang = request.session.get(LANGUAGE_SESSION_KEY, 'uz')
    translation.activate(lang)
    return render(request, "nav.html")


def sotuvchi_bolish(request):
    lang = request.session.get(LANGUAGE_SESSION_KEY, 'uz')
    translation.activate(lang)
    return render(request, "sotuvchi_bolish.html")

def topshirsh_punkiti(request):
    lang = request.session.get(LANGUAGE_SESSION_KEY, 'uz')
    translation.activate(lang)
    return render(request, "topshirish_punkiti.html")


def savol_javob(request):
    lang = request.session.get(LANGUAGE_SESSION_KEY, 'uz')
    translation.activate(lang)
    return render(request, "savol.html")

def footer(request):
    lang = request.session.get(LANGUAGE_SESSION_KEY, 'uz')
    translation.activate(lang)
    return render(request, "foter.html")


def sotuvchi_login(request):
    lang = request.session.get(LANGUAGE_SESSION_KEY, 'uz')
    translation.activate(lang)
    return render(request, "sotuvchi_login.html")


def buyurtmalar(request):
    lang = request.session.get(LANGUAGE_SESSION_KEY, 'uz')
    translation.activate(lang)
    return render(request, "buyurtmalar.html")



def mahsulot_detail(request, id):
    lang = request.session.get(LANGUAGE_SESSION_KEY, 'uz')
    translation.activate(lang)
    mahsulotlar = get_object_or_404(Mahsulot, id=id)
    return render(request, "detail.html", {"mahsulotlar": mahsulotlar})


def Motherboard(request):
    lang = request.session.get(LANGUAGE_SESSION_KEY, 'uz')
    translation.activate(lang)
    return render(request, "motherboard.html")


def ContactUs(request):
    lang = request.session.get(LANGUAGE_SESSION_KEY, 'uz')
    translation.activate(lang)
    return render(request, "contact.html")

def topshirish_punkitini(request):
    lang = request.session.get(LANGUAGE_SESSION_KEY, 'uz')
    translation.activate(lang)
    return render(request, "topshirish.html")


def location(request):
    lang = request.session.get(LANGUAGE_SESSION_KEY, 'uz')
    translation.activate(lang)
    return render(request, "location.html")


def filtered(request):
    lang = request.session.get(LANGUAGE_SESSION_KEY, 'uz')
    translation.activate(lang)
    
    tur = request.GET.get("turi")

    if tur:
        mahsulotlar = Mahsulot.objects.filter(turi__turi=tur)
    else:
        mahsulotlar = Mahsulot.objects.none()  

    return render(request, "filtered.html", {"mahsulotlar": mahsulotlar, "tur": tur, "current_lang": lang})

def splash(request):
    lang = request.session.get(LANGUAGE_SESSION_KEY, 'uz')
    translation.activate(lang)
    return render(request, "splash.html")


def search(request):
    lang = request.session.get(LANGUAGE_SESSION_KEY, 'uz')
    translation.activate(lang)
    q = request.GET.get("q", "")
    if q:
        mahsulotlar = Mahsulot.objects.filter(tavsifi__icontains=q)
    else:
        mahsulotlar = Mahsulot.objects.all()
    return render(request, "home.html", {"mahsulotlar": mahsulotlar, "q": q, "current_lang": lang})