const canvas = document.getElementById("gameCanvas");
const ctx = canvas.getContext("2d");

// Game variables
let birdY = canvas.height / 2;
let velocity = 0;
let gravity = 0.1;
let gap = 110; // Increased gap size
let score = 0;
let isGameOver = true; // Game starts as over
const pipeWidth = 50;
const pipeHeight = canvas.height / 1.5;
let pipes = [];
let animationId;

// Handle key press
document.addEventListener("keydown", jump);

// Start game button
const startButton = document.getElementById("startButton");
startButton.addEventListener("click", startGame);

// Reset game button
const resetButton = document.getElementById("resetButton");
resetButton.addEventListener("click", resetGame);

// Bird image
const birdImage = new Image();
birdImage.src = "7c289805-b287-438a-b310-43d9a0c75cbc__1_-removebg-preview.png"; // Replace with the path to your bird image
birdImage.addEventListener("load", startGame);

// Background image
const backgroundImage = new Image();
backgroundImage.src = "e0594550-3466-47ae-b280-c71ce37f222b.png"; // Replace with the path to your background image

// Pipe colors
const pipeColors = ["#FF0000", "#00FF00", "#0000FF"]; // Replace with desired colors

function jump(event) {
  if (event.code === "Space" && !isGameOver) {
    velocity = -3; // Increase the upward velocity
  }
}

function startGame() {
  isGameOver = false;
  startButton.disabled = true;
  animationId = requestAnimationFrame(gameLoop);
}

function resetGame() {
  cancelAnimationFrame(animationId);
  birdY = canvas.height / 2;
  velocity = 0;
  gap = 110; // Reset gap size
  score = 0;
  pipes = [];
  isGameOver = true;
  startButton.disabled = false;
  ctx.clearRect(0, 0, canvas.width, canvas.height);
  drawScore();
}

// Generate pipes
function generatePipes() {
  const pipe = {
    x: canvas.width,
    topHeight: Math.random() * (canvas.height - gap - 300) + 100,
    color: pipeColors[Math.floor(Math.random() * pipeColors.length)]
  };
  pipes.push(pipe);
}

// Game loop
function gameLoop() {
  if (!isGameOver) {
    // Update
    velocity += gravity;
    birdY += velocity;
    if (birdY < 5 || birdY > canvas.height) {
      gameOver();
    }

    for (let i = 0; i < pipes.length; i++) {
      const pipe = pipes[i];
      pipe.x -= 1; // Slow down the pipes speed

      // Collision detection
      if (
        (birdY + 20 < pipe.topHeight || birdY + 10 > pipe.topHeight + gap) &&
        pipe.x < 80 &&
        pipe.x + pipeWidth > 50
      ) {
        gameOver();
      }

      // Score increment
      if (pipe.x === 50 - pipeWidth) {
        score++;
      }
    }

    // Remove off-screen pipes
    if (pipes.length > 0 && pipes[0].x + pipeWidth < 0) {
      pipes.shift();
    }

    // Generate new pipes
    if (pipes.length === 0 || pipes[pipes.length - 1].x < canvas.width - 200) {
      generatePipes();
    }
  }

  // Clear the canvas
  ctx.clearRect(0, 0, canvas.width, canvas.height);

  // Draw the background image
  ctx.drawImage(backgroundImage, 0, 0, canvas.width, canvas.height);

  // Draw bird
  ctx.drawImage(birdImage, 50, birdY, 30, 30);

  // Draw pipes
  for (let i = 0; i < pipes.length; i++) {
    const pipe = pipes[i];
    const gradient = ctx.createLinearGradient(pipe.x, 0, pipe.x + pipeWidth, 0);
    gradient.addColorStop(0, pipe.color);
    gradient.addColorStop(0.5, "#888888");
    gradient.addColorStop(1, pipe.color);

    ctx.fillStyle = gradient;
    ctx.fillRect(pipe.x, 0, pipeWidth, pipe.topHeight);
    ctx.fillRect(
      pipe.x,
      pipe.topHeight + gap,
      pipeWidth,
      canvas.height - pipe.topHeight - gap
    );
  }

  // Draw score
  drawScore();

  if (isGameOver) {
    ctx.fillStyle = "red";
    ctx.font = "40px Arial";
    ctx.fillText("Game Over!", canvas.width / 2 - 100, canvas.height / 2);
  } else {
    animationId = requestAnimationFrame(gameLoop);
  }
}

function drawScore() {
  ctx.fillStyle = "black";
  ctx.font = "20px Arial";
  ctx.fillText("Score: " + score, 10, 30);
}

function gameOver() {
  isGameOver = true;
  cancelAnimationFrame(animationId);
}

// Start the game
resetGame();
