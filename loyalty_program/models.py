from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields.related import ForeignKey
from django.db.models.signals import post_save
from django.dispatch import receiver

# Brand is highly coupled with all of the microservices
# I'm assuming here that the brand gets duplicated with the event bus when needed

# toDo: Change the name of the class to brand (id, name, pourcentages[array of numbers])
# when you generate codes you need to publish to the microservices that require the discount codes that new codes have been generated
# when a user take a code you need to publish to the brand that they have new informations disclosed

# i publish discount code and user info
# i consume brand

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
