from django.contrib import admin
from orders.models import Order,OrderedItem    

# Register your models here.1
class OrderAdmin(admin.ModelAdmin):
    list_filter=[
        "owner",
        "order_status",
    ]
    search_fields=(
        "owner",
        "id",
    )
admin.site.register(Order,OrderAdmin)
