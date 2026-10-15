"""
URL configuration for FirstDjangoLearning project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path,include
# Changes the text in the upper-left corner of every admin page and the login page header
admin.site.site_header = "Learning python Admin"

# Changes the welcoming sub-header text at the top of the admin index (home) page
admin.site.index_title = "Welcome to the Management Portal"

# Changes the text displayed in the browser's title bar/tab
admin.site.site_title = "Django Admin Portal"

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",include('Home.urls')),
]
