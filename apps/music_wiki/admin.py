from django.contrib import admin

from .models import Group, Album, GroupMember, Song


@admin.register(Group)
class AdminGroup(admin.ModelAdmin):
    list_display = ['id', 'title', 'date', 'image']
    list_display_links = ['id', 'title']
    search_fields = ['title', 'description']
    list_filter = ['date']
    readonly_fields = ['date']


@admin.register(Album)
class AdminAlbum(admin.ModelAdmin):
    list_display = ['id', 'title', 'group', 'date', 'image']
    list_display_links = ['id', 'title']
    search_fields = ['title', 'description']
    list_filter = ['group', 'date']
    readonly_fields = ['date']
    autocomplete_fields = ['group']

@admin.register(Song)
class AdminSong(admin.ModelAdmin):
    list_display = ['id', 'title', 'album', 'group', 'duration', 'file']
    list_display_links = ['id', 'title']
    search_fields = ['title', 'description', 'lyrics']
    list_filter = ['album', 'group']
    autocomplete_fields = ['album', 'group']
    fieldsets = (
        ('Основная информация', {
            'fields': ('title', 'description', 'album', 'group', 'duration', 'file')
        }),
        ('Дополнительно', {
            'fields': ('lyrics',),
            'classes': ('collapse',),
        }),
    )


@admin.register(GroupMember)
class AdminGroupMember(admin.ModelAdmin):
    list_display = ['id', 'name', 'role', 'group', 'birth_day', 'image']
    list_display_links = ['id', 'name']
    search_fields = ['name', 'bio', 'role']
    list_filter = ['group', 'role']
    autocomplete_fields = ['group']
    readonly_fields = ['birth_day']
    fieldsets = (
        ('Основная информация', {
            'fields': ('name', 'bio', 'role', 'group', 'image')
        }),
        ('День рождения', {
            'fields': ('birth_day',),
            'classes': ('collapse',),
        }),
    )