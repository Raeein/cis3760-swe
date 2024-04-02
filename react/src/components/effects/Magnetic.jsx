import React from "react";
import { useRef, useState } from "react";
import { motion } from "framer-motion";

export default function Magnetic({ children }) {
    function onMouseMove(e) {
        const { clientX, clientY } = e;
        const { left, top, width, height } =
            magRef.current.getBoundingClientRect();
        const x = clientX - left - width / 2;
        const y = clientY - top - height / 2;
        setPosition({ x, y });
    }

    function onMouseLeave() {
        setPosition({ x: 0, y: 0 });
    }

    const magRef = useRef(null);
    const [position, setPosition] = useState({ x: 0, y: 0 });
    return (
        <motion.div
            ref={magRef}
            animate={{ x: position.x * 0.5, y: position.y * 0.5 }}
            onMouseMove={onMouseMove}
            onMouseLeave={onMouseLeave}
            className="magnetic"
            transition={{
                type: "spring",
                stiffness: 300,
                damping: 10,
                mass: 0.5,
            }}
        >
            {children}
        </motion.div>
    );
}
