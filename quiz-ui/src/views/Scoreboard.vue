<template>
  <div class="ScoreBoard">
    <h4> Scoreboard:</h4>
    <div v-for="scoreEntry in registeredScores" v-bind:key="scoreEntry.date">
      {{ scoreEntry.playerName }} - {{ scoreEntry.score }}
    </div>
  </div>
    <button class="button" @click="effacerScoreboard">Effacer scoreboard</button>
</template>

<script>
import quizApiService from "@/services/QuizApiService";

export default {
  // eslint-disable-next-line vue/multi-word-component-names
  name: "Scoreboard",
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
    console.log("Composant scoreboard 'created'");
  },
  methods:{
      async effacerScoreboard(){
        var token =  window.localStorage.getItem("token", );
        var scoreboardPromise = quizApiService.deleteParticipation(token);
        var scoreboardAPIResult = await scoreboardPromise;
        this.registeredScores = scoreboardAPIResult.data;
        console.log(scoreboardAPIResult);
      }
  }
};
</script>

<style>
@import '@/assets/theme.css';
.button {
    display: flex;
    padding: 5%;
    margin: 1%;
    margin-top : 20px;
    margin-bottom : 40px;
    border-radius: 15px;
    background-color: rgb(132, 67, 67);
    color: white;
  }
.ScoreBoard{
  display: flex;
  padding: 5%;
  width: 75%;
  border-radius: 15px;
  background-color: rgba(60, 61, 82, 0.384);
  color: white;
}
</style>