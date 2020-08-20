# Generated by Django 3.1 on 2020-08-16 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_article_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='image',
            new_name='image_0',
        ),
        migrations.RemoveField(
            model_name='article',
            name='body',
        ),
        migrations.AddField(
            model_name='article',
            name='body_0',
            field=models.TextField(default='None'),
        ),
        migrations.AddField(
            model_name='article',
            name='body_1',
            field=models.TextField(default='None'),
        ),
        migrations.AddField(
            model_name='article',
            name='body_2',
            field=models.TextField(default='None'),
        ),
        migrations.AddField(
            model_name='article',
            name='body_3',
            field=models.TextField(default='None'),
        ),
        migrations.AddField(
            model_name='article',
            name='body_4',
            field=models.TextField(default='None'),
        ),
        migrations.AddField(
            model_name='article',
            name='image_1',
            field=models.ImageField(blank=True, default='default.png', upload_to=''),
        ),
        migrations.AddField(
            model_name='article',
            name='image_2',
            field=models.ImageField(blank=True, default='default.png', upload_to=''),
        ),
        migrations.AddField(
            model_name='article',
            name='image_3',
            field=models.ImageField(blank=True, default='default.png', upload_to=''),
        ),
        migrations.AddField(
            model_name='article',
            name='image_4',
            field=models.ImageField(blank=True, default='default.png', upload_to=''),
        ),
    ]
