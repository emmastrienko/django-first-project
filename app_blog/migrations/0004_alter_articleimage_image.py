# Generated by Django 5.1 on 2024-09-25 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_blog', '0003_alter_article_options_alter_articleimage_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articleimage',
            name='image',
            field=models.ImageField(blank=True, upload_to='photos', verbose_name='Фото'),
        ),
    ]
