"use strict";


import Swiper, {Navigation, Thumbs, Autoplay} from "swiper";

import Page from "./modules/page.js";

import initMap from "./blocks/map.js";
import initStories from "./blocks/stories.js";
import initPhoneFields from "./blocks/phone-field.js";
// import QtyInput from "./blocks/qty-input.js";
import Popup from "./blocks/popup.js";
import PriceFilter from "./blocks/price-filter.js";
import FilterForm from "./blocks/filter-form.js";

import RequestForm from "./blocks/request-form.js";
import CartUpdateForm from "./blocks/cart-update-form.js";
// import CartRemoveForm from "./blocks/cart-remove-form.js";

import "./blocks/products.js";
import "./blocks/category-nav.js";


window.addEventListener("load", () => {
    window.page = new Page();


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







    const $requestPopup = document.getElementById("requestPopup");

    if ($requestPopup) {
        new Popup($requestPopup);
    }



    const $requestForm = document.forms.requestForm;

    if ($requestForm) {
        new RequestForm($requestForm);
    }






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

    if ($filter) {
        new PriceFilter($filter);
    }


    const $filterForm = document.querySelector(".filter-form");

    if ($filterForm) {
        new FilterForm($filterForm);
    }














    // const $qtyInputs = document.querySelectorAll(".qty-input");
    // $qtyInputs.forEach($qtyInput => new QtyInput($qtyInput));






































    const $cartUpdateForms = document.querySelectorAll(".cart-update-form");
    $cartUpdateForms.forEach($form => new CartUpdateForm($form));

    // const $cartRemoveForms = document.querySelectorAll(".cart-remove-form");
    // $cartRemoveForms.forEach($form => new CartRemoveForm($form));
});
