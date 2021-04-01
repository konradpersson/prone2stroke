<template>
  <div>
      <code>Result goes here</code>
       <p>{{ prediction.probability }}%</p>
  </div>
</template>

<script>
import Prediction from './components/Prediction.vue'
export default {
  components: {
    Prediction
  },
  computed: {
    prediction() {
      return this.$store.state.prediction
    }
  }
}
</script>

<style>

</style>