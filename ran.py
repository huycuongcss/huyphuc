import streamlit as st


def main():

    game = r'''
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">

<style>

body {
    margin: 0;
    padding: 10px;
    font-family: Arial, sans-serif;
    text-align: center;
    background: #f5f5f5;
}

h1 {
    margin: 5px;
    color: #1b5e20;
}

.info {
    font-size: 18px;
    font-weight: bold;
    margin: 8px;
}

#game {
    width: 400px;
    height: 400px;
    margin: auto;
    background: #111;
    border: 5px solid #333;
    display: grid;
    grid-template-columns: repeat(20, 1fr);
    grid-template-rows: repeat(20, 1fr);
}

.o {
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

button {
    font-size: 20px;
    padding: 10px 18px;
    margin: 5px;
    border: none;
    border-radius: 10px;
    cursor: pointer;
}

.control {
    background: #2196f3;
    color: white;
}

.restart {
    background: #4caf50;
    color: white;
}

.pause {
    background: #ff9800;
    color: white;
}

.message {
    font-size: 22px;
    font-weight: bold;
    margin: 10px;
}

#up {
    display: block;
    margin: 5px auto;
}

</style>
</head>


<body>

<h1>🐍 RẮN SĂN MỒI</h1>

<div class="info">
    Điểm: <span id="score">0</span>
    &nbsp;&nbsp;
    Độ dài: <span id="length">3</span>
    &nbsp;&nbsp;
    Tốc độ: <span id="speed">5</span>
</div>

<div id="message"></div>

<div id="game"></div>

<br>

<button id="up" class="control">⬆️</button>

<div>
    <button class="control" id="left">⬅️</button>
    <button class="control" id="down">⬇️</button>
    <button class="control" id="right">➡️</button>
</div>

<br>

<button class="pause" id="pause">⏸️ Tạm dừng</button>
<button class="restart" id="restart">🔄 Chơi lại</button>

<p>
    💻 Máy tính: dùng phím mũi tên<br>
    📱 Điện thoại: bấm các nút điều khiển
</p>


<script>

const SIZE = 20;

let snake;
let food;

let direction;
let nextDirection;

let score;
let running;
let paused;

let speed;
let timer;


// ============================
// KHỞI ĐỘNG GAME
// ============================

function startGame() {

    snake = [
        [10, 10],
        [9, 10],
        [8, 10]
    ];

    food = createFood();

    direction = "RIGHT";
    nextDirection = "RIGHT";

    score = 0;

    speed = 200;

    running = true;
    paused = false;

    document.getElementById("message").innerHTML = "";

    updateInfo();

    clearInterval(timer);

    timer = setInterval(gameLoop, speed);
}


// ============================
// TẠO MỒI
// ============================

function createFood() {

    let position;

    do {

        position = [
            Math.floor(Math.random() * SIZE),
            Math.floor(Math.random() * SIZE)
        ];

    } while (
        snake.some(
            part =>
            part[0] === position[0] &&
            part[1] === position[1]
        )
    );

    return position;
}


// ============================
// VÒNG LẶP GAME
// ============================

function gameLoop() {

    if (!running || paused) {
        return;
    }

    direction = nextDirection;

    let head = [...snake[0]];

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


    // ĐỤNG TƯỜNG

    if (
        head[0] < 0 ||
        head[0] >= SIZE ||
        head[1] < 0 ||
        head[1] >= SIZE
    ) {

        gameOver();
        return;
    }


    // ĐỤNG THÂN

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


    // ĂN MỒI

    if (
        head[0] === food[0] &&
        head[1] === food[1]
    ) {

        score += 10;

        food = createFood();

        // Tăng tốc

        if (speed > 60) {
            speed -= 10;
        }

        clearInterval(timer);

        timer = setInterval(gameLoop, speed);

    } else {

        snake.pop();
    }


    draw();

    updateInfo();
}


// ============================
// VẼ GAME
// ============================

function draw() {

    const board = document.getElementById("game");

    board.innerHTML = "";


    // Vẽ rắn

    snake.forEach(
        (part, index) => {

            const cell = document.createElement("div");

            cell.className =
                index === 0
                ? "o head"
                : "o snake";

            cell.style.gridColumn =
                part[0] + 1;

            cell.style.gridRow =
                part[1] + 1;

            board.appendChild(cell);
        }
    );


    // Vẽ mồi

    const foodCell =
        document.createElement("div");

    foodCell.className = "o food";

    foodCell.style.gridColumn =
        food[0] + 1;

    foodCell.style.gridRow =
        food[1] + 1;

    board.appendChild(foodCell);
}


// ============================
// CẬP NHẬT THÔNG TIN
// ============================

function updateInfo() {

    document.getElementById("score")
        .innerText = score;

    document.getElementById("length")
        .innerText = snake.length;

    document.getElementById("speed")
        .innerText =
        Math.round(1000 / speed);
}


// ============================
// GAME OVER
// ============================

function gameOver() {

    running = false;

    clearInterval(timer);

    let message = "";

    if (score < 50) {

        message =
            "😅 GÀ MỚI TẬP CHƠI";

    } else if (score < 100) {

        message =
            "👍 KHÁ";

    } else if (score < 200) {

        message =
            "🔥 GIỎI";

    } else {

        message =
            "👑 CAO THỦ RẮN SĂN MỒI";
    }


    document.getElementById("message").innerHTML =
        "💥 GAME OVER!<br>" +
        "Điểm: " + score +
        "<br>" +
        message;
}


// ============================
// ĐỔI HƯỚNG
// ============================

function changeDirection(newDirection) {

    if (newDirection === "UP" &&
        direction !== "DOWN") {

        nextDirection = "UP";
    }

    if (newDirection === "DOWN" &&
        direction !== "UP") {

        nextDirection = "DOWN";
    }

    if (newDirection === "LEFT" &&
        direction !== "RIGHT") {

        nextDirection = "LEFT";
    }

    if (newDirection === "RIGHT" &&
        direction !== "LEFT") {

        nextDirection = "RIGHT";
    }
}


// ============================
// BÀN PHÍM
// ============================

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

        if (event.key === " ") {

            event.preventDefault();

            togglePause();
        }
    }
);


// ============================
// NÚT ĐIỀU KHIỂN
// ============================

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


// ============================
// TẠM DỪNG
// ============================

function togglePause() {

    if (!running) {
        return;
    }

    paused = !paused;

    document.getElementById("pause")
        .innerText =
        paused
        ? "▶️ Tiếp tục"
        : "⏸️ Tạm dừng";
}


document.getElementById("pause")
    .onclick = togglePause;


// ============================
// CHƠI LẠI
// ============================

document.getElementById("restart")
    .onclick = startGame;


// ============================
// BẮT ĐẦU
// ============================

startGame();

</script>

</body>
</html>
'''


    # =================================
    # HIỂN THỊ GAME TRÊN STREAMLIT
    # =================================

    st.components.v1.html(
        game,
        height=850,
        scrolling=False
    )


# =====================================
# CHẠY FILE
# =====================================

if __name__ == "__main__":
    main()