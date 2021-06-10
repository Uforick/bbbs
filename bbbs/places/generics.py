
from rest_framework import generics


class CreateUpdateAPIView(generics.CreateAPIView,
                          generics.UpdateAPIView,
                          generics.GenericAPIView):
    """
    Concrete view for creating, updating a model instance.
    """
    pass
