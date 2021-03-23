import { createStore } from 'vuex'

// Reach this from anywhere
// this.$store.state.prediction
const state = {
    prediction: {
        willClick: false,
        probability: 0
    }
}

// Call this from anywhere
// this.$store.commit('setPrediction', prediction)
const mutations = {
    setPrediction(state, prediction) {
        state.prediction = prediction
    }
}

export default createStore({ state, mutations})