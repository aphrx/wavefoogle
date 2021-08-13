import React from 'react';
import './Result.css';

export default function Result(result){

    return (
        <div className="card">
            
            <iframe className="video-frame" width="560" height="315" src={`https://www.youtube.com/embed/${result.videoId}?start=${result.startTime}`} title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
            <div className="contents">
                <p>"...{result.caption}..."</p>
            </div>
        </div>
    )
}

