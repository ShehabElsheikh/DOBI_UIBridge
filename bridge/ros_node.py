# bridge/ros_node.py

import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class ROSBridgeNode(Node):
    def __init__(self):
        super().__init__('dobi_bridge_node')
        self.publisher_ = self.create_publisher(String, 'dobi_commands', 10)
        self.subscription = self.create_subscription(
            String,
            'dobi_status',
            self.listener_callback,
            10
        )
        self.latest_data = None

    def listener_callback(self, msg):
        self.latest_data = msg.data

    def publish_command(self, command):
        msg = String()
        msg.data = command
        self.publisher_.publish(msg)

class RosNodeHandler:
    def __init__(self):
        rclpy.init(args=None)
        self.node = ROSBridgeNode()

    def publish_command(self, command):
        self.node.publish_command(command)

    def get_latest_data(self):
        rclpy.spin_once(self.node, timeout_sec=0.01)
        return self.node.latest_data
