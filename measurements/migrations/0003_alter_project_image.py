# Generated by Django 3.2.9 on 2021-11-13 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('measurements', '0002_project_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ImageField(null=True, upload_to='./image/project'),
        ),
    ]
