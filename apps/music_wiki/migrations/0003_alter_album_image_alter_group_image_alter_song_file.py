# Generated by Django 5.1.4 on 2024-12-19 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music_wiki', '0002_alter_album_date_alter_album_discription_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='image',
            field=models.ImageField(default='default/album/Crosses.jpg', upload_to='avatars/'),
        ),
        migrations.AlterField(
            model_name='group',
            name='image',
            field=models.ImageField(default='default/group/Sumerian.jpg', upload_to='avatars/'),
        ),
        migrations.AlterField(
            model_name='song',
            name='file',
            field=models.FileField(default='default/song.mp3', upload_to='songs/'),
        ),
    ]