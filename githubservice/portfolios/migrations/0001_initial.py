

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color1', models.CharField(max_length=20)),
                ('color2', models.CharField(max_length=20)),
                ('color3', models.CharField(max_length=20)),
                ('color4', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Github',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_img', models.CharField(max_length=200)),
                ('git_repourl', models.CharField(max_length=200)),
                ('git_reponame', models.CharField(max_length=200)),
                ('git_username', models.CharField(max_length=200)),
                ('git_email', models.CharField(max_length=200)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill_kind', models.CharField(max_length=20)),
                ('skill_name', models.CharField(max_length=20)),
                ('skill_img', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Usercontent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job', models.CharField(max_length=15)),
                ('introduce', models.CharField(max_length=200)),
                ('develop_content1', models.CharField(max_length=15)),
                ('develop_content2', models.CharField(max_length=15)),
                ('develop_content3', models.CharField(max_length=15)),
                ('develop_content4', models.CharField(max_length=15)),
                ('develop_content5', models.CharField(max_length=15)),
                ('develop_content6', models.CharField(max_length=15)),
                ('allskill', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='allskill', to='portfolios.Skill')),
                ('color', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolios.Color')),
                ('majorskill', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='majorskill', to='portfolios.Skill')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
