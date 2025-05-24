from rest_framework import viewsets
from .models import Planet  # Import the Planet model
from .serializers import PlanetSerializer  # Import the serializer for the Planet model

# --- PLANET VIEWSET ---

class PlanetViewSet(viewsets.ModelViewSet):
    queryset = Planet.objects.all()  # Define the queryset for all Planet records
    serializer_class = PlanetSerializer  # Specify the serializer to use

