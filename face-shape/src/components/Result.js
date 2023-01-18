import React, { Component } from "react";
import aviators from "../assets/aviators.jpg";
import browline from "../assets/browline.jpg";
import classicWayFrame from "../assets/classicwayframe.jpg";
import geometric from "../assets/geometric.jpg";
import oval from "../assets/oval.jpg";
import rectSpecs from "../assets/rectanglespecs.jpg";
import round from "../assets/round.jpg";
import square from "../assets/square.jpg";
import wrap from "../assets/wrap.jpg";

const Result = (props) => {
    const { type } = props;
    var specs;
    switch(type) {
        case "aviators":
            specs = aviators;
            break;
        case "browline":
            specs = browline;
            break;
        case "classic wayframe":
            specs = classicWayFrame;
            break;
        case "geometric":
            specs = geometric;
            break;
        case "oval":
            specs = oval;
            break;
        case "rectangle":
            specs = rectSpecs;
            break;
        case "round":
            specs = round;
            break;
        case "square":
            specs = square;
            break;
        case "wrap":
            specs = wrap;
            break;
    }

    return (
        <div>
            <h2>{type} frame</h2>
            <img src={specs}></img>
        </div>
    );
};

export default Result