import React from "react";
import { useNavigate } from "react-router-dom";

export default function SearchBar({ onSearched }) {
    const navigate = useNavigate();
    const handleClick = () => {
        navigate("/search");
    };

    return (
        <input
            className="search-bar"
            type="text"
            placeholder="search for a job..."
            onClick={handleClick}
            onChange={onSearched}
        />
    );
}
