from django.conf.urls import url
from .vistas.post import Post
from .vistas.userControl import UserControl

urlpatterns = [
    url(r'^welcome/', UserControl().welcome)
    ,url(r'^userControl/addUser/', UserControl().addUser)
    ,url(r'^userControl/login/', UserControl().login)
    ,url(r'^userControl/user_inactive/', UserControl().userInactive)
    ,url(r'^userControl/user_not_found/', UserControl().userNotFound)
    
    ,url(r'^post/add/', Post().add)
    ,url(r'^post/',  Post().index)
]
