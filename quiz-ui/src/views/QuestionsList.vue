<template>
<div class="AdminConsole" v-show="display">
    <h3>Admin console</h3>
    <Scoreboard  ></Scoreboard>
    <router-link to="/question-creation">Créer une question</router-link>
</div>
<div class="QuestionList" v-show="display">
    <h3>Question List:</h3>
        <div class="question" v-for="(question, index) in  questionList" v-bind:key="question.position" @click="showQuestionDetails(index)">
        position : {{question.position}} <br>
        title : {{ question.title }} <br>
        text : {{question.text}}
        </div>
</div>
<div class="QuestionDetail" v-show="!display">
    <QuestionDisplay :question="currentQuestion" />
    <button @click="editQuestion(currentQuestion)">Editer</button>
    <button @click="deleteQuestion(currentQuestion)">Supprimer</button>
    <button @click="display='!display'">Retour</button>
</div>
</template>

<script>
import quizApiService from "@/services/QuizApiService";
import QuestionDisplay from "@/views/QuestionDisplay.vue";
import Scoreboard from "@/views/Scoreboard.vue";

export default {
  name: "QuestionList",
  data() {
      return {
        display : true,
        questionList:[],
        totalNumberOfQuestion : 0,
        currentQuestion:{
            questionTitle:"",
            questionText:"",
            possibleAnswers:[]
            }
        }
  },
  components:{
    QuestionDisplay,
    Scoreboard
  },
  async created(){
      this.display = true;
      this.displayscoreboard = false;
      this.getQuestions();
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
    async showQuestionDetails(index){
        console.log("index " + index);
        this.display = !this.display;
        var questionInfoPromise = quizApiService.getQuestion(parseInt(index)+1);
        var questionInfoAPIResult = await questionInfoPromise;
        var questionInfo = questionInfoAPIResult.data;
        this.currentQuestion = questionInfo;
    },
    async editQuestion(){
        this.$router.push('/edit-question');
    },
    async deleteQuestion(currentQuestion){
        try{
            const token = window.localStorage.getItem("token");
            var questionDeletePromise = quizApiService.deleteQuestion(currentQuestion.position, token);
            var questionDeleteAPIResult = await questionDeletePromise;
            console.log(questionDeleteAPIResult);
            this.questionList = this.getQuestions();
            this.display = !this.display;
        }
        catch(error){
            console.log(error);
        }

    },
    async deleteScoreboard(){
        const token = window.localStorage.getItem("token");
        var participationDeletePromise = quizApiService.deleteParticipation(token);
        var participationDeleteAPIResult = await participationDeletePromise;
        console.log(participationDeleteAPIResult);
    }
  }
}
</script>

<style>
@import '@/assets/theme.css';
@media (min-width: 1024px) {
  .QuestionList {
    min-height: 100vh;
    display: block;
    align-items: center;
  }
  .AdminConsole{
    height: 750px;
  }
}
 .question:hover{
      background-color: bisque;
      color: black;
  }
</style>
