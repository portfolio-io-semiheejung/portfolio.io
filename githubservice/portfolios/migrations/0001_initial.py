# Generated by Django 2.1.15 on 2020-07-03 09:42

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
            name='Aboutme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job', models.CharField(max_length=15)),
                ('introduce', models.CharField(max_length=200)),
            ],
        ),
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
            name='Develop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('develop_content', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('edu_name', models.CharField(max_length=20)),
                ('edu_content', models.TextField()),
                ('edu_data_start', models.DateField()),
                ('edu_data_finish', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ex_name', models.CharField(max_length=20)),
                ('ex_content', models.TextField()),
                ('ex_data_start', models.DateField()),
                ('ex_data_finish', models.DateField()),
            ],
            options={
                'ordering': ['-ex_data_start'],
            },
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
            name='Portfolio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=20)),
                ('project_start', models.DateField()),
                ('project_finsh', models.DateField()),
                ('project_role', models.CharField(max_length=20)),
                ('project_skill', models.CharField(max_length=200)),
                ('project_content', models.TextField()),
                ('project_img', models.ImageField(upload_to='')),
                ('portfolio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolios.Portfolio')),
            ],
            options={
                'ordering': ['-project_start'],
            },
        ),
        migrations.CreateModel(
            name='Skil',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill_name', models.CharField(max_length=20)),
                ('skill_img', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Skillkind',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill_kind_name', models.CharField(max_length=20)),
                ('cust_allskill', models.ManyToManyField(related_name='allskill', to='portfolios.Portfolio')),
                ('cust_majorskill', models.ManyToManyField(related_name='majorskill', to='portfolios.Portfolio')),
            ],
        ),
        migrations.AddField(
            model_name='skil',
            name='skillkind',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolios.Skillkind'),
        ),
        migrations.AddField(
            model_name='experience',
            name='portfolio',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolios.Portfolio'),
        ),
        migrations.AddField(
            model_name='education',
            name='portfolio',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolios.Portfolio'),
        ),
        migrations.AddField(
            model_name='develop',
            name='portfolio',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolios.Portfolio'),
        ),
        migrations.AddField(
            model_name='color',
            name='portfolio',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolios.Portfolio'),
        ),
        migrations.AddField(
            model_name='aboutme',
            name='portfolio',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolios.Portfolio'),
        ),
    ]