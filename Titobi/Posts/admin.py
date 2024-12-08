from django.contrib import admin
from .models import post, init_img, gif, detail, order

# Register your models here.

admin.site.register(post)
admin.site.register(init_img)
admin.site.register(gif)
admin.site.register(detail)
admin.site.register(order)