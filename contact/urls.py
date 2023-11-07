from django.urls import path
from contact import views

app_name = 'contact'

urlpatterns = [

    # contacts (CRUD)
    path('contact/<int:contact_id>/detail/', views.contact, name='contact'),
    path('contact/<int:contact_id>/update/', views.update, name='update'),
    path('contact/<int:contact_id>/delete/', views.delete, name='delete'),
    path('contact/create/', views.create, name='create'),
    
    path('user/create/', views.register, name='register'),

    path('search/', views.search, name='search'),
    path('', views.index, name='index'),
]
