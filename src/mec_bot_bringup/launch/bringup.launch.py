from launch import LaunchDescription
from launch.actions import TimerAction, IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node
import os

def generate_launch_description():
    pkg_share = os.path.join(os.getenv('HOME'), 'mec_ws', 'install', 'mec_bot_description', 'share', 'mec_bot_description')
    gazebo_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(pkg_share, 'launch', 'gazebo.launch.py')
        )
    )

    # Spawners (con delay para que el robot ya esté en el mundo)
    joint_state_broadcaster_spawner = TimerAction(
        period=5.0,  # segundos, ajusta si hace falta
        actions=[
            Node(
                package="controller_manager",
                executable="spawner",
                arguments=["joint_state_broadcaster", "--controller-manager", "/controller_manager"],
                output="screen",
            )
        ]
    )

    mecanum_controller_spawner = TimerAction(
        period=6.0,
        actions=[
            Node(
                package="controller_manager",
                executable="spawner",
                arguments=["mecanum_controller", "--controller-manager", "/controller_manager"],
                output="screen",
            )
        ]
    )

    return LaunchDescription([
        gazebo_launch,
        joint_state_broadcaster_spawner,
        mecanum_controller_spawner,
    ])
