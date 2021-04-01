<template>
  <div>
      <code>Result goes here</code>
       <p>{{ prediction.probability }}%</p>
  </div>
</template>

<script>
export default {
  computed: {
    prediction() {
      return this.$store.state.prediction
    }
  }
}
</script>

<style>

</style>