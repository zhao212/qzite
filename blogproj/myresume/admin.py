from django.contrib import admin
from myresume.models import res_basic,res_education,res_project,res_work,res_skill,res_award
# Register your models here.

admin.site.register(res_basic)
admin.site.register(res_education)
admin.site.register(res_project)
admin.site.register(res_work)
admin.site.register(res_skill)
admin.site.register(res_award)
