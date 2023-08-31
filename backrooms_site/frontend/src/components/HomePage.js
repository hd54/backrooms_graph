import React, { Component } from "react";
import ReactFlow, { ReactFlowProvider } from 'reactflow';
import CytoscapeGraph from "./CytoscapeGraph"; // Import the CytoscapeGraph component

export default class HomePage extends Component {
    constructor(props) {
        super(props);

        this.state = {
            elements: {
                nodes: [],
                edges: [],
            },
    };

        this._isMounted = false;
    };


    componentDidMount() {
        this._isMounted = true;
        function transformDataToElements(data) {
            const nodes =  data.map((node) => ({
                id: node.level,
                type: 'default',
                data: {
                    level: node.level,
                    description: node.description,
                    link: node.link,
                    entrance: node.entrance,
                    outlet: node.outlet
                },
            }));

            const edges = []
            data.forEach((node) => {
                const entranceArray = JSON.parse(node.entrance)
                entranceArray.forEach((targetID) => {
                    edges.push({
                        id: `edge-${node.level}-${targetID}`,
                        source: node.level,
                        target: targetID,
                    });
                });
            });

            return { nodes, edges };
        }

         fetch('/backrooms/api')
            .then(response => response.json())
            .then(data => {
                if (this._isMounted) {
                    const elements = transformDataToElements(data);
                    this.setState({ elements });
                }
            })
            .catch(error => {
                console.error('Error fetching data:', error);
            })
    };

    componentWillUnmount() {
        this._isMounted = false;
    }

    render() {
        if (!this._isMounted) return null;
        const { elements } = this.state;

        return (
            <div style={{ width: '100%', height: '100%' }}>
                <CytoscapeGraph elements={elements} />
            </div>
        )
    };
}
