let show_menu = document.getElementById("show_menu")
let nav = document.getElementById('nav')
show_menu.addEventListener('click', () => {
    if (nav.style.display == "none") {
        nav.style.display = "block"

    } else { nav.style.display = "none" }

});