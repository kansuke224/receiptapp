# Generated by Django 2.2.5 on 2019-11-17 10:33

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('receiptapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('user_pass', models.CharField(max_length=20)),
                ('user_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.RemoveField(
            model_name='receipt',
            name='created_date',
        ),
        migrations.RemoveField(
            model_name='receipt',
            name='id',
        ),
        migrations.RemoveField(
            model_name='receipt',
            name='image',
        ),
        migrations.AddField(
            model_name='receipt',
            name='receipt_date',
            field=models.DateTimeField(default=django.utils.timezone.now, null=True),
        ),
        migrations.AddField(
            model_name='receipt',
            name='receipt_id',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('image_id', models.AutoField(primary_key=True, serialize=False)),
                ('image', models.ImageField(upload_to='receiptapp')),
                ('receipt_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='receiptapp.Receipt')),
            ],
        ),
        migrations.CreateModel(
            name='Food',
            fields=[
                ('food_id', models.AutoField(primary_key=True, serialize=False)),
                ('protein', models.CharField(max_length=20)),
                ('salt', models.CharField(max_length=20)),
                ('zinc', models.CharField(max_length=20)),
                ('receipt_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='receiptapp.Receipt')),
            ],
        ),
        migrations.AddField(
            model_name='receipt',
            name='user_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='receiptapp.User'),
        ),
    ]
