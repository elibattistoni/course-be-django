from django.urls import path
from cbv_app import views

app_name = "cbv_app"

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("cbv_simple/", views.CBView.as_view(), name="simple"),
    path("cbv_context/", views.CBViewContext.as_view(), name="context"),
    path("school_list/", views.SchoolListView.as_view(), name="school_list"),
    path("school_list/<int:pk>/", views.SchoolDetailView.as_view(), name="school_detail"),
]
