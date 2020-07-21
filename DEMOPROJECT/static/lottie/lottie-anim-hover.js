//Play an animation back on second click
/*https://lottiefiles.com/editor*/

let iconMenu = document.querySelectorAll('.bodymovi');

iconMenu.forEach( ic => {
    let animationMenu = bodymovin.loadAnimation({
            container: ic,
            renderer: 'svg',
            loop: false,
            autoplay: false,
            path: "/static/lottie/json/mail-white.json"
    });

    var directionMenu = 1;
      ic.addEventListener('mouseenter', (e) => {
      animationMenu.setDirection(directionMenu);
      animationMenu.play();
    });

      ic.addEventListener('mouseleave', (e) => {
      animationMenu.setDirection(-directionMenu);
      animationMenu.play();
    });
});

let iconLinkedIn = document.querySelectorAll('.bodylinkedIn');

iconLinkedIn.forEach( ic => {
    let animationMenu = bodymovin.loadAnimation({
            container: ic,
            renderer: 'svg',
            loop: false,
            autoplay: false,
            path: "/static/lottie/json/linkedIn.json"
    });

    var directionMenu = 1;
      ic.addEventListener('mouseenter', (e) => {
      animationMenu.setDirection(directionMenu);
      animationMenu.play();
    });

      ic.addEventListener('mouseleave', (e) => {
      animationMenu.setDirection(-directionMenu);
      animationMenu.play();
    });
});


let iconFacebook = document.querySelectorAll('.bodyfacebook');

iconFacebook.forEach( ic => {
    let animationMenu = bodymovin.loadAnimation({
            container: ic,
            renderer: 'svg',
            loop: false,
            autoplay: false,
            path: "/static/lottie/json/facebook.json"
    });

    var directionMenu = 1;
      ic.addEventListener('mouseenter', (e) => {
      animationMenu.setDirection(directionMenu);
      animationMenu.play();
    });

      ic.addEventListener('mouseleave', (e) => {
      animationMenu.setDirection(-directionMenu);
      animationMenu.play();
    });
});