from .models import Cart ,Courses
from rest_framework import serializers


class CartSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cart
        fields = "__all__"


class CourseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Courses
        fields = ['course_id','course_name','price','author_name','rating','image']