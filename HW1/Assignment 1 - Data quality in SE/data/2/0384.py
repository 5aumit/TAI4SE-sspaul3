from django.contrib import admin
from .models import Major,Student


class MajorAdmin(admin.ModelAdmin):
    list_display=['pk','major','num_of_women','num_of_men','isDelete','school']
    list_filter=['major']
    search_fields=['major']
    list_per_page=7


    fieldsets=[
        ("base",{"fields":['major','isDelete',]}),
        ("num",{"fields":['num_of_women','num_of_men']})
    ]
admin.site.register(Major,MajorAdmin)

class StudentsAdmin(admin.ModelAdmin):

    def gender(self):
        if self.gender:
            return"男"
        else:
            return"女"
    list_display=['sid','student_name','major',gender,'school','isDelete']
    list_filter=['student_name']
    search_fields=['student_name']
    list_per_page=6
admin.site.register(Student,StudentsAdmin)

