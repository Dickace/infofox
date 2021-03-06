# Generated by Django 3.0.7 on 2020-06-16 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('createDate', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(max_length=150, verbose_name='Название')),
                ('content', models.TextField(verbose_name='Содержание')),
                ('img', models.ImageField(upload_to='%Y_%m_%d')),
            ],
            options={
                'verbose_name': 'Новость',
                'verbose_name_plural': 'Новости',
            },
        ),
    ]
