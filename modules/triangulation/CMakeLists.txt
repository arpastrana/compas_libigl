cmake_minimum_required(VERSION 3.14)
project(triangulation)
set(CMAKE_CXX_STANDARD 11)

pybind11_add_module(triangulation MODULE triangulation.cpp)

target_link_libraries(triangulation PRIVATE igl::core)
target_link_libraries(triangulation PRIVATE igl::triangle)

set_target_properties(triangulation PROPERTIES
    LIBRARY_OUTPUT_DIRECTORY "${CMAKE_SOURCE_DIR}/src/compas_libigl/triangulation")

set_target_properties(triangulation PROPERTIES
    LIBRARY_OUTPUT_DIRECTORY_RELEASE "${CMAKE_SOURCE_DIR}/src/compas_libigl/triangulation")

configure_file(__init__.py "${CMAKE_SOURCE_DIR}/src/compas_libigl/triangulation/__init__.py" COPYONLY)
