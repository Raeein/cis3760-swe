import React from "react";

("use client");

import {
    APIProvider,
    Map,
    // useMap,
    // AdvancedMarker,
} from "@vis.gl/react-google-maps";
// import { MarkerClusterer } from "@googlemaps/markerclusterer";
// import { useEffect, useState, useRef } from "react";
import "./JobMap.css";

export default function JobMap() {
    return (
        <div className="JobMap">
            <APIProvider apiKey="AIzaSyD5jc3qLhA6YtegDcyd6DRL4PjEeVn8PR4">
                <Map center={{ lat: 43.64, lng: -79.41 }} zoom={10}></Map>
            </APIProvider>
        </div>
    );
}
