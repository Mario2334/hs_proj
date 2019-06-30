from django.conf.urls import url
from .views import rendergraph,sample1,page

urlpatterns = [
    url("analytics/",rendergraph),
    url("sample1/" , sample1 , name="sample1"),
    url("page/" , page , name="page")
]