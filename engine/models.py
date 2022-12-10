from django.db import models
import uuid
from accounts.models import Profile
# Create your models here.
class Article(models.Model):

     id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
     writer=models.ForeignKey(Profile,null=True,blank=True,on_delete=models.CASCADE)
     topic=models.CharField(max_length=255,default="....")
     content=models.TextField(max_length=100000)
     created_on=models.DateTimeField(auto_now_add=True,null=True,blank=True)
     summary=models.TextField(max_length=10000,null=True,blank=True)
     subjectivity=models.CharField(max_length=500,null=True,blank=True)
     polarity=models.CharField(max_length=500,null=True,blank=True)
     negativity=models.CharField(max_length=500,null=True,blank=True)
     neutrality=models.CharField(max_length=500,null=True,blank=True)
     positivity=models.CharField(max_length=500,null=True,blank=True)
     compound_score=models.CharField(max_length=500,null=True,blank=True)
     class Meta:
        ordering = ('-created_on', )
    



     def __str__(self):
         return self.topic
     
    

