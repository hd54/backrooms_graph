import React, { Component } from "react";
import ReactFlow, {MiniMap} from "reactflow";

export default class HomePage extends Component {
    constructor(props) {
        super(props);

        this.state = {
            elements: [],
        };
    }

     componentDidMount() {
        function transformDataToElements(data) {
            return JSON.stringify(data.map(node => ({
                id: node.id,
                type: 'default', // Use a default node type
                data: {
                    level: node.level,
                    description: node.description,
                    link: node.link,
                }
            })));
        }

        // Fetch data when the component mounts
        fetch('/backrooms/api')
            .then(response => response.json())
            .then(data => {
                const elements = transformDataToElements(data)
                this.setState({ elements })
            })
            .catch(error => {
                console.error('Error fetching data:', error);
            });
    }

    // template
    render() {
        const { elements } = this.state;

        return (
            <div>
                <ReactFlow elements={elements}>
                    <MiniMap/>
                    <p>Works now?</p>
                </ReactFlow>
            </div>
        );
    }
}
