# Generated by Django 2.1.15 on 2020-07-04 06:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portfolios', '0002_auto_20200704_1332'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usercontent',
            name='allskill',
        ),
        migrations.AddField(
            model_name='usercontent',
            name='allskill',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='portfolios.Skill'),
            preserve_default=False,
        ),
    ]
