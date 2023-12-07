from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    phone = models.CharField(max_length=20,blank=True,null=True)
    address = models.TextField(blank=True,null=True)

    def _str__(self):
        return self.user.username
    



@receiver(post_save, sender=User)
def profile_save(sender, instance,created,**kwargs):
    if created:
        Profile.objects.create(user=instance)

