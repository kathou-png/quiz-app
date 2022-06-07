<template>
<div>
  <h1>Home page</h1>
 <img
    src="../assets/logo.svg"
    alt="logoquizz"
    height="100%"
    width="100%" />
  <router-link to="/start-new-quiz-page">Démarrer le quiz !</router-link>
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
div{
  display: flex;
  flex-direction: column;
  align-items : center;
}
img{
  width : 50vw;
  height: 50vh;
}
router-link{
  background-color: aqua;
}
</style>