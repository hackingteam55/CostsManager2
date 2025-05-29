import uuid
from django.db import models
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    nume = models.CharField(max_length=200, blank=True, null=True)
    prenume = models.CharField(max_length=200, blank=True, null=True)
    bio = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(max_length=500, blank=True, null=True)
    username = models.CharField(max_length=200, blank=True, null=True)
    magazine_favorite = models.CharField(max_length=200, blank=True, null=True)
    poza_profil = models.ImageField(null=True, blank=True, upload_to='profiles/', default="profiles/user_default.png")
    social_github = models.CharField(max_length=200, blank=True, null=True)
    social_linkedin = models.CharField(max_length=200, blank=True, null=True)
    social_twitter = models.CharField(max_length=200, blank=True, null=True)
    social_instagram = models.CharField(max_length=200, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return str(self.user.username)


def createProfile(sender, instance, created, **kwargs):
    if created:
        user = instance
        profile = Profile.objects.create(
            user=user,
            username=user.username,
            email=user.email,
            nume=user.first_name,
        )



def deleteUser(sender, instance, **kwargs):
    user = instance.user
    user.delete()




post_save.connect(createProfile, sender=User)
post_delete.connect(deleteUser, sender=Profile)