from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    # path('hi/', views.hi, name='hi'),
    # path("<int:question_id>/", views.detail, name="detail"),
    # path("<slug:question_slug>/", views.detail, name="detail"),
    path("", views.QuestionList.as_view(), name="list"),
    # path("hi/", views.hi, name="index"),
    path("<int:pk>/",views.QuestionDetailView.as_view(), name="detail"),
    path("home/", views.HomeView.as_view(name="dear class"), name="home"),
    path("welcome/", views.HomeView.as_view(name="students"), name="home"),
    path("about/", views.AboutView.as_view(), name="about"),
    path("vote/<int:pk>/", views.VoteView.as_view(), name="vote"),
    path("create/question/", views.CreateQuestionView.as_view(), name="createquestion"),
    path("success/", views.SuccessView.as_view(), name="success"),
    path("create/question3/", views.CreateQuestionView3.as_view(), name="createquestion"),
]