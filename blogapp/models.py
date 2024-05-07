import uuid

from django.db import models
from django.contrib.auth.models import User

class User_register(models.Model):
    firstname=models.CharField(max_length=20)
    lastname=models.CharField(max_length=20)
    gender=models.CharField(max_length=10)
    email=models.CharField(max_length=50)
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=30)
    
    class Meta:
        db_table='User_register'
        
    def __str__(self):
        return self.username

def generate_uuid():
    return uuid.uuid4().hex
    

class Base(models.Model):
    reference_id= models.CharField(max_length=32,unique=True,primary_key=True,default=generate_uuid)
    is_delete= models.BooleanField(default=False)
    created_by= models.ForeignKey(User,on_delete=models.PROTECT,db_column='created_by',related_name='+')
    created_at= models.DateTimeField()
    updated_by= models.ForeignKey(User,null=True,on_delete=models.PROTECT,db_column='updated_by')
    updated_at= models.DateTimeField(null=True)
    
    class Meta:
        abstract=True
        
class BlogTable(Base):
    title= models.CharField(max_length=100)
    description=models.TextField(null=True)
    image=models.ImageField(default='noimage.jpg')
    username=models.CharField(max_length=50,null=True)
    firstname=models.CharField(max_length=50,null=True)
    lastname=models.CharField(max_length=50,null=True)
    
    
    
    class Meta:
        db_table='BlogTable'
        
    def __str__(self):
        return self.title
    
    
class commenttable(models.Model):
    comment_id=models.CharField(max_length=32)
    comment_time=models.DateTimeField()
    is_delete=models.BooleanField(default=False)
    comment_by=models.CharField(max_length=100)
    cmt=models.CharField(max_length=1000)
    
    class Meta:
        db_table='commenttable'
        
    def __str__(self):
        return self.comment_by
    
    
class usertag(models.Model):
    tagid=models.CharField(max_length=32)
    tag_by=models.CharField(max_length=50)
    tag_to=models.CharField(max_length=50)
    tag_title=models.CharField(max_length=100)
    
    class Meta:
        db_table='usertag'
        
    def __str__(self):
        return self.tag_title