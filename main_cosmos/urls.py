
from django.urls import path
from . import views

app_name = "main_cosmos"

urlpatterns = [
    path('',views.home, name = "home"),
    path('details/<int:id>/', views.detail, name="detail"),
    path('addshow/', views.add_show, name="add_show"),
    path('editshow/<int:id>/', views.edit_show, name="edit_show"),
    path('delshow/<int:id>/', views.del_show, name="del_show"),
    path('rateshow/<int:id>/', views.rate_show, name="rate_show")
    
]

  