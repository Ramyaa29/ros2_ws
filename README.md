# ROS2 Learning Journey 🚀

This repository contains my ROS2 learning practice using Python and Ubuntu.

I am learning ROS2 fundamentals including:
- Nodes
- ROS Graph
- Topics
- Publishers & Subscribers
- Services
- ROS2 Commands
- Communication between nodes

---

# Technologies Used

- ROS2 Humble
- Python
- Ubuntu 22.04 (WSL)
- VS Code

---

# Folder Structure

```bash
ros2_ws/
│
├── src/
│   └── my_robot_controller/
│       └── my_robot_controller/
│           ├── first_node.py
│           ├── publisher.py
│           ├── subscriber.py
│           └── service_node.py
│
├── build/
├── install/
└── log/
```

---

# Concepts Learned

## 1. ROS2 Nodes

A node is an executable process that performs a specific task in a robotic system.

Example:
- Camera Node
- LiDAR Node
- Navigation Node

---

## 2. Topics

Topics are communication channels used for asynchronous data exchange between nodes using the publisher-subscriber model.

---

## 3. Publisher & Subscriber

- Publisher sends messages to a topic.
- Subscriber receives messages from a topic.

Example:
```text
Publisher Node → Topic → Subscriber Node
```

---

## 4. Services

Services use request-response communication between nodes.

Example:
```text
Client Node → Request
Service Node → Response
```

---

# ROS2 Commands Used

## Run Python Node

```bash
python3 first_node.py
```

---

## List Active Nodes

```bash
ros2 node list
```

---

## List Topics

```bash
ros2 topic list
```

---

## View Topic Messages

```bash
ros2 topic echo /chatter
```

---

## List Services

```bash
ros2 service list
```

---

## Call Service

```bash
ros2 service call /add_two_ints example_interfaces/srv/AddTwoInts "{a: 5, b: 7}"
```

---

# Learning Goals

- Build strong ROS2 fundamentals
- Learn robot communication systems
- Integrate AI with robotics
- Work on autonomous robotics projects

---

# Future Topics

- Actions
- Parameters
- Launch Files
- TF
- URDF
- Gazebo
- RViz
- Navigation Stack (Nav2)

---

# Author

Ramya