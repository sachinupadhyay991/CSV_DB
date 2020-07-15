from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Employee, Member

# Register your models here.
@admin.register(Employee, Member)
class Emp(ImportExportModelAdmin):
    pass
