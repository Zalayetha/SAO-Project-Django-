from django.db import models
from django.utils.text import slugify
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
# Create your models here.
def validator(value):
     data = value
     categories =['Report','Review']
     if  data not in categories:
          print('berhasil')
          message = "maaf, " + data + " tidak bisa posting"
          raise ValidationError(message)


class Post(models.Model):
     subject = models.CharField(max_length=50)

     data_category = [
          ('Report','Report'),
          ('Review','Review'),
     ]
     category = models.CharField(
          max_length=10,
          choices=data_category,
          validators=[validator],
          )
     body = models.TextField()
     publish = models.DateTimeField(auto_now_add=True)
     update = models.DateTimeField(auto_now=True)
     slug = models.SlugField(blank=True,editable=False)


     def save(self,*args, **kwargs):
          self.slug = slugify(self.subject)
          super(Post,self).save(*args, **kwargs)

     def __str__(self):
          return "{}. {}".format(self.id,self.subject)