from django.contrib import admin
from django.urls import include, path
from polls.views import about, posts

urlpatterns = [
    path('admin/', admin.site.urls),
    path('polls/', include('polls.urls')),
    path('about/', about, name='about'),
    path('posts/', posts, name='post')
]
