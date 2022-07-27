<template>
    <header class="header">
        <div class="header__top">
            <div class="header__top-container page__container">
                <SiteSocials/>

                <span class="header__address">
                    Иркутск, ул. Академика Курчатова 3, офис 406
                </span>

                <a class="link header__mail" href="mailto:info-dandeline@mail.ru">
                    info-dandeline@mail.ru
                </a>

                <a class="link header__phone" href="tel:+73952436645">
                    +7 3952 43-66-45
                </a>

                <button class="link header__btn" type="button" data-popup="requestPopup">
                    Заказать звонок
                </button>

                <div class="header__auth">
                    <!-- {% if user.is_authenticated %}
                        <a class="link" href="{% url 'users:logout' %}?next={{ request.path }}">
                            Выход
                        </a>
                    {% else %}
                        <a class="link" href="{% url 'users:auth' %}?next={{ request.path }}">
                            Вход
                        </a>
                    {% endif %} -->
                </div>
            </div>
        </div>

        <div class="header__bottom">
            <div class="header__bottom-container page__container">
                <router-link to="/" class="logo header__logo">
                    <img class="logo__image" src="../assets/images/logo/logo.svg" alt="Dandeline" width="171" height="50">
                </router-link>

                <SiteNav/>

                <div class="header__actions">
                    <a class="header__action" href="{% url 'users:edit' %}">
                        <svg xmlns="http://www.w3.org/2000/svg" width="18" height="17" viewBox="0 0 18 17">
                            <path stroke="none" d="m6.774 9.049.206.721.145-1.384-.35.663Zm4.224 0-.341-.668.135 1.389.206-.721ZM16.386 16v.75h.75V16h-.75Zm-14.25 0c0-2.932 2.027-5.426 4.844-6.23l-.41-1.442C3.159 9.3.636 12.346.636 16h1.5Zm4.99-7.614c-1.16-.614-1.93-1.784-1.93-3.1h-1.5c0 1.924 1.125 3.576 2.727 4.425l.702-1.325Zm-1.93-3.1c0-1.94 1.615-3.536 3.69-3.536V.25c-2.853 0-5.19 2.219-5.19 5.036h1.5Zm3.69-3.536c2.075 0 3.69 1.597 3.69 3.536h1.5c0-2.817-2.337-5.036-5.19-5.036v1.5Zm3.69 3.536c0 1.323-.775 2.51-1.92 3.095l.683 1.336c1.618-.827 2.738-2.514 2.738-4.431h-1.5ZM10.793 9.77c2.818.804 4.844 3.298 4.844 6.23h1.5c0-3.654-2.522-6.7-5.932-7.672l-.412 1.442Zm5.594 5.48H6.18v1.5h10.207v-1.5ZM.636 16v.77h1.5V16h-1.5Z" />
                        </svg>
                    </a>
                    <span class="search-action header__action">
                        <button class="search-action__inner" type="button">
                            <svg xmlns="http://www.w3.org/2000/svg" width="19" height="18" fill="none" viewBox="0 0 19 18">
                                <path fill="none" stroke-miterlimit="10" stroke-width="1.5" d="m18.299 16.528-2.373-2.373a6.37 6.37 0 0 0-3.303-1.765 6.479 6.479 0 0 0-3.734.361c-.842.348-1.315.451-2.234.451a5.74 5.74 0 1 1 5.229-3.369" />
                            </svg>
                        </button>

                        <div class="search-popup search-action__popup">
                            <div class="search-popup__inner">
                                <form class="search-form" action="{% url 'catalog:products' %}" method="GET">
                                    <input class="search-form__field" type="search" name="s" placeholder="Поиск по товарам...">

                                    <button class="search-form__btn" type="submit">
                                        <svg width="19" height="18" viewBox="0 0 19 18" fill="none" xmlns="http://www.w3.org/2000/svg">
                                            <path fill="none" d="M18.2987 16.5278C17.372 15.601 16.8524 15.0814 15.9257 14.1547C14.9989 13.228 13.8736 12.6392 12.6225 12.39C11.3713 12.1408 10.0687 12.2643 8.88944 12.7511C8.0468 13.0989 7.57366 13.2024 6.65451 13.2024C3.48415 13.2024 0.914062 10.6323 0.914062 7.46194C0.914062 4.29158 3.48415 1.7215 6.65451 1.7215C9.82487 1.7215 12.3949 4.29158 12.3949 7.46194C12.3949 8.30755 12.2121 9.11045 11.8838 9.83327" stroke="#888888" stroke-width="1.5" stroke-miterlimit="10" />
                                        </svg>
                                    </button>
                                </form>
                            </div>
                        </div>
                    </span>
                    <a class="header__action" href="{% url 'bookmark:summary' %}">
                        <svg xmlns="http://www.w3.org/2000/svg" width="19" height="18" fill="none" viewBox="0 0 19 18">
                            <path fill="none" stroke-miterlimit="10" stroke-width="1.5" d="M9.107 5.965a4.147 4.147 0 1 1 8.29 0v.224c-.2 5.734-8.29 10.339-8.29 10.339S1.037 11.923.827 6.192v-.225a4.147 4.147 0 0 1 6.594-3.344" />
                        </svg>
                    </a>
                    <span class="cart-link header__action">
                        <a class="cart-link__inner" href="{% url 'cart:summary' %}">
                            <svg xmlns="http://www.w3.org/2000/svg" width="22" height="17" fill="none" viewBox="0 0 22 17">
                                <path fill="none" stroke-linejoin="round" stroke-width="1.5" d="M.927.721c.433.382.729.884.843 1.434L3.974 12.71M1.9 2.777h16.265c.397 0 .788.085 1.144.25.356.165.667.405.91.702.242.297.41.642.489 1.01a2.33 2.33 0 0 1-.032 1.11l-1.412 4.97a1.398 1.398 0 0 1-.528.759c-.26.19-.58.293-.908.293H7.777" />
                                <path fill="none" stroke-miterlimit="10" stroke-width="1.5" d="M3.974 12.71c.11.53.411 1.006.852 1.35.44.342.993.53 1.564.53h12.418" />
                                <path fill="none" stroke-miterlimit="10" stroke-width="1.5" d="M10.034 14.583a1.52 1.52 0 0 1-.11.629c-.08.2-.203.383-.36.538a1.692 1.692 0 0 1-.555.361 1.77 1.77 0 0 1-1.32 0 1.692 1.692 0 0 1-.554-.361 1.588 1.588 0 0 1-.361-.538 1.52 1.52 0 0 1-.11-.629m10.446 0a1.542 1.542 0 0 1-.472 1.167 1.692 1.692 0 0 1-.554.361 1.77 1.77 0 0 1-1.32 0 1.692 1.692 0 0 1-.554-.361 1.588 1.588 0 0 1-.362-.538 1.519 1.519 0 0 1-.11-.629" />
                            </svg>

                            <span class="cart-link__counter cart-counter">
                                <!-- {{ cart|length }} -->
                            </span>
                        </a>

                        <div class="cart-popup cart-link__popup">
                            <div class="cart-popup__inner">
                                <button class="cart-popup__closer" type="button">
                                    <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 32 32">
                                        <path fill="#000" d="M17.459,16.014l8.239-8.194c0.395-0.391,0.395-1.024,0-1.414c-0.394-0.391-1.034-0.391-1.428,0  l-8.232,8.187L7.73,6.284c-0.394-0.395-1.034-0.395-1.428,0c-0.394,0.396-0.394,1.037,0,1.432l8.302,8.303l-8.332,8.286  c-0.394,0.391-0.394,1.024,0,1.414c0.394,0.391,1.034,0.391,1.428,0l8.325-8.279l8.275,8.276c0.394,0.395,1.034,0.395,1.428,0  c0.394-0.396,0.394-1.037,0-1.432L17.459,16.014z" />
                                    </svg>
                                </button>
                                <div class="cart-popup__title">
                                    Корзина
                                </div>

                                <div class="cart-items">
                                    <ul class="cart-items__list cart-popup__items {% if cart|length == 0 %}empty{% endif %}">
                                        <!-- {% for item in cart %}
                                            {% include 'cart/_item.html' with item=item %}
                                        {% endfor %} -->
                                    </ul>

                                    <!-- <div class="cart-items__summary">
                                        Подытог: <span class="cart-items__total cart-total-price">{{ cart.total_price }}</span> ₽
                                    </div> -->

                                    <!-- <a class="btn btn--gray cart-items__link" href="{% url 'orders:checkout' %}">
                                        Оформление Заказа
                                    </a> -->

                                    <div class="cart-items__msg">
                                        Корзина пуста.
                                    </div>
                                </div>
                            </div>
                        </div>
                    </span>
                </div>
            </div>
        </div>
    </header>
</template>

<script>
    import SiteSocials from "@/components/SiteSocials.vue";
    import SiteNav from "@/components/SiteNav.vue";

    export default {
        name: "PageHeader",

        components: {
            SiteSocials,
            SiteNav,
        },

        props: {},
    };
</script>

<style lang="scss" scoped>
    .header {
        &__top,
        &__bottom {
            border-bottom: 1px solid rgba(136, 136, 136, 0.3);
        }

        &__top {
            font-size: 13px;
            line-height: 16px;

            color: #767676;
        }

        &__top-container {
            display: flex;
            align-items: center;
            padding-top: 8px;
            padding-bottom: 7px;
        }

        &__bottom-container {
            display: flex;
            align-items: center;
            padding-top: 11px;
            padding-bottom: 10px;
        }

        &__address {
            margin-left: 33px;
        }

        &__mail {
            margin-right: 42px;
            margin-left: auto;
        }

        &__phone {
            margin-right: 12px;
        }

        &__btn {
            margin-right: 42px;
            padding: 0;
            border: none;
            border-bottom: 1px solid rgba(136, 136, 136, 0.3);

            background-image: none;
            color: inherit;
            cursor: pointer;
        }

        &__logo {
            margin-right: 30px;
        }

        &__actions {
            display: flex;
            align-items: center;
            margin-left: auto;
        }

        &__action {
            svg {
                stroke: var(--color-gray);
                fill: var(--color-gray);

                path {
                    transition: stroke 0.3s ease,
                                fill 0.3s ease;
                }
            }

            &:hover svg {
                stroke: var(--color-gold);
                fill: var(--color-gold);
            }

            &:not(:last-child) {
                margin-right: 24px;
            }
        }
    }

    .search-action {
        position: relative;

        &__inner {
            padding: 0;
            border: none;

            background-image: none;
            color: inherit;
            cursor: pointer;
        }

        &__popup {
            position: absolute;
            top: 100%;
            right: 0;
            z-index: 3;
            display: none;

            &.active {
                display: block;
            }
        }
    }

    .search-popup {
        min-width: 300px;
        padding-top: 22px;

        &__inner {
            border: 1px solid #DDD;

            background-color: var(--color-white);
            // background-color: red;
        }
    }

    .search-form {
        display: flex;

        &__field {
            flex-grow: 1;
            padding: 10px;
            border: none;

            outline: none;
            color: var(--color-black);

            font: inherit;
        }

        &__btn {
            position: relative;
            width: 40px;
            height: 40px;
            border: none;

            background-image: none;
            cursor: pointer;

            &::before {
                content: "";
                position: absolute;
                top: 50%;
                left: 0;
                transform: translateY(-50%);
                width: 1px;
                height: 80%;

                background-color: #DDD;
            }
        }
    }

    .cart-popup {
        padding-top: 23px;

        &__inner {
            box-sizing: border-box;
            min-width: 300px;
            padding: 30px 20px 20px 20px;
            border: 1px solid #DDD;

            background-color: var(--color-white);
        }

        &__closer {
            position: absolute;
            top: 40px;
            right: 15px;
            width: 30px;
            height: 30px;
            padding: 0;
            border: none;

            background-image: none;
            color: inherit;
            cursor: pointer;
        }

        &__title {
            margin-bottom: 15px;

            color: #191919;

            font-weight: 600;
            font-size: 17px;
            line-height: 18px;
        }

        &__items {
            margin-right: -20px;
        }
    }

    .cart-link {
        position: relative;

        &__counter {
            position: absolute;
            top: -11px;
            right: -9px;
            min-width: 19px;
            min-height: 19px;

            border-radius: 50%;
            color: var(--color-white);
            background-color: var(--color-gold);

            font-weight: 700;
            font-size: 11px;
            line-height: 19px;
            text-align: center;
        }

        &__popup {
            position: absolute;
            top: calc(100%);
            right: 0;
            z-index: 6;

            opacity: 0;
            visibility: hidden;
            transition: opacity 0.3s ease,
                        visibility 0.3s ease;
        }

        &:hover &__popup {
            opacity: 1;
            visibility: visible;
        }
    }
</style>
