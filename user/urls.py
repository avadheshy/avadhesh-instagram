from django.urls import path
from user import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.login, name='login'),
    path('posts', views.posts, name='posts'),
    path('profile', views.profile, name='profile'),
    path('logout', views.logout, name='logout'),
]
#urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
