# Generated by Django 4.1.7 on 2023-03-31 14:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0025_alter_image_file_alter_rendition_file'),
        ('events_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='events',
            name='picture',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='picture', to='wagtailimages.image'),
        ),
    ]