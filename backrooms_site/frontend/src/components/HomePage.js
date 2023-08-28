import React, { Component, useEffect, useState } from "react";
import ReactFlow from "reactflow";

export default class HomePage extends Component {
    constructor(props) {
        super(props);
    }

    // template
    render() {
        fetch('/backrooms/api').then(response => response.json())
            .then(data => {
                console.log('Works')

            })
            .catch(error => {
                console.error('Error fetching data:', error);
            });
        return <h1>This should work</h1>
    }
}