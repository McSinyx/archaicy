cmake_minimum_required(VERSION 3.5.0)

project(palace)

set(CMAKE_MODULE_PATH ${CMAKE_MODULE_PATH} ${CMAKE_CURRENT_LIST_DIR}/cmake)
set(PYTHON_VERSION "3.6.0" CACHE STRING "Python version to compile against")

# FindPython3 is recommended by CMake to replace the deprecated FindPythonInterp
# and FindPythonLibs, but I can't get it to find any Python 3 on my machine.
#find_package(Python ${PYTHON_VERSION} REQUIRED
#             COMPONENTS Interpreter Development)
find_package(PythonInterp ${PYTHON_VERSION} REQUIRED)
find_package(PythonLibs ${PYTHON_VERSION} REQUIRED)
find_package(PythonExtensions ${PYTHON_VERSION} REQUIRED)
find_package(Cython ${PYTHON_VERSION} REQUIRED)
find_package(Alure2 REQUIRED)

# Sorry for the variable recycling
add_cython_target(palace CXX)
# Uncomment if FindPython3 is used.
#Python_add_library(palace MODULE ${palace})
add_library(palace MODULE ${palace})
target_link_libraries(palace Alure2::alure2)
python_extension_module(palace)
