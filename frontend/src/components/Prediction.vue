<template>
    <h3>Testing probability prediction</h3>
    <form @submit.prevent="predict">
        <label for="gender">Gender</label>
        <input v-model="gender" type="text" placeholder="gender"/>
        <label for="age">Age</label>
        <input v-model="age" type="text" placeholder="age"/>
        <label for="work_type">Work Type</label>
        <input v-model="work_type" type="text" placeholder="work-type"/>
        <label for="residence_type">Residence Type</label>
        <input v-model="residence_type" type="text" placeholder="residence-type"/>
        <label for="avg_glucose_level">AVG glucose level</label>
        <input v-model="avg_glucose_level" type="text" placeholder="avg-glucose-level"/>
        <label for="bmi">Bmi</label>
        <input v-model="bmi" type="text" placeholder="bmi"/>
        <label for="smoking_status">Smoking status</label>
        <input v-model="smoking_status" type="text" placeholder="smoking-status"/>
        <button>Submit</button>
    </form>
</template>

<script>
export default {
    data() {
        return {
            gender: 0,
            age: 0,
            work_type: 0,
            residence_type: 0,
            avg_glucose_level: 0,
            bmi: 0,
            smoking_status: 0
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
    }
}
</script>

<style scoped>

form{
    box-sizing: border-box;
    display: inline-block;
}

input{
    display: block;
    background-color: rgb(247, 247, 247);
    margin-bottom: 20px;
    outline: none;
    padding: 10px;
    border-bottom: 1px solid rgb(199, 199, 199);
    border-right: 1px solid rgb(199, 199, 199);
    border-left: none;
    border-top: none;
}

label{
    display: inline-block;
    margin-bottom: 2px;
    text-align: center;
}

button {
    background-color: black;
    width: 50%;
    font-size: 15px;
    color: white;
    margin: 20px 5px 5px 5px;
    padding: 15px;
    border: none;
    cursor: pointer;
    outline: none;
}

</style>