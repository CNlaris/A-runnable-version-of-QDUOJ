from django.urls import re_path as url, include

from ..views.oj import AnnouncementAPI

urlpatterns = [
    url(r"^announcement/?$", AnnouncementAPI.as_view(), name="announcement_api"),
]
