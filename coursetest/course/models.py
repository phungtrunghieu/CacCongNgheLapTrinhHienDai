from ckeditor.fields import RichTextField
from django.db import models
from django.contrib.auth.models import AbstractUser
from cloudinary.models import CloudinaryField

class User(AbstractUser):
    avatar=CloudinaryField(null=True)

class Category(models.Model):
    name=models.CharField(max_length=50,unique=True)

    def __str__(self):
        return self.name
class BaseModel(models.Model):
    active = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
class Course(BaseModel):
    subject = models.CharField(max_length=100)
    description = models.TextField(null=True)
    image = CloudinaryField(null=True)#models.ImageField(upload_to='course/%Y/%m',null=True)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)

    def __str__(self):
        return self.subject
class Lesson(BaseModel):
    subject = models.CharField(max_length=100)
    content=RichTextField()
    image = models.ImageField(upload_to='lessons/%Y/%m',
                              null=True)
    course=models.ForeignKey(Course,on_delete=models.RESTRICT)
    tags=models.ManyToManyField('Tag')

    def __str__(self):
        return self.subject
    class Meta:
        unique_together=('subject','course')


class Tag(BaseModel):
    name=models.CharField(max_length=50,unique=True)

    def __str__(self):
        return self.name