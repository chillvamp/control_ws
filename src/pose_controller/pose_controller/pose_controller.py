import rclpy
from rclpy.node import Node
from geometry_msgs.msg import PoseWithCovarianceStamped, PointStamped, Twist
import math

class PoseController(Node):
    def __init__(self):
        super().__init__('pose_controller')
        
        # Subscribe to the robot's pose from AMCL
        self.create_subscription(PoseWithCovarianceStamped, '/amcl_pose', self.pose_callback, 10)
        
        # Subscribe to the clicked goal point
        self.create_subscription
        
        # Publisher for velocity commands
        self.cmd_vel_pub = self.create_publisher
        
        self.current_pose = None
        self.goal_pose = None
        self.counter = 0
        self.timer = self.create_timer(0.1, self.control_loop)  # 10 Hz loop

    def pose_callback(self, msg):
        """ Update current robot pose. """
        self.current_pose = msg.pose.pose

    def goal_callback(self, msg):
        """ Update target goal when a point is clicked. """
        self.goal_pose = msg.point
        self.get_logger().info(f"New goal received: x={msg.point.x}, y={msg.point.y} ")

    def control_loop(self):
        """ Compute control commands and publish them. """
        if self.current_pose is None or self.goal_pose is None:
            return  # No control if we don't have a pose or goal
        
        # Get current pose
        x, y = self.current_pose.position.x, self.current_pose.position.y
        goal_x, goal_y = self.goal_pose.x, self.goal_pose.y
        
        # Compute error
        
        
        # Compute desired heading
        
        
        # Get current yaw from quaternion
        q = self.current_pose.orientation
        yaw = math.atan2(2.0 * (q.w * q.z + q.x * q.y), 1.0 - 2.0 * (q.y**2 + q.z**2))
        
        # Compute angular error
        
        # Control gains (adjust as needed)
        
        
        # Compute control signals
        cmd_vel = Twist()
        if distance > 0.1:  # Only move if far enough from the goal
            print ("Not too close to start")
            
        
        # Stop if very close
        if distance < 0.05:
            cmd_vel.linear.x = 0.0
            cmd_vel.angular.z = 0.0
            self.goal_pose = None  # Goal reached
        
        # Publish command
        self.counter+=1 
        if self.counter ==100:
            print (cmd_vel)
            self.counter=0
        self.cmd_vel_pub.publish(cmd_vel)

def main(args=None):
    rclpy.init(args=args)
    
    node = PoseController()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
