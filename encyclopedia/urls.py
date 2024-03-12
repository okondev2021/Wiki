from django.urls import path

from . import views



urlpatterns = [
    path('',views.index,name='index'),
    path('create',views.create,name='create'),
     path('Random_Page',views.rando,name='random'),
    path('error',views.error,name='error'),
    path('edit',views.edit,name='edit'),
    path('search',views.search,name='search'),
    path('<str:name>',views.wikip,name='wikip'),
    path('<str:result>',views.result,name='result'),
]