from django.db import models

from django.db import models

class Muallif(models.Model): #Здесь был создан таблица Автор книги
    J = [
        ("erkak", "erkak"),
        ("ayol", "ayol")
    ]
    ism = models.CharField(max_length=50)
    tirik = models.BooleanField()
    kitob_soni = models.SmallIntegerField()
    jins = models.CharField(max_length=5, choices=J, null=True)
    tugilgan_sana = models.DateField()
    def __str__(self):
        return self.ism



class Kitob(models.Model): # Здесь был создан таблица Книга
    nom = models.CharField(max_length=50)
    sahifa = models.CharField(max_length=50)
    muallif = models.ForeignKey(Muallif, on_delete=models.CASCADE)
    janr = models.CharField(max_length=50)
    def __str__(self):
        return self.janr

class Talaba(models.Model): # Здесь был создан таблица Студент
    ism = models.CharField(max_length=50)
    bitiruvchi = models.BooleanField()
    kitoblar_soni = models.PositiveSmallIntegerField(default=0)
    kurs = models.PositiveSmallIntegerField()

class Admin(models.Model): # Здесь был создан таблица Админ
    ism = models.CharField(max_length=50)
    ish_vaqti = models.TimeField()


class Record(models.Model): # Здесь был создан таблца рекордов
    talaba = models.ForeignKey(Talaba, on_delete=models.CASCADE)
    kitob = models.ForeignKey(Kitob, on_delete=models.CASCADE)
    admin = models.ForeignKey(Admin, on_delete=models.CASCADE)
    olingan_sana = models.DateField()
    qaytarish_sana = models.DateField()
    qaytardi = models.BooleanField()
