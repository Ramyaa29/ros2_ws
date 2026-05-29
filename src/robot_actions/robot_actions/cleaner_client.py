import rclpy
from rclpy.node import Node
from rclpy.action import ActionClient
from robot_actions.action import Cleaning

class MyClient(Node):
    def __init__(self):
        super().__init__("simple_client")
        self.client = ActionClient(
            self,
            Cleaning,
            "clean_robot"
        )
        goal = Cleaning.Goal()
        goal.cleaning_time =5
        self.future = self.client.send_goal_async(goal)
        self.future.add_done_callback(self.goal_response)
    def goal_response(self,future):
        goal_handle= future.result()
        self.get_logger().info("Goal Accepted")

def main(args=None):
    rclpy.init(args=args)
    node= MyClient()
    rclpy.spin(node)
if __name__ == "__main__":
    main()

