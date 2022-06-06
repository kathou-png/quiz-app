<template>
  <div class="admin">
    <h1>This is the admin page</h1>
    <div v-show="display">
      <p>Saissiez le mot de passe administrateur :</p>
      <input type="text" v-model="password" />
      <button @click="loginAdmin">OK</button>
      <p>{{message}}</p>
    </div>
    <!--QuestionList v-show = "!display"></QuestionList-->
      <button @click="logoutAdmin">Déconnexion</button>
  </div>
</template>

<script>
import quizApiService from "@/services/quizApiService";
//import QuestionList from "@/views/QuestionList.vue";

export default {
  name: "AdminVue",
  data() {
      return {
        display:true,
        password : "",
        message : ""
      }
  },
  components:{
   // QuestionList
  },

  methods:{
    async loginAdmin(){
      var body = {
        "password": this.password
      }
      var loginPromise = quizApiService.loginAdmin(body);
      var loginAPIResult = await loginPromise;
      try{
        if (loginAPIResult.status == 200){
          this.message = "right password";
          this.display = !this.display;
        }
      }
      catch(error){
          this.message = "wrong password";
      }
    },
    async logoutAdmin(){
    },
  }
};
</script>
<style>
@media (min-width: 1024px) {
  .admin {
    min-height: 100vh;
    display: flex;
    align-items: center;
  }
}
</style>
