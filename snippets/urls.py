from snippets import views
from django.urls import path

urlpatterns = [
    path('snippets/',views.snippet_list),
    path('snippets/<int:pk>/', views.snippet_detail)
]