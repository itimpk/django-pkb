from django.urls import path
from . import views ,api_views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('', views.note_list, name='note_list'),
    path('form/', views.note_form, name='note_create'),
    path('<int:id>/', views.note_detail, name='note_detail'),
    path('<int:id>/edit/', views.note_update, name='note_update'),
    path('<int:id>/delete/', views.note_delete, name='note_delete'),
    path('api/notes/', api_views.NoteListCreateView.as_view(), name='api_note_list'),
    path('api/notes/<int:pk>/', api_views.NoteDetailView.as_view(), name='api_note_detail'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
