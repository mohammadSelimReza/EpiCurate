import django_filters
from .models import Food


class FoodFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr="iexact")

    class Meta:
        model = Food
        fields = ["price", "category", "brand"]
