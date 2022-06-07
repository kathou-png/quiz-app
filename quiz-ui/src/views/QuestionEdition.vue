<template>
  <div class="EditQuestion">
    <h1>{{question.title}}</h1>
    <h2>{{question.text}}</h2>
    <img v-if="question.image" :src="question.image" />
     <div v-for="(reponse, index) in question.possibleAnswers" v-bind:key="reponse.position" @click="$emit('answer-selected', index)">
    {{ index  + 1 }} {{ reponse.text }}
  </div>
  </div>
</template>

<script>
export default {
  name: "EditQuestion",
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
@media (min-width: 1024px) {
  .newquizpage {
    min-height: 100vh;
    display: flex;
    align-items: center;
  }
}
</style>
