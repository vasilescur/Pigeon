# Generated by Django 2.1.7 on 2019-03-11 20:36

import app.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20190311_2035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='feature_image',
            field=models.ImageField(blank=True, null=True, upload_to=app.models.article_feature_img_path),
        ),
    ]
