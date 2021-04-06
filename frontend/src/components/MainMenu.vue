<template>
<main>
 <nav class="navbar">
  <div>
    <a href="/"><img class="icon" src="src/assets/p2s-logo.png" alt="Icon"></a>
    <a class="menu" href="/ProneAppDemo">StrokeApp</a>
  </div>
  </nav>
</main>
</template>

<script>
export default {

}
</script>

<style scoped>

a{
  margin-left: 1%;
}

.menu{
  margin-left: 59%;
}
div{
  display: flex;
  justify-content: flex-start;
  align-items: left;
  width: 100%;


}

.icon {
  background-size: cover;
  width: 30%;
  margin-top: -35px;
}

.navbar a{
  color: gray;
  text-decoration: none;
  padding: 0px 5px;
  margin-top: 50px;
  font-size: 20px;
}

.navbar a:hover {
  color: rgb(139, 164, 233);
}

@media (max-width: 1000px) {
.navbar {
  font-size: 15px;
  flex-direction: row;
  align-items: right;
  flex-wrap: wrap;
  display: flex;
  justify-content: space-between;
}
  
}


</style> 
