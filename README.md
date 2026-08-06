# 🤖 ROS 2 Differential Drive Mobile Robot

A complete ROS 2 Humble differential drive mobile robot simulation built using Gazebo, RViz, ros2_control, SLAM Toolbox, and Nav2.

This project demonstrates the complete workflow of designing a mobile robot, simulating it in Gazebo, generating a map using SLAM, and performing autonomous navigation using Nav2.

---

# Project Overview

This robot was developed as a learning project to understand the complete ROS 2 mobile robot pipeline.

The project includes:

- Robot modelling using URDF/Xacro
- Gazebo simulation
- Differential drive control using ros2_control
- LiDAR integration
- Camera integration
- IMU integration
- SLAM mapping
- Autonomous Navigation using Nav2
- RViz visualization

---

# Features

✔ Differential Drive Robot

✔ Gazebo Simulation

✔ RViz Visualization

✔ ros2_control Integration

✔ LiDAR Sensor

✔ Camera Sensor

✔ IMU Sensor

✔ SLAM Toolbox Mapping

✔ Occupancy Grid Map

✔ Nav2 Autonomous Navigation

✔ Goal-based Path Planning

---

# Robot Specifications

Base Type

- Differential Drive

Sensors

- 2D LiDAR
- RGB Camera
- IMU

Controller

- diff_drive_controller

Localization

- AMCL

Planner

- Nav2 Planner Server

Controller

- DWB Local Planner

Simulation

- Gazebo

Visualization

- RViz2

---

# Technologies Used

- ROS 2 Humble
- Gazebo
- RViz2
- Xacro
- URDF
- ros2_control
- Nav2
- SLAM Toolbox
- Ubuntu 22.04

---

# Folder Structure

```text
diff_drive_robot/

├── config/
├── images/
├── launch/
├── maps/
├── rviz/
├── urdf/
├── worlds/

├── CMakeLists.txt
├── package.xml
└── README.md
```

---

# Build

```bash
cd ~/ros2_projects_ws

colcon build

source install/setup.bash
```

---

# Launch Gazebo

```bash
ros2 launch diff_drive_robot gazebo.launch.py
```

---

# Launch Navigation

```bash
ros2 launch diff_drive_robot navigation.launch.py
```

---

# Launch RViz

```bash
rviz2 -d install/diff_drive_robot/share/diff_drive_robot/rviz/navigation.rviz
```

---

# SLAM Mapping

Launch SLAM

```bash
ros2 launch diff_drive_robot slam.launch.py
```

Save Map

```bash
ros2 run nav2_map_server map_saver_cli \
-f ~/ros2_projects_ws/src/diff_drive_robot/maps/my_map
```

---

# Autonomous Navigation

1. Launch Gazebo

2. Launch Navigation

3. Open RViz

4. Click **2D Pose Estimate**

5. Set Initial Pose

6. Click **2D Goal Pose**

7. Select Goal

The robot plans a path and autonomously reaches the destination.

---

# Screenshots

## Gazebo

(Add image here)

---

## RViz

(Add image here)

---

## Navigation

(Add image here)

---

# Future Improvements

- Obstacle Avoidance Improvements

- Dynamic Obstacles

- Camera-based Object Detection

- Autonomous Docking

- Multi-Robot Navigation

---

# Author

Prachi Kale

B.Tech Robotics and Automation Engineering

K. K. Wagh Institute of Engineering Education and Research

ROS 2 Humble Project
