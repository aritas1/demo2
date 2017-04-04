from django.contrib import admin
from kladaba.models import Exam, Lecture, Semester


# Register your models here.
class ExamAdmin(admin.ModelAdmin):
    # remove downloads flied from admin editing
    exclude = ('downloads', )

admin.site.register(Exam, ExamAdmin)

class LectureAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'ects',)
    list_display_links = ('id', 'title', )
    list_editable = ('ects', )
    search_fields = ('id', 'title', )
    ordering = ('-id',)

admin.site.register(Lecture, LectureAdmin)
admin.site.register(Semester)