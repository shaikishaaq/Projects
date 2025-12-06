1. Create package
mkdir -p ~/ros2_ws/src/image_conversion_pkg/image_conversion_pkg ~/ros2_ws/src/image_conversion_pkg/launch
cd ~/ros2_ws/src

2. Copy files from this submission (package.xml, setup.py, image_conversion_node.py, launch file)
3. Build
colcon build --packages-select image_conversion_pkg
source install/setup.bash

4. Launch
ros2 launch image_conversion_pkg image_conversion_launch.py

5. Test service
ros2 service call /image_conversion/set_color_mode std_srvs/srv/SetBool "{data: false}" # Mode1 Grayscale
ros2 service call /image_conversion/set_color_mode std_srvs/srv/SetBool "{data: true}" # Mode2 Color

6. View
ros2 run rqt_image_view rqt_image_view /processed_image


