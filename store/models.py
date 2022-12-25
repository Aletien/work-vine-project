from datetime import datetime
from django.db import models

class Store(models.Model):
    
    village_choices = (
        ('Kas', 'Kansanga'),
        ('Kab', 'Kabalagala'),
        ('Muy', 'Muyenga'),
        ('Bun', 'Bunga'),
        ('Gga', 'Ggaba'),
        ('Nsa', 'Nsambya'),
        ('Mak', 'Makindye'),
        ('Buz', 'Buzinga'),
        ('Ebb', 'Entebbe'),
        ('Mun', 'Munyonyo'),
        ('Bus', 'Busabala'),
        ('Kat', 'Katwe'),
        ('Nti','Ntinda'),
        ('Buk', 'Bukoto'),
        ('Kir', 'Kireka'),
        ('Ban', 'Banda'),
        ('Nam', 'Namuwongo'),
        ('Kaw', 'Kawempe'),
        ('Gay', 'Gayaza'),
        ('Kr', 'Kira'),
        ('Nak', 'Nakasero'),
        ('Nkw', 'Nakawa'),
        ('Klo', 'Kololo'),
    )

    year_choice = []
    for r in range(2022, (datetime.now().year+1)):
        year_choice.append((r,r))

    features_choices = (
        ('wood', 'wood'),
        ('metalic', 'metalic'),
        ('plastic', 'plastic'),
    )

    title = models.CharField(max_length=255)
    village = models.CharField(choices=village_choices, max_length=100)
    city = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    body_style = models.CharField(max_length=100)
    year = models.IntegerField(('year'),choices=year_choice)
    description = models.TextField(max_length=500)
    price = models.IntegerField()
    features = models.CharField(choices=features_choices, max_length=255)
    number_seats = models.CharField(max_length=100)
    is_featured = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=datetime.now, blank=True)
