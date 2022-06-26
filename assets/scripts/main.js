"use strict";


import Swiper, {Navigation, Thumbs, Autoplay} from "swiper";

import Page from "./modules/page.js";

import initMap from "./blocks/map.js";
import initStories from "./blocks/stories.js";
import initPhoneFields from "./blocks/phone-field.js";
// import QtyInput from "./blocks/qty-input.js";
import Popup from "./blocks/popup.js";
import PriceFilter from "./blocks/price-filter.js";
import "./blocks/products.js";


import CartUpdateForm from "./blocks/cart-update-form.js";
// import CartRemoveForm from "./blocks/cart-remove-form.js";


window.addEventListener("load", () => {
    new Page();


    new Swiper(".hero-slider", {
        modules: [Navigation, Autoplay],

        loop: true,
        autoplay: {
            delay: 4000,
        },

        navigation: {
            prevEl: ".hero-nav__btn--prev",
            nextEl: ".hero-nav__btn--next",
        },
    });

    new Swiper(".product-slider", {
        modules: [Thumbs],

        // watchSlidesProgress: true,

        thumbs: {
            swiper: new Swiper(".product-thumbs", {
                spaceBetween: 16,
                slidesPerView: 5,
            }),
            slideThumbActiveClass: "active",
        },
    });

    new Swiper(".similar-products", {
        modules: [Navigation],

        slidesPerView: 4,
        spaceBetween: 30,

        navigation: {
            prevEl: ".similar-products__nav-btn--prev",
            nextEl: ".similar-products__nav-btn--next",
        },
    });




    ymaps.ready(initMap);
    initStories();
    initPhoneFields("[data-phone-field]");







    const $searchAction = document.querySelector(".search-action__inner");

    if ($searchAction) {
        const $popup = $searchAction.nextElementSibling;

        $searchAction.addEventListener("click", e => {
            const $searchAction = e.currentTarget;

            $popup.classList.toggle("active");
        });

        document.addEventListener("mouseup", e => {
            if (e.target.closest(".search-action")) {
                return;
            }

            $popup.classList.remove("active");
        });
    }












    const $filter = document.querySelector(".price-filter");
    new PriceFilter($filter);

















    // const $qtyInputs = document.querySelectorAll(".qty-input");
    // $qtyInputs.forEach($qtyInput => new QtyInput($qtyInput));
























    const $catNavBtns = document.querySelectorAll(".category-nav__btn");
    $catNavBtns.forEach($catNavBtn => $catNavBtn.addEventListener("click", toggleNav));

    function toggleNav(event) {
        const $btn = event.currentTarget;
        const $nav = $btn.nextElementSibling;
        const $item = $btn.closest(".category-nav__item");

        let maxHeight = 0;

        if (!$item.classList.contains("active")) {
            maxHeight = $nav.scrollHeight;

            const $innerNavs = $nav.querySelectorAll(".category-nav--sub");
            $innerNavs.forEach($innerNav => maxHeight += $innerNav.scrollHeight);
        }

        $nav.style.maxHeight = `${maxHeight}px`;
        $item.classList.toggle("active");
    }













    const $cartUpdateForms = document.querySelectorAll(".cart-update-form");
    $cartUpdateForms.forEach($form => new CartUpdateForm($form));

    // const $cartRemoveForms = document.querySelectorAll(".cart-remove-form");
    // $cartRemoveForms.forEach($form => new CartRemoveForm($form));
});
