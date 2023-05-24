from django.db import models

# Create your models here.

class Fan(models.Model):
    class Meta:
        verbose_name_plural = 'Fanlar'
    nomi = models.CharField(max_length=25)
    haftalik_miqori = models.PositiveIntegerField(default=0)
    oquv_davomiyligi = models.FloatField(default=0, help_text='Yillar hisobida')

    def __str__(self) -> str:
        return self.nomi


class OqishNarxi(models.Model):
    class Meta:
        verbose_name_plural = "O'qish narxlari"
    fan = models.ForeignKey(Fan, on_delete=models.CASCADE, null=True)
    tolov = models.FloatField(default=0.0, help_text="to'lov 1 ta dars uchun $ da hisoblanadi")
    oylik_harajat = models.FloatField(default=0.0)
    oqish_yili = models.CharField(max_length=25, verbose_name="o'qish yili")


    def __str__(self):
        return f"{self.fan}"
    

class Guruh(models.Model):
    class Meta:
        verbose_name_plural = "Guruhlar"
    nomi = models.CharField(max_length=25)
    fan = models.ManyToManyField(Fan, blank=True)
    oqish_yili = models.CharField(max_length=15, verbose_name="O'qish yili")

    def __str__(self) -> str:
        return self.nomi


class Oqituvchi(models.Model):
    class Meta:
        verbose_name = "O'qituvchi"
        verbose_name_plural = "O'qituvchilar"
    familya = models.CharField(max_length=25)
    ism = models.CharField(max_length=25)
    otasining_ismi = models.CharField(max_length=25)
    telefon = models.CharField(max_length=25)

    def __str__(self) -> str:
        return self.ism


class Oquvchi(models.Model):
    class Meta:
        verbose_name = "O'quvchi"
        verbose_name_plural = "O'quvchilar"
    guruh = models.ForeignKey(Guruh, on_delete=models.CASCADE)
    familya = models.CharField(max_length=25)
    ism = models.CharField(max_length=25)
    otasining_ismi = models.CharField(max_length=25)
    telefon = models.CharField(max_length=25)

    def __str__(self) -> str:
        return self.ism


class Qongiroq(models.Model):
    class Meta:
        verbose_name = "Qo'ng'iroq Jadvali"
        verbose_name_plural = "Qo'ngiroq Jadvallari"

    davomiyligi = models.PositiveIntegerField(default=10)

    def __str__(self):
        return f"{self.davomiyligi}"
    

class DasrJadvali(models.Model):
    class Meta:
        verbose_name_plural = "Dars Jadvallari"

    oqituvchi = models.ForeignKey(Oqituvchi, on_delete=models.CASCADE)
    guruh = models.ForeignKey(Guruh, on_delete=models.CASCADE)
    tanaffus = models.ForeignKey(Qongiroq, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.guruh}"
