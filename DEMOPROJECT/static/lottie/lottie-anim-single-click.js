/* Play an animation on each click */
/*https://lottiefiles.com/editor*/


let iconSkipForward = document.querySelectorAll('.bodymovinan');
iconSkipForward.forEach(ic => {
    let animationSkipForward = bodymovin.loadAnimation({
        container: ic,
        renderer: 'svg',
        loop: false,
        autoplay: false,
        path: "https://raw.githubusercontent.com/thesvbd/Lottie-examples/master/assets/animations/skip-forward.json"
    });

    ic.addEventListener('click', function () {
        animationSkipForward.playSegments([0, 60], true);
    });
});


let iconArrowUp = document.querySelectorAll('.bodyarrowUp');
iconArrowUp.forEach(ic => {
    let animationSkipForward = bodymovin.loadAnimation({
        container: ic,
        renderer: 'svg',
        loop: false,
        autoplay: false,
        path: "/static/lottie/json/arrow-up-circle.json"
    });

    ic.addEventListener('click', function () {
        animationSkipForward.playSegments([0, 60], true);
    });
});