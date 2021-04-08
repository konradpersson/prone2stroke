<template>
<main>
  <div class="hero">
  <div class="pic">
    <img class="pic" src="https://media.istockphoto.com/vectors/three-doctors-are-standing-on-a-blue-background-vector-id1133023384?k=6&m=1133023384&s=612x612&w=0&h=3ssOjJvlSrkfoRA-HiDLk9eO-EqZfULrpGJm1pvcZqA=">
  </div>
  <div class="text">
      <h1>Connecting medical and AI-students</h1>
      <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Ab, impedit. Corporis molestiae tenetur, voluptate sit, voluptas incidunt, iure eaque ut vitae nostrum nobis. Fugit harum soluta, expedita, eius earum quibusdam aliquid rem ipsum eligendi quos perferendis autem nisi ea repellat nam! Soluta asperiores quae hic cum ex odit provident quibusdam vel ea! Vel voluptatibus minus rem.</p>
      <button onclick="window.location.href='/ProneAppDemo';" type="button">Get started</button>
  </div>
  </div>
  </main>
</template>

<script>
export default {

}
</script>

<style scoped>

.hero{
  margin-top: 15vh;
  justify-content: space-between;
  display: flex;
}
main{
  height: auto;
}

div{
  display: inline-block;
}

.pic{
  align-items: flex-start;
}

.text{
  display: inline-block;
  line-height: 1.8;
  color: rgb(168, 168, 168);
  text-align: left;
  margin-top: -80px;
  width: 50vw;
  height: 40vh;
  align-items: flex-end;

}

button{
  background-color: rgb(129, 152, 228);
  margin-top: 20px;
  padding: 20px;
  font-size: 15px;
  color: white;
  outline: none;
  border: none;
  border-radius: 25px;
  cursor: pointer;
  width: 250px;
}

h1{
  font-size: 70px;
  line-height: 0.9;
  color: rgb(58, 58, 58);
  margin-bottom: 30px;
}

@media (max-width: 1100px) {

  .hero{
    display: inline-flex;
    margin-bottom: 10vh;
    margin-top: 10vh;
  }

  .pic{
    width: 400px;
    height: auto;
  }

  .text{
    
    width: 30vw;
    height: 40vh;
  }

  button{
    padding: 10px;
    width: 150px;
  }

  h1{
    margin-top: 70px;
    font-size: 40px;
  }

}
@media (max-width: 1300px) {
  .pic{
    width: 400px;
    height: auto;
  }

  .text{
    
    width: 30vw;
    height: 40vh;
  }

  button{
    padding: 10px;
    width: 150px;
  }

  h1{
    margin-top: 70px;
    font-size: 40px;
  }
}

@media (max-width: 1100px) {

  .hero{
    margin-top: 5vh;
    display: inline-block;
    margin-bottom: 5vh;
  }

  .pic{
    width: 300px;
    height: auto;
  }

  .text{
    width: 60vw;
    height: 40vh;
    margin-left: 3vh; 
  }

  h1{
    margin-top: 90px;
    font-size: 50px;
  }

}

@media (max-width: 800px) {

  .hero{
    margin-top: 5vh;
    display: inline-block;
    margin-bottom: 5vh;
  }

  .pic{
    width: 200px;
    height: auto;
  }

  .text{
    width: 40vw;
    height: 40vh;
    margin-left: 3vh; 
  }

  h1{
    margin-top: 90px;
    font-size: 30px;
  }

}

@media (max-width: 500px) {

  .hero{
    margin-top: 5vh;
    display: inline-block;
    margin-bottom: 5vh;
  }

  .pic{
    width: 110px;
    height: auto;
    padding: 2px;
  }

  .text{
    width: 30vw;
    height: 40vh;
    font-size: 12px;
    margin-left: 0;
    
  }

  button{
    padding: 5px;
    width: 80px;
    font-size: 10px;
  }

  h1{
    margin-top: 70px;
    font-size: 17px;
  }
  
  @media (max-width: 400px) {

  .hero{
    margin-top: 5vh;
    display: inline-block;
    margin-bottom: 5vh;
  }

  .pic{
    width: 60px;
    height: auto;
    padding: 5px;

  }

  .text{
    width: 23vw;
    height: 40vh;
    font-size: 10px;
    
  }

  button{
    padding: 5px;
    width: 80px;
    font-size: 10px;
  }

  h1{
    margin-top: 70px;
    font-size: 12px;
  }
  }

    @media (max-width: 380px) {

  .hero{
    display: none;
  }

  
  }
}
</style>
