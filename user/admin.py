from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import User, Student, Profile

# Resource classes for each model
class UserResource(resources.ModelResource):
    class Meta:
        model = User

class StudentResource(resources.ModelResource):
    class Meta:
        model = Student

class ProfileResource(resources.ModelResource):
    class Meta:
        model = Profile

# Admin classes for each model
@admin.register(User)
class UserAdmin(ImportExportModelAdmin):
    resource_class = UserResource
    list_display = ('username', 'email', 'date_joined')
    search_fields = ('username', 'email')

@admin.register(Student)
class StudentAdmin(ImportExportModelAdmin):
    resource_class = StudentResource
    list_display = ('user', 'student_code')
    search_fields = ('user__username', 'student_code')

@admin.register(Profile)
class ProfileAdmin(ImportExportModelAdmin):
    resource_class = ProfileResource
    list_display = ('user', 'role', 'email_verified')
    search_fields = ('user__username', 'role__role_name')
