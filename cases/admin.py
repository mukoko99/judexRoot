from django.contrib import admin
from .models import Judge, DefendantGroup, Defendant, Case, Charge, JudgeGroup, Conviction, Prison

# Register your models here.
class CaseAdmin(admin.ModelAdmin):
    list_display = ('id', 'defendant', 'get_charges', 'judge', 'region', 'sentence', 'bail', 'jury', 'defendantGroup', 'judgeGroup')
    ordering = ('defendant', 'judge')
    search_fields =  ('defendant', 'judge', 'get_charges()')

class ConvictionAdmin(admin.ModelAdmin):
    def get_DOB(self, obj):
        return obj.defendant.DOB
    list_display = ('defendant', 'DIN', 'facility', 'status', 'get_DOB')
    search_fields = ('DIN', 'facility', 'status', 'get_DOB')
admin.site.register([Judge, JudgeGroup, Defendant, DefendantGroup, Charge, Prison])
admin.site.register(Case, CaseAdmin)
admin.site.register(Conviction, ConvictionAdmin)