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

    // initialize
    this.cy = cytoscape({
      container: this.cyContainer,
      elements: this.props.elements,
      layout: {
        name: "cose-bilkent",
        animate: true,
      },
      style: [
          {
            selector: "node",
            style: {
              shape: "ellipse",
              content: "data(level)",
              width: 10,
              height: 10,
              "background-color": "#3498db",
              color: "#ffffff",
              "font-size": 1,
              "text-valign": "center",
              "text-halign": "center"
            },
          }
      ],
      wheelSensitivity: 0.1,
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
