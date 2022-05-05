from argparse import Action
from unicodedata import name
from urllib import response
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.views import APIView
from .models import Cohort, Native

from .serializers import CohortSerializer, NativeSerializer

class CohortView(APIView):

    def post(self, request):
        data = request.data
        serializer = CohortSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    
    def get(self, request):
        cohort = Cohort.objects.all()
        if len(cohort) <= 0:
            return Response({'status': 'error', 'data': "", 'message': 'no Cohort found'})
        serializer = CohortSerializer(cohort, many=True)
        return Response({'status': 'success', 'data': serializer.data})

        
class CohortCrudView(APIView):
    def get(self, request, pk):
        try:
            cohort = Cohort.objects.get(pk=pk)
        except Cohort.DoesNotExist:
            return Response({'status': 'error', 'data': "", 'message': 'no Cohort found'})
        serializer = CohortSerializer(cohort)
        return Response({'status': 'success', 'data': serializer.data})


    def put(self, request, pk):
        try:
            cohort = Cohort.objects.get(pk=pk)
        except Cohort.DoesNotExist:
            return Response({'status': 'error', 'data': "", 'message': 'Cohort not found'})            
        serializer = CohortSerializer(cohort,  data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, pk):
        try:
            cohort = Cohort.objects.get(pk=pk)
        except Cohort.DoesNotExist:
            return Response({'status': 'error', 'data': "", 'message': 'no Cohort found'})
        cohort.delete()
        return Response({'status': 'success', 'data': "", 'message': 'Cohort deleted successfully'})
    



class NativeView(APIView):

    def post(self, request):
        data = request.data
        try:
            cohort = Cohort.objects.get(name=data['cohort'])
        except Cohort.DoesNotExist:
            return Response({"status": "notFound"})
        data['cohort'] = cohort.id
        serializer = NativeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


def get(self, request):
        native = Native.objects.all()
        if len(native) <= 0:
            return Response({'status': 'error', 'data': "", 'message': 'no Native found'})
        serializer = NativeSerializer(native, many=True)
        return Response({'status': 'success', 'data': serializer.data})


class NativeCrudView(APIView):

    def get(self, request, pk):
        try:
            native = Native.objects.get(pk=pk)
        except Native.DoesNotExist:
            return Response({'status': 'error', 'data': "", 'message': 'no Native found'})
        serializer = NativeSerializer(native)
        return Response({'status': 'success', 'data': serializer.data})



    def put(self, request, pk):
        try:
            native = Native.objects.get(pk=pk)
        except Native.DoesNotExist:
            return Response({'status': 'error', 'data': "", 'message': 'Native not found'})            
        serializer = NativeSerializer(native,  data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
        
        
    def delete(self, request, pk):
        try:
            native = Native.objects.get(pk=pk)
        except Native.DoesNotExist:
            return Response({'status': 'error', 'data': "", 'message': 'no Native found'})
        native.delete()
        return Response({'status': 'success', 'data': "", 'message': 'Native deleted successfully'})
    




# # Create your views here.
# class NativeViewSet(viewsets.ModelViewSet):
#     serializer_class = NativeSerializer
#     queryset = Native.objects.all()

   
    
#     @action(detail=False, methods=['get'])
#     def call_fola(self, request):
#         return Response({"status":"test"})
 

# class CohortViewSet(viewsets.ModelViewSet):
#     serializer_class = CohortSerializer
#     queryset = Cohort.objects.all()

#     @action(detail=False, methods=['get'])
#     def get_cohort_by_name(self, request):
#         cohort_name = self.request.query_params.get('cohort_name')
#         cohort = Cohort.objects.get(name=cohort_name)
#         serializer = CohortSerializer(cohort)
#         return Response(serializer.data)

 

# #  @action(detail=False, methods=['get'])
# #     def get_native(self, request):
# #         cohort_id = self.request.query_params.get('cohort_id')


#     def get_queryset(self):
#         user = self.kwargs.get("user", None)
#         if user is not None:
#             return Cohort.objects.filter(user=user)

#         return super().get_queryset()

