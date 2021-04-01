<template>
<main> <!-- Wrapped for linting -->
  <MainMenu />
  <router-view />
</main>
</template>

<script>
import MainMenu from "./components/MainMenu.vue";
export default {
  name: 'App',
  components: {
    MainMenu
  }
}
</script>

<style scoped>
  p{
    font-size: 100px;
  }
</style>