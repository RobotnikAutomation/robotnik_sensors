cmake_minimum_required(VERSION 3.5)
project(robotnik_sensors)

# find dependencies
find_package(ament_cmake REQUIRED)

install(
  DIRECTORY meshes urdf
  DESTINATION share/${PROJECT_NAME}/
)

set(_hook "${CMAKE_CURRENT_BINARY_DIR}/${PROJECT_NAME}.dsv")
file(WRITE "${_hook}"
"prepend-non-duplicate;GZ_SIM_RESOURCE_PATH;share/${PROJECT_NAME}/..\n")
install(FILES "${_hook}" DESTINATION share/${PROJECT_NAME})
ament_environment_hooks("${_hook}")

if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)
  find_package(ament_cmake_pytest REQUIRED)
  ament_lint_auto_find_test_dependencies()
  ament_add_pytest_test(urdf_xacro test/xacro_test.py)
endif()

ament_package()
