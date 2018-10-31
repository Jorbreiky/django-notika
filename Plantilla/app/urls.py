from django.conf.urls import url
from .vistas.post import Post
from .vistas.user import User

urlpatterns = [
    url(r'^$', Post().test)
    ,url(r'^user/add/', User().add)
    ,url(r'^user/insert/', User().insert)
]
