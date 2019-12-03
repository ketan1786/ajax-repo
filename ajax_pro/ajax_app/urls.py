from django.urls import path
from ajax_app import views
urlpatterns = [
    path('', views.CurdView.as_view(), name='ajax'),
    path('ajax/curd/create', views.CreateCrudUser.as_view(), name="ajax_create"),
    path('ajax/curd/update', views.UpdateCrudUser.as_view(), name="ajax_update"),
    path('ajax/crud/delete', views.DeleteCrudView.as_view(), name="ajax_delete"),
]


