import csv
from django.http import HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated

from course.models import Course
from course.serilaizer import CourseSerializer


class CourseDetailAPIView(APIView):
    def get_object(self, course_id):
        try:
            return Course.objects.get(id = course_id)   
        except Course.DoesNotExist as e:
            return Response({'error': str(e)})

    def get(self, request, course_id):
        company = self.get_object(course_id)
        serializer = CourseSerializer(company)
        return Response(serializer.data)

    def put(self, request, course_id):
        category = self.get_object(course_id)
        serializer = CourseSerializer(instance=category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({'error': serializer.errors})

    def delete(self, request, course_id):
        category = self.get_object(course_id)
        category.delete()

        return Response({'deleted': True})


class CourseListAPIView(APIView):
    def get(self, request):
        companies = Course.objects.all()
        serializer = CourseSerializer(companies, many=True)
        return Response(serializer.data)

    def post(self, request, ):
        serializer = CourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, 201)
        return Response({'error': serializer.errors},
                        status=status.HTTP_500_INTERNAL_SERVER_ERROR)








# 
# 
# def open_csv(request):
#     response = HttpResponse(content_type='text/csv')
#     writer = csv.writer(response)
#     writer.writerow(['id', 'week', 'data'])
#     for stat in Statistics_week.objects.all().values_list('id', 'week', 'data'):
#         writer.writerow(stat)
# 
#     response['Content-Disposition'] = 'attachment; filename = "stat.csv"'
#     return response
#
# @permission_classes([IsAuthenticated])
# @api_view(['GET', 'POST'])
# def statistics_list(request):
#     if request.method == 'GET':
#
#         categories = Statistics_week.objects.all()
#         serializer = StatisticsSerializer(categories, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#     elif request.method == 'POST':
#         serializer = StatisticsSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response({'error': serializer.errors}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# 
# class StatisticsListAPIView(APIView):
#     permission_classes = (IsAuthenticated,)
# 
#     def get(self, request):
#         companies = Statistics_week.objects.all()
#         serializer = StatisticsSerializer(companies, many=True)
#         return Response(serializer.data)
# 
#     def post(self, request, ):
#         serializer = StatisticsSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response({'error': serializer.errors},
#                         status=status.HTTP_500_INTERNAL_SERVER_ERROR)
# 
# 
# class StatisticsDetailAPIView(APIView):
#     permission_classes = (IsAuthenticated, )
#     def get_object(self, statistics_week_id):
#         try:
#             return Statistics_week.objects.get(id= statistics_week_id)
#         except Course.DoesNotExist as e:
#             return Response({'error': str(e)})
# 
#     def get(self, request, statistics_week_id):
#         company = self.get_object(statistics_week_id)
#         serializer = StatisticsSerializer(company)
#         return Response(serializer.data)
# 
#     def put(self, request, statistics_week_id):
#         category = self.get_object(statistics_week_id)
#         serializer = StatisticsSerializer(instance=category, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response({'error': serializer.errors})
# 
#     def delete(self, request, statistics_week_id):
#         category = self.get_object(statistics_week_id)
#         category.delete()
# 
#         return Response({'deleted': True})





#
# @api_view(['GET'])
# def categoryproducts(request, category_id):
#     try:
#         categories = Category.objects.get(id=category_id)
#     except Category.DoesNotExist as e:
#         return Response({'error': str(e)})
#
#     if request.method == 'GET':
#         products = categories.products.all()
#         serializer = ProductSerializer(products, many=True)
#         return Response(serializer.data)
#
#
# # CRUD AND SERIALIZER DONE
# @api_view(['GET', 'POST', 'DELETE'])
# def products_list(request):
#     if request.method == 'GET':
#         products = Product.objects.all()
#         serializer = ProductSerializer(products, many=True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = ProductSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response({'error': serializer.errors}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
#
#
# @api_view(['GET', 'PUT', 'DELETE'])
# def product_detail(request, product_id):
#     try:
#         products = Product.objects.get(id=product_id)
#     except Product.DoesNotExist as e:
#         return Response({'error': str(e)})
#     if request.method == 'GET':
#         serializer = ProductSerializer(products)
#         return Response(serializer.data)
#
#     elif request.method == 'PUT':
#         serializer = ProductSerializer(instance=products, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response({'error': serializer.errors})
#
#     elif request.method == 'DELETE':
#         products.delete()
#         return Response({'deleted': True})
#
#
# # order
#
# class OrdersListAPIView(APIView):
#     def get(self, request):
#         orders = Order.objects.all()
#         serializer = OrderSerializer(orders, many=True)
#
#         return Response(serializer.data)
#
#     def post(self, request):
#         serializer = OrderSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response({'error': serializer.errors},
#                         status=status.HTTP_500_INTERNAL_SERVER_ERROR)
#
# class CategoryProductAPIView(APIView):
#     #permission_classes = (IsAuthenticated, )
#     def get_object(self, id):
#         try:
#             return Category.objects.filter(id=id)
#         except Category.DoesNotExist as e:
#             return Response({'error': str(e)})
#
#     def get(self, request, category_id):
#         products = self.get_object(category_id)
#         serializer = ProductSerializer(products, many=True)
#         return Response(serializer.data)