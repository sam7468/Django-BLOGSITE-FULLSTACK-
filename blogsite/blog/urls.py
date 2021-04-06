from django.urls import path
from . import views
from .views import Postlistview,Postdetailview,Postcreateview,Postupdateview,Postdeleteview,Userpostlistview
urlpatterns = [
    path('', Postlistview.as_view() , name='blog-home'),
    path('post/<int:pk>/', Postdetailview.as_view() , name='post-detail'),
    path('about/', views.about , name='blog-about' ),
    path('post/new/', Postcreateview.as_view() , name='post-create'),
    path('post/<int:pk>/update/', Postupdateview.as_view() , name='post-update'),
    path('post/<int:pk>/delete', Postdeleteview.as_view(), name='post-delete'),
    path('user/<str:username>', Userpostlistview.as_view() , name='user-post'),
]
