# Generated by Django 2.1.15 on 2020-07-05 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolios', '0008_auto_20200706_0125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='project_img',
            field=models.ImageField(null=True, upload_to='media'),
        ),
    ]
