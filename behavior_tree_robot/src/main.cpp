#include <behaviortree_cpp_v3/bt_factory.h>
#include <behaviortree_cpp_v3/loggers/bt_cout_logger.h>
#include <iostream>
#include "robot_actions.hpp"

int main()
{
    BT::BehaviorTreeFactory factory;

    // Register custom nodes
    factory.registerNodeType<NavigateTo>("NavigateTo");
    factory.registerNodeType<OpenFridge>("OpenFridge");
    factory.registerNodeType<PickApple>("PickApple");
    factory.registerNodeType<ExitRoom>("ExitRoom");

    // Load tree from XML
    const std::string xml_filename = "bt_xml/robot_bt.xml";
    std::cout << "Loading BT from: " << xml_filename << std::endl;

    auto tree = factory.createTreeFromFile(xml_filename);

    BT::StdCoutLogger logger_cout(tree);

    std::cout << "Ticking the tree..." << std::endl;
    tree.tickRoot();

    std::cout << "Tree finished." << std::endl;
    return 0;
}
