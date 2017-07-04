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
    var main = document.getElementById('main');
    var footer = document.getElementById('menu-footer');
    sidenav.style.transform = "translate(0)";
    sidenav.style.borderRightWidth = "5px";
    footer.style.transform = "translate(0)";
    main.style.transform = "translate(125px)";
    document.getElementById('overlay').className += ' overlay-show';
}

function closeNav() {
    var sidenav = document.getElementById('sidenav');
    var main = document.getElementById('main');
    var footer = document.getElementById('menu-footer');
    sidenav.style.transform = "translate(-100%)";
    sidenav.style.borderRightWidth = "0";
    footer.style.transform = "translate(-100%)";
    main.style.transform = "translate(0)";
    document.getElementById('overlay').className = 'overlay';
}
