"""community URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
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
from django.conf.urls import (handler404, handler500)
from django.contrib import admin
from django.urls import path, include
from user.views import home

# handler400 = 'views.bad_request'
# handler403 = 'views.bad_request'
handler404 = 'user.views.page_not_found'
handler500 = 'user.views.server_error'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('user.urls')),
    path('board/', include('board.urls')),
    path('', home),
]
