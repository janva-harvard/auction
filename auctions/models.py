from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class AuctionListings(models.Model):
    #Users should also optionally be able to provide a URL 
    # for an image for the listing and/or a category 
    # (e.g. Fashion, Toys, Electronics, Home, etc.).
    title = models.CharField (max _length=64)
    description=models.CharField (max _length=300)
    starting_bid = models.DecimalField(_(""), max_digits=5, decimal_places=2)
    image_url= models.URLField(_(""), max_length=200)
    category = 

class Bids(models.Model):
    pass

class Comments(models.Model):
    pass

class Categories(models.Model):
    pass

    