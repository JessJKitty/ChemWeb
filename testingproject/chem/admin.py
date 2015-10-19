from django.contrib import admin

# Register your models here.
from chem.models import Category, Page, UserProfile, Question, Choice


class PageAdmin(admin.ModelAdmin):
	list_display = ('title', 'category', 'url')

admin.site.register(Category)
admin.site.register(Page, PageAdmin)
admin.site.register(UserProfile)
admin.site.register(Question)
admin.site.register(Choice)