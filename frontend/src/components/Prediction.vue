<template>
    <form @submit.prevent="predict">
        <h3>Testing probability prediction</h3>
        <input v-model="gender" type="text" placeholder="gender"/>
        <input v-model="age" type="text" placeholder="age"/>
        <input v-model="hypertension" type="text" placeholder="hypertension"/>
        <input v-model="heart_disease" type="text" placeholder="heart-disease"/>
        <input v-model="ever_married" type="text" placeholder="ever-married"/>
        <input v-model="work_type" type="text" placeholder="work-type"/>
        <input v-model="residence_type" type="text" placeholder="residence-type"/>
        <input v-model="avg_glucose_level" type="text" placeholder="avg-glucose-level"/>
        <input v-model="bmi" type="text" placeholder="income"/>
        <input v-model="smoking_status" type="text" placeholder="smoking-status"/>
        <button>Submit</button>
    </form>
</template>

<script>
export default {
    data() {
        return {
            gender: '',
            age: '',
            hypertension: '',
            heart_disease: '',
            ever_married: '',
            work_type: '',
            residence_type: '',
            avg_glucose_level: '',
            bmi: '',
            smoking_status: ''

        }
    },
    methods: {
        async predict() {
            let values = {
                gender: this.gender,
                age: this.age,
                hypertension: this.hypertension,
                heart_disease: this.heart_disease,
                ever_married: this.ever_married,
                work_type: this.work_type,
                residence_type: this.residence_type,
                avg_glucose_level: this.avg_glucose_level,
                bmi: this.bmi,
                smoking_status: this.smoking_status
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