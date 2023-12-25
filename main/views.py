from django.shortcuts import render, redirect

from model.builder import TriangleBuilder
from utils.strateges.TriangleTableFillStrategy import TriangleTableFillStrategy
from utils.table_factory.TableFactory import TableFactory
from .enums import ActionType
from database import Session


def get_home_page(request):
    return render(request, 'home.html')


def get_calculator_page(request):
    return render(request, 'calculator.html')


def get_triangles_from_db(request):
    factory = TableFactory()
    table = factory.create_table('html', 'table')
    strategy = TriangleTableFillStrategy(table)
    column_names = ["id", "Первая сторона", "Вторая сторона", 'Гиппотенуза', "Периметр", "Площадь"]
    return render(request, 'triangles_from_db.html', {'triangles_table': strategy.fill_table(column_names)})


def get_calculated_results(request):
    session = Session()
    if request.method == 'POST':
        side_a = float(request.POST.get('side_a'))
        side_b = float(request.POST.get('side_b'))
        # инициализиурем класс стрроитель нашего треугольника
        builder = TriangleBuilder()
        triangle = builder.set_first_side(side_a).set_second_side(side_b).get_triangle()

        if request.POST.get('form_mode') == ActionType.CALCULATE.value:
            return render(request, 'calculator.html', {
                'hypotenuse': triangle.hypotenuse,
                'area': triangle.area,
                'perimeter': triangle.perimeter,
            })

        session.add(triangle)
        session.commit()
        return redirect('triangles_from_db')

    return render(request, 'calculator.html', {
        'hypotenuse': None,
        'area': None,
        'perimeter': None,
    })
