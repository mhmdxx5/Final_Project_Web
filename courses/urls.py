from django.contrib import admin
from django.urls import path,include
from project import views
from django.conf.urls.static import static
from django.conf import settings
from courses import views as views_c
urlpatterns = [
    path('',views_c.courses,name='courses'),
    path('addcourse/',views_c.addcourse,name='addcourse'),
    path('updatecourse/<int:course_pk>',views_c.updatecourse,name='updatecourse'),
    path('deletecourse/<int:course_pk>',views_c.deletecourse,name='deletecourse'),
    path('coursesList/',views_c.courseslist,name='courseslist'),
    path('coursesList/viewcourse/<int:course_pk>',views_c.viewcourse,name='viewcourse'),
]
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
