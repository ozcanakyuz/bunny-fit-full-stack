//! log in
const signUpButton = document.getElementById('signUp');
const signInButton = document.getElementById('signIn');
const container = document.getElementById('containerlog');

signUpButton.addEventListener('click', () => {
	container.classList.add("right-panel-active");
});

signInButton.addEventListener('click', () => {
	container.classList.remove("right-panel-active");
});

// OLANAKLARIMIZ
function showMore() {
	var dots = document.getElementById("dots");
	var moreText = document.getElementById("more");
	var btnText = document.getElementById("showBtn");

	if (dots.style.display === "none") {
		dots.style.display = "inline";
		btnText.innerHTML = "Daha Fazla";
		moreText.classList = "d-none";
	} else {
		dots.style.display = "none";
		btnText.innerHTML = "Daha az göster";
		moreText.classList = "d-inline";
	}
}

// SCROLL PAGE FUNCTIONS NAVBAR ACTIVE

document.addEventListener("scroll", function() {
    var navbarLinks = document.querySelectorAll('[data-nav-link]');
    navbarLinks.forEach(function(navbarLink) {
        var sectionId = navbarLink.getAttribute('href').replace('#', '');
        var section = document.getElementById(sectionId);
        
        if (section) {
            var bounding = section.getBoundingClientRect();

            if (
                bounding.top <= 50 &&
                bounding.bottom >= 50
            ) {
                navbarLinks.forEach(function(link) {
                    link.classList.remove('active');
                });
                navbarLink.classList.add('active');
            }
        }
    });
});
