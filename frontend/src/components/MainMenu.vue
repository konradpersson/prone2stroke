<template>

 <div class="navbar">
    <img class="icon" src="src/assets/images.jfif" alt="Icon">
    <p>StrokeStats</p>
    <div class="dropdown">
      <button class="dropbtn">Demos<i class="fa fa-caret-down"></i>
      </button>
      <div class="dropdown-content">
        <a href="#">Link 1</a>
        <a href="#">Link 2</a>
        <a href="#">Link 3</a>
    </div>
  </div>
  <a href="#"> Blog </a>
  <router-link to="/">About</router-link>
  <input class="search" type="text" placeholder="Search...">
  <router-link to="/"><button  class="signup"> Sign Up </button></router-link>
  </div>

</template>

<script>
export default {

}
</script>

<style scoped>

.navbar{
  font-size: 20px;
  overflow: hidden;
  height: 90px;
  width: 100%;
  margin: 0px;
  position: sticky;
  justify-content: space-evenly;
  display: inline-flex;
}

.icon {
  float: left;
  padding: 30px 16px;
  width: 35px;
  height: 35px;
}
.navbar .p {
  float: left;
  color: rgb(41, 39, 40);
  padding: 30px, 16px;
  text-align: center;
  text-decoration: none;
}
.search {
  height: 30px;
  margin-top: 30px;
  border-radius: 7px;
  border-color: rgba(168, 166, 166, 0.521);
  border-style: solid;
  border-width: 1px;
  
}
  


.navbar a{
  float: left;
  color: gray;
  text-decoration: none;
  padding: 34px 16px;
}

.signup {
  background: rgb(129, 152, 228);
  border-radius: 7px;
  height: 30px;
  color: white;
  border: none;
  padding: 15px;
} 

.signup:hover {
  color: rgb(139, 164, 233);
}

.dropdown { 
  overflow: hidden; 
}

.dropdown .dropbtn {
  font-size: 20px;  
  border: none;
  outline: none;
  color: gray;
  padding: 34px 16px;
  background-color: inherit;
  margin: 0;
  font-family: inherit;
}
.navbar a:hover, .dropdown:hover .dropbtn {
  color: rgb(139, 164, 233);
}

.dropdown-content {
  display: none;
  position: absolute;
  background-color: rgba(128, 128, 128, 0.5);
  min-width: 122px;
  box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
  z-index: 1;
}

.dropdown-content a {
  float: none;
  color: gray;
  padding: 12px 16px;
  text-decoration: none;
  display: block;
  text-align: left;
}

.dropdown-content a:hover {
  background-color: #ddd;
}

.dropdown:hover .dropdown-content {
  display: block;
}

</style> 
