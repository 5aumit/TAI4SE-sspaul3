from django.conf.urls import url
from ..views import (buildings_upload, keytype_upload, key_upload, keystatus_upload, keyissue_upload)
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^buildings_csv/$',  # NOQA
        buildings_upload,
        name="buildings_upload"),
    url(r'^keytype_csv/$',  # NOQA
            keytype_upload,
            name="keytype_upload"),
    url(r'^key_csv/$',  # NOQA
            key_upload,
            name="key_upload"),
    url(r'^keystatus_csv/$',  # NOQA
            keystatus_upload,
            name="keystatus_upload"),
    url(r'^keyissue_csv/$',  # NOQA
            keyissue_upload,
            name="keyissue_upload"),
]

