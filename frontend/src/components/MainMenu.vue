<template>
  <div>
  <nav>
      <router-link to="/">LOGO</router-link>
      <router-link to="/">Charts</router-link>
      <router-link to="/strokeinput">Stroke-Input</router-link>
  </nav>
  </div>
</template>

<script>
export default {

}
</script>

<style scoped>
nav{
  background-color: rgb(43, 43, 43);
  color: white;
  font-size: 20px;
}
a{
  color: white;
  margin-right: 50px;
  text-decoration: none;
}

div{
  padding: 50px;
  background-color: rgb(43, 43, 43);
  margin-bottom: 80px;
}

</style>