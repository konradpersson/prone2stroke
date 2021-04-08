<template>
  <div>
      <code></code>
       <p>{{ prediction.probability }}% chance to get a stroke</p>
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
  font-size: 8em;
}


</style>