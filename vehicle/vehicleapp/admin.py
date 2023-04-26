from django.contrib import admin
from .models import Vehicle
# Register your models here.

#admin.site.register(Vehicle)

class ReadOnlyAdminMixin:
    def has_add_permission(self, request):
        if request.user.has_perm('vehicleapp.add_vehicle'):
            return True
        else:
            return False
        
    def has_change_permission(self, request, obj = None):
        if request.user.has_perm('vehicleapp.change_vehicle'):
            return True
        else:
            return False
    def has_view_permission(self, request, obj = None):
        if request.user.has_perm('vehicleapp.view_vehicle'):
            return True
        else:
            return False
        
    def has_delete_permission(self, request, obj = None):
        if request.user.has_perm('vehicleapp.delete_vehicle'):
            return True
        else:
            return False

@admin.register(Vehicle)
class VehicleAdmin(ReadOnlyAdminMixin, admin.ModelAdmin):
    list_display = ("vehicleNumber",)

    

