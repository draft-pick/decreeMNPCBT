from django.contrib import admin

from .models import Type, Decrees, DecreesChanged

admin.site.register(Type)

admin.site.register(Decrees)

admin.site.register(DecreesChanged)
