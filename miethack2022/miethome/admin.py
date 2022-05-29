from django.contrib import admin

# Register your models here.
from miethome.models import Student


class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'birth_date', 'room')
    list_display_links = ('id', 'full_name')
    search_fields = ('id', 'full_name')


admin.site.register(Student, StudentAdmin)
