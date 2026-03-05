from django.urls import path
from .import views


urlpatterns = [

    path('machine/', views.machine_learning),
    # path('dl/',views.deep_learning),
    # path('about/',views.about_us),
    path('rn/', views.random),
    path('knn/', views.K_nearest),
    path('dt/', views.dtree),

]