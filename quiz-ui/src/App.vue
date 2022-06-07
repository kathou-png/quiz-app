<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>

<template>
  <header>

    <div class="wrapper">

      <nav>
        <RouterLink to="/">Home</RouterLink>
        <RouterLink to="/admin">Admin</RouterLink>
      </nav>
    </div>
  </header>

  <RouterView />
</template>

<style>
@import '@/assets/base.css';

* {
    margin: 0;
    padding: 0;
}
#app{
  background-color: black;
  color: antiquewhite; 
  max-width: 1280px;
  height: 100vh;
  margin: 0 auto;
  padding: 2rem;
  font-weight: normal;
}
h1{
  padding-top: 10%;
  font-family: Arial, sans-serif;
}
nav{
  max-width: 1280px;
  background-color: beige;
  width: 80vw;
  height: 10vh;
  display: flex;
  flex-direction: row;
  justify-content: space-evenly;
  align-items: center;
}
nav a{
  width: 100%;
  height: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
}
nav a:hover{
  background-color: blanchedalmond;
}
</style>
