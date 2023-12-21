import json
import threading

import pika
from PySide6.QtWidgets import QLabel, QDoubleSpinBox


class RabbitMQListener(threading.Thread):

    def __init__(self, qt_el_first_side: QDoubleSpinBox, qt_el_second_side: QDoubleSpinBox, qt_el_Hyp: QLabel, qt_el_perimetr: QLabel, qt_el_area: QLabel):
        super().__init__()
        self.firstSideNum = qt_el_first_side
        self.secondSideNum =  qt_el_second_side
        self.Hyp = qt_el_Hyp
        self.perimetr = qt_el_perimetr
        self.area = qt_el_area

    def run(self):
        connection = pika.BlockingConnection(
            pika.ConnectionParameters(
                host='rabbitmq',
                credentials=pika.PlainCredentials('user', 'password')
            )
        )
        channel = connection.channel()

        channel.queue_declare(queue='triangles')

        def callback(ch, method, properties, body):
            data = json.loads(body.decode())
            self.firstSideNum.setValue(int(data["side_a"]))
            self.secondSideNum.setValue(int(data["side_b"]))
            self.Hyp.setText(str(data["hypotenuse"]))
            self.perimetr.setText(str(data["perimeter"]))
            self.area.setText(str(data["area"]))
        channel.basic_consume(queue='triangles', on_message_callback=callback, auto_ack=True)
        channel.start_consuming()

