# Generated by Django 2.2 on 2021-12-05 08:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_product'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cata',
            options={'ordering': ('name',), 'verbose_name': 'categery', 'verbose_name_plural': 'categeries'},
        ),
    ]
