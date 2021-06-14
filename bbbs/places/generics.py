
from rest_framework import generics


class CreateRetrieveAPIView(generics.CreateAPIView,
                            generics.RetrieveAPIView,
                            generics.GenericAPIView):
    """
    Concrete view for creating, updating a model instance.
    """
    pass
