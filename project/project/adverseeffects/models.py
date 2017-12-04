from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=15)
    userID = models.IntegerField()
    age = models.IntegerField()
    sex = models.BooleanField()
    height = models.IntegerField()
    weight = models.IntegerField()
    credibility = models.IntegerField()
    drugusage = []

    def __str__(self):
        return format(self.username)

class Drug(models.Model):
    drugID = models.IntegerField()
    drugname = models.CharField(max_length = 50)
    activeingredients = []

    def __str__(self):
        return format(self.drugname)

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
    content = models.CharField(max_length = 300)
    timestamp = ""
    tagID = models.ForeignKey(Tag, on_delete=models.CASCADE)
    rating = models.IntegerField()

    def __str__(self):
        return format(self.blogID)


class Comment(models.Model):
    userID = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.CharField(max_length = 300)
    timestamp = ""
    commentID = models.CharField(max_length = 50)
    blogID = models.ForeignKey(Blog, on_delete=models.CASCADE)

    def __str__(self):
        return format(self.commentID)


