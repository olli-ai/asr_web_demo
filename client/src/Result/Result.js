import React, { useState, useEffect } from "react";

function Result({ res }) {
    const [time_cfm, setTime_cfm] = useState('');
    const [cfm, setCfm] = useState('');

    useEffect(() => {
        if (res) {
            setCfm(res.cfm.transcript);
            setTime_cfm(res.cfm.time);
        }
    }, [res]);

    return (

        <div>
            <div className="row mt-4 pt-3 ">
                <h3 className="col-md-2">Model</h3>
                <h3 className="col-md-8 text-center">Transcript</h3>
                <h3 className="col-md-2">Time (s)</h3>
            </div>
            {res && (
                <div className="mt-2 pt-2">
                    <div className="row justify-content-sm-center overflow-auto">
                        <h4 className="col-2">Conformer</h4>
                        <div id="res" className="col-md-8">
                            <span className="align-middle font-weight-bold" style={{ fontSize: 15 }}>{cfm}</span>
                        </div>
                        <p className="col-md-2 font-italic">{time_cfm}</p>
                    </div>
                </div>
            )
            }
        </div>
    );
}

export default Result;