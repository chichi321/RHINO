cmake_minimum_required(VERSION 3.9)

project(mpi_lambda_project LANGUAGES CXX)


set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED True)


find_package(MPI REQUIRED)


set(CMAKE_PREFIX_PATH "/usr/local/lambda-install")


find_package(aws-lambda-runtime REQUIRED)


add_executable(${PROJECT_NAME} main.cpp)


target_link_libraries(${PROJECT_NAME} PRIVATE MPI::MPI_CXX AWS::aws-lambda-runtime)


target_compile_options(${PROJECT_NAME} PRIVATE "-Wall" "-Wextra")


target_include_directories(${PROJECT_NAME} PRIVATE ${MPI_INCLUDE_PATH})


target_compile_features(${PROJECT_NAME} PRIVATE cxx_std_11)


if(MPI_COMPILE_FLAGS)
    set_target_properties(${PROJECT_NAME} PROPERTIES
        COMPILE_FLAGS "${MPI_COMPILE_FLAGS}")
endif()

if(MPI_LINK_FLAGS)
    set_target_properties(${PROJECT_NAME} PROPERTIES
        LINK_FLAGS "${MPI_LINK_FLAGS}")
endif()


aws_lambda_package_target(${PROJECT_NAME})
