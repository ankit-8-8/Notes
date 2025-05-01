from django.db import models
import shortuuid

# Create your models here.


class tbl_register(models.Model):
    username=models.CharField(max_length=50,unique=True)  
    name=models.CharField(max_length=50,null=True)
    email=models.EmailField(max_length=50,null=True)  
    mobile=models.CharField(max_length=20,primary_key=True)
    password=models.CharField(max_length=200,null=True)
    role=models.CharField(max_length=20,null=True)
    Key=models.CharField(max_length=200,null=True)
    def __str__(self):
        return self.username

class post(models.Model):   
    postid=models.CharField(default=shortuuid.uuid,primary_key=True,max_length=50)
    pcreated_by=models.ForeignKey(tbl_register,on_delete=models.CASCADE)
    pheading = models.CharField(max_length=100)
    pdescription = models.TextField(max_length=2000,blank=True)
    pimage= models.ImageField(upload_to='static/post_image/',blank=True)
    pfile = models.FileField(upload_to='static/post_file/',blank=True)
    pdate = models.DateField(auto_now_add=True)
    ptime = models.TimeField(auto_now_add=True)
    plike=models.ManyToManyField(tbl_register,related_name="likes")
    def __str__(self):
        return self.postid
    
    
    
class tbl_super(models.Model):
    name=models.CharField(max_length=100,unique=True)
    password=models.CharField(max_length=200,null=True)
    email=models.EmailField(max_length=50,null=True)  
    mobile=models.CharField(max_length=20,primary_key=True)
    

    