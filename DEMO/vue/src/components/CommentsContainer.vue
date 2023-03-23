<template>
  <ChartsContainer :chartParams="chartParams"></ChartsContainer>
  <div>
    <label>Filter Options</label>
    <br>
    <label>option with * will also filter the display of dashboard</label>
    <br>
    <div style="outline: auto;text-align: center;">
      <label>*Branch:</label><select v-model="filterOption.branch" @change="onEngageFilter">
        <option :value="nullValue">all</option>
        <option value="Disneyland_California">California</option>
        <option value="Disneyland_HongKong">HongKong</option>
        <option value="Disneyland_Paris">Paris</option>
      </select>
      <br>
      <label>*Rating:</label><select v-model="filterOption.rating" @change="onEngageFilter">
        <option :value="nullValue">all</option>
        <option value=1>1</option>
        <option value=2>2</option>
        <option value=3>3</option>
        <option value=4>4</option>
        <option value=5>5</option>
      </select>
      <br>
      <label>Time:</label><select v-model="filterOption.monthNotLastThan" @change="onEngageFilter">
        <option :value="nullValue">all</option>
        <option value=1>within 1 month</option>
        <option value=6>within 6 months</option>
        <option value=12>within 1 year</option>
        <option value=24>within 2 years</option>
        <option value=60>within 5 years</option>
        <option value=120>within 10 years</option>
      </select>
      <br>
      <label>*Reviewer Location:</label><select v-model="filterOption.reviewerLocation" @change="onEngageFilter">
        <option :value="nullValue">all</option>
        <option v-for="i in possibleReviewerLocationList.length - 1" :key="i" :value="possibleReviewerLocationList[i]">{{
          possibleReviewerLocationList[i] }}</option>
      </select>
      <br>
      <label>*Sentiment:</label><select v-model="filterOption.sentiment" @change="onEngageFilter">
        <option :value="nullValue">all</option>
        <option value="positive">positive</option>
        <option value="negative">negative</option>
      </select>
      <br>
      <label>Order by:</label><select v-model="filterOption.orderBy" @change="onEngageFilter">
        <option value="yearMonth">Time</option>
        <option value="rating">Rating</option>
      </select>
      <br>
      <select v-model="filterOption.DESCorASC" @change="onEngageFilter">
        <option value="DESC">descend</option>
        <option value="ASC">ascend</option>
      </select>
      <div v-if="filterOption.dominantTopic">
        <label>You are using topic filter</label>
        <br>
        <button @click="disengageDominantTopicFilter">disengage topic filter</button>
      </div>
    </div>
    <div style="margin-top: 10px;">
      <label>page:{{ filterOption.page + 1 }}</label>
      <br>
      <button @click="pageChange(-1)">pre page</button><button @click="pageChange(0)">return to head</button><button
        @click="pageChange(1)">nxt page</button>
    </div>
    <div style="margin-top: 5px;">
      <CommentItemCard v-for="comment in commentsArray" :key="comment[0]" :comment="comment"
        @engageDominantTopicFilter="engageDominantTopicFilter"></CommentItemCard>
    </div>
  </div>
</template>

<script>
import ChartsContainer from './ChartsContainer.vue';
const axios = require('axios').default
import CommentItemCard from './CommentItemCard.vue';
export default {
  data() {
    return ({
      commentsArray: null,
      filterOption: {
        returnNumberLimit: 8,
        rating: null,
        monthNotLastThan: null,
        reviewerLocation: null,
        branch: null,
        dominantTopic: null,
        sentiment: null,
        orderBy: "yearMonth",
        DESCorASC: "DESC",
        page: 0
      },
      chartParams:{
        xName:[],
        yValue:[]
      },
      possibleReviewerLocationList: [],
      nullValue: null
    })
  },
  created: function () {
    axios.get("/cmd/getPossibleReviewerLocation").then(reponse => {
      this.possibleReviewerLocationList = reponse.data
      console.log(this.possibleReviewerLocationList)
    })

    this.refreshList()
  },
  methods: {
    refreshList() {
      axios.post("/cmd/getCommentsWithFilter", this.filterOption).then(response => {
        console.log(response.data)
        this.commentsArray = response.data
      })
      axios.post("/cmd/getCommentsNumberGroupByYearMonthWithFilter",this.filterOption).then(response=>{
        console.log(response.data)
        this.chartParams=response.data
      })
    },
    onEngageFilter() {
      this.filterOption.page = 0
      this.refreshList()
    },
    pageChange(index) {
      if (index == 0) this.filterOption.page = 0
      else this.filterOption.page = this.filterOption.page + index

      if (this.filterOption.page < 0) this.filterOption.page = 0
      this.refreshList()
    },
    engageDominantTopicFilter(n) {
      console.log(n)
      this.filterOption.dominantTopic = n
      this.onEngageFilter()
    },
    disengageDominantTopicFilter(){
      this.filterOption.dominantTopic=null
      this.onEngageFilter()
    }
  },
  name: 'CommentsContainer',
  components: {
    CommentItemCard,
    ChartsContainer
  },
  props: {
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped></style>
