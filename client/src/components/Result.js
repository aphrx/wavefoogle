import React from 'react';
import './Result.css';
import { motion } from "framer-motion"

export default function Result(result){



    return (
        <motion.div className="section" initial={{x:1000}} animate={{x:0}}>
            <iframe className="video-frame"  src={`https://www.youtube.com/embed/${result.videoId}?start=${result.startTime}`} title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
            <div className="contents">
                <p>"...{result.caption}..."</p>
            </div>
        </motion.div>
    )
}

