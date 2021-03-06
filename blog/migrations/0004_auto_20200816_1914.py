# Generated by Django 3.1 on 2020-08-16 22:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20200816_1909'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='image_0',
            new_name='body_image_0',
        ),
        migrations.RenameField(
            model_name='article',
            old_name='image_1',
            new_name='body_image_1',
        ),
        migrations.RenameField(
            model_name='article',
            old_name='image_2',
            new_name='body_image_2',
        ),
        migrations.RenameField(
            model_name='article',
            old_name='image_3',
            new_name='body_image_3',
        ),
        migrations.RenameField(
            model_name='article',
            old_name='image_4',
            new_name='body_image_4',
        ),
        migrations.AddField(
            model_name='article',
            name='image',
            field=models.ImageField(blank=True, default='default.png', upload_to=''),
        ),
    ]
