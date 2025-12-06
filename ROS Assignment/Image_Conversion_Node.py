# #STEP1: Import required ROS2 and OpenCV libraries
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from std_srvs.srv import SetBool
import cv2
from cv_bridge import CvBridge
import numpy as np

class ImageConversionNode(Node):
    def __init__(self):
        # #STEP2: Initialize node with proper name
        super().__init__('image_conversion_node')
        
        # #STEP3: Declare configurable parameters for topics
        self.declare_parameter('input_topic', '/image_raw')
        self.declare_parameter('output_topic', '/processed_image')
        
        # #STEP4: Get parameter values
        self.input_topic = self.get_parameter('input_topic').value
        self.output_topic = self.get_parameter('output_topic').value
        
        # #STEP5: Initialize mode (True=Color Mode2, False=Grayscale Mode1)
        self.mode_color = True
        self.bridge = CvBridge()
        
        # #STEP6: Create subscriber for input images from usb_cam
        self.sub = self.create_subscription(
            Image, self.input_topic, self.image_callback, 10)
        
        # #STEP7: Create publisher for processed output images
        self.pub = self.create_publisher(Image, self.output_topic, 10)
        
        # #STEP8: Create service server for mode switching
        self.srv = self.create_service(SetBool, 'set_color_mode', self.mode_callback)
        
        # #STEP9: Print node information
        self.get_logger().info(f'# Subscribed to: {self.input_topic}')
        self.get_logger().info(f'# Publishing to: {self.output_topic}')
        self.get_logger().info('# Service /set_color_mode ready (True=Color Mode2, False=Grayscale Mode1)')

    def image_callback(self, msg):
        # #STEP10: Convert ROS Image message to OpenCV image (BGR format)
        cv_image = self.bridge.imgmsg_to_cv2(msg, desired_encoding='bgr8')
        
        # #STEP11: Apply grayscale conversion if in Mode 1
        if not self.mode_color:  # Mode 1: Grayscale
            gray = cv2.cvtColor(cv_image, cv2.COLOR_BGR2GRAY)
            # #STEP12: Convert grayscale back to 3-channel BGR for consistency
            cv_image = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)
        
        # #STEP13: Convert processed image back to ROS Image message
        processed_msg = self.bridge.cv2_to_imgmsg(cv_image, encoding='bgr8')
        processed_msg.header = msg.header  # #STEP14: Preserve timestamp and frame_id
        
        # #STEP15: Publish processed image continuously
        self.pub.publish(processed_msg)

    def mode_callback(self, request, response):
        # #STEP16: Update mode based on service request (True=Color, False=Grayscale)
        self.mode_color = request.data
        mode_name = "Color (Mode 2)" if self.mode_color else "Grayscale (Mode 1)"
        
        # #STEP17: Log mode change and return success response
        self.get_logger().info(f'# Mode changed to: {mode_name}')
        response.success = True
        response.message = f'Set to {mode_name}'
        return response

# #STEP18: Main function to initialize and spin the node
def main(args=None):
    rclpy.init(args=args)
    node = ImageConversionNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

