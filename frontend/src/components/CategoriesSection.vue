<template>
    <section class="categories-section">
        <div class="page__container">
            <div class="section-header recommended-section__header">
                <h2 class="section-header__title">
                    Категории
                </h2>
            </div>

            <div class="categories">
                <ul class="categories__list">
                    <li class="category categories__item">
                        <a class="category__link" href="#">
                            <div class="category-thumb">
                                <img class="category-thumb__image" src="../assets/images/category-thumb/00.jpg" alt="">
                            </div>

                            <div class="category__body">
                                <div class="category__title">
                                    Мужское
                                </div>
                            </div>
                        </a>
                    </li>
                    <li class="category categories__item">
                        <a class="category__link" href="#">
                            <div class="category-thumb">
                                <img class="category-thumb__image" src="../assets/images/category-thumb/01.jpg" alt="">
                            </div>

                            <div class="category__body">
                                <div class="category__title">
                                    Женское
                                </div>
                            </div>
                        </a>
                    </li>
                    <li class="category categories__item">
                        <a class="category__link" href="#">
                            <div class="category-thumb">
                                <img class="category-thumb__image" src="../assets/images/category-thumb/02.jpg" alt="">
                            </div>

                            <div class="category__body">
                                <div class="category__title">
                                    Детское
                                </div>
                            </div>
                        </a>
                    </li>
                </ul>
            </div>
        </div>
    </section>
</template>

<script>
    export default {
        name: "CategoriesSection",
    };
</script>

<style lang="scss" scoped>
    .recommended-section {
        padding: 48px 0 120px;

        background-color: #F8F8F8;

        &__header {
            margin-bottom: 46px;
        }
    }

    .categories-section {
        padding: 25px 0 29px;

        &__header {
            margin-bottom: 22px;
        }
    }

    .categories {
        &__list {
            display: flex;
            flex-wrap: wrap;
            margin: -15px;
            padding: 0;
            list-style: none;
        }

        &__item {
            width: calc(100%*1/3 - 30px);
            margin: 15px;
        }
    }

    .category {
        &__link {
            text-decoration: none;
        }

        &__body {
            display: flex;
            flex-direction: column;
            align-items: flex-start;
        }

        &__title {
            position: relative;

            margin-top: 20px;

            color: var(--color-black);

            font-size: 20px;
            line-height: 24px;

            &::after {
                content: "";
                position: absolute;
                top: 100%;
                left: 0;
                width: 100%;
                height: 2px;
                transform: scaleX(0);
                transform-origin: left center;

                background-color: var(--color-black);

                transition: transform 0.3s ease;
            }
        }

        &:hover &__title {
            &::after {
                transform: scaleX(1);
            }
        }
    }
</style>
