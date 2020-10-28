from django.urls import path

from course.views import CourseListAPIView, CourseDetailAPIView

urlpatterns = [
     path('course/', CourseListAPIView.as_view()),
     path('course/<int:course_id>/', CourseDetailAPIView.as_view()),

]
