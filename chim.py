import streamlit as st
import streamlit.components.v1 as components

def main():

```
st.header("🐦 FLAPPY BIRD")

game_html = """
<!DOCTYPE html>
<html lang="vi">

<head>

<meta charset="UTF-8">

<meta name="viewport"
      content="width=device-width,
               initial-scale=1.0,
               maximum-scale=1.0,
               user-scalable=no">

<style>

    * {
        box-sizing: border-box;
    }

    html,
    body {
        margin: 0;
        padding: 0;
        width: 100%;
        height: 100%;
        overflow: hidden;

        background: transparent;

        font-family: Arial, sans-serif;

        -webkit-user-select: none;
        user-select: none;

        -webkit-touch-callout: none;
    }


    /* =========================
       KHUNG GAME
    ========================= */

    #game {
        width: min(400px, 96vw);
        height: min(600px, 144vw);

        aspect-ratio: 2 / 3;

        position: relative;

        margin: 0 auto;

        overflow: hidden;

        background:
            linear-gradient(
                #70c5ce 0%,
                #aee8ef 75%,
                #ded895 75%,
                #ded895 100%
            );

        border: 4px solid #333;

        border-radius: 12px;

        cursor: pointer;

        touch-action: none;

        -webkit-user-select: none;
        user-select: none;

        -webkit-tap-highlight-color: transparent;
    }


    /* =========================
       MẶT TRỜI
    ========================= */

    #sun {
        position: absolute;

        right: 25px;
        top: 25px;

        font-size: 45px;

        z-index: 1;

        pointer-events: none;
    }


    /* =========================
       MÂY
    ========================= */

    .cloud {
        position: absolute;

        font-size: 45px;

        opacity: 0.8;

        z-index: 1;

        pointer-events: none;
    }


    #cloud1 {
        left: 40px;
        top: 80px;
    }


    #cloud2 {
        left: 240px;
        top: 150px;
    }


    /* =========================
       CHIM
    ========================= */

    #bird {
        position: absolute;

        left: 70px;
        top: 250px;

        width: 42px;
        height: 32px;

        z-index: 10;

        font-size: 34px;

        line-height: 32px;

        transform: rotate(0deg);

        pointer-events: none;
    }


    /* =========================
       ỐNG
    ========================= */

    .pipe {
        position: absolute;

        width: 65px;

        background: #28a745;

        border: 3px solid #176b2c;

        z-index: 5;

        pointer-events: none;
    }


    .pipe-top {
        top: 0;
    }


    .pipe-bottom {
        bottom: 0;
    }


    .pipe::after {
        content: "";

        position: absolute;

        left: -7px;

        width: 75px;

        height: 22px;

        background: #35c759;

        border: 3px solid #176b2c;
    }


    .pipe-top::after {
        bottom: -3px;
    }


    .pipe-bottom::after {
        top: -3px;
    }


    /* =========================
       ĐIỂM
    ========================= */

    #score {
        position: absolute;

        top: 15px;
        left: 20px;

        color: white;

        font-size: 32px;

        font-weight: bold;

        text-shadow:
            2px 2px 3px #333;

        z-index: 20;

        pointer-events: none;
    }


    /* =========================
       HƯỚNG DẪN
    ========================= */

    #help {
        position: absolute;

        bottom: 15px;
        left: 0;

        width: 100%;

        text-align: center;

        color: white;

        font-size: 16px;

        font-weight: bold;

        text-shadow:
            1px 1px 2px #333;

        z-index: 20;

        pointer-events: none;
    }


    /* =========================
       GAME OVER
    ========================= */

    #gameover {

        position: absolute;

        left: 20px;
        right: 20px;

        top: 190px;

        padding: 25px 15px;

        background: rgba(0, 0, 0, 0.78);

        color: white;

        text-align: center;

        border-radius: 15px;

        z-index: 100;

        display: none;

        pointer-events: none;
    }


    #gameover h1 {

        margin: 0 0 10px 0;

        color: #ff5252;

        font-size: 35px;
    }


    #finalScore {

        font-size: 24px;

        margin: 10px;
    }


    #restartText {

        margin-top: 15px;

        font-size: 16px;

        color: #ffeb3b;
    }


    /* =========================
       START
    ========================= */

    #startScreen {

        position: absolute;

        inset: 0;

        background: rgba(0, 0, 0, 0.35);

        z-index: 90;

        display: flex;

        justify-content: center;

        align-items: center;

        touch-action: none;
    }


    #startBox {

        background: white;

        padding: 25px;

        border-radius: 15px;

        text-align: center;

        box-shadow:
            0 5px 20px rgba(0,0,0,0.3);

        pointer-events: none;
    }


    #startBox h2 {

        margin-top: 0;

        color: #333;
    }


    #startButton {

        padding: 14px 30px;

        font-size: 20px;

        font-weight: bold;

        border: none;

        border-radius: 10px;

        background: #28a745;

        color: white;

        cursor: pointer;

        pointer-events: auto;
    }


    /* =========================
       NÚT CHẠM
    ========================= */

    #mobileHint {

        position: absolute;

        left: 0;
        right: 0;

        bottom: 45px;

        text-align: center;

        color: white;

        font-size: 15px;

        font-weight: bold;

        text-shadow:
            1px 1px 3px #333;

        z-index: 25;

        pointer-events: none;
    }


</style>

</head>


<body>


<div id="game">


    <div id="sun">
        ☀️
    </div>


    <div id="cloud1" class="cloud">
        ☁️
    </div>


    <div id="cloud2" class="cloud">
        ☁️
    </div>


    <div id="score">
        0
    </div>


    <div id="bird">
        🐦
    </div>


    <div id="help">
        👆 CHẠM MÀN HÌNH ĐỂ BAY
    </div>


    <div id="mobileHint">
        SPACE / CHẠM
    </div>


    <!-- START -->

    <div id="startScreen">

        <div id="startBox">

            <h2>
                🐦 FLAPPY BIRD
            </h2>

            <p>
                Vượt qua các ống nước!
            </p>

            <button id="startButton">
                ▶ BẮT ĐẦU
            </button>

        </div>

    </div>


    <!-- GAME OVER -->

    <div id="gameover">

        <h1>
            💥 GAME OVER
        </h1>

        <div id="finalScore">
            Điểm: 0
        </div>

        <div id="restartText">
            👆 Chạm màn hình để chơi lại
        </div>

    </div>


</div>


<script>


// =====================================
// LẤY ĐỐI TƯỢNG
// =====================================

const game =
    document.getElementById("game");

const bird =
    document.getElementById("bird");

const scoreText =
    document.getElementById("score");

const gameover =
    document.getElementById("gameover");

const finalScore =
    document.getElementById("finalScore");

const startScreen =
    document.getElementById("startScreen");

const startButton =
    document.getElementById("startButton");


// =====================================
// KÍCH THƯỚC GAME GỐC
// =====================================

const GAME_WIDTH = 400;

const GAME_HEIGHT = 600;

const BIRD_X = 70;

const BIRD_WIDTH = 42;

const BIRD_HEIGHT = 32;

const PIPE_WIDTH = 65;

const PIPE_GAP = 160;


// =====================================
// TỐC ĐỘ GAME
// =====================================

const PIPE_SPEED = 2.5;

const GRAVITY = 0.35;

const JUMP = -6.5;


// =====================================
// BIẾN GAME
// =====================================

let birdY = 250;

let birdVelocity = 0;

let score = 0;

let running = false;

let gameOver = false;

let pipes = [];

let lastTime = 0;


// =====================================
// RESET GAME
// =====================================

function resetGame() {

    birdY = 250;

    birdVelocity = 0;

    score = 0;

    gameOver = false;

    scoreText.innerText = "0";

    bird.style.top =
        birdY + "px";

    bird.style.transform =
        "rotate(0deg)";

    gameover.style.display =
        "none";


    createPipe(430);

    createPipe(680);
}


// =====================================
// TẠO ỐNG
// =====================================

function createPipe(x) {

    const minGapY = 180;

    const maxGapY = 400;


    const gapY =
        Math.floor(
            Math.random() *
            (maxGapY - minGapY)
        ) + minGapY;


    const topHeight =
        gapY - PIPE_GAP / 2;


    const bottomTop =
        gapY + PIPE_GAP / 2;


    const topPipe =
        document.createElement("div");


    topPipe.className =
        "pipe pipe-top";


    topPipe.style.left =
        x + "px";


    topPipe.style.height =
        topHeight + "px";


    const bottomPipe =
        document.createElement("div");


    bottomPipe.className =
        "pipe pipe-bottom";


    bottomPipe.style.left =
        x + "px";


    bottomPipe.style.height =
        (GAME_HEIGHT - bottomTop) + "px";


    game.appendChild(topPipe);

    game.appendChild(bottomPipe);


    pipes.push({

        x: x,

        gapY: gapY,

        top: topPipe,

        bottom: bottomPipe,

        passed: false

    });

}


// =====================================
// CHIM BAY
// =====================================

function jump() {

    if (!running) {
        return;
    }


    if (gameOver) {

        restartGame();

        return;

    }


    birdVelocity = JUMP;

}


// =====================================
// VA CHẠM
// =====================================

function collision(pipe) {

    const birdLeft =
        BIRD_X;

    const birdRight =
        BIRD_X + BIRD_WIDTH;

    const birdTop =
        birdY;

    const birdBottom =
        birdY + BIRD_HEIGHT;


    const pipeLeft =
        pipe.x;

    const pipeRight =
        pipe.x + PIPE_WIDTH;


    if (
        birdRight > pipeLeft &&
        birdLeft < pipeRight
    ) {

        const gapTop =
            pipe.gapY -
            PIPE_GAP / 2;


        const gapBottom =
            pipe.gapY +
            PIPE_GAP / 2;


        if (
            birdTop < gapTop ||
            birdBottom > gapBottom
        ) {

            return true;

        }

    }


    return false;

}


// =====================================
// GAME OVER
// =====================================

function endGame() {

    running = false;

    gameOver = true;


    finalScore.innerText =
        "Điểm: " + score;


    gameover.style.display =
        "block";

}


// =====================================
// XÓA ỐNG
// =====================================

function removePipe(pipe) {

    if (pipe.top) {
        pipe.top.remove();
    }


    if (pipe.bottom) {
        pipe.bottom.remove();
    }

}


// =====================================
// CẬP NHẬT GAME
// =====================================

function update(delta) {

    if (!running || gameOver) {
        return;
    }


    // TRỌNG LỰC

    birdVelocity +=
        GRAVITY * delta;


    birdY +=
        birdVelocity * delta;


    // XOAY CHIM

    let angle =
        birdVelocity * 4;


    if (angle > 90) {
        angle = 90;
    }


    if (angle < -25) {
        angle = -25;
    }


    bird.style.transform =
        "rotate(" + angle + "deg)";


    bird.style.top =
        birdY + "px";


    // DI CHUYỂN ỐNG

    for (
        let i = pipes.length - 1;
        i >= 0;
        i--
    ) {

        const pipe =
            pipes[i];


        pipe.x -=
            PIPE_SPEED * delta;


        pipe.top.style.left =
            pipe.x + "px";


        pipe.bottom.style.left =
            pipe.x + "px";


        // TÍNH ĐIỂM

        if (
            !pipe.passed &&
            pipe.x + PIPE_WIDTH < BIRD_X
        ) {

            pipe.passed = true;

            score++;

            scoreText.innerText =
                score;

        }


        // VA CHẠM

        if (
            collision(pipe)
        ) {

            endGame();

            return;

        }


        // XÓA ỐNG

        if (
            pipe.x < -PIPE_WIDTH
        ) {

            removePipe(pipe);

            pipes.splice(i, 1);

        }

    }


    // TẠO ỐNG MỚI

    if (pipes.length > 0) {

        const lastPipe =
            pipes[pipes.length - 1];


        if (
            lastPipe.x < 180
        ) {

            createPipe(
                GAME_WIDTH + 50
            );

        }

    }


    // ĐỤNG TRẦN

    if (birdY <= 0) {

        birdY = 0;

        endGame();

        return;

    }


    // ĐỤNG ĐẤT

    if (
        birdY + BIRD_HEIGHT >=
        GAME_HEIGHT
    ) {

        endGame();

        return;

    }

}


// =====================================
// GAME LOOP
// =====================================

function gameLoop(time) {

    if (!lastTime) {

        lastTime = time;

    }


    let delta =
        (time - lastTime) / 16.67;


    if (delta > 2) {

        delta = 2;

    }


    lastTime = time;


    update(delta);


    requestAnimationFrame(
        gameLoop
    );

}


// =====================================
// BẮT ĐẦU
// =====================================

function startGame() {

    startScreen.style.display =
        "none";


    // XÓA ỐNG CŨ

    for (
        let pipe of pipes
    ) {

        removePipe(pipe);

    }


    pipes = [];


    resetGame();


    running = true;

    gameOver = false;


    lastTime =
        performance.now();

}


// =====================================
// CHƠI LẠI
// =====================================

function restartGame() {

    for (
        let pipe of pipes
    ) {

        removePipe(pipe);

    }


    pipes = [];


    resetGame();


    running = true;

    gameOver = false;


    gameover.style.display =
        "none";


    lastTime =
        performance.now();

}


// =====================================
// NÚT BẮT ĐẦU
// =====================================

startButton.addEventListener(
    "click",
    function(event) {

        event.stopPropagation();

        startGame();

    }
);


// =====================================
// BÀN PHÍM
// =====================================

document.addEventListener(
    "keydown",
    function(event) {

        // START

        if (
            startScreen.style.display !==
            "none"
        ) {

            startGame();

            return;

        }


        // GAME OVER

        if (gameOver) {

            restartGame();

            return;

        }


        // SPACE

        if (
            event.code === "Space"
        ) {

            event.preventDefault();

            jump();

        }

    }
);


// =====================================
// ĐIỆN THOẠI + CHUỘT + BÚT CẢM ỨNG
// =====================================

game.addEventListener(
    "pointerdown",
    function(event) {

        event.preventDefault();


        // Nếu bấm nút bắt đầu

        if (
            event.target ===
            startButton
        ) {

            return;

        }


        // MÀN HÌNH START

        if (
            startScreen.style.display !==
            "none"
        ) {

            startGame();

            return;

        }


        // GAME OVER

        if (gameOver) {

            restartGame();

            return;

        }


        // ĐANG CHƠI

        if (running) {

            jump();

        }

    }
);


// =====================================
// CHỐNG MENU CHUỘT PHẢI
// =====================================

game.addEventListener(
    "contextmenu",
    function(event) {

        event.preventDefault();

    }
);


// =====================================
// CHẠY GAME
// =====================================

requestAnimationFrame(
    gameLoop
);


</script>

</body>
</html>
"""


components.html(
    game_html,
    height=640,
    scrolling=False
)
```

if **name** == "**main**":
main()
