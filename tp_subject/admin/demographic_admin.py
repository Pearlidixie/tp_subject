from django.contrib import admin
from tp_subject.models.demographic import Demographic
#from tp_screening.admin_site import tp_screening_admin


#@admin.register(SubjectScreening, site=tp_screening_admin)
class DemographicAdmin(admin.ModelAdmin):

    radio_fields = {
        'marital_status': admin.VERTICAL,
        'lives_with': admin.VERTICAL}

    fieldsets = (
        (None, {
            'fields': (
                'marital_status',
                'number_wives',
                'number_wives_men',
                'lives_with',)
        }),

    )


admin.site.register(Demographic, DemographicAdmin)
