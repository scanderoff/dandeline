<template>
    <section class="hero">
        <swiper
            :modules="[Navigation, Autoplay]"
            :navigation="{
                prevEl: '.hero-nav__btn--prev',
                nextEl: '.hero-nav__btn--next'
            }"
            :autoplay="{
               delay: 4000,
            }"
        >
            <swiper-slide class="hero-slide">
                <a class="hero-slide__link" href="#">
                    <img class="hero-slide__image" src="../assets/images/hero-slide/00.jpg" alt="">
                </a>
            </swiper-slide>
            <swiper-slide class="hero-slide">
                <a class="hero-slide__link" href="#">
                    <img class="hero-slide__image" src="../assets/images/hero-slide/01.jpg" alt="">
                </a>
            </swiper-slide>
            <swiper-slide class="hero-slide">
                <a class="hero-slide__link" href="#">
                    <img class="hero-slide__image" src="../assets/images/hero-slide/02.jpg" alt="">
                </a>
            </swiper-slide>

            <div class="hero-nav hero-slider__nav">
                <div class="hero-nav__container page__container">
                    <button class="hero-nav__btn hero-nav__btn--prev" type="button">
                        <svg xmlns="http://www.w3.org/2000/svg" width="10" height="18" fill="none" viewBox="0 0 10 18">
                            <path stroke="#fff" d="M9.423 17.106 1.11 8.792 9.423.48" />
                        </svg>
                    </button>
                    <button class="hero-nav__btn hero-nav__btn--next" type="button">
                        <svg xmlns="http://www.w3.org/2000/svg" width="11" height="18" fill="none" viewBox="0 0 11 18">
                            <path stroke="#fff" d="m1.135.895 8.313 8.313-8.313 8.313" />
                        </svg>
                    </button>
                </div>
            </div>
        </swiper>
    </section>
</template>

<script>
    import { Navigation, Autoplay } from "swiper";
    import { Swiper, SwiperSlide } from "swiper/vue";

    import "swiper/scss";
    import "swiper/scss/navigation";
    import "swiper/scss/autoplay";

    export default {
        name: "HeroSection",

        components: {
            Swiper,
            SwiperSlide,
        },

        setup() {
            return {
                Navigation,
                Autoplay,
            };
        },
        // created() {
        //     new Swiper(".hero-slider", {
        //         modules: [Navigation, Autoplay],

        //         loop: true,
        //         autoplay: {
        //             delay: 4000,
        //         },

        //         navigation: {
        //             prevEl: ".hero-nav__btn--prev",
        //             nextEl: ".hero-nav__btn--next",
        //         },
        //     });
        // },
    };
</script>

<style lang="scss" scoped>
    .hero-slider {
        position: relative;

        &__slides {
            margin: 0;
            padding: 0;
            list-style: none;
        }

        &__nav {
            position: absolute;
            top: 50%;
            left: 0;
            z-index: 3;
            transform: translateY(-50%);
        }
    }

    .hero-slide {
        height: 640px;

        &__link {
            height: 100%;
        }

        &__image {
            width: 100%;
            height: 100%;
            object-fit: cover;
        }
    }

    .hero-nav {
        width: 100%;

        pointer-events: none;

        &__container {
            display: flex;
            justify-content: space-between;
        }

        &__btn {
            position: relative;
            width: 70px;
            height: 70px;
            padding: 0;
            border: none;

            border-radius: 50%;
            background-image: none;
            background-color: rgba(0, 0, 0, 0.5);
            color: inherit;
            cursor: pointer;
            pointer-events: auto;

            &::before {
                content: "";
                position: absolute;
                top: 50%;
                left: 50%;
                transform: translate(-50%, -50%) scale(0);
                width: 100%;
                height: 100%;

                border-radius: 50%;
                background-color: rgba(30, 30, 30, 0.8);
                pointer-events: none;
                transition: transform 0.3s ease;
            }

            &:hover::before {
                transform: translate(-50%, -50%) scale(1);
            }

            svg {
                position: relative;
            }
        }
    }
</style>
