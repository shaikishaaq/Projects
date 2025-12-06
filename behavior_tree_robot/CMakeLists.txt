cmake_minimum_required(VERSION 3.5)
project(behavior_tree_robot LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

find_package(behaviortree_cpp_v3 REQUIRED)

include_directories(include)

add_executable(behavior_tree_robot src/main.cpp src/robot_actions.cpp)
target_link_libraries(behavior_tree_robot PRIVATE behaviortree_cpp_v3::behaviortree_cpp_v3)
