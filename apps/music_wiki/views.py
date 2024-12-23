from django.shortcuts import render, get_object_or_404, redirect

from .models import Group, Album, Song, GroupMember
from .forms import SongForm


def main_page(request):
    groups = Group.objects.all().order_by('-date')[:5]
    albums = Album.objects.all().order_by('-date')[:5]
    songs = Song.objects.all().order_by('-id')[:5]
    context = {
        'groups': groups,
        'albums': albums,
        'songs': songs,
    }
    return render(request, 'index.html', context)

def group_detail(request, group_id):
    group = get_object_or_404(Group, id=group_id)
    return render(request, 'group_detail.html', {'group': group})

def groups(request):
    groups = Group.objects.all()
    return render(request, 'groups.html', {'groups': groups})

def album_detail(request, album_id):
    album = get_object_or_404(Album, id=album_id)
    return render(request, 'album_detail.html', {'album': album})

def albums(request):
    albums = Album.objects.all()
    return render(request, 'albums.html', {'albums': albums})



def song_detail(request, song_id):
    if request.method == 'POST':
        form = SongForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('songs')  # Перенаправление на список песен
    else:
        form = SongForm()
    return render(request, 'song_detail.html', {'form': form})

def songs(request):
    songs = Song.objects.all()
    return render(request, 'songs.html', {'songs': songs})



def groupmember_detail(request, groupmember_id):
    groupmember = get_object_or_404(GroupMember, id=groupmember_id)
    return render(request, 'groupmember_detail.html', {'groupmember': groupmember})

def groupmembers(request):
    groupmembers = GroupMember.objects.all()
    return render(request, 'groupmembers.html', {'groupmembers': groupmembers})