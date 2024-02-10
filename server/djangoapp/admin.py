from django.contrib import admin
# from .models import related models
from .models import CarMake, CarModel

# Register your models here.

#admin.site.register(CarMake)
#admin.site.register(CarModel)
# CarModelInline class
class CarModelInline(admin.StackedInline):
    #fields = ['name', 'dealer_id', 'type','year','model']
    model = CarModel 
    extra = 5
    print("Me")
# CarModelAdmin class
class CarModelAdmin(admin.ModelAdmin):
    fields = ['name', 'dealer_id', 'type','year','model']

# CarMakeAdmin class with CarModelInline
class CarMakeAdmin(admin.ModelAdmin):
    fields = ['name', 'description']
    inlines = [CarModelInline]
# Register models here
admin.site.register(CarMake, CarMakeAdmin)
admin.site.register(CarModel, CarModelAdmin)
#admin.site.register(CarMakeAdmin, CarModelInline)