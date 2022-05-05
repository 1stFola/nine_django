from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.views import APIView

from .models import Native

from .models import Project

from .serializers import ProjectSerializer


class ProjectView(APIView):

    def post(self, request):
        data = request.data
        try:
            native = Native.objects.get(first_name=data['native'])
        except Native.DoesNotExist:
            return Response({"status": "notFound"})
        data['native'] = native.id
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


    def get(self, request):
        project = Project.objects.all()
        if len(project) <= 0:
            return Response({'status': 'error', 'data': "", 'message': 'no project found'})
        serializer = ProjectSerializer(project, many=True)
        return Response({'status': 'success', 'data': serializer.data})


class ProjectCrudView(APIView):

    def get(self, request, pk):
        try:
            project = Project.objects.get(pk=pk)
        except Project.DoesNotExist:
            return Response({'status': 'error', 'data': "", 'message': 'no project found'})
        serializer = ProjectSerializer(project)
        return Response({'status': 'success', 'data': serializer.data})

    def put(self, request, pk):
        try:
            project = Project.objects.get(pk=pk)
        except Project.DoesNotExist:
            return Response({'status': 'error', 'data': "", 'message': 'project not found'})            
        serializer = ProjectSerializer(project,  data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
        
        
    def delete(self, request, pk):
        try:
            project = Project.objects.get(pk=pk)
        except Project.DoesNotExist:
            return Response({'status': 'error', 'data': "", 'message': 'no project found'})
        project.delete()
        return Response({'status': 'success', 'data': "", 'message': 'project deleted successfully'})
    
    

# class ProjectViewSet(viewsets.ModelViewSet):
#     serializer_class = ProjectSerializer
#     queryset = Project.objects.all() 


# Create your views here.
# class ProjectViewSet(viewsets.ModelViewSet):
#     @action(detail=False, methods=['get'])
#     def call_fola(self, request):
#         return Response({})