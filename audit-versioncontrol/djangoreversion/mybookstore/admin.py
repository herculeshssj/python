from django.contrib import admin
from .models import Client, Book, SellOrder, SellOrderItem, BorrowRequest, BorrowedBook
from reversion.admin import VersionAdmin

# Register your models here.
admin.site.site_header = "My Bookstore Admin"
admin.site.site_title = "My Bookstore Admin Portal"
admin.site.index_title = "Welcome to My Bookstore Admin"

admin.site.register(Client)
admin.site.register(Book)
admin.site.register(SellOrder)
admin.site.register(SellOrderItem)
admin.site.register(BorrowRequest)
admin.site.register(BorrowedBook)

