<template>
    <div style="outline: auto;">
        <label style="float: left;">Posted at: {{ comment[2] }}</label>
        <br>
        <label style="float: left;">&emsp; Visitor from: {{ comment[3] }}</label>
        <br>
        <div style="margin-left: 30px;">{{ comment[4] }}</div>
    </div>
</template>

<script>
export default {
    data() {
        return ({
        })
    },
    methods: {
    },
    components: {
    },
    props: {
        comment:Array
    }
}
</script>

<style></style>