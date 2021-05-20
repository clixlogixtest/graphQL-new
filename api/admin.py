from django.contrib import admin
from api.models import Business

# admin.site.register(Business)

@admin.register(Business)
class BusinessAdmin(admin.ModelAdmin):
    search_fields = ('address', 'id', 'employee_size')