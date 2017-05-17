#cmake_minimum_required(VERSION 3.8.3)
project(sphero_gui)

find_package(catkin REQUIRED message_generation dynamic_reconfigure std_msgs)

#add_message_files(FILES
  #                SpheroCollision.msg
#                 )

generate_messages(DEPENDENCIES std_msgs)
#generate_dynamic_reconfigure_options(cfg/Reconfig.cfg)

catkin_package(DEPENDS std_msgs)

include_directories(${catkin_INCLUDE_DIRS})

install(PROGRAMS src/sphero_gui.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)

