# Hackathon
Lesgo
This project combines real-time object detection using YOLOv5 and route optimization with GIS data, providing an efficient system to detect parking zones and plan optimal routes in urban environments. It consists of two key components:

Real-Time Parking Zone Detection:

Utilizing YOLOv5, this system processes video streams to detect parking spaces in real-time. With OpenCV, video frames are analyzed to identify and track cars and open parking spots.
Detected locations are cross-referenced with predefined GIS polygons to verify if they are within designated parking zones. Integration with Geopy and Shapely allows geographic validation of these parking areas.
Route Optimization:

The project leverages OSMnx and NetworkX to calculate the shortest driving routes between two points (e.g., start and destination) in a city, using Baku, Azerbaijan as an example.
The optimal route is displayed on an interactive map using Folium, which marks the start and end points, and plots the shortest path based on road data.
Features:
YOLOv5-based object detection for real-time vehicle and parking space identification.
GIS integration to verify parking availability within specific zones.
OSMnx and NetworkX to compute shortest driving routes.
Interactive maps with route visualization using Folium.
OpenCV for video processing and frame analysis.
How to Run:
Install dependencies (PyTorch, OpenCV, Geopy, Shapely, OSMnx, NetworkX, Folium).
Load a video for real-time parking detection.
Define GIS data for parking zones as polygons.
Use OSMnx to fetch road networks and NetworkX to calculate optimal routes.
Visualize the route on a map using Folium.
Use Cases:
Smart City Applications: Optimize urban mobility by providing real-time parking data and efficient route planning for vehicles.
Sustainable Transportation: Reduce traffic congestion and emissions by guiding vehicles to available parking efficiently.
Feel free to customize the system for different cities or use cases by updating GIS data and integrating real-time GPS locations.
