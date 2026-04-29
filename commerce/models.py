from django.db import models
from django.utils.html import format_html

from accounts.models import UserAccount

# Create your models here.



class Student(models.Model):
    name = models.CharField(max_length=100, verbose_name="اسم الطالب")
    age = models.IntegerField(verbose_name="العمر")
    university_id = models.CharField(max_length=20, verbose_name="الكود الجامعي")

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "طالب"
        verbose_name_plural = "الطلاب"
    
    
class Course(models.Model):
    name = models.CharField(max_length=100, verbose_name="اسم الدورةالتعليمية")
    code = models.CharField(max_length=20, verbose_name="كود الدورة التعليمية")
    credit_hours = models.IntegerField(verbose_name="عدد ساعات الدورة التعليمية")

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "دورة تعليمية"
        verbose_name_plural = "الدورات التعليمية"
    
    
# class Enrollment(models.Model):
#     student = models.ForeignKey(Student, on_delete=models.CASCADE)
#     course = models.ForeignKey(Course, on_delete=models.CASCADE)
#     enrolled_at = models.DateTimeField(auto_now_add=True)

class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, verbose_name="الطالب")
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name="الدورة التعليمية")
    enrolled_at = models.DateTimeField(auto_now_add=True)

    # class Meta:
    #     unique_together = ('student', 'course')
    class Meta:
        verbose_name = "تسجيل"
        verbose_name_plural = "التسجيلات"
        constraints = [
            models.UniqueConstraint(fields=['student', 'course'], name='unique_enrollment')
        ]