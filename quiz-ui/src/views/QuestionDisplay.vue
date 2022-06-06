<template>
  <div class="QuestionDisplay">
    <h1>{{question.texte}}</h1>
    <img v-if="question.image" :src="question.image" />
    <a @click="$emit('answer-selected', 1)">La réponse 1</a>
    <a @click="$emit('answer-selected', 2)">La réponse 2</a>
    <a @click="$emit('answer-selected', 3)">La réponse 3</a>
    <a @click="$emit('answer-selected', 4)">La réponse 4</a>
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
  emits: ["answer-selected"]
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
