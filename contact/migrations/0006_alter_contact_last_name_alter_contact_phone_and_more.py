# Generated by Django 4.2.5 on 2023-10-06 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0005_rename_emial_contact_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='last_name',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='contact',
            name='phone',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='contact',
            name='picture',
            field=models.ImageField(blank=True, upload_to='pictures/%Y/%m/'),
        ),
    ]
