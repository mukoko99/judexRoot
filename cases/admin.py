from django.contrib import admin
from .models import Judge, DefendantGroup, Defendant, Case, Charge, JudgeGroup, Convict, Prison

# Register your models here.
class CaseAdmin(admin.ModelAdmin):
    list_display = ('id', 'defendant', 'get_charges', 'judge', 'region', 'sentence', 'bail', 'jury', 'defendantGroup', 'judgeGroup')
    ordering = ('defendant', 'judge')
    search_fields =  ('defendant', 'judge', 'get_charges()')

class ConvictAdmin(admin.ModelAdmin):
    list_display = ('firstName', 'lastName', 'middleName', 'DIN', 'facility', 'status')
    search_fields = ('DIN', 'facility', 'status', 'lastName', 'middleName', 'firstName', 'age', 'gender', 'race')

admin.site.register([Judge, JudgeGroup, Defendant, DefendantGroup, Charge, Prison])
admin.site.register(Case, CaseAdmin)