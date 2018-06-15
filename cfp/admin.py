from django.contrib import admin
from cfp.models import Proposal
from ironcage.admin import OurActionsOnlyMixin


@admin.register(Proposal)
class ProposalAdmin(OurActionsOnlyMixin, admin.ModelAdmin):
    list_filter = ('session_type', )
    search_fields = ['proposer__name', 'title', 'description',
                     'description_private', 'outline']

    def get_fields(self, request, obj=None):
        if request.user.is_superuser:
            return ['id', 'proposer_name', 'session_type', 'title', 'subtitle',
                    'copresenter_names', 'description', 'description_private',
                    'outline', 'aimed_at_new_programmers', 'aimed_at_teachers',
                    'aimed_at_data_scientists', 'would_like_mentor',
                    'would_like_longer_slot', 'state', 'track',
                    'special_reply_required', 'scheduled_room',
                    'scheduled_time']

        return ['id', 'session_type', 'title', 'subtitle', 'description']

    def get_readonly_fields(self, request, obj=None):
        if request.user.is_superuser:
            return ['id', 'proposer_name', 'session_type', 'title', 'subtitle',
                    'copresenter_names', 'description', 'description_private',
                    'outline', 'would_like_mentor', 'would_like_longer_slot',
                    'state', 'track', 'scheduled_room', 'scheduled_time']

        return self.get_fields(request, obj)

    def get_list_display(self, request):
        return ('title', 'subtitle', 'proposer_name', 'session_type')

    def get_search_fields(self, request):
        if request.user.is_superuser:
            return ['proposer__name', 'title', 'subtitle', 'description',
                    'description_private', 'outline']

        return ['title', 'subtitle', 'description']

    def get_queryset(self, request):

        queryset = super().get_queryset(request)

        users_permissions = request.user.get_all_permissions()
        if ('cfp.review_education_proposal' in users_permissions
                and 'cfp.change_proposal' in users_permissions  # noqa: W503
                and 'cfp.review_proposal' not in users_permissions):  # noqa: W503
            return queryset.filter(session_type__in=[
                'kidsworkshop', 'teachersworkshop', 'teacherstalk'
            ])
        else:
            return queryset

    def proposer_name(self, obj):
        return obj.proposer.name
