from django.db import models


class port_model(models.Model):
    port_number = models.CharField(max_length=100,default='')


    class Meta:
        db_table = 'port_number'


class Profile_Table(models.Model):
    bussiness_name = models.CharField(max_length=100,default='')
    city = models.CharField(max_length=100,default='')
    state = models.CharField(max_length=100,default='')
    country = models.CharField(max_length=100,default='')
    postal_code = models.CharField(max_length = 10 ,default='')
    contact_name = models.CharField(max_length=100,default='')
    streets = models.CharField(max_length=100,default='')
    phone = models.CharField(max_length=100,default='')
    email = models.CharField(max_length=100,default='')
    port = models.IntegerField(default = 0)
    downloadSpeed = models.CharField(max_length=100,default='')
    uploadSpeed = models.CharField(max_length=100,default='')

    class Meta:
        db_table='profile'

class register(models.Model):
    username = models.CharField(max_length=100,default='')
    email = models.CharField(max_length=100,default='')
    password = models.CharField(max_length=100,default='')

    class Meta:
        db_table = 'register'

class enable(models.Model):
    availabilty = models.CharField(max_length=100,default=True)
