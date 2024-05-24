from django.urls import path
from . import views as v

app_name = "posts"
urlpatterns = [
    path("create/", v.create_post, name="create_post"),
    # path("<int:pk>/", v.post_detail, name="post_detail"),
    # path("<int:pk>/update/", v.post_update, name="post_update"),
    # path("<int:pk>/delete/", v.post_delete, name="post_delete")
    path("", v.post_list, name="post_list"),
    path("like/", v.like, name="like"),
]
