# Generated by Django 4.2.5 on 2023-09-29 09:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0004_alter_category_options_contact_owner'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='emial',
            new_name='email',
        ),
    ]