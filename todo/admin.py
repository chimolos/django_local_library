from django.contrib import admin
from . models import Todo, Category, Profile, Plan, Appraisal

# Register your models here.

class TodoAdmin(admin.ModelAdmin):
    list_display = ('title','user', 'category', 'date_created', 'completed_status', 'decision')
    list_filter = ('title', 'category',)
    list_display_links = ('title', 'category', 'user')

class CategoryAdmin(admin.ModelAdmin):
    list_display =('myCategory', 'user')
    list_filter = ('myCategory', 'user')
    list_display_links =['user']

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id','user','address','email', 'phone_number', 'plan')
    list_filter = ('address',)
    list_display_links = ('user','address', 'phone_number')

class AppraisalAdmin(admin.ModelAdmin):
    list_display =('rate', 'experience', 'thoughts')
    list_filter =('rate',)

class PlanAdmin(admin.ModelAdmin):
    list_display =('your_plans', 'alternatives')

admin.site.register(Todo, TodoAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Plan, PlanAdmin)
admin.site.register(Appraisal, AppraisalAdmin)


