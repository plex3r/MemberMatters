from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('signin/', auth_views.login, name='signin'),
    path('signup/', views.signup, name='signup'),
    path('signout/', auth_views.logout, {'next_page': '/loggedout'}, name='signout'),
    path('loggedout/', views.loggedout, name='loggedout'),
    path('profile/', views.profile, name='profile'),
    path('profile/password/', views.change_password, name='change_password'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('profile/spacebucks/history/', views.manage_spacebucks, name='manage_spacebucks'),
    path('profile/spacebucks/add/', views.add_spacebucks, name='add_spacebucks'),
    path('profile/spacebucks/add/<int:amount>', views.add_spacebucks, name='add_spacebucks'),
    path('profile/spacebucks/paymentdetails/save/', views.add_spacebucks_payment_info, name='add_spacebucks_payment_info'),
    path('profile/spacebucks/paymentdetails/delete/', views.delete_spacebucks_payment_info, name='delete_spacebucks_payment_info'),
    path('profile/access/view/', views.access_permissions, name='access_permissions'),
    path('profile/theme/edit/', views.edit_theme_song, name='edit_theme_song'),
    path('members/list/', views.member_list, name='member_list'),
    path('members/recent/', views.recent_swipes, name='recent_swipes'),
    path('members/lastseen/', views.last_seen, name='last_seen'),
    path('member/<int:member_id>/edit/', views.admin_edit_member, name='admin_edit_member'),
    path('doors/', views.manage_doors, name='manage_doors'),
    path('door/add/', views.add_door, name='add_door'),
    path('door/<int:door_id>/edit/', views.edit_door, name='edit_door'),
    path('api/door/<int:door_id>/delete/', views.delete_door, name='delete_door'),
    path('api/door/<int:door_id>/open/', views.open_door, name='open_door'),
    path('api/door/<int:door_id>/grant/<int:member_id>/', views.admin_grant_door, name='admin_grant_door'),
    path('api/door/<int:door_id>/revoke/<int:member_id>/', views.admin_revoke_door, name='admin_revoke_door'),
    path('api/door/<int:door_id>/request/', views.request_access, name='request_access'),
    path('api/door/<int:door_id>/check/<int:rfid_code>/', views.check_access, name='check_access'),
    path('api/door/check/<int:rfid_code>/', views.check_access, name='check_access'),
    path('api/door/authorised/<int:door_id>/', views.authorised_tags, name='authorised_tags'),
    path('api/door/authorised/', views.authorised_tags, name='authorised_tags'),
    path('api/member/<int:member_id>/state/<str:state>/', views.set_state, name='set_state'),
    path('api/member/<int:member_id>/edit/', views.admin_edit_member, name='admin_edit_member'),
    path('api/member/<int:member_id>/access/', views.admin_edit_access, name='admin_edit_access'),
    path('api/member/<int:member_id>/logs/', views.admin_member_logs, name='admin_member_logs'),
    path('api/spacebucks/debit/', views.spacebucks_debit, name="spacebucks_debit"),
    path('api/member/<int:member_id>/email/welcome', views.resend_welcome_email, name='resend_welcome_email'),
    path('causes/', views.manage_causes, name='manage_causes'),
    path('cause/<int:cause_id>/delete/', views.delete_cause, name='delete_cause'),
    path('cause/<int:cause_id>/edit/', views.edit_cause, name='edit_cause'),
    path('cause/list/', views.list_causes, name='list_causes'),
    path('webcams/', views.webcams, name='webcams'),
    path('', views.home, name='home'),
    path('spacebug/report/', views.spacebug, name='report_spacebug')
]
