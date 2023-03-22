<template>
  <div>
    <textarea>Filter Options</textarea>
    <br>
    <div style="outline: auto;text-align: center;">
      <label>Rating:</label><select></select>
      <br>
      <label>Time:</label><select></select>
      <br>
      <label>Reviewer Location:</label><select></select>
      <br>
      <label>Sentiment:</label><select></select>
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
      commentsArray:null,
      filterOption: "NONE"
    })
  },
  created: function () {
    axios.get("/cmd/getAllComments").then(response=>{
      console.log(response.data)
      this.commentsArray=response.data
    })
  },
  methods: {
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
