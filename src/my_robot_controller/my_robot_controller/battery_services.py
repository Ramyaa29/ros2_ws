import rclpy
from rclpy.node import Node 

from example_interfaces.srv import AddTwoInts

class Battery_srv(Node):
    def __init__(self):
        super().__init__("batter_services")
        self.service = self.create_service(
            AddTwoInts,
            "battery_srv",
            self.add_callback
        )
        self.get_logger().info("Service Ready")
    def add_callback(self,request,response):
        if request.a < request.b:
            self.get_logger().info("Battery Low")
            response.sum=0
        else:
            self.get_logger().info("Battery OK")
            response.sum=1
        return response
def main(args=None):
    rclpy.init(args=args)
    node=Battery_srv()
    rclpy.spin(node)
    rclpy.shutdown()
if __name__ == "__main__":
    main()
