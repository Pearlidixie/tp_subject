from django.contrib import admin
from tp_subject.models.education import Education
#from tp_screening.admin_site import tp_screening_admin


#@admin.register(SubjectScreening, site=tp_screening_admin)
class EducationAdmin(admin.ModelAdmin):

    radio_fields = {
        'working': admin.VERTICAL,
        'job_type': admin.VERTICAL,
        'work_done': admin.VERTICAL,
        'salary': admin.VERTICAL}


    #filter_horizontal = ('job_type', )


admin.site.register(Education, EducationAdmin)