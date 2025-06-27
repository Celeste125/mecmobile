#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from nav_msgs.msg import Odometry
from tf2_ros import TransformBroadcaster
from geometry_msgs.msg import TransformStamped

class OdomTFPublisher(Node):
    def __init__(self):
        super().__init__('odom_tf_publisher')
        self.br = TransformBroadcaster(self)
        self.sub = self.create_subscription(Odometry, '/mecanum_controller/odom', self.callback, 10)

    def callback(self, msg):
        t = TransformStamped()
        t.header.stamp = msg.header.stamp
        t.header.frame_id = msg.header.frame_id or "odom"  # si viene vacío
        t.child_frame_id = msg.child_frame_id or "base_link"  # o "body_link" según tu robot
        t.transform.translation.x = msg.pose.pose.position.x
        t.transform.translation.y = msg.pose.pose.position.y
        t.transform.translation.z = msg.pose.pose.position.z
        t.transform.rotation = msg.pose.pose.orientation
        self.br.sendTransform(t)

def main():
    rclpy.init()
    node = OdomTFPublisher()
    rclpy.spin(node)

if __name__ == '__main__':
    main()
