from django.contrib import admin
from .models import Clothes,Color,Size
# Register your models here.
admin.site.register(Clothes)
admin.site.register(Color)
admin.site.register(Size)