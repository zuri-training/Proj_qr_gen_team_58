// Form Validation
    const form = document.getElementById('form');

// function to check email pattern
    const isValid = (email) => {
        var re = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
        return re.test(String(email).toLowerCase());
    }

// function for error messages
    const addErrorTo = (field, message) => {
        const formControl = form[field].parentNode;
        formControl.classList.add('error');
        const small = formControl.querySelector('small');
        small.innerText = message;
}

//  function to remove error messages
    const removeErrorFrom = (field) => {
        const formControl = form[field].parentNode;
        formControl.classList.remove('error');
        const small = formControl.querySelector('small');
        small.style.display = 'none';
    }

// Form check
    form.addEventListener('submit', e => {
        e.preventDefault();

        const fullName = form['fullName'].value;
        const email = form['email'].value;
        const Password = form['password'].value;
        const ConfirmPassword = form['confirmPassword'].value

        // Error Message for not entering full name
        if (!fullName) {
            addErrorTo('fullName', 'Please enter your full name');
        } else {
            removeErrorFrom('fullName');
        }

        // Error Meassges fo email
        if (!email) {
            addErrorTo('email', 'Please enter your email');
        } else if (!isValid(email)) {
            addErrorTo('email', 'Please enter a valid email');
        } else {
            removeErrorFrom('email');
        }

        // Error Message for password
        if (!Password) {
            addErrorTo('password', 'Please enter a password');
        } else {
            removeErrorFrom('password');
        }

        // Error Message for Confirm Password
        if (!ConfirmPassword) {
            addErrorTo('confirmPassword', 'Please confirm your password');
        } else if (ConfirmPassword != Password) {
            addErrorTo('confirmPassword', 'Passwords do not match');
        } else {
            removeErrorFrom('confirmPassword');
        }

        // Error Message for checkbox
        if (!document.getElementById('checkbox').checked) {
            addErrorTo('checkbox', 'Please check this box if you want to proceed');
        } else {
            removeErrorFrom('checkbox');
        }
    });

    // Form check login page
    form.addEventListener('submit', e => {
        e.preventDefault();

        const email = form['email'].value;
        const Password = form['password'].value;

        // Error Meassges fo email
        if (!email) {
            addErrorTo('email', 'Please enter your email');
        } else if (!isValid(email)) {
            addErrorTo('email', 'Please enter a valid email');
        } else {
            removeErrorFrom('email');
        }

        // Error Message for password
        if (!Password) {
            addErrorTo('password', 'Please enter a password');
        } else {
            removeErrorFrom('password');
        }
    });

    // form check for forgot password page
    form.addEventListener('submit', e => {
        e.preventDefault();

        const email = form['email'].value;

        // Error Meassges for email
        if (!email) {
            addErrorTo('email', 'Please enter your email');
        } else if (!isValid(email)) {
            addErrorTo('email', 'Please enter a valid email');
        } else {
            removeErrorFrom('email');
        }
    });

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

     
var swiper = new Swiper(".slide-content", {
    slidesPerView: 3,
    spaceBetween: 25,
    loop: true,
    centerSlide: 'true',
    fade: 'true',
    grabCursor: 'true',
    pagination: {
      el: ".swiper-pagination",
      clickable: true,
      dynamicBullets: true,
    },
    navigation: {
      nextEl: ".swiper-button-next",
      prevEl: ".swiper-button-prev",
    },

    breakpoints:{
        0: {
            slidesPerView: 1,
        },
        520: {
            slidesPerView: 2,
        },
        950: {
            slidesPerView: 3,
        },
    },
  });
