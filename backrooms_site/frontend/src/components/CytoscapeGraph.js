import React, { Component } from "react";
import cytoscape from "cytoscape";
import coseBilkentLayout from "cytoscape-cose-bilkent";

class CytoscapeGraph extends Component {
  constructor(props) {
    super(props);
    this.cy = null;
  }

  componentDidMount() {
    cytoscape.use(coseBilkentLayout);
    console.log(this.props.elements);
    // initialize
    this.cy = cytoscape({
      container: this.cyContainer,
      layout: {
        name: "cose-bilkent",
      },
      style: [
          {
            selector: "node",
            style: {
              "label": "data(level)",
              width: 10,
              height: 10,
              "background-color": "#3498db",
              color: "#ffffff",
              "font-size": 1,
              'text-wrap': 'wrap',
              "text-valign": "center",
              "text-halign": "center"
            },
          },
          {
            selector: "edge",
            style: {
              'width': 3,
              'line-color': '#ccc',
              'target-arrow-color': '#ccc',
              'target-arrow-shape': 'triangle'
            },
          },
      ],
      wheelSensitivity: 0.2,
    });
    const { nodes, edges } = this.props.elements;
    this.cy.add(nodes);
    this.cy.ready(() => {
      this.cy.add(edges);
    });

    this.cy.layout({ name: "cose-bilkent" }).run();
  }

  componentWillUnmount() {
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
