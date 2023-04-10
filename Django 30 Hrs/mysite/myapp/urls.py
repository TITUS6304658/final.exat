from django.urls import path
from .import views

urlpatterns = [
     
    path('',views.main,name='main'),
    path('my_view',views.my_view,name='my_view'),
    path('my_viewtitle/<int:project_id>/', views.my_viewtitle, name='my_viewtitle'),
    path('save_text/',views.save_text, name='save_text'),
    path('ask_form/',views.ask_form,name='ask_form'),
    path('mainmenu/',views.mainmenu,name='mainmenu'),

    path('home/',views.home,name='home'), 
    path('save_data/',views.save_data),
    path('save_owner/', views.save_owner, name='save_owner'),
    path('edit_data/<int:id>/', views.edit_data, name='edit_data'),
    path('save_data2/', views.save_data2, name='save_data2'),
    path('adminmin/', views.adminmin, name='adminmin'),
    path('projectject/', views.projectject, name='projectject'),
    path('contracttract/', views.contracttract, name='contracttract'),
    path('showed_project_table/', views.showed_project_table, name='showed_project_table'),
    path('edit_project_topic_for_admin/<int:id>/', views.edit_project_topic_for_admin, name='edit_project_topic_for_admin'),
    path('delete_project/<int:id>/', views.delete_project, name='delete_project'),
    path('showed_contract_table/', views.showed_contract_table, name='showed_contract_table'),
    path('edit_contract_topic_for_admin/<int:id>/', views.edit_contract_topic_for_admin, name='edit_contract_topic_for_admin'),
    path('delete_contract/<int:id>/', views.delete_contract, name='delete_contract'),
    path('showed_title_table/', views.showed_title_table, name='showed_title_table'),
    path('delete_title/<int:id>/', views.delete_title, name='delete_title'),
    path('edit_title_topic_for_admin/<int:id>/', views.edit_title_topic_for_admin, name='edit_title_topic_for_admin'),
    path('sub_date/', views.sub_date, name='sub_date'),
    path('approve_form/<int:project_id>/', views.approve_form, name='approve_form'),
    path('home_appove/', views.home_appove, name=' home_appove'),
    path('approve_sub_date/',views.approve_sub_date, name='approve_sub_date'),
    path('save_text_appove/',views.save_text_appove, name='save_text_appove'),
   
]
