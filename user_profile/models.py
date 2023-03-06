from django.db import models
from django.contrib.auth.admin import User
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.


class Profile(models.Model):
    GENDER_CHOICES = (
        ("MALE", "Male"),
        ("FEMALE", "Female")
    )

    def user_directory_path(instance, filename):
        return f"img/user_{instance.user.id}/{filename}"

    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    date_birth = models.DateField(blank=True, null=True)
    whatsapp = models.CharField(max_length=15)
    gender = models.CharField(
        max_length=6, choices=GENDER_CHOICES, default="MALE")

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
