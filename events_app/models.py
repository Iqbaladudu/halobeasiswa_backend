from django.db import models

# Create your models here.


class Events(models.Model):
    def user_directory_path(instance, filename):
        return f"img/admin/events/{instance.name}/{filename}"

    STATUS_CHOICE = (
        ("OPEN", "Open"),
        ("CLOSED", "Closed"),
        ("COMINGSOON", "Cooming Soon")
    )

    HIGHLIGHT_CHOICE = (
        ("TRUE", "Iya"),
        ("FALSE", "Tidak")
    )

    name = models.CharField(max_length=100)
    picture = models.ImageField(
        upload_to=user_directory_path)
    date = models.DateTimeField(null=True)
    date_open = models.DateField()
    date_closes = models.DateField()
    status = models.CharField(
        max_length=10, choices=STATUS_CHOICE, default='OPEN')
    description = models.TextField()
    registration_link = models.URLField()
    price = models.IntegerField()
    highlight = models.TextField(
        max_length=6, choices=HIGHLIGHT_CHOICE, default="FALSE")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Event"
        verbose_name_plural = "Events"
