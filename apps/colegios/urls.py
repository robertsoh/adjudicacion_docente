from django.conf.urls import url

from apps.colegios.views import ColegioListView

urlpatterns = [
    url(r'^$', ColegioListView.as_view(), name='list'),
]
