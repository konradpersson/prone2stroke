<template>
  <main>
    <h2>Patient Values</h2>
      <h3>Testing probability prediction</h3>
      <form @submit.prevent="predict">
      <label for="gender">Gender:</label><input v-model="gender" type="text" placeholder="gender"/>
      <input v-model="age" type="text" placeholder="age"/>
      <input v-model="work_type" type="text" placeholder="work-type"/>
      <input v-model="residence_type" type="text" placeholder="residence-type"/>
      <input v-model="avg_glucose_level" type="text" placeholder="avg-glucose-level"/>
      <input v-model="bmi" type="text" placeholder="income"/>
      <input v-model="smoking_status" type="text" placeholder="smoking-status"/>
      </form>
      <button>Submit</button>

      <h2>Prediction</h2>
      <p>45% Chance to get a stroke</p>
  </main>
</template>

<script>
export default {

}
</script>

<style scoped>
form{
  margin: 20px;
  display: inline-block;
  width: 100%;
  box-shadow: 20px;
}

input{
  width: 50%;
  height: 50px;
  margin: auto;
  border-bottom: 2px solid rgb(199, 199, 199);
  border-right: 2px solid rgb(199, 199, 199);
  border-left: none;
  border-top: none;
  background-color: white;
  margin: 5px;
  float: left;
  font-size: 16px;
  padding-left: 20px;
  outline: none;
}

button{
  background-color: black;
  width: 10%;
  font-size: 20px;
  color: white;
  margin: 20px 5px 5px 5px;
  padding: 20px;
  border: none;
  cursor: pointer;
  outline: none;
}

</style>