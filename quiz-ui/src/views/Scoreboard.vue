<template>
  <div v-for="scoreEntry in registeredScores" v-bind:key="scoreEntry.date">
    {{ scoreEntry.playerName }} - {{ scoreEntry.score }}
  </div>
  
    <button @click="effacerScoreboard" >Effacer scoreboard</button>
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