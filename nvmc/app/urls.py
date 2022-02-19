from django.urls import path
from .views import NvmcList, NvmcDetail

urlpatterns = [
    path('', NvmcList.as_view(), name="list"),
    path('detail/<int:pk>', NvmcDetail.as_view(), name="detail")
]