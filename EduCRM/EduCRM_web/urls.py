"""EduCRM URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from EduCRM_web.integral import views as intergral
from EduCRM_web.inter_skill import views as inter_skill
from EduCRM_web.message_commu import views as message_commu
from EduCRM_web.message_publish import views as message_publish
from EduCRM_web.parents import views as parents
from EduCRM_web.person_cent import views as person_cent
from EduCRM_web.score_query import views as score_query
from EduCRM_web.smart import views as smart
from EduCRM_web.user_manage import views as user_manage

urlpatterns = [
    path('sadmin/', user_manage.index),
    path('parents_register/', parents.Parents_Register),
    path('parents_login/', parents.Parents_Login),
    path('sadmin/teacher_login/', user_manage.Teacher_Login),
    path('', parents.index),
    path('logout/', parents.logout),

]
