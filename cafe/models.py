from django.db import models


class Order(models.Model):
    table_number = models.IntegerField()
    worker = models.ForeignKey("Worker", on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    status = models.ForeignKey("Status", on_delete=models.CASCADE)
    price = models.IntegerField()


class Status(models.Model):
    status_type = models.CharField(max_length=15)


class Worker(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    login = models.CharField(max_length=100)
    password = models.CharField(max_length=10)
    photo = models.ImageField(upload_to='users/')
    post = models.ForeignKey("Post", on_delete=models.CASCADE)


class Post(models.Model):
    name = models.CharField(max_length=15)
