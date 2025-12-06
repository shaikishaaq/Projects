# #STEP1: Create workspace and package
mkdir -p ~/ros2_ws/src/image_conversion_ws/src
cd ~/ros2_ws/src/image_conversion_ws/src
ros2 pkg create --build-type ament_python image_conversion_pkg --dependencies rclpy sensor_msgs std_srvs cv_bridge

# #STEP2: Replace files with above content (copy each file exactly)
# Copy package.xml, setup.py, image_conversion_node.py, launch file

# #STEP3: Make node executable
chmod +x image_conversion_pkg/image_conversion_pkg/image_conversion_node.py

# #STEP4: Build package
cd ~/ros2_ws
colcon build --packages-select image_conversion_pkg
source install/setup.bash

# #STEP5: Launch complete system
ros2 launch image_conversion_pkg image_conversion_launch.py

# #STEP6: Test service calls (in new terminal)
ros2 service call /image_conversion/set_color_mode std_srvs/srv/SetBool "{data: false}"  # Grayscale Mode 1
ros2 service call /image_conversion/set_color_mode std_srvs/srv/SetBool "{data: true}"   # Color Mode 2

# #STEP7: View output
ros2 run rqt_image_view rqt_image_view /processed_image

