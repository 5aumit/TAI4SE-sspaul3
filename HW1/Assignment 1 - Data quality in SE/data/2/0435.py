from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin

from .views import (
        PickingbillAssignView,
        WaybillCompleteView,
        LineChartJSONView,
        PickingbillStatView,
)

urlpatterns = [
    url(r'^pickingbillassign$', PickingbillAssignView.as_view(), name='pickingbill_assign'),  
    url(r'^waybillcomplete$', WaybillCompleteView.as_view(), name='waybill_assign'),  
    url(r'^pickingbillstat$', PickingbillStatView.as_view(), name='pickingbill_stat'),  
    url(r'^linechartjason1$', LineChartJSONView.as_view(), name='line_chart_json1'),   
]