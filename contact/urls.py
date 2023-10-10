from django.urls import path
from contact import views

app_name = 'contact'

urlpatterns = [

    # contacts (CRUD)
    path('contact/<int:contact_id>/detail/', views.contact, name='contact'),
    # path('contact/<int:contact_id>/update/', views.contact, name='contact'),
    # path('contact/<int:contact_id>/delete/', views.contact, name='contact'),
    path('contact/create/', views.create, name='create'),

    path('search/', views.search, name='search'),
    path('', views.index, name='index'),
]
