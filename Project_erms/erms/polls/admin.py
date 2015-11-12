from django.contrib import admin

# Register your models here.
from .forms import InfoBasicForm
from .models import InfoBasic

class InfoAdmin(admin.ModelAdmin):
    form = InfoBasicForm
   #list_display = ['__unicode__', 'timestamp', 'updated']
    #class Meta:
    #   model = InfoBasic

admin.site.register(InfoBasic, InfoAdmin)
