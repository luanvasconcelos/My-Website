# Generated by Django 2.1.5 on 2019-03-15 13:44

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_used', models.DateTimeField(default=django.utils.timezone.now)),
                ('img', models.ImageField(upload_to='image_input')),
            ],
        ),
    ]
