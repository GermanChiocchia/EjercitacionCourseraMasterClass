# Generated by Django 3.2 on 2021-04-07 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='image',
            field=models.ImageField(default='Images/None/sampleImg.jpg', upload_to='Images'),
        ),
    ]