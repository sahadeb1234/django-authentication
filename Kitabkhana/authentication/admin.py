from django.contrib import admin

# Register your models here.
from .models import(
   SliderImage
)

@admin.register(SliderImage)
class SliderImageModelAdmin(admin.ModelAdmin):
    list_display = ['id','image']