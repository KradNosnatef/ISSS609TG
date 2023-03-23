<template>
    <div style="text-align: center;">
        <button @click="drawChart">draw</button>
        <div id="main" style="width: 80%;height: 200px;position: relative;margin: auto;outline: auto;"></div>
        <button @click="pageChange(-1)">nxt {{ stepLength }} year</button><select v-model="stepLength" @change="initialChart">
            <option value=1>1y</option>
            <option value=2>2y</option>
            <option value=5>5y</option>
            <option value=10>10y</option>
        </select><button @click="pageChange(1)">pre {{ stepLength }} year</button>
    </div>
</template>

<script>
import * as echarts from 'echarts'
export default {
    data() {
        return ({
            page:0,
            notZeroHead:0,
            stepLength:1
        })
    },
    watch:{
        chartParams(){
            this.initialChart()
        }
    },
    created: function () {
        setTimeout(this.initialChart,1000)
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
                    data: this.chartParams.xName.slice(this.notZeroHead+12*this.page,this.notZeroHead+12*this.page+12*this.stepLength),
                    //data: this.chartParams.xName.slice(46,58),
                    name:"month"
                },
                yAxis: {
                    type: 'value',
                    name: "Number",
                    minInterval: 1
                },
                series: [
                    {
                        data: this.chartParams.yValue.slice(this.notZeroHead+12*this.page,this.notZeroHead+12*this.page+12*this.stepLength),
                        //data: this.chartParams.yValue.slice(46,58),
                        type: 'bar'
                    }
                ]
            }
            myChart.setOption(option)
        },
        initialChart(){
            for(var i=0;i<this.chartParams.xName.length;i++){
                if (this.chartParams.yValue[i]>0){
                    this.notZeroHead=i
                    break
                }
            }
            this.page=0
            this.drawChart()
            //alert(i)
        },
        pageChange(n){
            this.page=this.page+n*this.stepLength
            if(this.page<0)this.page=0
            this.drawChart()
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