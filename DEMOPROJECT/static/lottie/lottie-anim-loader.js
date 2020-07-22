//Animation in infinite loop
/*https://lottiefiles.com/editor*/

let svgContainer = document.querySelectorAll('.bodymovinani');
svgContainer.forEach( ic => {
    let animItem = bodymovin.loadAnimation({
        wrapper: ic,
        animType: 'svg',
        loop: true,
        path: "/static/lottie/json/infinity.json"
    });
});

let iconArrowUpLoad = document.querySelectorAll('.bodyarrowUpload');
iconArrowUpLoad.forEach( ic => {
     bodymovin.loadAnimation({
        wrapper: ic,
        animType: 'svg',
        loop: true,
        path: "/static/lottie/json/arrow-up-load-white.json"
    });

});