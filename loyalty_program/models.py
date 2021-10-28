from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields.related import ForeignKey
from django.db.models.signals import post_save
from django.dispatch import receiver

class Brand (models.Model):
    id_brand = models.PositiveIntegerField()
    
class DiscountCode(models.Model):
    value = models.CharField(null=False, blank=False, max_length=255)
    brand = models.ForeignKey(
        Brand, null=False, blank=False, on_delete=models.CASCADE)

class Follower (models.Model):
    id_user = models.PositiveIntegerField(default='', editable=False)
    discount_code = models.ForeignKey(
        DiscountCode, null=True,blank=True, on_delete=models.CASCADE)
