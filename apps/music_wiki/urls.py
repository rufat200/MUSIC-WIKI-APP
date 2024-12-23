from django.urls import path

from . import views


urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('groups/', views.groups, name='groups'),
    path('group/<int:group_id>/', views.group_detail, name='group_detail'),
    path('albums/', views.albums, name='albums'),
    path('album/<int:album_id>/', views.album_detail, name='album_detail'),
    path('songs/', views.songs, name='songs'),
    path('song/<int:song_id>/', views.song_detail, name='song_detail'),
    path('groupmembers/', views.groupmembers, name='groupmembers'),
    path('groupmember/<int:groupmember_id>/', views.groupmember_detail, name='groupmember_detail'),
]