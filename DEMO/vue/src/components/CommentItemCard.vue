<template>
    <div style="outline: auto;">
        <label style="float: left;">Posted in: {{ comment[2] }}</label>
        <br>
        <div style="float: left;margin-left: 30px;">
            <label v-for="i in comment[1]" style="float: left;" :key="i">&#127775;</label>
        </div>
        <br>
        <label style="float: left;">Visitor from: {{ comment[3] }}</label>
        <br>
        <p style="text-align: left;margin-left: 30px;">{{ comment[4] }}</p>
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
        comment: Array
    }
}
</script>

<style></style>