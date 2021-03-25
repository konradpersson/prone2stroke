<template>
<main> <!-- Wrapped for linting -->
  <MainMenu />
  <router-view />
  <!-- <img alt="Vue logo" src="./assets/logo.png" /> -->
  <!-- <HelloWorld msg="Hello Vue 3.0 With Sanic and AI + Vite" /> -->
  <!-- <Prediction /> -->
  <!-- <p>Will click: {{ prediction.WillClick }}</p> -->
  <!-- <p>probability: {{ prediction.probability }}</p> -->
</main>
</template>

<script>
import HelloWorld from './components/HelloWorld.vue'
import Prediction from './components/Prediction.vue'
import MainMenu from "./components/MainMenu.vue";

export default {
  name: 'App',
  components: {
    HelloWorld,
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