from django.urls import path
from . import views

app_name = 'visitors_card_app'

urlpatterns = [
    path('index/', views.index, name='index'),
    # 入力フォーム
    path('welcome/', views.welcome, name='welcome'),
    path('welcome_widget/', views.welcome_widget, name='welcome_widget'),
    path('confirm/', views.confirm, name='confirm'),
    path('thankyou/', views.sent, name='sent'),
    # 情報閲覧管理者画面
    path('history/<int:page>/', views.history, name='history'),
    path('history/1/', views.history, name='history_default'),
    path('detail/<int:pk>/', views.detail, name='detail'),
    path('confirm_contact/<int:pk>/', views.confirm_contact, name='confirm_contact'),
    path('sent_contact/<int:pk>/', views.sent_contact, name='sent_contact'),

    path('update_visitors/<int:pk>/', views.VisitorsUpdate.as_view(), name='update_visitors'),
    path('update_contact/<int:pk>/<int:id>/', views.ContactUpdate.as_view(), name='update_contact'),
    # path('update_contact_all/<int:pk>/', views.VisitorsContactUpdateFormSetView.as_view(), name='update_contact_all'),
    path('update_allpost/<int:pk>/', views.update_allpost, name='update_allpost'),

    path('delete_contact/<int:pk>/', views.ContactDelete.as_view(), name='delete_contact'),
    path('delete_contact_all/<int:pk>/', views.VisitorsDelete.as_view(), name='delete_contact_all'),

    # 集計情報メニューのpath
    path('analysis_index/', views.analysis_index, name='analysis_index'),
    path('list_company/', views.list_company, name='list_company'),
    path('list_name/', views.list_name, name='list_name'),
    path('list_interviewer/', views.list_interviewer, name='list_interviewer'),
    path('list_history/', views.list_history, name='list_history'),
]