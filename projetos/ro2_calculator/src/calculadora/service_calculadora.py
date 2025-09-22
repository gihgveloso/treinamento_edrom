from example_interfaces.srv import AddTwoInts

import rclpy
from rclpy.node import Node


class ServiceCalculadora(Node):
    def __init__(self):
        super().__init__('service_calculadora')
        self.srv = self.create_service(AddTwoInts, 'add_two_ints', self.add_two_ints_callback)
        self.get_logger().info('Servidor da calculadora está pronto para receber números.')

    def add_two_ints_callback(self, request, response):
        response.sum = request.a + request.b
        self.get_logger().info('Números recebidos: a: %d b: %d' % (request.a, request.b))
        self.get_logger().info('Resposta: %d' % (response.sum))
        return response

def main(args=None):
    rclpy.init(args=args)
    service_calculadora = ServiceCalculadora()
    rclpy.spin(service_calculadora)
    rclpy.shutdown()

if __name__ == '__main__':
    main()