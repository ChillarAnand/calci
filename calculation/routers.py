from swampdragon import route_handler
from swampdragon.route_handler import ModelPubRouter
from .models import Calculation
from .serializers import CalculationSerializer


class NotificationRouter(ModelPubRouter):
    valid_verbs = ['subscribe']
    route_name = 'calculations'
    model = Calculation
    serializer_class = CalculationSerializer


route_handler.register(NotificationRouter)
