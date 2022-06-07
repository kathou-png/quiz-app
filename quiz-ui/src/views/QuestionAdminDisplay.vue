<template>
  <div class="admin">
    <h1>Page administrateur</h1>
    <div v-show="display">
      <p>Saissiez le mot de passe :</p>
      <input type="text" v-model="password" />
      <button @click="loginAdmin">OK</button>
      <p>{{message}}</p>
    </div>
      <button @click="logoutAdmin">Déconnexion</button>
  </div>
</template>

<script>
import quizApiService from "@/services/QuizApiService";

export default {
  name: "AdminVue",
  data() {
      return {
        display:true,
        password : "",
        message : ""
      }
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
          console.log(loginAPIResult);
          this.display = !this.display;
          //saving token
          window.localStorage.setItem("token", loginAPIResult.data.token);
          this.$router.push('/question-list');
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
@media (min-width: 1024px)  {
  .admin {
    min-height: 100vh;
    display: flex;
    align-items: center;
  }
}
</style>
