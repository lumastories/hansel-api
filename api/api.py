from api.models import Kid

class KidList(generics.ListAPIView):
    serializer_class = KidSerializer

    def get_queryset(self):
        user = self.request.user
        return Kid.objects.filter(purchaser=user)
