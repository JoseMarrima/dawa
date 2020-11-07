from django.contrib import admin
from clinicapp.models import Exam

admin.site.site_header = 'Dawa Admin'

class ExamAdmin(admin.ModelAdmin):
    list_display = ('name', 'passport', 'id','created_date', 'qr_code', 'result')

# Register your models here.
admin.site.register(Exam, ExamAdmin)