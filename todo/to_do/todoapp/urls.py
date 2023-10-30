from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('',views.add,name='add'),
#    path('detail',views.detail,name='detail')
    path('delete/<int:taskid>/',views.delete,name='delete'),
    path('update/<int:id>/', views.update, name='update'),
    path('listview/',views.tasklistview.as_view(),name='listview'),
    path('detailview/<int:pk>', views.taskdetailview.as_view(), name='detailview'),
    path('updateview/<int:pk>', views.taskupdateview.as_view(), name='updateview'),
    path('deleteview/<int:pk>', views.taskdeleteview.as_view(), name='deleteview'),
]