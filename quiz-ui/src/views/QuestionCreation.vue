<template>
<div>
  <h1>Créer une question</h1>
  <div >
    <p>Titre</p>
    <input type="text" v-model="title" required />
    
    <p>Texte</p>
    <input type="text" v-model="text" required />
    
    <p>Image</p>
    <ImageUpload @file-change="imageFileChangedHandler"/>


    <p>Réponses (cocher la bonne réponse)</p>
    <div>
    <input type="text" v-model="possibleAnswer[0]" placeholder="Réponse 1" />
    <input type="radio" value="0" name="reponse" Checked/>
    </div>
    <div>
    <input type="text" v-model="possibleAnswer[1]" placeholder="Réponse 2" />
    <input type="radio" value="1" name="reponse"/>
    </div>
    <div>
    <input  type="text" v-model="possibleAnswer[2]" placeholder="Réponse 3" />
    <input type="radio" value="2"  name="reponse"/>
    </div>
    <div>
    <input  type="text" v-model="possibleAnswer[3]" placeholder="Réponse 4" />
    <input type="radio" value="3" name="reponse"/>
    </div>

  </div>
  <button @click="backtoQuestionList" class="glow-on-hover">Retour</button>
  <button @click="createQuestion" class="glow-on-hover">Créer</button>
</div>
</template>

<script>
import quizApiService from "@/services/QuizApiService";
import ImageUpload from "@/views/ImageUpload.vue";
export default {
  name: "QuestionCreation",
  data() {
    return {
      title:"",
      text:"",
      image:"",
      possibleAnswer : [],
      selectedAnswer : 0,
      totalNumberOfQuestion : 0
    }
  },
  components:{
      ImageUpload
  },
  async created() {
    var quizInfoPromise = quizApiService.getQuizInfo();
    var quizInfoAPIResult = await quizInfoPromise;
    var quizInfo = quizInfoAPIResult.data.size;
    this.totalNumberOfQuestion= quizInfo;
  },
  methods:{
    imageFileChangedHandler(b64String) {
    this.image = b64String;
    },
    getNumberOfQuestion(){

    },
    async createQuestion(){
        var reponse = document.querySelector('input[name="reponse"]:checked').value;
        console.log(reponse);
        var possibleAnswers = [];
        for (var i = 0; i < 4; i++){
            var isCorrect = true;
            if (i != parseInt(reponse))
                isCorrect = false;
            else
             isCorrect = true;
            var object = {
                "text" : this.possibleAnswer[i],
                "isCorrect" : isCorrect
            }
            possibleAnswers.push(object);
        }
        var body = {
            "text": this.text,
            "title": this.title,
            "image": this.image,
            "position": this.totalNumberOfQuestion + 1,
            "possibleAnswers": possibleAnswers
        }
        console.log(body);
        const token = window.localStorage.getItem("token");
        var quizInfoPromise = quizApiService.createQuestion(token, body);
        var quizInfoAPIResult = await quizInfoPromise;
        console.log(quizInfoAPIResult);
        this.$router.push('/admin');
    },
    backtoQuestionList(){
        this.$router.push('/admin');
    }
  }
}; 
</script>
<style>
input{
    color: black}</style>