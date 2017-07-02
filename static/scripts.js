window.onload = charCounter;

function charCounter() {
    var text = document.getElementById('textarea');
    var counter = document.getElementById('counter');

    document.getElementById('counter').innerHTML = (500 - text.value.length);

    function count() {
        counter.innerHTML = (500 - this.value.length);
        if (this.value.length >= 450) {
            counter.style.color = "#f44336";
        } else {
            counter.style.color = "#3f3f43";
        };
    };

    text.addEventListener('keyup', count);
    text.addEventListener('keydown', count);
};