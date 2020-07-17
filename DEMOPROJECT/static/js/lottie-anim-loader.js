//Animation in infinite loop

let svgContainer = document.querySelector('.bodymovinani');
    let animItem = bodymovin.loadAnimation({
      wrapper: svgContainer,
      animType: 'svg',
      loop: true,
      path: "/static/json/infinity.json"
    });