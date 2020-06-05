from django.contrib import admin
from .models import *

admin.site.site_header = "Simple Todo Project"
admin.site.site_title = "Simple Todo Project"
admin.site.index_title = "Simple Todo Project"

class StudentsAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "email","group", "completed"]
    class Meta:
        model = Student
admin.site.register(Student, StudentsAdmin)