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
  background-color: #081b3b;
  color: #415272; 
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
  background-color: #081b3b;
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
  background-color: #162f5e;
}
</style>
