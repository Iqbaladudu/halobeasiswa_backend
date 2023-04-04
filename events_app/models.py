from django.db import models
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel, FieldRowPanel

# Create your models here.


class Events(models.Model):
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
    picture = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='img'
    )
    date = models.DateField(null=True)
    time = models.TimeField(null=True)
    status = models.CharField(
        max_length=10, choices=STATUS_CHOICE, default='OPEN')
    description = RichTextField()
    registration_link = models.URLField()
    price = models.IntegerField()

    panels = [
        FieldPanel('name', heading="Nama Acara"),
        FieldPanel('picture', heading="Gambar"),
        FieldRowPanel([
            FieldPanel('date', heading="Tanggal Acara"),
            FieldPanel('time', heading="Waktu Acara"),
        ]),
        FieldPanel('description', heading="Deskripsi Acara"),
        FieldPanel('price', heading="Biaya Acara",
                   help_text="Masukkan 0 jika acaranya gratis"),
        FieldPanel('registration_link', heading="Link Pendaftaran Acara"),
        FieldPanel('status', heading="Status Acara"),
    ]

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Acara"
        verbose_name_plural = "Event Halo Beasiswa"
