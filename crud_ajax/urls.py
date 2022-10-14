from django.urls import path
from crud_ajax.views import CreateCrudUser, CrudView, DeleteCrudUser, UpdateCrudUser

app_name='crud'
urlpatterns = [
    path('crud/', CrudView.as_view(), name='crud_ajax'),
    path('crud/create/', CreateCrudUser.as_view(), name='crud_ajax_create'),
    path('crud/delete/', DeleteCrudUser.as_view(), name='crud_ajax_delete'),
    path('crud/update/', UpdateCrudUser.as_view(), name='crud_ajax_update'),
]
