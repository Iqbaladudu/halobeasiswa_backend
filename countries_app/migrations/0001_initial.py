# Generated by Django 4.1.7 on 2023-03-31 13:36

from django.db import migrations, models
import django.db.models.deletion
import wagtail.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailimages', '0025_alter_image_file_alter_rendition_file'),
        ('wagtaildocs', '0012_uploadeddocument'),
    ]

    operations = [
        migrations.CreateModel(
            name='CountriesToStudy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('status', models.CharField(choices=[('OPEN', 'Open'), ('CLOSED', 'Closed'), ('COMINGSOON', 'Cooming Soon')], default='OPEN', max_length=10)),
                ('description', wagtail.fields.RichTextField()),
                ('registration_link', models.URLField()),
                ('booklet', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtaildocs.document')),
                ('picture', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image')),
            ],
            options={
                'verbose_name': 'Negara Tujuan',
                'verbose_name_plural': 'Negara Tujuan Kuliah Halo Beasiswa',
            },
        ),
    ]
