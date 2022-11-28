from django.contrib import admin
from .models import Judge, DefendantGroup, Defendant, Case, Charge, JudgeGroup

# Register your models here.
class CaseAdmin(admin.ModelAdmin):
    list_display = ('id', 'defendant', 'get_charges', 'judge', 'region', 'sentence', 'bail', 'jury', 'defendantGroup', 'judgeGroup')
    ordering = ('defendant', 'judge')
    search_fields =  ('defendant', 'judge', 'get_charges()')

admin.site.register([Judge, JudgeGroup, Defendant, DefendantGroup, Charge])
admin.site.register(Case, CaseAdmin)