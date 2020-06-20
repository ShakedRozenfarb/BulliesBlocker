import React, { Component } from "react";
import ReactDOM from "react-dom";
import { Charts, ChartContainer, ChartRow, YAxis, LineChart, Baseline} from "react-timeseries-charts";
import { TimeSeries, TimeRange } from "pondjs";
import _ from 'lodash';

class GraphComponent extends Component {

    constructor(props) {
        super(props);
        const iteratees = array => array[0];
        this.state = {
            userResults: this.props.userResults,
            timeSeries: new TimeSeries({
                name: "tweets",
                columns: ["time", "bullyScore"],
                points: _.sortBy(this.props.userResults.tweets.map(result => {
                    const resultArray = [];
                    resultArray.push(new Date(result.tweet_date).getTime());
                    resultArray.push(result.is_bully*1);
                    return resultArray;
                }), iteratees)
            })
        };

        this.getTimeRange = this.getTimeRange.bind(this);
    }

    getTimeRange() {
        console.log(this.state.timeSeries.points);
        return this.state.timeSeries.timerange();
    }

    render() {
        return (
            <div>
                <ChartContainer timeRange={this.getTimeRange()} width={600}>
                    <ChartRow height="400">
                        <YAxis id="bullyScore" label="bullyScore" min={0} max={1} width="60" type="linear" format=",.2f"/>
                        <Charts>
                            <LineChart axis="bullyScore" series={this.state.timeSeries} columns={["bullyScore"]} style={{
                                bullyScore: {
                                    normal: {stroke: "#40b6ce", fill: "none", strokeWidth: 1},
                                    highlighted: {stroke: "#40b6ce", fill: "none", strokeWidth: 1},
                                    selected: {stroke: "#40b6ce", fill: "none", strokeWidth: 1},
                                    muted: {stroke: "#40b6ce", fill: "none", opacity: 0.4, strokeWidth: 1}
                                }
                            }}/>
                            <Baseline axis="bullyScore" value={1} label="Max" position="right"/>
                        </Charts>
                    </ChartRow>
                </ChartContainer>
            </div>
        )
    }
}

export default GraphComponent;

