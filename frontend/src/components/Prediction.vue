<template>
    <form @submit.prevent="predict">
        <h3>Testing probability prediction</h3>
        <input v-model="gender" type="text" placeholder="gender"/>
        <input v-model="age" type="text" placeholder="age"/>
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
        console.log("Prediction Component Created")
        this.predict({
            gender: 1, 
            age: 72, 
            work_type: 1, 
            residence_type: 1, 
            avg_glucose_level: 1, 
            bmi: 32, 
            smoking_status: 1
            })
    }
}
</script>

<style>

</style>