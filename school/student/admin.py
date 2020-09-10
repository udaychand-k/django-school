from django.contrib import admin

# Register your models here.
from .models import registration
#admin.site.register(Post);
#@admin.register(Post)
#class
@admin.register(registration)
class r(admin.ModelAdmin):
    list_display=('firstname','lastname',)
    ordering = ('username',)
    search_fields = ('firstname','lastname',)
