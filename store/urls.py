from django.urls import path
from store import views

urlpatterns = [
    path("tshort/", views.TShortListView.as_view()),
    path("tshort/create", views.TShortCreateView.as_view()),
    path("tshort/<int:tsh_pk>/", views.TShortDetailView.as_view()),
    path("brand/create/", views.BrandCreateView.as_view()),

]