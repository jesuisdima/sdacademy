from django.contrib import admin
from courses.models import Course, Lesson

class LessonInline(admin.TabularInline):
    model = Lesson
    fieldsets = [(None, {'fields': ['subject', 'description', 'order']})
    ]
    extra = 0

class CourseAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ['name', 'short_description']
    inlines = [LessonInline]

admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson)