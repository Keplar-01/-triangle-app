import pika
import json
from django.shortcuts import render, redirect

from database import Session
from model.models import Triangle
from .enums import ActionType

def get_home_page(request):
    return render(request, 'home.html')


def get_calculator_page(request):
    return render(request, 'calculator.html')


def get_triangles_from_db(request):
    all_triangles = Session().query(Triangle).all()
    return render(request, 'triangles_from_db.html', {'triangles': all_triangles})

def get_calculated_results(request):
    if request.method == 'POST':
        side_a = float(request.POST.get('side_a'))
        side_b = float(request.POST.get('side_b'))
        triangle = Triangle(first_side=side_a, second_side=side_b)

        if request.POST.get('form_mode') == ActionType.CALCULATE.value:
            connection = pika.BlockingConnection(pika.ConnectionParameters(
                'rabbitmq',
                credentials=pika.PlainCredentials('user', 'password')
            ))
            channel = connection.channel()
            channel.queue_declare(queue='triangles')

            message = json.dumps({
                'side_a': side_a,
                'side_b': side_b,
                'hypotenuse': triangle.hypotenuse,
                'area': triangle.area,
                'perimeter': triangle.perimeter
            })
            channel.basic_publish(exchange='', routing_key='triangles', body=message)
            connection.close()

            return render(request, 'calculator.html', {
                'hypotenuse': triangle.hypotenuse,
                'area': triangle.area,
                'perimeter': triangle.perimeter,
            })

        Session().add(triangle)
        Session().commit()
        return redirect('triangles_from_db')

    return render(request, 'calculator.html', {
        'hypotenuse': None,
        'area': None,
        'perimeter': None,
    })
