import sys

from example_interfaces.srv import AddTwoInts
import rclpy
from rclpy.node import Node


class ClientCalculadora(Node):
    def __init__(self):
        super().__init__('client_calculadora')
        self.cli = self.create_client(AddTwoInts, 'add_two_ints')
        while not self.cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Serviço não disponível, aguardando...')
        self.req = AddTwoInts.Request()

    def send_request(self, a, b):
        self.req.a = a
        self.req.b = b
        return self.cli.call_async(self.req)

def main(args=None):
    rclpy.init(args=args)

    client_calculadora = ClientCalculadora()
    future = client_calculadora.send_request(int(sys.argv[1]), int(sys.argv[2]))
    rclpy.spin_until_future_complete(client_calculadora, future)
    response = future.result()
    client_calculadora.get_logger().info(
        'Resultado da soma: %d + %d = %d' %
        (int(sys.argv[1]), int(sys.argv[2]), response.sum))

    client_calculadora.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()