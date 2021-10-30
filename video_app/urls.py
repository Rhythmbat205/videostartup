from django.urls import path
from . import views
from .views import PostDetails

urlpatterns = [
    path("",views.indexView,name='index'),
    path('<uuid:post_id>', PostDetails, name='postdetails'),
]