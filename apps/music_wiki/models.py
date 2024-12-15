from django.db import models

class Group(models.Model):
    title = models.CharField(max_length=50)
    discription = models.TextField(max_length=600, null=True, blank=True)
    date = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to='avatars/', default='default/CHOOSE.png')

    def __str__(self):
        return self.title

class Album(models.Model):
    title = models.CharField(max_length=50)
    discription = models.TextField(max_length=600, null=True, blank=True)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True, null=True, blank=True)
    image = models.ImageField(upload_to='avatars/', default='default/CHOOSE.png')

    def __str__(self):
        return self.title
    
class Song(models.Model):
    title = models.CharField(max_length=50)
    discription = models.TextField(max_length=600, null=True, blank=True)
    album = models.ForeignKey(Album, on_delete=models.SET_NULL, null=True, blank=True)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    duration = models.DurationField()
    file = models.FileField(upload_to='songs/')
    lyrics = models.TextField(blank=True, null=True)

class GroupMember(models.Model):
    name = models.CharField(max_length=50)
    bio = models.TextField(max_length=600, null=True, blank=True)
    role = models.CharField(max_length=100, null=True, blank=True)
    birth_day = models.CharField(max_length=20, null=True, blank=True)
    image = models.ImageField(upload_to='avatars/', default='default/CHOOSE.png')
    group = models.ForeignKey(Group, on_delete=models.CASCADE)

