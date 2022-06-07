<template>
  <div class="admin">
    <h1>Page administrateur</h1>
    <div v-show="display">
      <p>Saissiez le mot de passe :</p>
      <input type="text" v-model="password" style="color:black"/>
      <button class="OkButton" @click="loginAdmin">Valider le mot de passe</button>
      <p>{{message}}</p>
    </div>
      <button class="UnlogButton" @click="logoutAdmin">Déconnexion</button>
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
          this.message = "mot de passe incorrect";
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
.OkButton{
    display: flex;
    padding: 5%;
    margin: auto;
    margin-top : 40px;
    margin-bottom: 10px;
    border-radius: 15px;
    width: 70%;
    vertical-align: middle;
    background-color: rgb(67, 132, 78);
    color: white;
  }
.UnlogButton{
    display: flex;
    padding: 5%;
    margin: 1%;
    margin-top : 20px;
    border-radius: 15px;
    width: 61%;
    text-align: center;
    background-color: rgb(132, 67, 67);
    color: white;
  }
  h1{
    margin-bottom: 40px;
  }
  p{
    color: white;
  }
</style>
