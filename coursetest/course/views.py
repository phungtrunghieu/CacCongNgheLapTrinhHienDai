from rest_framework.decorators import action

from course import serializers,paginators
from rest_framework import viewsets,generics,parsers
from course.models import Category,Course,Lesson,User

class CategoryView(viewsets.ViewSet,generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = serializers.CategorySerializer

class CourseView(viewsets.ViewSet,generics.ListAPIView):
    queryset = Course.objects.filter(active=True)
    serializer_class = serializers.CourseSerializer
    pagination_class = paginators.ItemPagination

    def get_queryset(self):
        query=self.queryset

        q=self.request.query_params.get('q')
        if q:
            query=query.filter(subject__icontains=q)
        cate_id=self.request.query_params.get('category_id')
        if cate_id:
            query=query.filter(category_id=cate_id)
        return query

class LessonView(viewsets.ViewSet,generics.RetrieveAPIView):
    queryset = Lesson.objects.prefetch_related('tags').filter(active=True)
    serializer_class = serializers.LessonDetailSerializer

class UserView(viewsets.ViewSet,generics.CreateAPIView):
    queryset = User.objects.filter(is_active=True)
    serializer_class = serializers.UserSerializer
    parser_classes = [parsers.MultiPartParser]

    @action(methods=['get'],url_path='current-user',detail=False)
    def get_current_user(self,request):
        pass