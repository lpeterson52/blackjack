let x = Math.random() * 100;
let winstreak = 0;
let highscore = 0;


function randint() {
    x = Math.random() * 100
    document.getElementById("demo").innerHTML = x;
    if (x > winstreak) {
        winstreak++;
    }
    else {
        if (winstreak > highscore) {
            highscore = winstreak;
        }
        winstreak = 0;

    }
    document.getElementById("wins").innerHTML = winstreak;
    document.getElementById("highscore").innerHTML = highscore;
}




function calculateOdds(streak) {
    if (streak == 0) {
        return 1 - (streak / 100);
    }
    return (1 - (streak / 100)) * calculateOdds(streak - 1);

}

function setCalculatedOdds(streak) {
    document.getElementById("odds").innerHTML = calculateOdds(streak) * 100 + "%";
}