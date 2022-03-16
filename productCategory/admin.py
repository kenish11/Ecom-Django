from django.contrib import admin
from .models import Category

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('c_name',)}
    list_display = ('c_name','slug')

admin.site.register(Category,CategoryAdmin)


# Register your models here.
