from .models import Cart ,Courses, UserCourses
from rest_framework import serializers


class CartSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cart
        fields = ['course_id','uid', 'cust_name', 'course_name','author_name','price','quantity','id','image']


class CourseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Courses
        fields = ['course_id','course_name','price','author_name','rating','image']

class UserCourseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserCourses
        fields = ['id','course_id','uid','course_name','author_name','price','rating','image']