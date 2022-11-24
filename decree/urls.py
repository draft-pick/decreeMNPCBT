from django.urls import path

from .views import (decree_list,
                    decree_create,
                    decree_detail,
                    decree_changed_create,
                    decree_changed_detail)

app_name = 'decree'

urlpatterns = [
    path('', decree_list, name='decree_list'),
    path('create/', decree_create, name='decree_create'),
    path('detail/<int:decree_id>/', decree_detail, name='decree_detail'),
    path('detail/<int:decree_id>/create_changed/',
         decree_changed_create,
         name='decree_changed_create'),
    path('detail/<int:decree_id>/detail_changed/<int:decree_changed_id>',
         decree_changed_detail,
         name='decree_changed_detail')
]
