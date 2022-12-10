from django.db import models
from django.contrib.auth.models import User
import uuid
from django.db.models.signals import post_save,post_delete
from django.dispatch import receiver
#from blogs.models import Tags
# Create your models here.
class Profile(models.Model):

    user=models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True)
    full_name=models.CharField(max_length=200,blank=True,null=True)
    username=models.CharField(max_length=200,blank=True,null=True)
    email=models.EmailField(max_length=200,blank=True,null=True)
    phone_no=models.CharField(blank=True,null=True,max_length=13)
    address=models.TextField(blank=True,null=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    

    created_on=models.DateTimeField(auto_now_add=True,null=True,blank=True)
    roles=(
        ('BLOGGER','BLOGGER'),
    

     )
    user_role=models.CharField(max_length=255,blank=True,choices=roles,default='BLOGGER') 
    bio=models.TextField(default="Writing...............")
    def __str__(self):
         if self.full_name: 
            return self.full_name
         elif self.user:
            return f"{self.user}"
         else:
            return f"{self.id}"
   
    







