from django.contrib import admin
from .models import Sale,CSV,Position

# Register your models here.
admin.site.register(Sale)
admin.site.register(Position)
admin.site.register(CSV)