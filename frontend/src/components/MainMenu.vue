<template>

 <nav class="navbar">
    <div class="logo">
    <a href="/"><img class="icon" src="src/assets/p2s-logo.png" alt="Icon"></a>
   </div>
        <a href="/ProneAppDemo">StrokeApp</a>
  </nav>

</template>

<script>
export default {
}
</script>

<style scoped>
.navbar{
  font-size: 20px;
  margin: 0px;
  justify-content: space-around;
  align-items: center;
  display: flex;
}
.logo{
  float: left;
}
.icon {
  padding: 15px;
  background-size: cover;
  width: 30%;
  margin-top: 20px;
}

  
.navbar a{
  color: gray;
  text-decoration: none;
  padding: 0px 5px;
}

.navbar a:hover{
  color: rgb(139, 164, 233);
}


@media (max-width: 1000px) {
  .navbar {
      font-size: 15px;
      flex-direction: row;
      align-items: center;
      flex-wrap: wrap;
      display: flex;
      justify-content: space-between;
  }
}

</style>