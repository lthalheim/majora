from django.urls import path,re_path

from django.views.decorators.csrf import csrf_exempt

from . import views
from . import account_views

urlpatterns = [
    #search
    path('artifact/tabulate/', views.tabulate_artifact, name='tabulate_artifact'),
    path('search/', views.search, name='search'),

    path('artifact/<uuid:artifact_uuid>/', views.detail_artifact, name='detail_artifact'),
    re_path(r'artifact/(?P<artifact_dice>[A-z]*-[A-z]*-[A-z]*)/$', views.detail_artifact_dice, name='detail_artifact_dice'),

    path('group/<uuid:group_uuid>/favourite/', views.favourite_group, name='group_favourite'),
    path('group/<uuid:group_uuid>/', views.group_artifact, name='group_artifact'),
    re_path(r'group/(?P<group_dice>[A-z]*-[A-z]*-[A-z]*)/$', views.group_artifact_dice, name='group_artifact_dice'),

    path('process/<uuid:process_uuid>/', views.detail_process, name='detail_process'),
    path('chain/<uuid:pgroup_uuid>/favourite/', views.favourite_pgroup, name='pgroup_favourite'),
    path('chain/<uuid:group_uuid>/', views.group_process, name='group_process'),

    path('accounts/profile/', views.profile, name='profile'),

    # API
    #path(r'api/command/update/$', csrf_exempt(views.update_command), name='update_command'),
    #path(r'api/command/new/$', csrf_exempt(views.new_command), name='new_command'),
    #path(r'api/resource/meta/$', csrf_exempt(views.tag_meta), name='tag_meta'),
    #path(r'api/resource/group/$', csrf_exempt(views.group_resources), name='group_resources'),

    path('api/checkin/', csrf_exempt(views.api_checkin_tube), name='api_checkin'),
    path('api/extract/', csrf_exempt(views.api_extract), name='api_extract'),
    #path('api/pipeline/', csrf_exempt(views.api_add_pipeline), name='api_pipeline'),

    path('api/tubecontainer/add/', csrf_exempt(views.api_checkin_container), name="api_add_tubecontainer"),
    path('api/dm/hello/', csrf_exempt(views.api_hello), name="api_hello"),

    path('dm/<uuid:uuid>/', views.barcode, name="barcode"),

    # FORMS ####################################################################
    path('forms/testsample/', views.form_sampletest, name='form_sampletest'),
    path('forms/register/', account_views.form_register, name='form_register'),
    
    # OCARINA ##################################################################
    path('ocarina/api/command/update/', csrf_exempt(views.ocarina_update_command), name='ocarina_update_command'),
    path('ocarina/api/command/new/', csrf_exempt(views.ocarina_new_command), name='ocarina_new_command'),
    path('ocarina/api/group/view/', csrf_exempt(views.ocarina_view_group), name='ocarina_view_group'),


    # Home
    path('', views.home, name='home'),
]