from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

from . import views, api_views


urlpatterns = [
    # Regular Django Views
    url(r'^$', views.index, name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
    url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),


] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
