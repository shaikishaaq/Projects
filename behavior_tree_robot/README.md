Behavior Tree Robot (C++) - Ready-to-build example
==================================================

What this contains
- A minimal BehaviorTree.CPP v3 example that models:
    1) NavigateTo (enter room)
    2) OpenFridge
    3) PickApple
    4) ExitRoom
  The nodes are dummy implementations that print messages and return SUCCESS.
- CMakeLists.txt for building the executable.
- An XML file describing the tree.
- Simple instructions to build & run.

Requirements
- C++17 compiler
- CMake (>=3.5)
- BehaviorTree.CPP library installed (v3). On Ubuntu you can install from source or package.
  Example (build from source):
    git clone https://github.com/BehaviorTree/BehaviorTree.CPP.git
    cd BehaviorTree.CPP
    mkdir build && cd build
    cmake .. && make -j && sudo make install

  On some systems a package may be available as 'ros-<distro>-behaviortree-cpp-v3' when using ROS.
  The example uses the official include <behaviortree_cpp_v3/bt_factory.h>.

Build
-----
mkdir build
cd build
cmake ..
make -j

Run
---
./behavior_tree_robot

Files in this archive
- CMakeLists.txt
- README.md
- src/main.cpp
- include/robot_actions.hpp
- src/robot_actions.cpp
- bt_xml/robot_bt.xml

Notes
-----
- This is independent of ROS (pure C++).
- Nodes simply print to stdout to demonstrate execution order.
- If BehaviorTree.CPP is installed in a non-standard location, set CMAKE_PREFIX_PATH
  to include its install folder when running cmake, e.g.:
    cmake -DCMAKE_PREFIX_PATH=/opt/behaviortree .. 

