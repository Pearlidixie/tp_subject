from tp_subject.models.community_engagement import CommunityEngagement
from django import forms


class CommunityEngagementForm(forms.ModelForm):
    class Meta:
        model = CommunityEngagement
        fields = '__all__'
