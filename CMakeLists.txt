cmake_minimum_required(VERSION 3.12.0)

project(palace)

set(CMAKE_MODULE_PATH ${CMAKE_MODULE_PATH} ${CMAKE_CURRENT_LIST_DIR}/cmake)
set(PYTHON_VERSION "3.6.0" CACHE STRING "Python version to compile against")

find_package(Python3 ${PYTHON_VERSION} EXACT
             REQUIRED COMPONENTS Interpreter Development)
find_package(PythonExtensions ${PYTHON_VERSION} EXACT REQUIRED)
find_package(Cython ${PYTHON_VERSION} EXACT REQUIRED)
find_package(Alure2 REQUIRED)

# Sorry for the variable recycling
add_cython_target(palace CXX)
Python3_add_library(palace MODULE ${palace})
target_link_libraries(palace PRIVATE Alure2::alure2)
python_extension_module(palace)
