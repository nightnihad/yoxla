from django.contrib import admin
from .models import Addermodel,AreaCategorymodel,Commentarticle
# Register your models here.
@admin.register(Addermodel)
class Addadmin(admin.ModelAdmin):
    list_display=('name','author','wdate','udate')
    search_fields=('name','author')

admin.site.register(AreaCategorymodel)

@admin.register(Commentarticle)
class Commentadmin(admin.ModelAdmin):
    list_display=('author','wdate')
    search_fields=['name']
