<template>
    <div class="intro">
        <ProneAppIntro />
        <!-- <ProneAppKSP /> -->
    </div>
  <div>
      <div class="app">
        <Prone2StrokeApp />
      </div>

    <div class="result">
        <Prone2StrokeAppResult />
    </div>

  </div>
</template>

<script>
import Prone2StrokeApp from '../components/Prone2StrokeApp.vue'
import Prone2StrokeAppResult from '../components/Prone2StrokeAppResult.vue'
import ProneAppIntro from '../components/ProneAppIntro.vue'
import ProneAppKSP from '../components/ProneAppKSP.vue'
export default {
  components: { ProneAppIntro, ProneAppKSP, Prone2StrokeApp, Prone2StrokeAppResult },

}
</script>

<style scoped>
.intro{
  margin-left: 6em;
  margin-right: 6em;
}


.app{
  margin-left: 6em;
  margin-right: 6em;
  display: inline-block;

}

.result{
  display: inline-block;
  line-height: 1;
  margin-left: 1em;
  width: 50%
}


</style>