from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.urls import reverse
from django.db.models import Q

class samochody(models.Model):
    SKRZYNIA_SELECT = (
        ('0', 'Manualna'),
        ('1', 'Automatyczna')
    )

    KLIMATYZACJA_SELECT = (
        ('0', 'Manualna'),
        ('1', 'Automatyczna')
    )

    PALIWO_SELECT = (
        ('0', 'Benzyna'),
        ('1', 'Olej napędowy'),
        ('2', 'Benzyna + LPG'),
        ('3', 'Hybryda'),
    )

    image = models.ImageField(default='nocar.jpg', upload_to='car_pics')
    model = models.CharField(max_length=100,null=True,blank=True)
    cena = models.IntegerField(null=True,blank=True)
    skrzynia = models.CharField(max_length=11,choices=SKRZYNIA_SELECT,null=True,blank=True)
    paliwo = models.CharField(max_length=50,choices=PALIWO_SELECT,null=True,blank=True)
    klimatyzacja = models.CharField(max_length=20,choices=KLIMATYZACJA_SELECT,null=True,blank=True)
    miejsca = models.IntegerField(null=True,blank=True)
    nadwozie = models.CharField(max_length=100,null=True,blank=True)
    klasa = models.CharField(max_length=50,null=True,blank=True)
    moc_silnika = models.IntegerField(null=True,blank=True)
    pojemnosc_silnika = models.FloatField(null=True,blank=True)
    spalanie_miasto = models.FloatField(null=True,blank=True)
    spalanie_trasa = models.FloatField(null=True,blank=True)
    wyposazenie = models.TextField(null=True,blank=True)


    def __str__(self):
        return self.model

    def save(self):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

class Zamow(models.Model):

    MIEJSCE_SELECT = (
        ('0', 'Rzeszów, Dworzec Główny PKP'),
        ('1', 'Rzeszów, Lotnisko Jasionka'),
        ('2', 'Sopot, Dworzec Główny PKP'),
        ('3', 'Warszawa, Lotnisko Chopina'),
        ('4', 'Warszawa, Metro Wilanowska'),
        ('5', 'Warszawa, Dworzec Centralny'),
        ('6', 'Wrocław, Dworzec Główny PKP'),
        ('7', 'Sosnowiec, Dworzec Główny PKP'),
        ('8', 'Poznań, Lotnisko Ławica'),
        ('9', 'Olsztyn, Dworzec Główny PKP'),
        ('10', 'Łódź, Dworzec Łódź Kaliska'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    samochod = models.ForeignKey(samochody, on_delete=models.CASCADE)
    miejsce_odbioru = models.CharField(max_length=100,choices=MIEJSCE_SELECT,null=True,blank=True)
    miejsce_oddania = models.CharField(max_length=100,choices=MIEJSCE_SELECT,null=True,blank=True)
    data_odbioru = models.DateField(null=True,blank=True)
    data_oddania = models.DateField(null=True,blank=True)


    def check_dates(self):

        if Zamow.objects.\
                filter(samochod=self.samochod_id).\
                filter(
            Q(data_odbioru__gte=self.data_odbioru, data_odbioru__lte=self.data_oddania)
           | Q(data_oddania__gte=self.data_odbioru, data_oddania__lte=self.data_oddania)).\
                exists():
            print(self.data_odbioru)
            print(self.data_oddania)

            return False
        if Zamow.objects.filter(samochod=self.samochod_id, data_odbioru__lte=self.data_odbioru, data_oddania__gte=self.data_oddania).\
            exists():
            return False

        return True


    def __str__(self):
        return f'Zamówienie {self.user.username}'

