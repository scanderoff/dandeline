<template>
    <footer class="footer">
        <div class="footer__top">
            <div class="footer__top-container page__container">
                <div class="footer__col footer__col--1">
                    <a class="logo" href="{% url 'marketing:homepage' %}">
                        <img class="logo__image" src="../assets/images/logo/logo.svg" alt="Dandeline">
                    </a>

                    <div class="footer__contacts">
                        <div class="footer-contact footer__contact">
                            <svg class="footer-contact__icon" xmlns="http://www.w3.org/2000/svg" width="15" height="21" fill="none" viewBox="0 0 15 21">
                                <path stroke="#000" stroke-miterlimit="10" d="M7.257 19.987a15.529 15.529 0 0 1 1.405-6.233 16.857 16.857 0 0 1 4.861-6.109A6.262 6.262 0 0 0 1 7.65a16.857 16.857 0 0 1 4.862 6.11c.282.617.523 1.253.72 1.903.431 1.402.66 2.858.68 4.324h-.005Z" />
                            </svg>
                            <span class="footer-contact__text">
                                Иркутск, ул. Академика<br>
                                Курчатова 3, офис 406
                            </span>
                        </div>

                        <a class="link footer-contact footer__contact" href="tel:+73952436645">
                            <svg class="footer-contact__icon" xmlns="http://www.w3.org/2000/svg" width="15" height="14" fill="none" viewBox="0 0 15 14">
                                <path stroke="#010101" stroke-miterlimit="10" d="M13.52 12.451a.695.695 0 0 1-.695.695A11.838 11.838 0 0 1 1 1.322a.695.695 0 0 1 .695-.695H4.27a.695.695 0 0 1 .696.695 7.651 7.651 0 0 0 .773 3.403.695.695 0 0 1-.323.934l-1.039.498A9.806 9.806 0 0 0 7.991 9.77l.5-1.037a.706.706 0 0 1 .4-.355.714.714 0 0 1 .534.032 7.677 7.677 0 0 0 3.403.778.696.696 0 0 1 .696.696l-.003 2.568Z" />
                            </svg>
                            <span class="footer-contact__text">
                                +7 3952 43-66-45
                            </span>
                        </a>

                        <a class="link footer-contact footer__contact" href="mailto:info-dandeline@mail.ru">
                            <svg class="footer-contact__icon" xmlns="http://www.w3.org/2000/svg" width="19" height="14" fill="none" viewBox="0 0 19 14">
                                <path stroke="#010101" stroke-miterlimit="10" d="m1.441 1.673 7.82 5.915 7.821-5.915M1.442 12.1l4.4-5.247m11.24 5.247-4.4-5.247M1.916 1.058h14.691c.771 0 1.396.625 1.396 1.396v8.864c0 .771-.625 1.396-1.396 1.396H1.917A1.396 1.396 0 0 1 .52 11.318V2.454c0-.77.625-1.396 1.396-1.396Z" />
                            </svg>
                            <span class="footer-contact__text">
                                info-dandeline@mail.ru
                            </span>
                        </a>
                    </div>
                </div>

                <div class="footer__col footer__col--2">
                    <div class="footer-nav">
                        <div class="footer-title footer-nav__title">
                            Каталог
                        </div>

                        <ul class="footer-nav__list">
                            <li class="footer-nav__item">
                                <a class="link footer-nav__link" href="{% url 'catalog:products' 'мужское' %}">
                                    Мужская
                                </a>
                            </li>
                            <li class="footer-nav__item">
                                <a class="link footer-nav__link" href="{% url 'catalog:products' 'женское' %}">
                                    Женская
                                </a>
                            </li>
                            <li class="footer-nav__item">
                                <a class="link footer-nav__link" href="{% url 'catalog:products' 'детское' %}">
                                    Детская
                                </a>
                            </li>
                        </ul>
                    </div>

                    <div class="footer-nav">
                        <div class="footer-title footer-nav__title">
                            Другое
                        </div>

                        <ul class="footer-nav__list">
                            <li class="footer-nav__item">
                                <a class="link footer-nav__link" href="#">
                                    Акции
                                </a>
                            </li>
                            <li class="footer-nav__item">
                                <a class="link footer-nav__link" href="{% url 'marketing:delivery-and-payment' %}">
                                    Доставка и оплата
                                </a>
                            </li>
                            <li class="footer-nav__item">
                                <a class="link footer-nav__link" href="{% url 'marketing:return' %}">
                                    Возврат
                                </a>
                            </li>
                            <li class="footer-nav__item">
                                <a class="link footer-nav__link" href="{% url 'marketing:about-us' %}">
                                    О нас
                                </a>
                            </li>
                            <li class="footer-nav__item">
                                <a class="link footer-nav__link" href="{% url 'marketing:contact' %}">
                                    Контакты
                                </a>
                            </li>
                        </ul>
                    </div>
                </div>

                <div class="footer__col footer__col--3">
                    <form class="footer-form footer__form">
                        <div class="footer-title footer-form__title">
                            Подписка
                        </div>

                        <div class="footer-form__subtitle">
                            Оставьте ваш E-mail и будьте
                            в курсе новинок нашего каталога.
                        </div>
                        <div class="footer-form__group">
                            <input class="footer-form__field" type="email">

                            <button class="footer-form__btn" type="submit">
                                <svg xmlns="http://www.w3.org/2000/svg" width="27" height="19" fill="none" viewBox="0 0 27 19">
                                    <path fill="#000" d="M23.872 1.203H3.644a1.922 1.922 0 0 0-1.922 1.923V15.33c0 1.061.86 1.922 1.922 1.922h20.228c1.061 0 1.922-.86 1.922-1.922V3.126c0-1.062-.86-1.923-1.922-1.923Z" />
                                    <path stroke="#fff" stroke-miterlimit="10" stroke-width="1.5" d="m2.99 2.05 10.768 8.144 10.767-8.145M2.99 16.407l6.06-7.225m15.477 7.225-6.059-7.225M3.644 1.203h20.228c1.061 0 1.922.861 1.922 1.923V15.33c0 1.061-.86 1.922-1.922 1.922H3.644a1.922 1.922 0 0 1-1.922-1.922V3.126c0-1.062.86-1.923 1.922-1.923Z" />
                                </svg>
                            </button>
                        </div>
                    </form>

                    <SiteSocials/>
                </div>
            </div>
        </div>

        <div class="footer__bottom">
            <div class="footer__bottom-container page__container">
                <div class="footer__col footer__col--1">
                    <a class="link footer__public-offer" href="#">
                        Публичная оферта
                    </a>
                </div>

                <div class="footer__col footer__col--2">
                    <a class="link footer__policy" href="#">
                        Политика конфиденциальности
                    </a>
                </div>

                <div class="footer__col footer__col--3">
                    <div class="footer__payments">
                        <svg xmlns="http://www.w3.org/2000/svg" width="30" height="19" fill="none" viewBox="0 0 30 19">
                            <circle cx="9.128" cy="9.206" r="9.128" fill="#BBB" />
                            <circle cx="20.854" cy="9.206" r="9.128" fill="#E5E5E9" opacity=".8" />
                        </svg>

                        <svg xmlns="http://www.w3.org/2000/svg" width="48" height="16" fill="none" viewBox="0 0 48 16">
                            <path fill="#BBB" d="m19.3 1.088-2.43 14.266h3.888L23.19 1.088H19.3Zm-5.69.017-3.808 9.729-.406-1.47c-.751-1.77-2.883-4.311-5.386-5.913l3.482 11.897 4.114-.007L17.729 1.1l-4.119.004Z" />
                            <path fill="#BBB" d="M7.92 2.125C7.694 1.256 7.039.997 6.226.966H.198l-.05.284c4.69 1.138 7.795 3.88 9.083 7.177L7.92 2.125Zm23.15 1.699a7.178 7.178 0 0 1 2.91.546l.352.165.526-3.092c-.77-.29-1.977-.6-3.483-.6-3.842 0-6.55 1.936-6.571 4.709-.025 2.049 1.929 3.193 3.405 3.876 1.515.7 2.023 1.145 2.016 1.77-.012.955-1.208 1.393-2.325 1.393-1.557 0-2.384-.215-3.661-.747l-.501-.228-.547 3.193c.91.399 2.589.742 4.332.76 4.087 0 6.743-1.912 6.77-4.875.018-1.621-1.02-2.858-3.266-3.873-1.36-.662-2.192-1.102-2.184-1.77 0-.593.706-1.227 2.228-1.227Zm13.766-2.72h-3.004c-.933 0-1.627.254-2.037 1.184l-5.773 13.075h4.083s.666-1.758.817-2.143l4.979.005c.116.498.474 2.138.474 2.138h3.607L44.836 1.104ZM40.041 10.3c.32-.819 1.549-3.987 1.549-3.987-.021.04.317-.825.518-1.362l.262 1.23.901 4.12h-3.23Z" />
                        </svg>
                    </div>
                </div>
            </div>
        </div>
    </footer>
</template>

<script>
    import SiteSocials from "@/components/SiteSocials.vue";

    export default {
        name: "PageFooter",

        components: {
            SiteSocials,
        },

        props: {},
    };
</script>

<style lang="scss" scoped>
    .footer {
        &__top,
        &__bottom {
            border-top: 1px solid rgba(136, 136, 136, 0.3);
        }

        &__top-container {
            display: flex;
            justify-content: space-between;
            padding-top: 42px;
            padding-bottom: 66px;
        }

        &__bottom-container {
            display: flex;
            justify-content: space-between;
            padding-top: 39px;
            padding-bottom: 40px;
        }

        &__bottom {
            color: #BBB;

            font-size: 12px;
            line-height: 14px;
        }

        &__col {
            display: flex;
            align-items: flex-start;

            &--1 {
                flex-direction: column;
                min-width: 230px;
            }

            &--2 {
                justify-content: space-between;
                min-width: 320px;
            }

            &--3 {
                flex-direction: column;
                min-width: 370px;
            }
        }

        &__contacts {
            margin-top: 9px;
            padding-left: 23px;
        }

        &__contact {
            &:not(:last-child) {
                margin-bottom: 20px;
            }
        }

        &__form {
            margin-bottom: 15px;
        }

        &__public-offer {
            margin: 0 auto;
            border-bottom: 1px solid #BBB;
        }

        &__policy {
            border-bottom: 1px solid #BBB;
        }

        &__payments {
            svg:not(:last-child) {
                margin-right: 22px;
            }
        }
    }

    .footer-contact {
        display: flex;
        align-items: center;

        color: #484848;

        font-size: 14px;
        line-height: 17px;

        &__icon {
            flex-shrink: 0;
        }

        &__text {
            margin-left: 16px;
        }
    }

    .footer-nav {
        &__title {
            margin-bottom: 28px;
        }

        &__list {
            margin: 0;
            padding: 0;
            list-style: none;
        }

        &__item {
            &:not(:last-child) {
                margin-bottom: 12px;
            }
        }

        &__link {
            color: #2E2E2E;

            font-size: 14px;
            line-height: 17px;
        }
    }

    .footer-title {
        color: var(--color-black);

        font-size: 15px;
        font-weight: 700;
        line-height: 18px;
    }

    .footer-form {
        &__title {
            margin-bottom: 28px;
        }

        &__subtitle {
            max-width: 200px;
            margin-bottom: 17px;

            color: var(--color-gray);

            font-size: 12px;
            line-height: 16px;
        }

        &__group {
            display: flex;
        }

        &__field {
            box-sizing: border-box;
            min-width: 290px;
            min-height: 45px;
            padding: 10px;
            border: none;

            outline: none;
            background-color: #F0F0F0;
            color: inherit;

            font: inherit;
        }

        &__btn {
            min-width: 70px;
            margin-left: 10px;
            padding: 0;
            border: 3px solid #F0F0F0;

            background-image: none;
            cursor: pointer;
        }
    }
</style>
