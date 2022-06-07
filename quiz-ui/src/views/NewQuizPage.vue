<template>
  <div class="newquizpage">
    <h1>Commencer un nouveau quiz</h1>
    <div id="form">
      <p>Saissiez votre nom :</p>
      <input type="text" v-model="username" />
      <button @click="launchNewQuiz" class="glow-on-hover">GO!</button>
    </div>
  </div>
</template>

<script>
import participationStorageService from "@/services/ParticipationStorageService";
export default {
  name: "NewQuizPage",
  data() {
    return {
      username: ''
    };
  },
  methods: {
    launchNewQuiz() {
      participationStorageService.savePlayerName(this.username);
      console.log("Launch new quiz with", participationStorageService.getPlayerName());
      this.$router.push('/questions');
    }
  }
};
</script>

<style>
@media (min-width: 1024px) {
  .newquizpage {
    min-height: 100vh;
    display: flex;
    align-items: center;
  }
}
.glow-on-hover {
  
    width: 10vw;
    height: 5vh;
}
input{
  background-color: white;
  color: var(--background-color);
}
</style>
