from django.contrib import admin
from .models import language, code

# Register your models here.


class codeAdmin(admin.ModelAdmin):
    date_hierarchy = 'updated_on'
    # This will show fields on admin Panel Update/inert
    fields = ('title', 'code', 'keywords', 'language', 'status', 'updated_on')
    list_display = ('title', 'keywords', 'language', 'updated_on')
    # list_display_links = ('title',)
    list_filter = ['keywords', 'language']
    search_fields = ['title', 'keywords']
    list_per_page = 10
    # '-' is used to display oject in descending order
    ordering = ['-updated_on']


admin.site.register(language)
admin.site.register(code, codeAdmin)
