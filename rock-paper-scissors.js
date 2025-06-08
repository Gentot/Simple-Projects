let score = JSON.parse(localStorage.getItem("score")) || {
  wins: 0,
  losses: 0,
  ties: 0,
};

document.querySelector(
  ".js-scores"
).innerHTML = `Wins: ${score.wins}, Losses: ${score.losses}, Ties: ${score.ties}`;

document.body.addEventListener("keydown", (event) => {
  if (event.key === "r") {
    playgame("rock");
  } else if (event.key === "p") {
    playgame("paper");
  } else if (event.key === "s") {
    playgame("scissors");
  }
});

let result = "";
let computer = "";
let isAutoPlaying = false;
let intervalid;

function autoplay() {
  if (!isAutoPlaying) {
    intervalid = setInterval(() => {
      const playerMove = computerrandom();
      playgame(playerMove);
    }, 1000);
    isAutoPlaying = true;
  } else {
    clearInterval(intervalid);
    isAutoPlaying = false;
  }
}

document.querySelector(".js-rock-button").addEventListener("click", () => {
  playgame("rock");
});

document.querySelector(".js-paper-button").addEventListener("click", () => {
  playgame("paper");
});
document.querySelector(".js-scissors-button").addEventListener("click", () => {
  playgame("scissors");
});

function playgame(playerMove) {
  computer = computerrandom();
  result = "";
  if (playerMove == "scissors") {
    if (computer == "rock") {
      result = "Lose!";
    } else if (computer == "paper") {
      result = "WIN!";
    } else {
      result = "Tie!";
    }
  } else if (playerMove == "paper") {
    computer = computerrandom();
    result = "";
    if (computer == "rock") {
      result = "WIN!";
    } else if (computer == "paper") {
      result = "Tie!";
    } else {
      result = "Lose!";
    }
  } else if (playerMove == "rock") {
    computer = computerrandom();
    result = "";
    if (computer == "rock") {
      result = "Tie!";
    } else if (computer == "paper") {
      result = "Lose!";
    } else {
      result = "WIN!";
    }
  }
  if (result === "WIN!") {
    score.wins += 1;
  } else if (result === "Lose!") {
    score.losses += 1;
  } else if (result === "Tie!") {
    score.ties += 1;
  }

  localStorage.setItem("score", JSON.stringify(score));

  updateScoreElement();

  document.querySelector(".js-result").innerHTML = `You ${result}!`;

  document.querySelector(
    ".js-moves"
  ).innerHTML = `You <img src="Elements/${playerMove}-emoji.png" class="move-icon" /><img
  src="Elements/${computer}-emoji.png"
  class="move-icon"/>Computer`;
}

function updateScoreElement() {
  document.querySelector(
    ".js-scores"
  ).innerHTML = `Wins: ${score.wins}, Losses: ${score.losses}, Ties: ${score.ties}`;
}

function computerrandom() {
  const randomNumber = Math.random();
  let computer = "";
  if (randomNumber >= 0 && randomNumber < 1 / 3) {
    computer = "rock";
  } else if (randomNumber >= 1 / 3 && randomNumber < 2 / 3) {
    computer = "paper";
  } else {
    computer = "scissors";
  }
  return computer;
}
