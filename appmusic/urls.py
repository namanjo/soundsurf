from django.urls import path
from appmusic import views

urlpatterns = [

    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('all/<str:its_type>/', views.all_albums_songs, name='all_albums_songs'),
    path('albums/created/', views.my_albums, name='my_albums'),

    path('album/<slug:album_slug>/', views.detail, name='album_detail'),
    path('add-album/', views.album_create, name='album_create'),
    path('album/<slug:album_slug>/add-song/', views.add_song, name='add_song'),
    path('album/<slug:album_slug>/delete/', views.album_delete, name='album_delete'),
    path('song/<int:song_id>/delete/', views.song_delete, name='song_delete'),

    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]
