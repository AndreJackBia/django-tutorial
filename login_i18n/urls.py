"""
login_i18n URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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

from . import views
from django.conf.urls import include, url, re_path
from django.contrib import admin
from django.conf.urls.i18n import i18n_patterns
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]

# urlpatterns = [
#     url(r'^(?P<filename>(robots.txt)|(humans.txt))$',
#         home_files, name='home-files'),
# ]
 
urlpatterns += i18n_patterns(
    path('', views.index, name='index'),
    path('accounts/', include('django.contrib.auth.urls')),
)