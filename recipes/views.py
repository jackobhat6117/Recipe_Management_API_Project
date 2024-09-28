from django.shortcuts import render
from .serializers import RecipesSerializer , User
from rest_framework import generics, permissions
from .models import Recipe
from .permissions import IsOwnerOrReadOnly
from django.db.models import Q
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter
from django.shortcuts import get_object_or_404
from rest_framework.exceptions import ValidationError
from rest_framework import status
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication


class RecipeCreateListView(generics.ListCreateAPIView):
    serializer_class = RecipesSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    authentication_classes = [JWTAuthentication]

    def get_queryset(self):
        return Recipe.objects.filter(user = self.request.user)
    
    def perform_create(self, serializer):
        return serializer.save(user = self.request.user) 


class RecipeDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = RecipesSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    authentication_classes = [JWTAuthentication]

    def get_queryset(self):
        return Recipe.objects.filter(user=self.request.user)

    def get_object(self):
        obj = get_object_or_404(Recipe, pk=self.kwargs.get('pk'), user=self.request.user)
        self.check_object_permissions(self.request, obj)  
        return obj

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            self.perform_update(serializer)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

class RecipeByCategoryView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = RecipesSerializer
    authentication_classes = [JWTAuthentication]

    def get_queryset(self):
        catagory = self.kwargs.get('catagory')
        queryset = Recipe.objects.filter(Category = catagory)

        if not queryset.exists():
            raise ValidationError(f"No recipes found for category: {catagory}")
        return queryset
    
    
class RecipeByIngredientView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = RecipesSerializer
    authentication_classes = [JWTAuthentication]

    def get_queryset(self):
        ingredient = self.kwargs.get('ingredient')
        queryset = Recipe.objects.filter(Ingredients = ingredient)

        if not queryset.exists():
            raise ValidationError( f"No recipes found for ingredients: {ingredient}")
        return queryset
        

class RecipeByMultipleIngredientsView(generics.ListAPIView):
    serializer_class = RecipesSerializer 
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    authentication_classes = [JWTAuthentication]
 
    def get_queryset(self):
        ingredients = self.request.query_params.getlist('ingredients')
        if not ingredients:
            raise ValidationError("You must provide at least one ingredient.")
        
        query = Q()
        for ingredient in ingredients:
            query &= Q(ingredients__icontains=ingredient)

        queryset = Recipe.objects.filter(query)
        if not queryset.exists():
            raise ValidationError(f"No recipes found with the given ingredients: {', '.join(ingredients)}")
        
        return queryset


class RecipeSearchFilterView(generics.ListAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipesSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    filterset_fields = ['Title', 'Category', 'Ingredients', 'Preparation_Time', 'Cooking_Time', 'Servings']
    ordering_fields = ['Preparation_Time', 'Cooking_Time', 'Servings']
    search_fields = ['Title', 'Category', 'Ingredients']
    ordering = ['Preparation_Time']


  

