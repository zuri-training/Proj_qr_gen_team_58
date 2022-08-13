var nav_elements = document.querySelectorAll(".sidenav-link");

for (var i = 0; i < nav_elements.length; i++) {
    nav_elements[i].addEventListener("click", function() {
        nav_elements.forEach(function(li) {
            li.classList.remove(".active-sidenav-link");
        });
        this.classList.add(".active-sidenav-link");}
    ); 
}

// Password toggle
const password = document.getElementById('password');
const toggle = document.getElementById('toggle');

show_password = () => {
    if (password.type == 'password') {
        password.setAttribute('type', 'text');
        toggle.classList.add('fa-eye-slash');
    } else {
        toggle.classList.remove('fa-eye-slash');
        password.setAttribute('type', 'password');
    }
};
toggle.addEventListener('click', show_password);

// Confirm password toggle
    const confirmPassword = document.getElementById('confirmPassword');
    const toggler = document.getElementById('toggler');

    showConfirmPassword = () => {
        if (confirmPassword.type == 'password') {
            confirmPassword.setAttribute('type', 'text');
            toggler.classList.add('fa-eye-slash');
        } else {
            toggler.classList.remove('fa-eye-slash');
            confirmPassword.setAttribute('type', 'password');
        }
    };
    toggler.addEventListener('click', showConfirmPassword);

// active state for navbar


