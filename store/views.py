from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView, ListCreateAPIView, CreateAPIView

from .models import TShort, Pants, Jacket, Bodysuit, Brand
from .serializers import TShortsListSerializer, TShortsCreateSerializer, BrandCreateSerializer


class BrandCreateView(CreateAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandCreateSerializer


class TShortListView(ListAPIView):
    queryset = TShort.objects.all()
    serializer_class = TShortsListSerializer


class TShortCreateView(CreateAPIView):
    queryset = TShort.objects.all()
    serializer_class = TShortsCreateSerializer


class TShortDetailView(RetrieveUpdateDestroyAPIView):
    queryset = TShort.objects.all()
    serializer_class = TShortsListSerializer
