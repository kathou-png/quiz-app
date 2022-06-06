<template>
  <div class = "QuestionList" v-show="!display">
     <div v-for="(question, index) in questionList" v-bind:key="question.id" @click="showQuestionDetails">
      id : {{question.id}}
      title : {{ question.title }}
      text : {{question.text}}
       <button @click="Detail">Details</button>
        <button @click="Editer">Editer</button>
  </div>
  </div>
</template>

<script>
import quizApiService from "@/services/quizApiService";
export default {
  name: "QuestionList",
  data() {
      return {
        questionList:[],
        totalNumberOfQuestion : 0}
  },
  async created(){
      this.questionList = this.getQuestions();
  },
  methods:{
    async getQuestions(){
    console.log("getting questions");
    var quizInfoPromise = quizApiService.getQuizInfo();
    var quizInfoAPIResult = await quizInfoPromise;
    var quizInfo = quizInfoAPIResult.data.size;
    this.totalNumberOfQuestion= quizInfo;
    for (var i = 0; i < this.totalNumberOfQuestion; i++){
      this.loadQuestionByPosition(i+1);
    }
    console.log("question list:");
    console.log(this.questionList);
    },
    
    async loadQuestionByPosition(currentPosition){
      var questionInfoPromise = quizApiService.getQuestion(currentPosition);
      var questionInfoAPIResult = await questionInfoPromise;
      var questionInfo = questionInfoAPIResult.data;
      this.questionList[currentPosition-1] = questionInfo;
    },
    showQuestionDetails(){

    }
  }
}
</script>

<style>
@media (min-width: 1024px) {
  .QuestionList {
    min-height: 100vh;
    display: flex;
    align-items: center;
  }
}
</style>
