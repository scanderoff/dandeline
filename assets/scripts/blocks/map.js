function initMap() {
    const $map = document.querySelector(".map");

    if (!$map) {
        return;
    }

    const center = JSON.parse($map.dataset.mapCenter);
    const pin = $map.dataset.pin;

    const map = new ymaps.Map($map, {
        center: center,
        zoom: 17,
    }, {
        searchControlProvider: "yandex#search"
    });

    // map.behaviors.disable("scrollZoom");

    const placemark = new ymaps.Placemark(map.getCenter(), {}, {
        iconLayout: "default#image",
        iconImageHref: pin,
        iconImageSize: [20, 30],
        // iconImageOffset: [-5, -38]
    });

    map.geoObjects
        .add(placemark)
    ;
}

export default initMap;
