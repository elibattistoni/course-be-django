from django.urls import path
from cbv_app import views

app_name = "cbv_app"

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("cbv_simple/", views.CBView.as_view(), name="simple"),
    path("cbv_context/", views.CBViewContext.as_view(), name="context"),
    path("school_list/", views.SchoolListView.as_view(), name="school_list"),
    path("school_list/<int:pk>/", views.SchoolDetailView.as_view(), name="school_detail"),
    path("school_create/", views.SchoolCreateView.as_view(), name="create_school"),
    path("school_update/<int:pk>/", views.SchoolUpdateView.as_view(), name="update_school"),
    path("school_delete/<int:pk>/", views.SchoolDeleteView.as_view(), name="delete_school"),
]
