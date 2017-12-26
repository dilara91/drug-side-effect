from .models import User, Drug, BodyPart, AdverseEffect, Comment, Tag, Blog
from django.contrib import admin

admin.site.register(User)
admin.site.register(Drug)
admin.site.register(BodyPart)
admin.site.register(AdverseEffect)
admin.site.register(Tag)
admin.site.register(Blog)
