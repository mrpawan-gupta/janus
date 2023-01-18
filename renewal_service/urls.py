
from django.urls import re_path
from renewal_service.Views.HopePageView import ServiceWidgetView, InsertServiceView


urlpatterns = [
    re_path(r'^service/widget/v(?P<version_id>\d+)/$', ServiceWidgetView.as_view()),
    re_path(r'^service/insert/v(?P<version_id>\d+)/$', InsertServiceView.as_view()),
]
