from django.contrib import admin

# Register your models here.
from appmusic.models import Album, Songs

admin.site.register(Album)
admin.site.register(Songs)
