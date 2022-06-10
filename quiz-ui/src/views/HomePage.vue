<template>
<div>
  <h1>Bienvenue</h1>
 <img
    src="../assets/logo.svg"
    alt="logoquizz"
    height="100%"
    width="100%" />
    <Scoreboard></Scoreboard>
  <router-link to="/start-new-quiz-page" class="glow-on-hover">Démarrer le quiz !</router-link>
</div>
</template>

<script>
import quizApiService from "@/services/QuizApiService";
import Scoreboard from "@/views/Scoreboard.vue";

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
    },
    components: { Scoreboard }
};
</script>
<style>

h1{
  padding:0%
}
a{
  text-align: center;
}
</style>