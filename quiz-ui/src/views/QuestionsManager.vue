<template>
  <div class="questions">
    <!--h1>This is the questions page</h1-->
  <h1>Question {{ currentQuestionPosition }} / {{ totalNumberOfQuestion }}</h1>
  <br>
  <QuestionDisplay v-show=display :question="currentQuestion" @answer-selected="answerClickedHandler" />
  <div v-show="!display"> congrats you ended the game. Scoreboard :
    <div v-for="scoreEntry in registeredScores" v-bind:key="scoreEntry.date">
    {{ scoreEntry.playerName }} - {{ scoreEntry.score }}
  </div></div>
  </div>
</template>

<script>
import quizApiService from "@/services/quizApiService";
import QuestionDisplay from "@/views/QuestionDisplay.vue";
import participationStorageService from "@/services/ParticipationStorageService";

export default {
  name: "QuestionManager",
  data() {
    return {
      player:{
        playerName:"",
        answers :[]
      },
      score: 0,
      display: true,
      registeredScores: [],
      currentQuestionPosition: 1,
      totalNumberOfQuestion:0,
      currentQuestion:{
        questionTitle:"",
        questionText:"",
        possibleAnswers:[]
      }
    }
  },
  components:{
    QuestionDisplay
  },
  async created(){
    var quizInfoPromise = quizApiService.getQuizInfo();
    var quizInfoAPIResult = await quizInfoPromise;
    var quizInfo = quizInfoAPIResult.data.size;
    this.totalNumberOfQuestion= quizInfo;
    this.player.playerName = participationStorageService.getPlayerName();
    console.log("total questions:", this.totalNumberofQuestion);
    console.log("current position" + this.currentQuestionPosition);
    console.log("player : " + this.player.playerName);
    this.loadQuestionByPosition(this.currentQuestionPosition);
  },
  methods: {
    async loadQuestionByPosition(currentPosition){
      var questionInfoPromise = quizApiService.getQuestion(currentPosition);
      var questionInfoAPIResult = await questionInfoPromise;
      var questionInfo = questionInfoAPIResult.data;
      this.currentQuestion = questionInfo;
      console.log(this.currentQuestion);
    },
    async answerClickedHandler(selectedAnswerPosition){
      console.log("answer Clicked Handler");
      this.player.answers[this.currentQuestionPosition-1] = selectedAnswerPosition;
      
      var rightAnswer = this.getRightAnswer();
      if (this.currentQuestionPosition == this.totalNumberOfQuestion){
        this.endQuizz();
      }
      else{
        if (rightAnswer == selectedAnswerPosition){
          this.score++;
        }
        this.currentQuestionPosition++;
        this.loadQuestionByPosition(this.currentQuestionPosition);
      }

    },
    async endQuizz(){
      console.log(this.player);
      this.display = false;
      var postPlayer = quizApiService.postScore(this.player);
      var postPlayerAPIResult = await postPlayer;
      console.log("score " + this.score);
      participationStorageService.saveParticipationScore(this.score);

      console.log("postscoreresult and score");
      console.log(postPlayerAPIResult);
      console.log(participationStorageService.getParticipationScore());
    
     var quizInfoPromise = quizApiService.getQuizInfo();
     var quizInfoAPIResult = await quizInfoPromise;
     var quizInfo = quizInfoAPIResult.data.scores;
     this.registeredScores = quizInfo;



    },
    getRightAnswer: function (){
      var i = 0;
      for (const answer of this.currentQuestion.possibleAnswers){
        console.log(answer);
        if (answer.isCorrect == true) return i;
        else i++;
      }
    }
  }
};
</script>


<style>
@media (min-width: 1024px) {
  .questions {
    min-height: 100vh;
    display: flex;
    align-items: center;
  }
}
</style>
