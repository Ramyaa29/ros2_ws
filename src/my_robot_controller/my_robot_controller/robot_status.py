import rclpy
from rclpy.node import Node

class RobotStatus(Node):
    def __init__(self):
        super().__init__("robot_status")
        self.timer= self.create_timer(
            2.0,
            self.status_monitor
        )
    def status_monitor(self):
            self.get_logger().info("Robot Monitoring")

def main(args=None):
    rclpy.init(args=args)
    node= RobotStatus()
    rclpy.spin(node)
    rclpy.shutdown()
if __name__=="__main__":
    main()
