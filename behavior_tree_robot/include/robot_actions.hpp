#pragma once
#include <behaviortree_cpp_v3/action_node.h>
#include <string>

class NavigateTo : public BT::SyncActionNode
{
public:
    NavigateTo(const std::string& name, const BT::NodeConfiguration& config);
    static BT::PortsList providedPorts() { return {}; }
    BT::NodeStatus tick() override;
};

class OpenFridge : public BT::SyncActionNode
{
public:
    OpenFridge(const std::string& name, const BT::NodeConfiguration& config);
    static BT::PortsList providedPorts() { return {}; }
    BT::NodeStatus tick() override;
};

class PickApple : public BT::SyncActionNode
{
public:
    PickApple(const std::string& name, const BT::NodeConfiguration& config);
    static BT::PortsList providedPorts() { return {}; }
    BT::NodeStatus tick() override;
};

class ExitRoom : public BT::SyncActionNode
{
public:
    ExitRoom(const std::string& name, const BT::NodeConfiguration& config);
    static BT::PortsList providedPorts() { return {}; }
    BT::NodeStatus tick() override;
};
