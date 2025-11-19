from course.models import Category,Course,Lesson,Tag,User
from rest_framework import serializers

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields=['id','name']

class ItemSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        data=super().to_representation(instance)
        data['image']=instance.image.url

        return data

class CourseSerializer(ItemSerializer):
    class Meta:
        model=Course
        fields=['id','subject','created_date','image']
class LessonSerializer(ItemSerializer):
    class Meta:
        model=Lesson
        fields=['id','subject','image','created_date']

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model=Tag
        fields=['id','name']

class LessonDetailSerializer(LessonSerializer):
    tags=TagSerializer(many=True)
    class Meta:
        model=LessonSerializer.Meta.model
        fields=LessonSerializer.Meta.fields+['content','tags']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password','avatar']
        extra_kwargs={
            'password':{
                'write_only':True
            }
        }

    def to_representation(self, instance):
        data=super().to_representation(instance)
        data['avatar']=instance.avatar.url

        return data

    def create(self, validated_data):
        user=User(**validated_data)
        user.set_password(user.password)
        user.save()

        return user
