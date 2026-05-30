import rclpy
from rclpy.node import Node

class MyParam(Node):
    def __init__(self):
        super().__init__("parameters")
        self.declare_parameter("speed",5.0)
        speed = self.get_parameter("speed").value
        self.get_logger().info(f"Speed: {speed}")
def main(args=None):
    rclpy.init(args=args)
    node = MyParam()
    rclpy.spin(node)
    rclpy.shutdown()
if __name__=="__main__":
    main()