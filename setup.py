from setuptools import setup

# #STEP1: Configure package entry points for ROS2 node executable
package_name = 'image_conversion_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        # #STEP2: Install launch files to share directory
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        # #STEP3: Include launch directory for launch files
        ('share/' + package_name + '/launch', ['launch/image_conversion_launch.py']),
    ],
    # #STEP4: Define executable entry point for image_conversion_node
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='student',
    maintainer_email='student@example.com',
    description='ROS2 Image Conversion Node',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            # #STEP5: Main executable for the image conversion node
            'image_conversion_node = image_conversion_pkg.image_conversion_node:main',
        ],
    },
)

