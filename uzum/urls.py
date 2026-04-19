from django.urls import path
from .views import *

urlpatterns = [
   path("home/", home, name="home"),
   path("", splash, name="splash"),
   path("nav/", nav, name="nav"),
   path("sotuvchi_bolish/", sotuvchi_bolish, name="satuvchi"),
   path("topshirish/", topshirsh_punkiti, name="topshirish"),
   path("savol/", savol_javob, name="savol"),
   path("sotuvchi_login", sotuvchi_login, name="login_sotuvchi"),
   path("buyurtmalar", buyurtmalar, name="buyurtmalar"),
   path("detail/<int:id>/", mahsulot_detail, name="detail"),
   path("motherboard/", Motherboard, name="motherboard"),
   path("contact/", ContactUs, name="contact"),
   path("topshirishni/", topshirish_punkitini, name="topshirish"),
   path("location/", location, name="location"),
path("filtered/", filtered, name="filtered"),
     path("search/", search, name="search"),
     path("lang/<str:lang_code>/", set_language, name="set_language"),
]

