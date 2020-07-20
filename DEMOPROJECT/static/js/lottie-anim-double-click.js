/* Lottie javascript for animation https://useanimations.com/ */

let iconPlus = document.querySelectorAll('.bodymovinanim');

iconPlus.forEach( ic => {

        let animationPlus = bodymovin.loadAnimation({
            container: ic,
            renderer: 'svg',
            loop: false,
            autoplay: false,
            path: '/static/json/plustox.json'
            /* Change the path above to an animation */
        });



    var directionPlus = 1;
    ic.addEventListener('click', (e) => {
        animationPlus.setDirection(directionPlus);
        animationPlus.play();
        directionPlus = -directionPlus;
    });

});


