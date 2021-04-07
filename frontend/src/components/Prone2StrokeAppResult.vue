<template>
  <div>
      <code></code>
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

<style scoped>
p{
  font-size: 15em;
}


</style>