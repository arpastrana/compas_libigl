cmake_minimum_required(VERSION 3.14)
project(isolines)
set(CMAKE_CXX_STANDARD 11)

pybind11_add_module(isolines MODULE isolines.cpp)

target_link_libraries(isolines PRIVATE igl::core)

set_target_properties(isolines PROPERTIES
    LIBRARY_OUTPUT_DIRECTORY "${CMAKE_SOURCE_DIR}/src/compas_libigl/isolines")

set_target_properties(isolines PROPERTIES
    LIBRARY_OUTPUT_DIRECTORY_RELEASE "${CMAKE_SOURCE_DIR}/src/compas_libigl/isolines")

configure_file(__init__.py "${CMAKE_SOURCE_DIR}/src/compas_libigl/isolines/__init__.py" COPYONLY)
