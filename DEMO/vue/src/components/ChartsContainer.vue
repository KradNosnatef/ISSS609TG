<template>
    <div style="text-align: center;">
        <button @click="drawChart">draw</button>
        <div id="main" style="width: 80%;height: 200px;position: relative;margin: auto;outline: auto;"></div>
    </div>
</template>

<script>
import * as echarts from 'echarts'
export default {
    data() {
        return ({
        })
    },
    watch:{
        chartParams(){
            this.drawChart()
        }
    },
    created: function () {
        setTimeout(this.drawChart,1000)
    },
    methods: {
        drawChart() {
            let myChart = echarts.init(document.getElementById("main"))
            let option = {
                xAxis: {
                    type: 'category',
                    axisTick: {
                        alignWithLabel: true
                    },
                    data: this.chartParams.xName,
                    name:"month"
                },
                yAxis: {
                    type: 'value',
                    name: "Number",
                    minInterval: 1
                },
                series: [
                    {
                        data: this.chartParams.yValue,
                        type: 'bar'
                    }
                ]
            }
            myChart.setOption(option)
        }
    },
    name: 'ChartsContainer',
    components: {
    },
    props: {
        chartParams:Object
    }
}
</script>

<style></style>