"""dj_first URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from atexit import register
from django.contrib import admin
from django.urls import path
from news.views import index, detail_view, create_views, edit_view, delete_view
from profiles.views import logout_view, login_view, register_view
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('id/<int:pk>/', detail_view),
    path('news/create/', create_views),
    path('logout/', logout_view),
    path('login/', login_view),
    path('register/', register_view),
    path('news/edit/<int:pk>', edit_view),
    path('news/delete/<int:pk>', delete_view)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)





