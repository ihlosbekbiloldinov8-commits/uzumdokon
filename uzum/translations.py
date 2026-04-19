from modeltranslation.translator import register, TranslationOptions
from .models import Mahsulot, Mahsulot_Turi, Main_banner

@register(Mahsulot)
class MahsulotTranslationOptions(TranslationOptions):
    fields = ('tavsifi',)

@register(Mahsulot_Turi)
class MahsulotTuriTranslationOptions(TranslationOptions):
    fields = ('turi',)

@register(Main_banner)
class MainBannerTranslationOptions(TranslationOptions):
    fields = ('tavsif_uchun',)