from django.urls import re_path as url, include
from ..views.admin import SubmissionRejudgeAPI

urlpatterns = [
    url(r"^submission/rejudge?$", SubmissionRejudgeAPI.as_view(), name="submission_rejudge_api"),
]
