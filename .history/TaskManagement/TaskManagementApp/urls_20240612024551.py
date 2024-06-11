from django.urls import path
from . import views
urlpatterns=[
    path('dolist/',views.dolist_view,name='dolist'),
    path('add_task/',views.add_task,name='add_task'),
    path('task_done/<int:id>',views.task_done,name='task_done'),
    path('update_task/<int:id>',views.update_task,name='update_task'),
    path('undo_task/<int:id>',views.undo_task,name='undo_task'),
    path('delete_task/<int:id>',views.delete_task,name='delete_task'),
    path('clear_incomplete/',views.clear_incomplete,name='clear_incomplete'),
    path('clear_complete/',views.clear_complete,name='clear_complete'),
]