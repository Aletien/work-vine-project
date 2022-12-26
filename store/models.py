from datetime import datetime
from django.db import models
from ckeditor.fields import RichTextField
from multiselectfield import MultiSelectField

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

    condition_choices = (
        ('New', 'New'),
        ('Used', 'Used'),
    )

    title = models.CharField(max_length=255)
    village = models.CharField(choices=village_choices, max_length=255)
    city = models.CharField(max_length=100, default='')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    color = models.CharField(max_length=100)
    condition = models.CharField(choices=condition_choices, max_length=100)
    body_style = models.CharField(max_length=100)
    year = models.IntegerField(('year'),choices=year_choice)
    description = RichTextField()
    price = models.IntegerField()
    features = MultiSelectField(choices=features_choices, max_length=255)
    number_seats = models.CharField(max_length=100)
    is_featured = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.title
