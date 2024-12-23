from django.db import models

class Group(models.Model):
    title = models.CharField(max_length=50, verbose_name='название группы')
    description = models.TextField(null=True, blank=True, verbose_name="описание")
    date = models.DateField(auto_now_add=True, verbose_name="дата создания")
    image = models.ImageField(upload_to='avatars/', default='default/group/group.png', verbose_name='группы')

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "группа"
        verbose_name_plural = "группы"


class Album(models.Model):
    title = models.CharField(max_length=50, verbose_name="Название альбома")
    description = models.TextField(null=True, blank=True, verbose_name="описание")
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name="albums", verbose_name='группа')
    date = models.DateField(auto_now_add=True, null=True, blank=True, verbose_name="дата создания")
    image = models.ImageField(upload_to='avatars/', default='default/album/album.png', verbose_name="изображение")

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "альбом"
        verbose_name_plural = "альбомы"
    

class Song(models.Model):
    title = models.CharField(max_length=50, verbose_name="Название песни")
    description = models.TextField(null=True, blank=True, verbose_name="описание")
    album = models.ForeignKey(Album, on_delete=models.SET_NULL, related_name="songs", null=True, blank=True, verbose_name="альбом")
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='songs', verbose_name="группа")
    duration = models.DurationField(verbose_name="длительность")
    file = models.FileField(upload_to='songs/', default='default/song/audio.mp3', verbose_name="аудиофайл")
    lyrics = models.TextField(blank=True, null=True, verbose_name='лирика')

    def __str__(self):
        return f"{self.title} - {self.group}"

    class Meta:
        verbose_name = "песня"
        verbose_name_plural = "песни"


class GroupMember(models.Model):
    name = models.CharField(max_length=50, verbose_name='имя члена группы')
    bio = models.TextField(null=True, blank=True, verbose_name="биография")
    role = models.CharField(max_length=100, null=True, blank=True, verbose_name="роль")
    birth_day = models.CharField(max_length=20, null=True, blank=True, verbose_name="день рождения")
    image = models.ImageField(upload_to='avatars/', default='default/groupmember/avatar.png', verbose_name="аватар")
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name="groupmembers", verbose_name="группа")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "участник группы"
        verbose_name_plural = "участники группы"


