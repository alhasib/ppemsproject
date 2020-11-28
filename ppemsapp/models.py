from django.db import models
from django.contrib.auth.models import User 
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department = models.CharField(max_length = 250)
    profile_image = models.ImageField(blank = True, null = True, upload_to='img', default='si.png')

    def __str__(self):
        return str(self.user)
    
    def imgurl(self):
        try:
            image = self.profile_image.url 
        except:
            image = ''
        return image  

class Department(models.Model):
    name = models.CharField(max_length = 250)
    head_of_dept = models.CharField(max_length = 250, blank=True, null=True)
    number_of_employe = models.IntegerField(blank=True, null=True)
    access_number = models.CharField(max_length = 250, blank=True, null=True)

    def __str__(self):
        return self.name 

class DailyTask(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    title = models.CharField(max_length = 250, blank=True, null = True)
    description = models.TextField(blank=True, null = True)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title 


class Leave(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cause_of_leave = models.TextField(blank=True, null=True)
    from_date = models.DateField()
    to_date = models.DateField()
    status = models.BooleanField(default=False)
    checked_in = models.BooleanField(default=False)

    def __str__(self):
        return str(self.user)


class TodoList(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    what_to_do = models.TextField(blank=True, null=True)
    when_to_do = models.DateField(blank = True, null = True)
    pending_status = models.BooleanField(default=True)
    working_status = models.BooleanField(default = False)
    done_status = models.BooleanField(default=False)

    def __str__(self):
        return str(self.user) 


