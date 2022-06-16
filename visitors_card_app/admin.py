from django.contrib import admin
from .models import CustomUser, Visitors, Post, Member, Contact
# Register your models here.
admin.site.register(CustomUser)


class ContactInline(admin.StackedInline):
    model = Contact


class VisitorAdmin(admin.ModelAdmin):
    inlines = [ContactInline]

admin.site.register(Visitors, VisitorAdmin)
admin.site.register(Post)
admin.site.register(Member)
admin.site.register(Contact)