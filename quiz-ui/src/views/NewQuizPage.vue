<template>
  <div class="newquizpage">
    <h1>This is the new quiz page</h1>
    <div id="form">
      <p>Saissiez votre nom :</p>
      <input type="text" placeholder="Username">
      <button>GO!</button>
    </div>
  </div>
</template>

<style>
@media (min-width: 1024px) {
  .newquizpage {
    min-height: 100vh;
    display: flex;
    align-items: center;
  }
}
</style>
