import django_filters
from django.utils.translation import ugettext_lazy as _

from marketplace.campaigns.models import Campaign, Review


class CampaignFilter(django_filters.rest_framework.FilterSet):

    is_draft = django_filters.BooleanFilter(
        field_name='is_draft',
        help_text=_("Filter draft campaigns.")
    )
    kind = django_filters.CharFilter(
        field_name='kind',
        help_text=_("Filter campaigns by kind.")
    )
    state = django_filters.CharFilter(
        field_name='state',
        help_text=_("Filter campaigns by state.")
    )

    user = django_filters.NumberFilter(
        field_name='user__id',
        help_text=_("Filter campaigns by given user.")
    )
    followed_by = django_filters.NumberFilter(
        field_name="followers__id",
        help_text=_("Filter the athletes followed by the user given by ID.")
    )

    class Meta:
        model = Campaign
        fields = ["is_draft", "kind", "user", "followed_by"]


class ReviewFilter(django_filters.rest_framework.FilterSet):

    state = django_filters.CharFilter(
        field_name="state",
        help_text=_("Filter the reviews by the state.")
    )
    campaign = django_filters.NumberFilter(
        field_name='campaign__id',
        help_text=_("Filter reviews by campaign.")
    )

    class Meta:
        model = Review
        fields = ['state', 'campaign']