from django.contrib import admin
from .models import User, Drug, BodyPart, AdverseEffect, Comment, Tag, Blog

# Register your models here.

admin.site.register(User)
admin.site.register(Drug)
admin.site.register(BodyPart)
admin.site.register(AdverseEffect)
admin.site.register(Tag)
admin.site.register(Blog)
admin.site.register(Comment)