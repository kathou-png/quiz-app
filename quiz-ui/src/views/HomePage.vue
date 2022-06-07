<template>
<div>
  <h1>Bienvenue</h1>
 <img
    src="../assets/logo.svg"
    alt="logoquizz"
    height="100%"
    width="100%" />
  <router-link to="/start-new-quiz-page" class="glow-on-hover">Démarrer le quiz !</router-link>
</div>
</template>

<script>
import quizApiService from "@/services/QuizApiService";

export default {
  name: "HomePage",
  data() {
    return {
      registeredScores: []
    };
  },
  async created() {
    var quizInfoPromise = quizApiService.getQuizInfo();
    var quizInfoAPIResult = await quizInfoPromise;
    var quizInfo = quizInfoAPIResult.data.scores;
    this.registeredScores = quizInfo;
    console.log("Composant Home page 'created'");
    console.log("Registered Scores :", this.registeredScores);
  }
};
</script>
<style>

h1{
  padding:0%
}
a{
  padding: 2%;
  padding: 25px 0;
  text-align: center;
}
</style>