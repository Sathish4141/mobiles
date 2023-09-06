from django.urls import path
from MI import views
from rest_framework.urlpatterns import format_suffix_patterns
urlpatterns = [
    path("mobiles/",views.MobilesList.as_view(),name = "mobile_list"),
    path("mobiles/<int:id>/",views.MobileDetails.as_view(),name = "mobiles_details"),

]

urlpatterns = format_suffix_patterns(urlpatterns)