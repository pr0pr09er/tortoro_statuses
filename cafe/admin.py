from django.contrib import admin
from .models import Order, Status, Worker, Post

# Register your models here.
admin.site.register(Order)
admin.site.register(Status)
admin.site.register(Worker)
admin.site.register(Post)
