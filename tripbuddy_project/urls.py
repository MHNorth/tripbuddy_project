"""tripbuddy_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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

from django.conf.urls import url, include 
from django.contrib import admin
from django.urls import path
from apps.trip import views
from apps.trip.views import (
    ReviewCreate, 
    DashboardView, 
    TripDelete, 
    TripCreate, 
    TripDetail, 
    TripUpdate, 
    JoinTrip, 
    ReviewComment,
    CommentDetail,
    )





urlpatterns = [
    ##-------Home--------##
    path('admin/', admin.site.urls),
    path('', views.index, name='home'),

    ##-------Account Authorization Urls--------##
    path('accounts/', include('apps.accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
        
    ##-------Travel Plan Urls--------##
    path('dashboard', DashboardView.as_view(), name='dash'),
    path('join/<int:pk>/jointrip', JoinTrip.as_view(), name='join'),
    path('remove/<int:pk>/delete', TripDelete.as_view(), name='delete'),
    path('createtrip', TripCreate.as_view(), name='create'),
    path('detailview/<int:pk>/detail', TripDetail.as_view(), name='tripdetail'),
    path('updatetrip/<int:pk>/update', TripUpdate.as_view(), name='update'),



    ##-------Review Urls--------##
    path('createreview', ReviewCreate.as_view(), name='reviews'),
    path('createresponse/<int:pk>/comment', ReviewComment.as_view(), name='comments'),
    path('reviewdetail/<int:pk>/detail', views.ReviewDetail.as_view(), name='reviewdetail'),
    path('reviewdetail/<int:pk>/detail', views.CommentDetail.as_view(), name='commentdetail'),




]