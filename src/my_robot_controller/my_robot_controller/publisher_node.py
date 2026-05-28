import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class MyPublisher(Node):
    def __init__(self):
        super().__init__("publisher_node")
        self.publisher_=self.create_publisher(
            String,
            "chatter",
            10
        )
        self.timer = self.create_timer(1.0, self.publish_message)
    def publish_message(self):
        msg=String()
        msg.data="Hello"
        self.publisher_.publish(msg)
        self.get_logger().info(msg.data)
def main (args=None):
    rclpy.init(args=args)
    node = MyPublisher()
    rclpy.spin(node)
    rclpy.shutdown()
if __name__ == "__main__":
    main()