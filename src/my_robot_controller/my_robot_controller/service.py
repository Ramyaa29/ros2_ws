import rclpy
from rclpy.node import Node

from example_interfaces.srv import AddTwoInts

class MyService(Node):
    def __init__(self):
        super().__init__("service")
        self.service = self.create_service(
            AddTwoInts,
            "add_two_ints",
            self.add_callback
        )
        self.get_logger().info("Service Ready")
    def add_callback( self, request, response):
        response.sum = request.a +request.b
        self.get_logger().info(f"Incoming Request: {request.a}+ {request.b}")
        return response
def main(args=None):
    rclpy.init(args=args)
    node= MyService()
    rclpy.spin(node)
    rclpy.shutdown()
if __name__ == "__main__":
    main()
#ros2 service call /add_two_ints example_interfaces/srv/AddTwoInts "{a: 5, b: 7}"