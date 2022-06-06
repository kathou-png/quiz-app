<template>
  <div class="questions">
    <!--h1>This is the questions page</h1-->
  <h1>Question {{ currentQuestionPosition }} / {{ totalNumberOfQuestion }}</h1>
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
      currentQuestion:{
        questionTitle:"",
        questionText:"",
        possibleAnswers:[]
      },
      currentQuestionPosition: 1,
      totalNumberofQuestion:0
    }
  },
  components:{
    QuestionDisplay
  },
  async created(){
    var quizInfoPromise = quizApiService.getQuizInfo();
    var quizInfoAPIResult = await quizInfoPromise;
    var quizInfo = quizInfoAPIResult.data.size;
    this.totalNumberofQuestion= quizInfo;
    console.log("total questions:", this.totalNumberofQuestion);
    this.loadQuestionByPosition(this.currentPosition);

    var questionInfoPromise = quizApiService.getQuestion();
      var questionInfoAPIResult = await questionInfoPromise;
      console.log("api rsult");
      console.log(questionInfoAPIResult)
  },
  methods: {
    async loadQuestionByPosition(currentPosition){
      var questionInfoPromise = quizApiService.getQuestion();
      var questionInfoAPIResult = await questionInfoPromise;
      console.log("api rsult");
      console.log(questionInfoAPIResult)
     /*
      var questionInfo = questionInfoAPIResult.data;
      this.currentQuestion.questionTitle = questionInfo.title;
      this.currentQuestion.questionText = questionInfo.text;
      this.currentQuestion.possibleAnswers = questionInfo.possibleAnswers;*/
      console.log("current question");
      console.log(this.currentQuestion)

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
