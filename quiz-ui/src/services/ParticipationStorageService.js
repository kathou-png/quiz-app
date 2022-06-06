export default {
  clear() {
    // todo : implement
  },
  savePlayerName(playerName) {
    window.localStorage.setItem("playerName", playerName);
  },
  getPlayerName() {
    return window.localStorage.getItem("playerName");
  },
  saveParticipationScore(participationScore) {
    window.localStorage.setItem("score", participationScore);
    
  },
  getParticipationScore() {
    return window.localStorage.getItem("score");
  }
};