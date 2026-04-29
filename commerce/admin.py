from django.contrib import admin
from commerce import models
# Register your models here.

from django.utils.html import format_html

from import_export.admin import ImportExportModelAdmin

from rest_framework.authtoken.models import TokenProxy

admin.site.unregister(TokenProxy)

admin.site.site_header = 'منظومة تسجيل الطلاب'
admin.site.site_title = 'أحمد رشاد'

# admin.site.site_header = 'أحمد رشاد'
# admin.site.site_title = 'أحمد رشاد'

# from rest_framework.authtoken.models import Token

# admin.site.unregister(Token)
# class CustomerAdmin(admin.ModelAdmin):
#     list_display = ("name","age","address","phone_number","national_id","created_at","disability_degree","disability_type","request_type")



# @admin.register(models.Customer)
# class PromotinCSV(ImportExportModelAdmin, CustomerAdmin):
#     pass

# admin.site.unregister(Token)
# class CustomerAdmin(admin.ModelAdmin):
#     list_display = ("name","age","address","phone_number","national_id","created_at","disability_degree","disability_type","request_type")


from django.contrib import admin
from .models import Student, Course, Enrollment


class EnrollmentInline(admin.TabularInline):
    model = Enrollment
    extra = 1


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'age', 'university_id')
    search_fields = ('name', 'university_id')
    list_filter = ('age',)
    inlines = [EnrollmentInline]


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'code', 'credit_hours')
    search_fields = ('name', 'code')
    list_filter = ('credit_hours',)


@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'student', 'course', 'enrolled_at')
    search_fields = ('student__name', 'course__name')
    list_filter = ('course', 'enrolled_at')