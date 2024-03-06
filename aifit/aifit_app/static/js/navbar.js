function toggleNavbar() {
    var navbar = document.getElementById('navbar');
    navbar.style.display = (navbar.style.display === 'none' || navbar.style.display === '') ? 'block' : 'none';
}

// Close navbar when clicking outside of it
document.addEventListener('click', function(event) {
    var navbar = document.getElementById('navbar');
    var toggleButton = document.querySelector('.navbar-toggle');
    if (!navbar.contains(event.target) && event.target !== toggleButton) {
        navbar.style.display = 'none';
    }
});