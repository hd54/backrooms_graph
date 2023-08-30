import React, { Component } from "react";
import cytoscape from "cytoscape";

class CytoscapeGraph extends Component {
  constructor(props) {
    super(props);
    this.cy = null; // Reference to the Cytoscape instance
  }

  componentDidMount() {
    // Initialize Cytoscape within the container element
    this.cy = cytoscape({
      container: this.cyContainer,
      elements: this.props.elements, // Pass graph data as a prop
      layout: { name: "preset" }, // Adjust layout as needed
      style: [
        {
          selector: "node",
          style: {
            shape: "circle", // Change the shape to ellipse or your preferred style
            content: "data(level)",
            width: 5,
            height: 5,
            "background-color": "#3498db", // Customize node background color
            color: "#ffffff", // Customize label text color
            "font-size": 1,
            "text-valign": "center",
            "text-halign": "center",
          },
        },
        // Define additional styles for edges or other elements if needed
      ],
    });
  }

  componentWillUnmount() {
    // Ensure you clean up the Cytoscape instance when unmounting
    if (this.cy) {
      this.cy.destroy();
    }
  }

  render() {
    return (
      <div
        ref={(cyContainer) => (this.cyContainer = cyContainer)}
        style={{ width: "100%", height: "100%" }}
      />
    );
  }
}

export default CytoscapeGraph;
