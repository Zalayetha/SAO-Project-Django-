from django.db import models
from django.utils.text import slugify
# Create your models here.
class Post(models.Model):
     subject = models.CharField(max_length=50)
     body = models.TextField()
     category = models.TextField()
     publish = models.DateTimeField(auto_now_add=True)
     update = models.DateTimeField(auto_now=True)
     slug = models.SlugField(blank=True,editable=False)


     def save(self):
          self.slug = slugify(self.subject)
          super(Post,self).save()

     def __str__(self):
          return "{}. {}".format(self.id,self.subject)