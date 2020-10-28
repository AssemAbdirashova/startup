from rest_framework import serializers

from course.models import Course


class CourseSerializer(serializers.ModelSerializer):
    # category = CategorySerializer2(read_only=True)
    # category_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Course
        fields = '__all__'
