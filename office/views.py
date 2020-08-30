from rest_framework.generics import CreateAPIView
from rest_framework.mixins import ListModelMixin

from .models import OfficeModel
from .serializers import OfficeSerializer, CitySerializer


class OfficeViev(ListModelMixin, CreateAPIView):
    serializer_class = OfficeSerializer
    queryset = OfficeModel.objects.all()

    def get(self, reuquest, *args, **kwargs):
        return self.list(reuquest, *args, **kwargs)


