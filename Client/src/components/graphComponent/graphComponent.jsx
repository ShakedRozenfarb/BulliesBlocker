import React, { Component } from "react";
import ReactDOM from "react-dom";
import { Charts, ChartContainer, ChartRow, YAxis, LineChart, Baseline} from "react-timeseries-charts";
import { TimeSeries, TimeRange } from "pondjs";
import _ from 'lodash';

class GraphComponent extends Component {

    constructor(props) {
        super(props);

        this.state = {
            userResults: this.props.userResults,
            timeSeries: new TimeSeries({
                name: "tweets",
                columns: ["time", "bullyScore"],
                points: this.getTimeSeries()
            })
        };

        this.getTimeRange = this.getTimeRange.bind(this);
    }

    getTimeSeries() {
        const timeDict = {};
        const iteratees = array => array[0];
        this.props.userResults.tweets.forEach(result => {
            const date = new Date(result.tweet_date);
            const monthBegining = new Date(date.getFullYear(), date.getMonth(), 1);
            if (!timeDict[monthBegining]) {
                timeDict[monthBegining] = 0;
            }
            if (result.is_bully) {
                timeDict[monthBegining] += 1;
            }
        });
        const today = new Date;
        const sortedDates = _.sortBy(_.keys(timeDict), function(value) {return new Date(value);});
        let date = new Date(sortedDates[0]);
        while (date < today) {
            date = new Date(date.getFullYear(), date.getMonth() + 1, 1);
            if (!timeDict[date]) {
                timeDict[date] = 0;
            }
        }
        return _.sortBy(_.keys(timeDict).map(date => {
            const resultArray = [];
            resultArray.push(new Date(date).getTime());
            resultArray.push(timeDict[date]);
            return resultArray;
        }), iteratees)
    }

    getTimeRange() {
        console.log(this.state.timeSeries.timerange());
        return this.state.timeSeries.timerange();
    }

    render() {
        return (
            <div>
                <ChartContainer timeRange={this.getTimeRange()} width={600}>
                    <ChartRow height="250">
                        <YAxis id="bullyScore" label="bullyScore" min={0} max={this.state.timeSeries.max("bullyScore")} width="60" format=",.2f" tickCount={this.state.timeSeries.max("bullyScore") + 1}/>
                        <Charts>
                            <LineChart axis="bullyScore" series={this.state.timeSeries} columns={["bullyScore"]} style={{
                                bullyScore: {
                                    normal: {stroke: "#40b6ce", fill: "none", strokeWidth: 1},
                                    highlighted: {stroke: "#40b6ce", fill: "none", strokeWidth: 1},
                                    selected: {stroke: "#40b6ce", fill: "none", strokeWidth: 1},
                                    muted: {stroke: "#40b6ce", fill: "none", opacity: 0.4, strokeWidth: 1}
                                }
                            }}/>
                            <Baseline axis="bullyScore" value={this.state.timeSeries.max("bullyScore")} label="Max" position="right"/>
                        </Charts>
                    </ChartRow>
                </ChartContainer>
            </div>
        )
    }
}

export default GraphComponent;

