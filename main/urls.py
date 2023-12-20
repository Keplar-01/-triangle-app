from django.urls import path

from .views import get_home_page, get_calculator_page, \
    get_triangles_from_db, get_calculated_results

urlpatterns = [
    path('', get_home_page, name='home'),
    path('calculator/', get_calculator_page, name='calculator'),
    path('triangles-from-db/', get_triangles_from_db, name='triangles_from_db'),
    path('calculate-triangle/', get_calculated_results, name='calculate_triangle'),

]
