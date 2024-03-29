from datetime import datetime
from email.policy import default
from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField
from django.utils import timezone



class Asset(models.Model):
    title = models.CharField(max_length=20)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(default=datetime.now)
    description = models.CharField(max_length=100)
    price = models.IntegerField()
    asset_quantity = models.IntegerField(default=1)
    status=models.BooleanField(default=False)

    def __str__(self):
         return self.title

class Assetinfo(models.Model):
    tag_no = models.ForeignKey(Asset, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    item_id = models.CharField(max_length=20,default='')
    entry_date = models.DateField(default=datetime.now)
    statusID = models.CharField(max_length=20)

    def __str__(self):
        return self.item_id

class Department(models.Model):
    department_id = models.IntegerField(primary_key=True)
    department_name = models.CharField(max_length=20,default='')
    
class Item(models.Model):
    item_id = models.ForeignKey(Assetinfo, on_delete=models.CASCADE)
    item_name = models.CharField(max_length=20,default='')
    categoryId = models.CharField(max_length=20)
    
class Category(models.Model):
    category_id = models.IntegerField(primary_key=True)
    category_name = models.CharField(max_length=20,default='')

class Employeeinfo(models.Model):
    empolyeeID = models.IntegerField()
    employeeName = models.ForeignKey(User, on_delete=models.CASCADE)
    departmentId = models.IntegerField()
    contact = models.IntegerField()

class Assetstatus(models.Model):
    statusid = models.IntegerField(primary_key=True)
    statusname = models.CharField(max_length=20,default='')    

class Assetrequest(models.Model):
    asset_name= models.ForeignKey(Asset, on_delete=models.CASCADE,default='')
    request_quantity= models.IntegerField(default=0)
    User_id=models.ForeignKey(User, on_delete=models.CASCADE, default='')
    time = models.DateTimeField(default=timezone.now)

class Maintenancerequest(models.Model):
    Maintenance_name = models.ForeignKey(Asset, on_delete=models.CASCADE, default='')
    user_name = models.ForeignKey(User, on_delete=models.CASCADE)
    time = models.DateTimeField(default=timezone.now)
    