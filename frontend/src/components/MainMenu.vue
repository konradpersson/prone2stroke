<template>

 <div class="navbar">
   <div class="logo">
    <img class="icon" src="src/assets/images.jfif" alt="Icon">
    <p class="strokestats">StrokeStats</p>
   </div>
    <div class="dropdown">
      <button class="dropbtn">Demos 
      </button>
      <div class="dropdown-content">
        <a href="/ProneAppDemo">StrokeApp</a>
        <a href="#">Link 2</a>
        <a href="#">Link 3</a>
    </div>
  </div>
  <a href="#"> Blog </a>
  <router-link to="/">Home</router-link>
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
  margin: 0px;
  justify-content: space-around;
  align-items: center;
  display: flex;
}

.logo{
  display: flex;
  justify-content: flex-start;
}
.icon {
  padding: 15px;
  width: 35px;
  height: 35px;
}
.navbar .p {
  color: rgb(41, 39, 40);
  text-decoration: none;
}
.search {
  height: 30px;
  border-radius: 7px;
  border-color: rgba(168, 166, 166, 0.521);
  border-style: solid;
  border-width: 1px; 
}
  


.navbar a{
  color: gray;
  text-decoration: none;
  padding: 1px;
}



.signup {
  background: rgb(129, 152, 228);
  border-radius: 7px;
  height: 30px;
  color: white;
  border: none;
  padding: 10px 25px 25px 25px;
  min-width: 100px;
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
  min-width: 90px;
}
.navbar a:hover, .dropdown:hover .dropbtn {
  color: rgb(139, 164, 233);
}

.navbar .dropdown:hover .dropbtn {
  color: rgb(139, 164, 233);
  background-color:  rgba(183, 191, 196, 0.096);
}

.dropdown-content {
  font-size: 13px;
  display: none;
  position: absolute;
  background-color: rgba(183, 191, 196, 0.623);
  min-width: 95px;
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
  background-color: rgba(152, 173, 190, 0.404);
}

.dropdown:hover .dropdown-content {
  display: block;
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

    .strokestats {
      display: none;
  }

  .search {
  height: 20px;
  border-radius: 7px;
  border-color: rgba(168, 166, 166, 0.521);
  border-style: solid;
  border-width: 1px;
  font-size: 12px; 
}


.signup {
  
  background: rgb(129, 152, 228);
  border-radius: 7px;
  height: 10px;
  color: white;
  border: none;
  padding: 5px 15px 18px 15px;
  width: 15vw;
} 
.dropdown .dropbtn { 
  font-size: 15px;  
}

.dropdown-content {
  min-width: 80px;
}
  
}

@media (max-width: 600px) {
  .search {
  height: 20px;
  border-radius: 7px;
  border-color: rgba(168, 166, 166, 0.521);
  border-style: solid;
  border-width: 1px;
  width: 25vw;
  font-size: 12px; 
}

}

</style> 
