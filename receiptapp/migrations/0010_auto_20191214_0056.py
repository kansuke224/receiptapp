# Generated by Django 2.2.5 on 2019-12-13 15:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('receiptapp', '0009_auto_20191214_0050'),
    ]

    operations = [
        migrations.RenameField(
            model_name='receipt',
            old_name='food',
            new_name='foods',
        ),
    ]
