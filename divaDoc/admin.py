from django.contrib import admin
from .models import Testdoc, TestChoice

# Register your models here.

class TestChoiceInline(admin.TabularInline):
    model = TestChoice
    extra = 3

class TestdocAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Type', {'fields': ['d_type']}),
    ]
    inlines = [TestChoiceInline]

admin.site.register(Testdoc, TestdocAdmin)
#admin.site.register(TestChoice)
#admin.site.register(Patient)

