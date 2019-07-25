from django.contrib import admin
from .models import disease, medicine

# Register your models here.

class MedInline(admin.TabularInline):
    model = medicine
    extra = 3
    
class DiseaseAdmin(admin.ModelAdmin):
    fieldsets = [
        ('disease_name', {'fields': ['dis_name']})
    ]
    inlines = [MedInline]

admin.site.register(disease, DiseaseAdmin)
