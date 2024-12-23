# Generated by Django 5.1.4 on 2024-12-19 01:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music_wiki', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='album',
            name='discription',
            field=models.TextField(blank=True, max_length=600, null=True),
        ),
        migrations.AlterField(
            model_name='group',
            name='discription',
            field=models.TextField(blank=True, max_length=600, null=True),
        ),
        migrations.AlterField(
            model_name='groupmember',
            name='bio',
            field=models.TextField(blank=True, max_length=600, null=True),
        ),
        migrations.AlterField(
            model_name='groupmember',
            name='birth_day',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='groupmember',
            name='role',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='song',
            name='discription',
            field=models.TextField(blank=True, max_length=600, null=True),
        ),
    ]
