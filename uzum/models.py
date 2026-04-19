from django.db import models

class Mahsulot_soni(models.Model):
    soni = models.IntegerField()

    def __str__(self):
        return str(self.soni)

class Mahsulot_Turi(models.Model):
    turi = models.CharField(max_length=30)
    def __str__(self):
        return self.turi
class Mahsulot(models.Model):
    rasm = models.ImageField(upload_to="media")
    ikkinchi_rasm = models.ImageField(upload_to="media", null=True)
    qoshimchi_birinchi_rasm = models.ImageField(upload_to="media", null=True, blank=True)
    qoshimcha_ikkinchi_rasm = models.ImageField(upload_to="media", null=True, blank=True)
    qoshimcha_uchunchi_rasm = models.ImageField(upload_to="media", null=True, blank=True)
    qoshimcha_tortinchi_rasm = models.ImageField(upload_to="media", null=True, blank=True)
    turi = models.ForeignKey(Mahsulot_Turi, on_delete=models.CASCADE, related_name="mahsulotlar", null=True)
    tavsifi = models.TextField()
    chegirma = models.IntegerField()
    narxi = models.IntegerField()
    arzon_narx = models.BooleanField(default=False)
    xaqiqiy = models.BooleanField(default=False)
    rangi = models.CharField(max_length=20, null=True)
    soni = models.ForeignKey(Mahsulot_soni, on_delete=models.CASCADE, related_name="mahsulotlar", null=True)

    def __str__(self):
        return self.tavsifi
    
    
    
class Main_banner(models.Model):
    img = models.ImageField(upload_to="media")
    tavsif_uchun = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.tavsif_uchun
    
    