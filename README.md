Candidate Network Graph
This project visualizes the relationships between candidates using a network graph. Each node in the graph represents a candidate, and the links between nodes represent relationships such as shared skills, colleges, or degrees. The graph is built using Highcharts, a JavaScript charting library, with a specific focus on network graphs.

Purpose
The Candidate Network Graph aims to provide a visual representation of how different candidates are connected based on their educational backgrounds, skills, and professional attributes. It's designed to help recruiters, hiring managers, or team leads better understand the network of available candidates and identify potential synergies based on shared attributes.

Features
Interactive Graph: A dynamic and interactive network graph where users can explore the connections between candidates.
Force-Directed Layout: Uses a force-directed algorithm that creates a fluid, organic structure for the graph, ensuring clear visualization.
Customizable: The network graph can be customized to show different types of relationships based on user-defined criteria, such as shared skills, universities, or graduation years.
CSV Data Integration: The candidate data can be imported directly from a CSV file, allowing for easy updates and management of candidate information.
Neo4j Database Support: (Optional) The project can be extended to integrate with a Neo4j graph database, allowing for more complex querying and visualization of large datasets.
How It Works
Data
The project can be powered by either a CSV file or a graph database (e.g., Neo4j) containing candidate information such as:

Name: The full name of the candidate.
Email: Contact information for reference purposes.
College: The university or college the candidate attended.
Year of Passout: The year the candidate completed their degree.
Degree: The candidate's degree (e.g., B.Tech, B.E., M.Sc.).
Skills: A list of relevant skills or expertise (e.g., Python, Machine Learning, CAD).
Graph Structure
Nodes: Represent individual candidates.
Links/Edges: Represent relationships between candidates, which can be based on common attributes such as shared skills, the same educational institution, or professional collaborations.
Visualization
The network graph is rendered on a web page, where users can explore how different candidates are connected. The force-directed algorithm ensures that the layout of the graph is dynamically adjusted, making it easy to identify clusters of candidates who share common traits.

Customization
Users can modify:

Relationship types: Define which relationships should be shown (e.g., candidates from the same college, candidates with similar skills).
Node/Link appearance: Customize the appearance of nodes and links for better readability.
Setup Instructions
Clone the Project: Download or clone the repository.
Data Preparation: Place the candidate data in a CSV file or populate a Neo4j database with candidate information.
Run the Application: Open the HTML file in a browser or set up a local server if required.
Explore the Graph: Once the data is loaded, the interactive graph will be displayed. Users can hover over nodes to view candidate details and explore connections.
Data Sources
The project is designed to be flexible with data sources:

CSV file: Candidate data can be stored in a CSV file, which is parsed to populate the graph.
Neo4j Database (optional): For more advanced use cases, you can connect the project to a Neo4j graph database, enabling large-scale data handling and querying.
