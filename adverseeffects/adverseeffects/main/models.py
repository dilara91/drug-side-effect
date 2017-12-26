from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver

# Create your models here.

class DrugUsage(models.Model):
    drug = models.CharField(max_length=15)
    def __str__(self):
        return format(self.drug)

class User(models.Model):
    username = models.CharField(max_length=15)
    password = models.IntegerField(blank=True)
    userID = models.IntegerField(blank=True)
    age = models.IntegerField(blank=True)
    sex = models.BooleanField(blank=True)
    height = models.IntegerField(blank=True)
    weight = models.IntegerField(blank=True)
    credibility = models.IntegerField(blank=True)

    def __str__(self):
        return format(self.username)
class ActiveIngredients(models.Model):
    aiID = models.IntegerField()
    ainame = models.CharField(max_length = 50)

    def __str__(self):
        return format(self.ainame)

class Drug(models.Model):
    drugID = models.IntegerField()
    drugname = models.CharField(max_length = 50)

    def __str__(self):
        return format(self.drugname)
class DrugUsage(models.Model):
    drug = models.CharField(max_length=15)
    def __str__(self):
        return format(self.drug)

class BodyPart(models.Model):
    bodypartID = models.IntegerField()
    name = models.CharField(max_length = 50)

    def __str__(self):
        return format(self.name)

class AdverseEffect(models.Model):
    adverseID = models.IntegerField()
    drugID = models.ForeignKey(Drug, on_delete=models.CASCADE)
    name = models.CharField(max_length = 50)
    bodypartID = models.ForeignKey(BodyPart, on_delete=models.CASCADE)
    userID = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return format(self.name)

class Tag(models.Model):
    tagID = models.IntegerField()
    name = models.CharField(max_length = 50)

    def __str__(self):
        return format(self.name)

class Blog(models.Model):
    blogID = models.CharField(max_length = 50)
    content = models.CharField(max_length = 500)
    timestamp = ""
    tag = models.CharField(max_length = 50, default='')
    rating = models.IntegerField()

    def __str__(self):
        return format(self.content)


class Comment(models.Model):
    userID = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.CharField(max_length = 300)
    timestamp = ""
    commentID = models.CharField(max_length = 50)
    blogID = models.ForeignKey(Blog, on_delete=models.CASCADE)

    def __str__(self):
        return format(self.commentID)