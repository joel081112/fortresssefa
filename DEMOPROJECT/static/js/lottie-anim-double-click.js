/* Lottie javascript for animation https://useanimations.com/ */

let iconPlus = document.querySelector('.bodymovinanim');
    let animationPlus = bodymovin.loadAnimation({
            container: iconPlus,
            renderer: 'svg',
            loop: false,
            autoplay: false,
            path: '/static/json/plustox.json'
    });
    /* Change the path above to an animation */
    var directionPlus = 1;
      iconPlus.addEventListener('click', (e) => {
      animationPlus.setDirection(directionPlus);
      animationPlus.play();
      directionPlus = -directionPlus;
    });