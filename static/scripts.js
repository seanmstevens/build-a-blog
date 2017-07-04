window.onload = charCounter;

function charCounter() {
    if (window.location.pathname == "/newpost") {
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
};

function openNav() {
    var sidenav = document.getElementById('sidenav');
    sidenav.style.width = "250px";
    sidenav.style.borderRightWidth = "3px";
    document.getElementById("main").style.marginLeft = "250px";
}

function closeNav() {
    var sidenav = document.getElementById('sidenav');
    sidenav.style.width = "0";
    sidenav.style.borderRightWidth = "0";
    document.getElementById("main").style.marginLeft = "0";
}