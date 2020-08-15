function scrollfun() {
    var y = window.scrollY;
    var a = document.getElementById('totop');
    if (y > 10) {
        a.style.display = 'block';
    } else {
        a.style.display = 'none';
    }
}
window.addEventListener("scroll", scrollfun);

function totop() {
    document.body.scrollTop = 0; // For Safari
    document.documentElement.scrollTop = 0; // For Chrome, Firefox, IE and Opera
}