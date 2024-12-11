from django.contrib import admin

# Register your models here.
from django.contrib.auth.models import Group,User
admin.site.unregister(Group)
admin.site.unregister(User)

from .models import *
admin.site.register(categories)
admin.site.register(product)
admin.site.register(product_image)