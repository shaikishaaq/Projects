# #STEP1: Import launch system components
from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration

def generate_launch_description():
    # #STEP2: Define configurable parameters
    input_topic = LaunchConfiguration('input_topic', default='/image_raw')
    output_topic = LaunchConfiguration('output_topic', default='/processed_image')
    
    # #STEP3: Create launch description
    return LaunchDescription([
        # #STEP4: Parameter declarations for topic customization
        DeclareLaunchArgument('input_topic', default_value=input_topic,
                            description='Input image topic from usb_cam'),
        DeclareLaunchArgument('output_topic', default_value=output_topic,
                            description='Output processed image topic'),
        
        # #STEP5: Launch usb_cam node with camera parameters
        Node(
            package='usb_cam',
            executable='usb_cam_node_exe',
            name='usb_cam',
            parameters=[{
                # #STEP6: USB camera configuration parameters
                'device_name': '/dev/video0',
                'image_size': [640, 480],
                'framerate': 30.0,
                'pixel_format': 'yuyv',
                'camera_name': 'usb_camera',
                'camera_info_url': ''
            }],
            output='screen',
            remappings=[
                # #STEP7: Remap camera output topic
                ('image_raw', input_topic)
            ]
        ),
        
        # #STEP8: Launch image_conversion node
        Node(
            package='image_conversion_pkg',
            executable='image_conversion_node',
            name='image_conversion',
            parameters=[{
                'input_topic': input_topic,
                'output_topic': output_topic
            }],
            output='screen'
        )
    ])

