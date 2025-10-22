from django.contrib import admin
from course.models import Category,Course,Lesson
from django.utils.safestring import mark_safe

from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget

class LessonForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget)
    class Meta:
        model = Lesson
        fields = '__all__'

class CourseAdmin(admin.ModelAdmin):
    list_display = ['id','subject','created_date','active']
    search_fields = ['subject']
    list_filter = ['id','subject','created_date']

    readonly_fields = ['image_view']

    def image_view(self,course):
        return mark_safe(f"<img src='/static/{course.image.name}' width='120' />")

    class Media:
        css = {
            'all': ('/static/css/style.css',)
        }
class LessonAdmin(admin.ModelAdmin):
    form = LessonForm

admin.site.register(Category)
admin.site.register(Course,CourseAdmin)
admin.site.register(Lesson,LessonAdmin)
