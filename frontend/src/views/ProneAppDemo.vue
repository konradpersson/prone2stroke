<template>
    <div>
        <ProneAppIntro />
        <ProneAppKSP />
        <Prone2StrokeApp />
        <Prone2StrokeAppResult />
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

<style>

</style>