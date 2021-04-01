<template>
  <div>
    <HomeHero />
    <HomePronePreview />
    <HomeProneKSPs />
  </div>
</template>

<script>
import HomeHero from '../components/HomeHero.vue'
import HomeProneKSPs from '../components/HomeProneKSPs.vue'
import HomePronePreview from '../components/HomePronePreview.vue'

export default {
  components: { HomeHero, HonePronePreview, HomeProneKSPs },
}
</script>

<style>

</style>