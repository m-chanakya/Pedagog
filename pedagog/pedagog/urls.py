"""pedagog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from user import views as uviews
from forums import views as fviews

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', uviews.index, name="index"),
    url(r'^account/login$', uviews.login.as_view(), name="login"),
    url(r'^account/signup$', uviews.login.as_view(), name="signup"),
    url(r'^forum/topics$',  fviews.topics, name="forum_topics"),
    url(r'^forum/threads$',  fviews.threads, name="forum_threads"),
    url(r'^forum/questions$',  fviews.questions, name="forum_questions"),
    url(r'^forum/question$',  fviews.question, name="forum_question")
]
