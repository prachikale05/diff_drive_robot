# ROS2 Differential Drive Robot

A complete differential drive mobile robot simulation developed using **ROS2 Humble**, **Gazebo**, **SLAM Toolbox**, and **Nav2**. The robot is capable of autonomous navigation using a saved map, LiDAR-based localization, and path planning.

---

## 📌 Project Overview

This project demonstrates the complete workflow of developing a mobile robot in ROS2, starting from robot modeling to autonomous navigation.

The robot includes:
- Differential drive mechanism
- Gazebo simulation
- LiDAR sensor
- Camera sensor
- IMU sensor
- SLAM Toolbox for mapping
- Nav2 for autonomous navigation
- RViz visualization

---

## ✨ Features

- Differential drive mobile robot
- Modular URDF/Xacro robot description
- Gazebo simulation environment
- ros2_control integration
- LiDAR sensor
- Camera sensor
- IMU sensor
- SLAM Toolbox mapping
- Occupancy Grid Map generation
- Autonomous navigation using Nav2
- RViz visualization

---

## 🛠 Technologies Used

- ROS2 Humble
- Gazebo
- RViz2
- Nav2
- SLAM Toolbox
- Xacro
- URDF
- ros2_control
- C++

---

## 📂 Project Structure

```
diff_drive_robot/
│
├── config/
├── launch/
├── maps/
├── rviz/
├── urdf/
├── worlds/
├── CMakeLists.txt
├── package.xml
├── README.md
└── LICENSE
```

---

## 🤖 Robot Description

The robot is built using modular Xacro files.

It consists of:

- Base Link
- Base Footprint
- Left Wheel
- Right Wheel
- Caster Wheel
- LiDAR
- Camera
- IMU

---

## 📡 Sensors

### LiDAR

- 360° Laser Scanner
- Publishes LaserScan messages on `/scan`

### Camera

- RGB Camera
- Publishes image topics

### IMU

- Orientation and acceleration measurements

---

## 🗺 SLAM Mapping

The environment map is created using **SLAM Toolbox**.

Generated map files:

- `maps/my_map.yaml`
- `maps/my_map.pgm`

---

## 🧭 Autonomous Navigation

Navigation is implemented using **Nav2**.

Capabilities include:

- Localization using AMCL
- Global path planning
- Local path planning
- Obstacle avoidance
- Goal navigation using RViz

---

## 🚀 Build

```bash
cd ~/ros2_projects_ws

colcon build --symlink-install

source install/setup.bash
```

---

## ▶️ Launch Gazebo

```bash
ros2 launch diff_drive_robot gazebo.launch.py
```

---

## ▶️ Launch SLAM

```bash
ros2 launch diff_drive_robot slam.launch.py
```

---

## ▶️ Launch Navigation

```bash
ros2 launch diff_drive_robot navigation.launch.py
```

---

## ▶️ Launch RViz

```bash
rviz2
```

Load:

```
rviz/navigation.rviz
```

---

## 📸 Results

The robot successfully:

- Simulates in Gazebo
- Generates maps using SLAM Toolbox
- Localizes using AMCL
- Plans paths using Nav2
- Reaches user-defined goals using 2D Goal Pose

---

## 🎥 Demo

A demonstration video will be added soon.

---

## 🚀 Future Improvements

- Dynamic obstacle avoidance
- Camera-based object detection
- Waypoint navigation
- Multi-robot simulation
- Autonomous exploration

---

## 👩‍💻 Author

**Prachi Kale**

B.Tech Robotics & Automation Engineering

K. K. Wagh Institute of Engineering Education and Research

---

## 📜 License

This project is licensed under the MIT License.
