from django.contrib import admin
from tp_subject.models.community_engagement import CommunityEngagement
#from tp_screening.admin_site import tp_screening_admin


#@admin.register(SubjectScreening, site=tp_screening_admin)
class CommunityEngagementAdmin(admin.ModelAdmin):

    radio_fields = {
        'how_active': admin.VERTICAL,
        'voted': admin.VERTICAL,
        'major_problems': admin.VERTICAL,
        'work_together': admin.VERTICAL}


admin.site.register(CommunityEngagement, CommunityEngagementAdmin)