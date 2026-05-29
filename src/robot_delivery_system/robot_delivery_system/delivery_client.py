import rclpy
from rclpy.node import Node
from rclpy.action import ActionClient
from robot_actions.action import Delivery

class MyClient(Node):
    def __init__(self):
        super().__init__("delivery_client")
        self.client = ActionClient(
            self,
            Delivery,
            "delivery_robot"
        )
        goal= Delivery.Goal()
        goal.distance= 20
        self.client.wait_for_server()
        self.future = self.client.send_goal_async(goal, feedback_callback = self.feedback_callback)
        self.future.add_done_callback(self.goal_response)
    def feedback_callback(self, feedback_msg):
        feedback = feedback_msg.feedback
        self.get_logger().info(
            f"Progress: {feedback.progress}%"
        )
    def goal_response(self, future):
        goal_handle= future.result()
        self.result_future = goal_handle.get_result_async()
        self.result_future.add_done_callback(self.result_callback)
        self.get_logger().info("Goal Accepted")
    def result_callback(self, future):
        result = future.result().result
        self.get_logger().info(
            f"Result: {result.delivered}"
        )

def main(args=None):
    rclpy.init(args=args)
    node= MyClient()
    rclpy.spin(node)
if __name__ == "__main__":
    main()
