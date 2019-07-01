from django.conf.urls import url
from .views import rendergraph, sample1, page, getweatherdata

urlpatterns = [
    url("analytics/", rendergraph),
    url("sample1/", sample1, name="sample1"),
    url("page/", page, name="page"),
    url("getweatherdata/", getweatherdata, name="weatherdata")
]
