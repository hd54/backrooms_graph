import React, { Component } from "react";
import ReactFlow, { ReactFlowProvider } from 'reactflow';
import CytoscapeGraph from "./CytoscapeGraph"; // Import the CytoscapeGraph component

export default class HomePage extends Component {
    constructor(props) {
        super(props);

        this.state = {
            elements: []
        }

        this._isMounted = false;
    };


    componentDidMount() {
        this._isMounted = true;
        function transformDataToElements(data) {
            return data.map((node) => ({
                id: node.id,
                type: 'default',
                data: {
                    level: node.level,
                    description: node.description,
                    link: node.link
                },
                position: {
                    x: Math.random() * 1000,
                    y: Math.random() * 1000,
                },
            }));
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
