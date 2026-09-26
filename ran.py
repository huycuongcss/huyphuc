import streamlit as st


def main():

    game = r'''
<!DOCTYPE html>
<html>
<head>

<meta charset="UTF-8">

<style>

* {
    box-sizing: border-box;
}

body {
    margin: 0;
    padding: 10px;
    font-family: Arial, sans-serif;
    text-align: center;
    background: #f5f5f5;
}

h1 {
    margin: 5px 0;
    color: #1b5e20;
}

.info {
    font-size: 18px;
    font-weight: bold;
    margin: 8px;
}

#message {
    height: 65px;
    font-size: 20px;
    font-weight: bold;
    margin: 5px;
}

#game {
    width: 400px;
    height: 400px;
    margin: auto;
    background: #111;
    border: 5px solid #333;

    display: grid;

    grid-template-columns:
        repeat(20, 1fr);

    grid-template-rows:
        repeat(20, 1fr);
}

.cell {
    width: 100%;
    height: 100%;
}

.snake {
    background: #00e676;
}

.head {
    background: #76ff03;
}

.food {
    background: #ff1744;
    border-radius: 50%;
}

.controls {
    margin-top: 10px;
}

button {
    border: none;
    border-radius: 10px;
    padding: 10px 18px;
    margin: 4px;
    font-size: 20px;
    cursor: pointer;
}

.direction {
    background: #2196f3;
    color: white;
}

.pause {
    background: #ff9800;
    color: white;
}

.restart {
    background: #4caf50;
    color: white;
}

.help {
    font-size: 14px;
    color: #555;
    margin-top: 8px;
}

</style>

</head>


<body>

<h1>🐍 RẮN SĂN MỒI</h1>


<div class="info">

Điểm:
<span id="score">0</span>

&nbsp;&nbsp;

Độ dài:
<span id="length">3</span>

&nbsp;&nbsp;

Tốc độ:
<span id="speed">0</span>

</div>


<div id="message">
▶️ Bấm phím mũi tên để bắt đầu
</div>


<div id="game"></div>


<div class="controls">

    <div>

        <button
            class="direction"
            id="up">
            ⬆️
        </button>

    </div>


    <div>

        <button
            class="direction"
            id="left">
            ⬅️
        </button>

        <button
            class="direction"
            id="down">
            ⬇️
        </button>

        <button
            class="direction"
            id="right">
            ➡️
        </button>

    </div>


    <div>

        <button
            class="pause"
            id="pause">
            ⏸️ Tạm dừng
        </button>

        <button
            class="restart"
            id="restart">
            🔄 Chơi lại
        </button>

    </div>

</div>


<div class="help">

💻 Máy tính: dùng phím mũi tên<br>

📱 Điện thoại: bấm các nút<br>

⏸️ Phím Space: tạm dừng

</div>


<script>


// ========================================
// CÀI ĐẶT
// ========================================

const SIZE = 20;

const START_SPEED = 350;

const MIN_SPEED = 100;


// ========================================
// BIẾN
// ========================================

let snake;

let food;

let direction;

let nextDirection;

let score;

let speed;

let timer;

let running;

let paused;


// ========================================
// TẠO GAME
// ========================================

function startGame() {

    snake = [
        [10, 10],
        [9, 10],
        [8, 10]
    ];


    food = createFood();


    direction = null;

    nextDirection = null;


    score = 0;


    speed = START_SPEED;


    running = false;

    paused = false;


    clearInterval(timer);


    document.getElementById("message").innerHTML =
        "▶️ Bấm phím mũi tên để bắt đầu";


    document.getElementById("pause").innerText =
        "⏸️ Tạm dừng";


    draw();

    updateInfo();
}


// ========================================
// TẠO MỒI
// ========================================

function createFood() {

    let position;


    do {

        position = [

            Math.floor(
                Math.random() * SIZE
            ),

            Math.floor(
                Math.random() * SIZE
            )

        ];

    }

    while (

        snake.some(

            part =>

            part[0] === position[0] &&
            part[1] === position[1]

        )

    );


    return position;
}


// ========================================
// BẮT ĐẦU CHẠY
// ========================================

function startMoving(newDirection) {

    direction = newDirection;

    nextDirection = newDirection;

    running = true;

    paused = false;


    document.getElementById("message").innerHTML =
        "🐍 Đang chơi";


    clearInterval(timer);


    timer = setInterval(
        gameLoop,
        speed
    );


    updateInfo();
}


// ========================================
// VÒNG LẶP GAME
// ========================================

function gameLoop() {

    if (!running || paused) {

        return;
    }


    direction = nextDirection;


    let head = [

        snake[0][0],

        snake[0][1]

    ];


    if (direction === "UP") {

        head[1]--;

    }


    if (direction === "DOWN") {

        head[1]++;

    }


    if (direction === "LEFT") {

        head[0]--;

    }


    if (direction === "RIGHT") {

        head[0]++;

    }


    // ====================================
    // ĐỤNG TƯỜNG
    // ====================================

    if (

        head[0] < 0 ||

        head[0] >= SIZE ||

        head[1] < 0 ||

        head[1] >= SIZE

    ) {

        gameOver();

        return;
    }


    // ====================================
    // ĐỤNG THÂN
    // ====================================

    if (

        snake.some(

            part =>

            part[0] === head[0] &&
            part[1] === head[1]

        )

    ) {

        gameOver();

        return;
    }


    snake.unshift(head);


    // ====================================
    // ĂN MỒI
    // ====================================

    if (

        head[0] === food[0] &&
        head[1] === food[1]

    ) {

        score += 10;


        food = createFood();


        if (speed > MIN_SPEED) {

            speed -= 15;

        }


        clearInterval(timer);


        timer = setInterval(
            gameLoop,
            speed
        );


    }

    else {

        snake.pop();

    }


    draw();

    updateInfo();
}


// ========================================
// VẼ GAME
// ========================================

function draw() {

    const board =
        document.getElementById("game");


    board.innerHTML = "";


    // RẮN

    snake.forEach(

        function(part, index) {

            const cell =
                document.createElement("div");


            cell.className =
                "cell " +

                (

                    index === 0

                    ? "head"

                    : "snake"

                );


            cell.style.gridColumn =
                part[0] + 1;


            cell.style.gridRow =
                part[1] + 1;


            board.appendChild(cell);

        }

    );


    // MỒI

    const foodCell =
        document.createElement("div");


    foodCell.className =
        "cell food";


    foodCell.style.gridColumn =
        food[0] + 1;


    foodCell.style.gridRow =
        food[1] + 1;


    board.appendChild(foodCell);
}


// ========================================
// THÔNG TIN
// ========================================

function updateInfo() {

    document.getElementById("score")
        .innerText = score;


    document.getElementById("length")
        .innerText = snake.length;


    if (running) {

        document.getElementById("speed")
            .innerText =
            Math.round(1000 / speed);

    }

    else {

        document.getElementById("speed")
            .innerText = 0;

    }
}


// ========================================
// GAME OVER
// ========================================

function gameOver() {

    running = false;

    paused = false;


    clearInterval(timer);


    let ranking;


    if (score < 50) {

        ranking =
            "😅 GÀ MỚI TẬP CHƠI";

    }

    else if (score < 100) {

        ranking =
            "👍 KHÁ";

    }

    else if (score < 200) {

        ranking =
            "🔥 GIỎI";

    }

    else {

        ranking =
            "👑 CAO THỦ RẮN SĂN MỒI";

    }


    document.getElementById("message").innerHTML =

        "💥 GAME OVER!<br>" +

        "Điểm: " + score +
        " - " +
        ranking;


    document.getElementById("pause")
        .innerText =
        "⏸️ Tạm dừng";


    updateInfo();
}


// ========================================
// ĐỔI HƯỚNG
// ========================================

function changeDirection(newDirection) {


    // Nếu game chưa chạy
    // thì bắt đầu luôn

    if (!running) {

        startMoving(newDirection);

        return;
    }


    if (

        newDirection === "UP" &&

        direction !== "DOWN"

    ) {

        nextDirection = "UP";

    }


    if (

        newDirection === "DOWN" &&

        direction !== "UP"

    ) {

        nextDirection = "DOWN";

    }


    if (

        newDirection === "LEFT" &&

        direction !== "RIGHT"

    ) {

        nextDirection = "LEFT";

    }


    if (

        newDirection === "RIGHT" &&

        direction !== "LEFT"

    ) {

        nextDirection = "RIGHT";

    }
}


// ========================================
// PHÍM MŨI TÊN
// ========================================

document.addEventListener(
    "keydown",
    function(event) {


        if (event.key === "ArrowUp") {

            event.preventDefault();

            changeDirection("UP");

        }


        if (event.key === "ArrowDown") {

            event.preventDefault();

            changeDirection("DOWN");

        }


        if (event.key === "ArrowLeft") {

            event.preventDefault();

            changeDirection("LEFT");

        }


        if (event.key === "ArrowRight") {

            event.preventDefault();

            changeDirection("RIGHT");

        }


        if (event.code === "Space") {

            event.preventDefault();

            togglePause();

        }

    }
);


// ========================================
// NÚT ĐIỀU KHIỂN
// ========================================

document.getElementById("up")
    .onclick = function() {

        changeDirection("UP");

    };


document.getElementById("down")
    .onclick = function() {

        changeDirection("DOWN");

    };


document.getElementById("left")
    .onclick = function() {

        changeDirection("LEFT");

    };


document.getElementById("right")
    .onclick = function() {

        changeDirection("RIGHT");

    };


// ========================================
// TẠM DỪNG
// ========================================

function togglePause() {


    if (!running) {

        return;
    }


    paused = !paused;


    if (paused) {

        document.getElementById("pause")
            .innerText =
            "▶️ Tiếp tục";

        document.getElementById("message")
            .innerHTML =
            "⏸️ ĐANG TẠM DỪNG";

    }

    else {

        document.getElementById("pause")
            .innerText =
            "⏸️ Tạm dừng";

        document.getElementById("message")
            .innerHTML =
            "🐍 Đang chơi";

    }
}


document.getElementById("pause")
    .onclick = togglePause;


// ========================================
// NÚT CHƠI LẠI
// ========================================

document.getElementById("restart")
    .onclick = function() {

        startGame();

    };


// ========================================
// KHỞI ĐỘNG
// ========================================

startGame();


</script>

</body>
</html>
'''


    st.components.v1.html(
        game,
        height=780,
        scrolling=False
    )


if __name__ == "__main__":
    main()