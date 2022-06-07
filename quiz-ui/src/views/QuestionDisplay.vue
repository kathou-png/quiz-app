<template>
  <div class="QuestionDisplay">
    <h1>{{question.title}}</h1>
    <h2>{{question.text}}</h2>
    <img v-if="question.image" :src="question.image" />
    <div class="container">
     <div class="reponse" v-for="(reponse, index) in question.possibleAnswers" v-bind:key="reponse.position" @click="$emit('answer-selected', index)">
     {{ reponse.text }} 
    </div>
  </div>
  </div>
</template>

<script>
export default {
  name: "QuestionDisplay",
  data() {
      return {}
  },
  props: {
    question: {
        type: Object
    }
  },
  async created(){
  },
};
</script>

<style>
@import '@/assets/theme.css';
@media (min-width: 1024px) {
  .newquizpage {
    min-height: 100vh;
    display: flex;
    align-items: center;
  }
}
h1{
  padding : 0%;
  font-size: 100%;
  font-style: italic;
}
h2{
  color:white;
}
.reponse{
  font-size:80%;
  justify-content: center;
}
</style>
