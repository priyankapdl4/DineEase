# Generated by Django 5.0.4 on 2024-06-16 04:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menus', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='fooditem',
            name='image',
            field=models.ImageField(default='path/to/default/image.jpg', upload_to='food_images/'),
            preserve_default=False,
        ),
    ]
