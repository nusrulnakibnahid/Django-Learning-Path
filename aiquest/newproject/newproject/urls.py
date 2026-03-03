"""
URL configuration for newproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from django.urls import path

#another method to import views (first 3 lines)
from Machine_Learning.views import machine_learning
from Machine_Learning.views import deep_learning
from Machine_Learning.views import about_us

from Blogs import views as blg
from Deep_Learning import views as dpl
from Data_Analysis import views as da
from About_Us import views as abt



urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', machine_learning),
    path('dl/',deep_learning),
    path('about/',about_us),

    path('blog/', blg.blog1),
    path('deepl/', dpl.deep_learning),
    path('analysis/', da.data_analysis),
    path('about_us/',abt.about_us),
]
