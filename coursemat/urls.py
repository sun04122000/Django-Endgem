"""coursemat URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import include,path
from igem import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sign/',views.firstpage),
    path('signup/',views.signup),
    path('signup2/',views.signup2),
    path('signup3/',views.signup3),
    path('signup3/Login/',views.HomePage.as_view()),
    path('mainpage/',views.main),
    #path('subj1/',views.subject1),
    path('upload/',views.upload_file),
    path('upload2/',views.upload_file2),
    path('upload3/',views.upload_file3),
    path('upload4/',views.upload_file4),
    path('upload5/',views.upload_file5),
    path('upload6/',views.upload_file6),
    path('upload7/',views.upload_file7),
    path('upload8/',views.upload_file8),
    path('ContactUs/',views.ContactUs),
    path('delete/',views.delete_file),
    path('delete2/',views.delete_file2),
    path('delete3/',views.delete_file3),
    path('delete4/',views.delete_file4),
    path('delete5/',views.delete_file5),
    path('delete6/',views.delete_file6),
    path('delete7/',views.delete_file7),
    path('delete8/',views.delete_file8),
    path('Forgot/',views.ForgotPassword),
    path('change_password/',views.change_password),
]

