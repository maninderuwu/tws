from django.urls import path
from .views import add_contacts,index,edit_contact,delete_contact

urlpatterns = [
    path('',index,name='index'),
    path('addcontact/',add_contacts,name='add'),
    path('editcontact/<int:pk>',edit_contact,name='edit'),
    path('deletecontact/<int:pk>',delete_contact,name='delete'),
]