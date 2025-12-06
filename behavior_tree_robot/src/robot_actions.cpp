#include "robot_actions.hpp"
#include <iostream>
#include <thread>
#include <chrono>

using namespace std::chrono_literals;

NavigateTo::NavigateTo(const std::string& name, const BT::NodeConfiguration& config)
: BT::SyncActionNode(name, config)
{}

BT::NodeStatus NavigateTo::tick()
{
    std::cout << "[NavigateTo] Navigating to enter the room..." << std::endl;
    // simulate some work
    std::this_thread::sleep_for(500ms);
    std::cout << "[NavigateTo] Arrived at door." << std::endl;
    return BT::NodeStatus::SUCCESS;
}

OpenFridge::OpenFridge(const std::string& name, const BT::NodeConfiguration& config)
: BT::SyncActionNode(name, config)
{}

BT::NodeStatus OpenFridge::tick()
{
    std::cout << "[OpenFridge] Opening the fridge..." << std::endl;
    std::this_thread::sleep_for(300ms);
    std::cout << "[OpenFridge] Fridge opened." << std::endl;
    return BT::NodeStatus::SUCCESS;
}

PickApple::PickApple(const std::string& name, const BT::NodeConfiguration& config)
: BT::SyncActionNode(name, config)
{}

BT::NodeStatus PickApple::tick()
{
    std::cout << "[PickApple] Reaching inside and picking an apple..." << std::endl;
    std::this_thread::sleep_for(400ms);
    std::cout << "[PickApple] Apple picked." << std::endl;
    return BT::NodeStatus::SUCCESS;
}

ExitRoom::ExitRoom(const std::string& name, const BT::NodeConfiguration& config)
: BT::SyncActionNode(name, config)
{}

BT::NodeStatus ExitRoom::tick()
{
    std::cout << "[ExitRoom] Exiting the room..." << std::endl;
    std::this_thread::sleep_for(500ms);
    std::cout << "[ExitRoom] Outside the room." << std::endl;
    return BT::NodeStatus::SUCCESS;
}
