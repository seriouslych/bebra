function playPause() {
    const audio = document.querySelector("#player");
    const playpause = document.querySelector("#playpause");

    if (playpause.checked) {
        audio.play();
    } else {
        audio.pause();
    }
}