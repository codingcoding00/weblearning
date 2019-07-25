from django.contrib import admin
from .models import disease, excercise

# Register your models here.

class ExInline(admin.TabularInline):
    model = excercise
    extra = 3
    
class DiseaseAdmin(admin.ModelAdmin):
    fieldsets = [
        ('disease_name', {'fields': ['dis_name']})
    ]
    inlines = [ExInline]

admin.site.register(disease, DiseaseAdmin)
