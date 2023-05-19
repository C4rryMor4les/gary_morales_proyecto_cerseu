from django.contrib import admin
from platos.models import Platos
# Register your models here.
#admin.site.register(Platos)
@admin.register(Platos)
class PlatosAdmin(admin.ModelAdmin):
    list_display = ('nombre','precio')
    list_filter = ('nombre','precio')
    search_fields = ('nombre','precio')
    fields = ('nombre','precio')
