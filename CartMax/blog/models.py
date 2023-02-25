from django.db import models

# Create your models here.

from django.db import models

class Blogpost(models.Model):
    post_id = models.AutoField(primary_key= True)
    Title = models.CharField(max_length=50)
    Head0 = models.CharField(max_length=500, default="")
    Chead0 = models.CharField(max_length=5000, default="")
    Head1 = models.CharField(max_length=500, default="")
    Chead1 = models.CharField(max_length=5000, default="")
    Head2 = models.CharField(max_length=500, default="")
    Chead2 = models.CharField(max_length=5000, default="")
    Pub_date = models.DateField()
    Thumbnail = models.ImageField(upload_to='shop/images', default="")

    def __str__(self):
        return self.title