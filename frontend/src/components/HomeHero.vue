<template>
<main>
  <div>
  <div class="pic">
    <img src="https://media.istockphoto.com/vectors/three-doctors-are-standing-on-a-blue-background-vector-id1133023384?k=6&m=1133023384&s=612x612&w=0&h=3ssOjJvlSrkfoRA-HiDLk9eO-EqZfULrpGJm1pvcZqA=">
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
main{
  margin-top: 60px;
  margin-bottom: 60px;
  margin-left: 120px;
  margin-right: 120px;
}

div{
  display: inline-block;
}

.pic{
  float:left;
  margin-top: -40px;

}

.text{
  display: inline-block;
  line-height: 1.8;
  color: rgb(168, 168, 168);
  margin-left: 60px;
  width: 50%;
  text-align: left;
  margin-top: -80px;
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
  width: 300px;
}

h1{
  font-size: 100px;
  line-height: 0.9;
  color: rgb(58, 58, 58);
  margin-bottom: 30px;
}


</style>