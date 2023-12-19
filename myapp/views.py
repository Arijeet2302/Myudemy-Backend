from django.shortcuts import render , HttpResponse
from myapp.models import Cart ,Courses
from rest_framework import viewsets , status
from myapp.serializers import CartSerializer , CourseSerializer
from rest_framework.permissions import AllowAny
from rest_framework.decorators import action
from rest_framework.response import Response


# Create your views here.

#self created
# def test(request):
#     # token = create_custom_token("IPPbeaQlEJgzzcPvgdChDeeNsCG3")
#     user = get_user("IPPbeaQlEJgzzcPvgdChDeeNsCG3")
#     email = user.email
#     return HttpResponse(email)

class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all().order_by("cust_name")
    serializer_class = CartSerializer
    permission_classes = [AllowAny]

    @action(detail=False, methods=['get'])
    def show(self,request):
        uid = request.query_params.get('uid')
        
        try:
            cartItems = Cart.objects.filter(uid=uid)
            serializer = CartSerializer(cartItems, many=True, context={'request': request})
            return Response(serializer.data)
        except Cart.DoesNotExist:
            return Response({'message': 'No cart items found.'})


    @action(detail=False, methods=['post'])
    def increment_quantity(self, request):
        incoming_data = request.data

        try:
            course = Cart.objects.get(cust_name=incoming_data['cust_name'],
                                      course_name=incoming_data['course_name']
                                    )
            course.quantity += 1
            course.save()
            return Response({'message': 'Quantity incremented in cart.'})
        except Cart.DoesNotExist:
            image_url = incoming_data['image']
            relative_path = image_url.split("https://myudemy-backend.vercel.app/")[-1]

            Cart.objects.create(uid=incoming_data['uid'], 
                                course_id_id=incoming_data['course_id'],
                                course_name=incoming_data['course_name'], 
                                cust_name=incoming_data['cust_name'], 
                                price=incoming_data['price'], 
                                author_name=incoming_data['author_name'], 
                                image = relative_path,
                                quantity=1
                                )
            return Response({'message': 'new added'})
       
    
    @action(detail=False, methods=['delete'], url_path='delete')
    def delete(self, request, *args, **kwargs):
        try :
            item_pk = request.query_params.get('item_no')
            items = Cart.objects.get(pk=item_pk)
            items.delete()
            return Response({'message': 'Cart Item has been removed'})
        except Cart.DoesNotExist:  
            return Response({'message': 'No cart items found.'})

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Courses.objects.all().order_by("course_id")
    serializer_class = CourseSerializer

    data = [
        {'course_id': 0, 'course_name': '100 Days of Code: The Complete Python Pro Bootcamp for 2023',
         'author_name':'Dr. Angela Yu', 'rating':4.6, 'price':1280, 'image':'static/2776760_f176_10.jpg'},
        {'course_id': 1, 'course_name': 'The complete Python Bootcamp From Zero To Hero',
         'author_name':'Jose Protilla', 'rating':4.4, 'price':8640, 'image':'static/2485240_d405_7.jpg'},
        {'course_id': 2, 'course_name': 'SQL Complete Bootcamp',
         'author_name':'AI Sweigart', 'rating':4.2, 'price':8640, 'image':'static/762616_7693_3.jpg'},
        {'course_id': 3, 'course_name': 'Python: Master Programming and Developement Within 15 Projects',
         'author_name':'Dev Nirwal', 'rating':3.8, 'price':8640, 'image':'static/567828_67d0.jpg'},
    ]

    for element in data:
        entry = Courses(**element)
        entry.save()
