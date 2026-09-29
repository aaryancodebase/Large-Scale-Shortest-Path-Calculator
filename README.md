# Large-Scale Shortest Path Analysis

A Python-based graph analysis project focused on implementing, testing, and optimizing shortest-path algorithms for weighted graphs.

The project aims to explore how shortest-path computation works, evaluate its performance as graph sizes increase, and eventually provide an interactive environment for graph visualization and analysis.

## 📌 Project Overview

Graphs are widely used to represent interconnected systems such as road networks, communication networks, transportation systems, and computer networks.

Finding the shortest path between two nodes is a fundamental problem in graph theory, with applications in navigation, network routing, and logistics.

**Large-Scale Shortest Path Analysis** explores this problem using Dijkstra's Algorithm, with an emphasis on algorithm correctness, efficiency, scalability, and visualization.

## ✨ Current Features

* **Weighted Graph Representation:** Uses Python dictionaries to represent nodes, edges, and their associated weights.
* **Dijkstra's Algorithm:** Computes shortest distances from a selected source node.
* **Path Reconstruction:** Reconstructs the shortest route between source and destination using predecessor tracking.
* **Input Validation:** Rejects negative edge weights, which are incompatible with Dijkstra's Algorithm.
* **Unreachable Node Detection:** Identifies destinations that cannot be reached from the source.
* **Edge-Case Testing:** Includes testing for normal paths, identical source and destination, and disconnected nodes.

## 🛠️ Technologies Used

| Technology           | Purpose                                |
| -------------------- | -------------------------------------- |
| Python 3             | Core programming language              |
| Dijkstra's Algorithm | Shortest-path computation              |
| Python Dictionaries  | Graph representation                   |
| Python Sets          | Tracking unvisited nodes               |
| Git & GitHub         | Version control and project management |

Additional visualization and data-analysis libraries are planned for future development.

## 📂 Project Structure

```text
Large-Scale-Shortest-Path-Analysis/
│
├── main.py          # Runs the algorithm and displays results
├── dijkstra.py      # Graph representation and Dijkstra implementation
└── README.md        # Project documentation
```

## ⚙️ How It Works

The project currently represents a weighted graph using an adjacency-list structure implemented with nested Python dictionaries.

### Algorithm Workflow

1. Initialize the source distance to zero and all other distances to infinity.
2. Maintain a collection of unvisited nodes.
3. Select the unvisited node with the smallest known distance.
4. Examine its neighboring nodes and update distances when a shorter route is discovered.
5. Track predecessor nodes to reconstruct the shortest path.
6. Continue until all reachable nodes have been processed.
7. Return the shortest distances and reconstruct the requested route.

## 🚀 Getting Started

### Prerequisites

* Python 3.10 or later
* Git (optional)
* A code editor such as Visual Studio Code

## 🧪 Testing

The implementation has been manually tested against several scenarios:

| Test Case                          | Expected Behavior                         |
| ---------------------------------- | ----------------------------------------- |
| Standard shortest path             | Returns minimum-cost path and distance    |
| Alternative source and destination | Calculates the correct route              |
| Same source and destination        | Returns the source node with distance 0   |
| Disconnected destination           | Identifies the destination as unreachable |
| Negative edge weight               | Raises a validation error                 |

These tests help establish a foundation for future performance benchmarking.

## 🗺️ Development Roadmap

* [x] Implement weighted graph representation
* [x] Implement basic Dijkstra's Algorithm
* [x] Add shortest-path reconstruction
* [x] Add negative-weight validation
* [x] Test edge cases and disconnected graphs
* [ ] Optimize Dijkstra using a min-heap (`heapq`)
* [ ] Add execution-time and processing metrics
* [ ] Implement large-scale graph generation
* [ ] Benchmark performance across different graph sizes
* [ ] Add graph visualization
* [ ] Develop an interactive Streamlit dashboard
* [ ] Visualize shortest-path exploration
* [ ] Add comparative performance charts

## 🌐 Potential Applications

* **Navigation Systems:** Finding efficient routes between locations.
* **Computer Networks:** Analyzing routing paths across connected devices.
* **Transportation Networks:** Exploring connections between stations or cities.
* **Logistics:** Evaluating route costs in delivery networks.
* **Graph Research:** Studying algorithm performance across graphs of varying sizes.

## 🎯 Project Goals

The long-term objective is to transform the initial shortest-path implementation into an interactive graph-analysis platform capable of:

* Processing larger weighted graphs.
* Measuring algorithm execution time and computational workload.
* Comparing performance across graph sizes.
* Visualizing graphs and computed shortest paths.
* Demonstrating the impact of algorithmic optimization on scalability.

---

**Project Status:** 🚧 Under Active Development

*Developed as an academic project for Large Scale Graph Analysis.*
