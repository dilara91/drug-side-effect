from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
# class User(models.Model):
#     username = models.CharField(max_length=15)
#     userID = models.IntegerField()
#     age = models.IntegerField()
#     sex = models.BooleanField()
#     height = models.IntegerField()
#     weight = models.IntegerField()
#     credibility = models.IntegerField()
#     drugusage = []
#
#     def __str__(self):
#         return format(self.username)


class User(AbstractUser):

    age = models.IntegerField()
    sex = models.CharField(max_length=1, choices=[("M", "Male"), ("F", "Female")])
    height = models.IntegerField()
    weight = models.IntegerField(null=True, blank=True, default=None)
    credibility = models.IntegerField(null=True, blank=True, default=None)
    # drugusage = []

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)

    class Meta:
        swappable = 'AUTH_USER_MODEL'


class ActiveIngredient(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return format(self.name)


class Drug(models.Model):
    # drugID = models.IntegerField()
    drugname = models.CharField(max_length=50)
    activeingredients = models.ManyToManyField(ActiveIngredient, default=None, blank=True)

    def __str__(self):
        return format(self.drugname)


class BodyPart(models.Model):
    # bodypartID = models.IntegerField()
    name = models.CharField(max_length=50)

    def __str__(self):
        return format(self.name)


class AdverseEffect(models.Model):
    # adverseID = models.IntegerField()
    drug = models.ForeignKey(Drug, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    bodypart = models.ForeignKey(BodyPart, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return format(self.name)


class Tag(models.Model):
    # tagID = models.IntegerField()
    name = models.CharField(max_length=50)

    def __str__(self):
        return format(self.name)


class Blog(models.Model):
    # blogID = models.CharField(max_length=50)
    title = models.CharField(max_length=64)
    content = models.CharField(max_length=300)
    timestamp = models.DateTimeField(auto_now_add=True)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)

    def __str__(self):
        return format(self.id)


class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.CharField(max_length=300)
    timestamp = models.DateTimeField(auto_now_add=True)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)

    def __str__(self):
        return format(self.id)


