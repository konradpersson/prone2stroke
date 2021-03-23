<template>
    <form @submit.prevent="predict">
        <h3>Testing probability prediction</h3>
        <input v-model="age" type="text" placeholder="age"/>
        <input v-model="income" type="text" placeholder="income"/>
        <button>Submit</button>
    </form>
</template>

<script>
export default {
    data() {
        return {
            age: '',
            income: '',
        }
    },
    methods: {
        async predict() {
            let values = {
                age: this.age,
                income: this.income
            }

            let res = await fetch('api/predict', {
                method: 'POST',
                body: JSON.stringify(values)
            })

            let prediction = await res.json()

            
            this.$store.commit('setPrediction', prediction)

            console.log(prediction)
        }
    },
    created() {
    }
}
</script>

<style>

</style>