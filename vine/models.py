from django.db import models


class Team(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    designation = models.CharField(max_length=300)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    twitter_link = models.URLField(max_length=150)
    linkedin_link = models.URLField(max_length=150)
    facebook_link = models.URLField(max_length=150)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name