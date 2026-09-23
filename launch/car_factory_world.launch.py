"""
Launches Gazebo Harmonic (gz sim) with the car_factory world.

Run with:
    ros2 launch SEDAR_Robotics_1 car_factory_world.launch.py
"""

import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource


def generate_launch_description():
    pkg_share = get_package_share_directory('SEDAR_Robotics_1')
    world_path = os.path.join(pkg_share, 'worlds', 'car_factory.sdf')

    ros_gz_sim_share = get_package_share_directory('ros_gz_sim')
    gz_sim_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(ros_gz_sim_share, 'launch', 'gz_sim.launch.py')
        ),
        launch_arguments={'gz_args': world_path}.items(),
    )

    return LaunchDescription([
        gz_sim_launch,
    ])