from django.conf.urls import url

from kladaba import views

urlpatterns = [
    url(r'^exams/?', views.ExamListView.as_view(), name='exams_list'),
    url(r'^exam/(\d+)/?', views.exam_detail, name='exam_detail'),
]