from shoestore.shoeapp.models import Manufacturer, Shoe, ShoeColor, ShoeType
from rest_framework import viewsets
from shoestore.shoeapp.serializers import (
    ManufacturerSerializer, ShoeSerializer, ShoeColorSerializer, ShoeTypeSerializer)


class ManufacturerViewSet(viewsets.ModelViewSet):
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer


class ShoeViewSet(viewsets.ModelViewSet):
    queryset = Shoe.objects.all()
    serializer_class = ShoeSerializer


class ShoeColorViewSet(viewsets.ModelViewSet):
    queryset = ShoeColor.objects.all()
    serializer_class = ShoeColorSerializer


class ShoeTypeViewSet(viewsets.ModelViewSet):
    queryset = ShoeType.objects.all()
    serializer_class = ShoeTypeSerializer
