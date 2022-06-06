<template>
  <div class="questions">
    <!--h1>This is the questions page</h1-->
  <h1>Question {{ currentQuestionPosition }} / {{ totalNumberOfQuestion }}</h1>
  <br>
  <QuestionDisplay :question="currentQuestion" @click-on-answer="answerClickedHandler" />
  </div>
</template>

<script>
import quizApiService from "@/services/quizApiService";
import QuestionDisplay from "@/views/QuestionDisplay.vue";

export default {
  name: "QuestionManager",
  data() {
    return {
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
    console.log("total questions:", this.totalNumberofQuestion);
    console.log("current position" + this.currentQuestionPosition);
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
    async answerClickedHandler(){

    },
    async endQuizz(){

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
