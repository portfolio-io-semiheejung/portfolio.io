# Generated by Django 2.1.15 on 2020-07-05 17:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portfolios', '0010_auto_20200706_0129'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='github',
            name='git_email',
        ),
        migrations.RemoveField(
            model_name='github',
            name='git_repourl',
        ),
        migrations.RemoveField(
            model_name='github',
            name='git_username',
        ),
        migrations.RemoveField(
            model_name='github',
            name='profile_img',
        ),
        migrations.RemoveField(
            model_name='github',
            name='user',
        ),
        migrations.AddField(
            model_name='project',
            name='github',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='portfolios.Github'),
        ),
    ]
