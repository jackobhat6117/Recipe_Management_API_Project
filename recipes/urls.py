from django.urls import path
from .views import  Recipe, RecipeDetailView, RecipeCreateListView, RecipeByCategoryView, RecipeByIngredientView, RecipeSearchFilterView, RecipeByMultipleIngredientsView

urlpatterns = [
    path('recipe/', RecipeCreateListView.as_view(), name='recipe'),
    path('recipe/<int:pk>/', RecipeDetailView.as_view(), name = 'recipe-detail'),
    path('recipe/catagory/<str:catagory>/', RecipeByCategoryView.as_view(), name = 'recipe-by-catagory'),
    path('recipe/ingredient/<str:ingredient>/', RecipeByIngredientView.as_view(), name='recipe-by-ingredient'),
    path('recipe/search/', RecipeSearchFilterView.as_view(), name = 'recipe-search-filter'),
    path('recipes/multipleingredient/', RecipeByMultipleIngredientsView.as_view(), name= 'recipe-by-multiple-ingredient')
    
]