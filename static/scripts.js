document.getElementById('textarea').onkeyup = function () {
    document.getElementById('count').innerHTML = "Characters left: " + (500 - this.value.length);
};
