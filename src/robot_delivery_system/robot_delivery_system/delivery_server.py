import rclpy

import time
from rclpy.node import Node
from rclpy.action import ActionServer
from robot_actions.action import Delivery

class MyServer(Node):
    def __init__(self):
        super().__init__("delivery_server")
        self.action_server = ActionServer(
            self,
            Delivery,
            "delivery_robot",
            self.execute_callback
        )
    def execute_callback(self,goal_handle):
        self.get_logger().info("Robot started Delivery")
        feedback_msg= Delivery.Feedback()
        total_distance= goal_handle.request.distance

        for current in range(total_distance):
            time.sleep(1)
            feedback_msg.progress=((current+1)/total_distance)*100
            goal_handle.publish_feedback(feedback_msg)
            self.get_logger().info(f"Moving: {feedback_msg.progress}%")
        goal_handle.succeed()
        result= Delivery.Result()
        result.delivered=True
        self.get_logger().info("Robot delivered Successfully")
        return result
    
def main(args=None):
    rclpy.init(args=args)
    node= MyServer()
    rclpy.spin(node)
    rclpy.shutdown()
if __name__ == "__main__":
    main()

