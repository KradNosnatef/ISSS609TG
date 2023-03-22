<template>
    <div style="outline: auto;margin-top: 10px;">
        <label style="float: left;">Posted in: {{ comment[2] }}</label>
        <br>
        <div style="float: left;margin-left: 30px;">
            <label v-for="i in comment[1]" style="float: left;" :key="i">&#127775;</label>
        </div>
        <br>
        <label style="float: left;">Visitor from: {{ comment[3] }}</label>
        <br>
        <p style="text-align: left;margin-left: 30px;">{{ comment[4] }}</p>
        <br>
        <button style="margin-bottom: 20px;" @click="engageDominantTopicFilter">see more reviews like this</button>
    </div>
</template>

<script>
export default {
    data() {
        return ({
        })
    },
    methods: {
        engageDominantTopicFilter(){
            this.$emit('engageDominantTopicFilter',this.comment[6])
        }
    },
    components: {
    },
    props: {
        comment: Array
    }
}
</script>

<style></style>