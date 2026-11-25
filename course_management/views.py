from django.shortcuts import render,get_object_or_404

# Create your views here.
# from rest_framework.generic import ListAPIView
from rest_framework.views import APIView
from course_management.serializers import CourseSerializer
from rest_framework import authentication,permissions
from course_management.models import Course
from rest_framework.response import Response


# class CourseListCreateView(ListAPIView):
#     serializer = CourseSerializer

#     authentication_classes=[authentication.TokenAuthentication]
#     permission_classes=[permissions.IsAuthenticated]
#     def get_quaryset(self):
#         return Course.objects.filter(trainer=self.request.user)


class CourseListCreateView(APIView):

    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]

    def get(self,request):
        qs=Course.objects.filter(trainer=request.user)
        serializer_instance=CourseSerializer(qs,many=True)

        return Response(serializer_instance.data)

    def post(self,request):
        form_data=request.data
        serializer_instance=CourseSerializer(data=form_data)
        if serializer_instance.is_valid():
            serializer_instance.save(trainer=request.user)
            return Response(serializer_instance.data)
        else:
            return Response(serializer_instance.errors)

class CourseRetrieveUpdateDeleteView(APIView):
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]

    def get(self,request,pk=None):
        qs=get_object_or_404(Course,id=pk)
        serializer_instance=CourseSerializer(qs)
        return Response(serializer_instance.data)

    def put(self,request,pk=None):
        form_data=request.data
        instance=get_object_or_404(Course,id=pk)
        serializer_instance=CourseSerializer(data=form_data,instance=instance)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(serializer_instance.data)
        else:
            return Response(serializer_instance.data)

    def delete(self,request,pk=None):
        qs=get_object_or_404(Course,id=pk)
        qs.delete()
        return Response({"message":"deleted"})




