from django.db import models
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel, FieldRowPanel
import wagtail

# Create your models here.


class CountriesToStudy(models.Model):
    def user_directory_path(instance, filename):
        return f"img/admin/countries/{instance.name}/{filename}"
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
    status = models.CharField(
        max_length=10, choices=STATUS_CHOICE, default='OPEN')
    description = RichTextField()
    registration_link = models.URLField()
    booklet = models.ForeignKey(wagtail.documents.get_document_model_string(
    ), null=True, blank=True, on_delete=models.SET_NULL, related_name='+')

    panels = [
        FieldPanel('name', heading="Nama Negara"),
        FieldPanel('picture', heading="Gambar"),
        FieldPanel('description', heading="Deskripsi Negara"),
        FieldPanel('registration_link', heading="Link Pendaftaran Kuliah"),
        FieldPanel('booklet', heading="Booklet"),
        FieldPanel('status', heading="Status Pendaftaran"),
    ]

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Negara Tujuan"
        verbose_name_plural = "Negara Tujuan Kuliah Halo Beasiswa"
