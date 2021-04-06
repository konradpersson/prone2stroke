<template>
<div>
    <h3>Testing probability prediction</h3>
    <form @submit.prevent="predict">

        <p>Gender</p>

        <div class="form--section">
        <div>
        <input v-model="gender" type="radio" id="male" name="gender" value="1">
        <label for="huey">Male</label>
        </div>

        <div>
        <input v-model="gender" type="radio" id="female" name="gender" value="2">
        <label for="dewey">Female</label>
        </div>
        </div>

        <label for="age" class="section-heading">Age</label>

        <div class="form--section">
        <input v-model="age" type="text" placeholder="age"/>
        </div>


        <p>Work type</p>

        <div class="form--section">
            <div>
                <input v-model="work_type" type="radio" id="private" name="work_type" value="0">
                <label for="private">Private</label>
            </div>

            <div>
                <input v-model="work_type" type="radio" id="self-employed" name="work_type" value="1">
                <label for="self-employed">Self employed</label>
            </div>

            <div>
                <input v-model="work_type" type="radio" id="gov-job" name="work_type" value="2">
                <label for="gov-job">Government Job</label>
            </div>

            <div>
                <input v-model="work_type" type="radio" id="children" name="work_type" value="-1">
                <label for="children">Children</label>
            </div>

            <div>
                <input v-model="work_type" type="radio" id="never-worked" name="work_type" value="-2">
                <label for="never-worked">Never worked</label>
            </div>
        </div>
        
        <p>Residence type</p>

        <div class="form--section">
            <div>
                <input v-model="residence_type" type="radio" id="rural" name="residence_type" value="0">
                <label for="rural">Rural</label>
            </div>

            <div>
                <input v-model="residence_type" type="radio" id="urban" name="residence_type" value="1">
                <label for="urban">Urban</label>
            </div>
        </div>


        <label for="avg_glucose_level" class="section-heading">AVG glucose level</label>
            <div class="form--section">
                <input v-model="avg_glucose_level" type="text" placeholder="avg-glucose-level"/>
            </div>

        <label for="bmi" class="section-heading">BMI</label>
        <div class="form--section">
            <input v-model="bmi" type="text" placeholder="bmi"/>
        </div>


        <p>Smoking status</p>
        
        <div class="form--section">
        <div>
            <input v-model="smoking_status" type="radio" id="smokes" name="smoking_status" value="2">
            <label for="smokes">Smokes</label>
        </div>

        <div>
            <input v-model="smoking_status" type="radio" id="formerly-smoked" name="smoking_status" value="1">
            <label for="formerly-smoked">Formerly Smoked</label>
        </div>

        <div>
            <input v-model="smoking_status" type="radio" id="never-smoked" name="smoking_status" value="0">
            <label for="never-smoked">Never Smoked</label>
        </div>
        </div>


        <button>Submit</button>
    </form>
</div>
</template>

<script>
export default {
    data() {
        return {
            gender: 1,
            age: 55,
            work_type: 0,
            residence_type: 1,
            avg_glucose_level: 140,
            bmi: 22,
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

form {
    box-sizing: border-box;
    display: inline-block;
}

form p, label.section-heading {
    display: block;
    font-weight: bold;
    margin-top: 3em;
    margin-bottom: 0.5em;
    font-size: 14px;
}

.form--section {
    border-radius: 7px;
    background-color: white;
    box-shadow:
        0  5px 10px rgba(154,160,185,0.05),
        0 15px 40px rgba(166,173,201,0.2);
    padding: 20px;
}

input[type=text] {
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

button {
    background-color: black;
    display: inline;
    width: 200px;
    font-size: 15px;
    color: white;
    margin: 20px 5px 5px 5px;
    padding: 15px;
    border: none;
    cursor: pointer;
    outline: none;
}

</style>