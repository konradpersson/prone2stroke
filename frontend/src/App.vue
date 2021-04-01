<template>
<main> <!-- Wrapped for linting -->
  <MainMenu />
  <router-view />
  <!-- <img alt="Vue logo" src="./assets/logo.png" /> -->
  <!-- <HelloWorld msg="Hello Vue 3.0 With Sanic and AI + Vite" /> -->
  <!-- <p>Will click: {{ prediction.WillClick }}</p> -->
  <!-- <p>probability: {{ prediction.probability }}</p> -->
    <div>
        <p>{{ prediction.probability }}% CHANCE TO GET A STROKE</p>
     </div>
</main>
</template>

<script>
import Prediction from './components/Prediction.vue'
import MainMenu from "./components/MainMenu.vue";

export default {
  name: 'App',
  components: {
    Prediction,
    MainMenu
  },
  computed: {
    prediction() {
      return this.$store.state.prediction
    }
  }
}
</script>

<style scoped>
  p{
    display: inline-block;
    font-size: 100px;
    width: 500px;
    margin-top: -50px;
  }

</style>