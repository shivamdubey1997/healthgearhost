from django.contrib import admin
from .models import Profile,Post,Uploadworkoutvideo,Bodyweight,Recepies
# Register your models here.
admin.site.register(Profile)
admin.site.register(Post)
admin.site.register(Uploadworkoutvideo)

admin.site.register(Bodyweight)
admin.site.register(Recepies)
