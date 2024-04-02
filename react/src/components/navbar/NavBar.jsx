import React from "react";
import { motion } from "framer-motion";
import Magnetic from "../effects/Magnetic";
import "./NavBar.css";
export default function NavBar() {
    return (
        <div className="navbar">
            <span className="logo-wrapper">
                <motion.h1
                    className="logo"
                    initial={{
                        y: 80,
                        opacity: 0,
                    }}
                    animate={{
                        y: 0,
                        opacity: 1,
                    }}
                    transition={{ duration: 1.2, ease: [0.33, 1, 0.68, 1] }}
                >
                    GeoJobSearch
                </motion.h1>
            </span>
            <nav>
                <ul className="nav-menu">
                    <li className="nav-item">
                        <Magnetic>
                            <a href="#">Home</a>
                        </Magnetic>
                    </li>
                    <li className="nav-item">
                        <Magnetic>
                            <a href="#">About</a>
                        </Magnetic>
                    </li>
                    <li className="nav-item">
                        <Magnetic>
                            <a href="#">Contact</a>
                        </Magnetic>
                    </li>
                    <li className="nav-item">
                        <Magnetic>
                            <a href="#">Maps</a>
                        </Magnetic>
                    </li>
                    <li className="nav-item">
                        <Magnetic>
                            <a href="#">Team</a>
                        </Magnetic>
                    </li>
                </ul>
            </nav>
        </div>
    );
}
