from django.db import models
from django.utils.text import slugify

from myuser.models import MyUser

# Create your models here.

class Listing(models.Model):
    seller = models.ForeignKey(MyUser)
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    pub_date = models.DateTimeField('Date added',auto_now_add=True)
    #
    listing_type = models.CharField(max_length=200,choices=(('ac','Auction'),('bin','Fixed Price')))
    description = models.TextField()
    
    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title)

        return super(Listing, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.title

class Bid(models.Model):
    bidder = models.ForeignKey(MyUser)
    listing = models.ForeignKey(Listing)

#class Order(models.Model):


