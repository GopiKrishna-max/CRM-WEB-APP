from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),

    # Contacts
    path('contacts/', views.contact_list, name='contact_list'),
    path('contacts/new/', views.contact_create, name='contact_create'),
    path('contacts/<int:pk>/edit/', views.contact_edit, name='contact_edit'),
    path('contacts/<int:pk>/delete/', views.contact_delete, name='contact_delete'),

    # Authentication
    path('accounts/', include('django.contrib.auth.urls')),
    path('signup/', views.signup, name='signup'),
]