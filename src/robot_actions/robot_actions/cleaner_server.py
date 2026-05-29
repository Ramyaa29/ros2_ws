import time
import rclpy
from rclpy.node import Node
from rclpy.action import ActionServer
from robot_actions.action import Cleaning

class CleaningAction(Node):
    def __init__(self):
        super().__init__("cleaning_action")
        self.action_server = ActionServer(
            self,
            Cleaning,
            "clean_robot",
            self.execute_callback
        )
    def execute_callback(self,goal_handle):
        self.get_logger().info("Started Cleaning")
        feedback_msg= Cleaning.Feedback()
        total = goal_handle.request.cleaning_time
        for i in range(total):
            time.sleep(1)
            feedback_msg.percentage=(i+1/total)*100
            goal_handle.publish_feedback(feedback_msg)
            self.get_logger().info(f"Cleaning: {feedback_msg.percentage}%")
        goal_handle.succeed()
        result = Cleaning.Result()
        result.success=True
        self.get_logger().info("Cleaning Completed")
        return result
def main(args=None):
    rclpy.init(args=args)
    node= CleaningAction()
    rclpy.spin(node)
    rclpy.shutdown()
if __name__ == "__main__":
    main()




# import rclpy

# import time
# from rclpy.node import Node
# from rclpy.action import ActionServer
# from robot_delivery_system.action import Delivery

# class MyServer(Node):
#     def __init__(self):
#         super().__init__("delivery_client")
#         self.action_server = ActionServer(
#             self,
#             Delivery,
#             "delivery_robot",
#             self.execute_callback
#         )
#     def execute_callback(self,goal_handle):
#         self.get_logger().info("Robot started Delivery")
#         feedback_msg= Delivery.Feedback()
#         total_distance= goal_handle.request.delivery_distance

#         for current in range(total):
#             time.sleep(1)
#             feedback_msg.percentage((current)/total_distance)*100
#             goal_handle.publish.feedback(feedback_msg)
#             self.get_logger().info(f"Moving: {feedback_msg.percentage}%")
#         goal_handle.succeed()
#         result= Delivery.Result()
#         result.succedd=True
#         self.get_logger().info("Robot delivered Successfully")
#         return result
    
# def main(args=None):
#     rclpy.init(args=args)
#     node= MyServer()
#     rclpy.spin(node)
#     rclpy.shutdown()
# if __name__ == "__main__":
#     main()


