from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from marketplace.tokens.models import Token, Purchase
from marketplace.tokens.api.v1.serializers import TokenSerializer, PurchaseSerializer
from marketplace.tokens.api.v1.filters import TokenFilter
from marketplace.tokens.api.v1.permissions import CanCreatePurchase, CantUpdateDelete
from marketplace.users.helpers import is_supporter, is_athlete


class TokenViewSet(viewsets.ModelViewSet):
    queryset = Token.objects.all()
    serializer_class = TokenSerializer
    permission_classes = [
        IsAuthenticated,
    ]
    filter_class = TokenFilter

    def perform_create(self, serializer):
        return serializer.save(athlete=self.request.user.athlete)


class PurchaseViewSet(viewsets.ModelViewSet):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer
    permission_classes = [
        IsAuthenticated,
        CantUpdateDelete,
        CanCreatePurchase,
    ]

    def get_queryset(self):
        queryset = super().get_queryset()
        if is_supporter(self.request.user):
            return queryset.filter(supporter__user=self.request.user)
        elif is_athlete(self.request.user):
            return queryset.filter(token__athlete__user=self.request.user)
        return queryset.none()

    def perform_create(self, serializer):
        return serializer.save(supporter=self.request.user.supporter)

