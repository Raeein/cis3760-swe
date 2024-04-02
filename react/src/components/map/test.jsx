import React, { useState, useEffect } from "react";
import { APIProvider, Map, Marker } from "@vis.gl/react-google-maps";
import "./JobMap.css";

export default function JobMap({ location }) {
    const [address, setAddress] = useState("");
    const [coordinates, setCoordinates] = useState({ lat: 0, lng: 0 });

    useEffect(() => {
        setAddress(location);
    }, [location]);

    useEffect(() => {
        const handleConvert = () => {
            const apiKey = "YOUR_API_KEY_HERE"; // Replace with your Google Maps API key
            const encodedAddress = encodeURIComponent(address);
            const apiUrl = `https://maps.googleapis.com/maps/api/geocode/json?address=${encodedAddress}&key=${apiKey}`;

            fetch(apiUrl)
                .then((response) => response.json())
                .then((data) => {
                    if (data.status === "OK") {
                        const { lat, lng } = data.results[0].geometry.location;
                        setCoordinates({ lat, lng });
                    } else {
                        console.error(
                            "Geocode was not successful for the following reason:",
                            data.status
                        );
                    }
                })
                .catch((error) => {
                    console.error("Error fetching geocode data:", error);
                });
        };

        if (address.trim() !== "") {
            handleConvert();
        }
    }, [address]);

    console.log(coordinates);

    return (
        <div className="JobMap">
            <APIProvider apiKey="YOUR_API_KEY_HERE">
                <Map
                    center={{
                        lat: coordinates.lat,
                        lng: coordinates.lng,
                    }}
                    zoom={10}
                    dragPan={true} // Enable dragging and panning
                >
                    <Marker
                        position={{
                            lat: coordinates.lat,
                            lng: coordinates.lng,
                        }}
                        label=""
                    />
                </Map>
            </APIProvider>
        </div>
    );
}
