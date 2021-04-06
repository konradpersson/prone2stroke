<template>
<div>
    <h3>Testing probability prediction</h3>
    <form @submit.prevent="predict">

        <p>Gender:</p>

        <div>
        <input v-model="gender" type="radio" id="male" name="gender" value="1"
                checked>
        <label for="huey">Male</label>
        </div>

        <div>
        <input v-model="gender" type="radio" id="female" name="gender" value="2">
        <label for="dewey">Female</label>
        </div>

        <div>
        <input v-model="gender" type="radio" id="other" name="gender" value="-1">
        <label for="louie">Other</label>
        </div>


        <label for="age">Age</label>
        <input v-model="age" type="text" placeholder="age"/>


        <p>Work type:</p>

        <div>
        <input v-model="work_type" type="radio" id="private" name="work_type" value="0"
                checked>
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
</div>
</template>

<script>
export default {
    data() {
        return {
            gender: 1,
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
    width: 200px;
    padding: 10px;
    border-bottom: 1px solid rgb(199, 199, 199);
    border-right: 1px solid rgb(199, 199, 199);
    border-left: none;
    border-top: none;
}

label{
    display: inline-block;
    margin-bottom: 4px;
    text-align: center;
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