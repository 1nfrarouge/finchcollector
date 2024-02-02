from django.contrib import admin
from .models import Finch
from .models import Cat, Feeding

# Register your models here.
admin.site.register(Finch)
admin.site.register(Feeding)