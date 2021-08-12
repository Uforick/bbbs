from rest_framework import generics


class CreateRetrieveAPIView(generics.CreateAPIView,
                            generics.RetrieveAPIView,
                            generics.GenericAPIView):

    """
    Concrete view for creating and retrieving a model instance.
    """
    pass
