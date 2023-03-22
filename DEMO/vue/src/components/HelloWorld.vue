<template>
  <div>
    <textarea>Filter Options</textarea>
    <br>
    <div style="outline: auto;text-align: center;">
      <label>Branch:</label><select v-model="filterOption.branch" @change="onEngageFilter">
        <option :value="nullValue">all</option>
        <option value="Disneyland_California">California</option>
        <option value="Disneyland_HongKong">HongKong</option>
        <option value="Disneyland_Paris">Paris</option>
      </select>
      <br>
      <label>Rating:</label><select v-model="filterOption.rating" @change="onEngageFilter">
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
      <label>Reviewer Location:</label><select v-model="filterOption.reviewerLocation" @change="onEngageFilter">
        <option :value="nullValue">all</option>
        <option v-for="i in possibleReviewerLocationList.length-1" :key="i" :value="possibleReviewerLocationList[i]">{{ possibleReviewerLocationList[i] }}</option>
      </select>
      <br>
      <label>Sentiment:</label><select v-model="filterOption.sentiment" @change="onEngageFilter">
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
    </div>

    <div style="margin-top: 30px;">
      <CommentItemCard v-for="comment in commentsArray" :key="comment[0]" :comment="comment"></CommentItemCard>
    </div>
  </div>
</template>

<script>
const axios = require('axios').default
import CommentItemCard from './CommentItemCard.vue';
export default {
  data() {
    return ({
      commentsArray: null,
      filterOption: {
        returnNumberLimit: 8,
        rating: null,
        monthNotLastThan:null,
        reviewerLocation:null,
        branch:null,
        dominantTopic:null,
        sentiment:null,
        orderBy:"yearMonth",
        DESCorASC:"DESC",
      },
      possibleReviewerLocationList:[],
      nullValue:null
    })
  },
  created: function () {
    axios.get("/cmd/getPossibleReviewerLocation").then(reponse=>{
      this.possibleReviewerLocationList=reponse.data
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
    },
    onEngageFilter(){
      this.refreshList()
    }
  },
  name: 'HelloWorld',
  components: {
    CommentItemCard
  },
  props: {
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped></style>
