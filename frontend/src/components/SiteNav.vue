<template>
    <nav class="nav">
        <ul class="nav__list">
            <li class="nav-item nav__item">
                <!-- <a class="nav-item__link" href="{% url 'catalog:products' %}">
                    <span>Каталог</span>
                    {% if categories %}
                        <svg class="nav-item__icon" xmlns="http://www.w3.org/2000/svg" width="11" height="6" fill="none" viewBox="0 0 11 6">
                            <path stroke-linecap="round" stroke-linejoin="round" d="m1.396.937 4.456 4.385L10.31.937" />
                        </svg>
                    {% endif %}
                </a> -->

                <!-- {% if categories %}
                    <div class="subnav nav-item__subnav">
                        <ul class="subnav__list">
                            {% recursetree categories %}
                                <li class="subnav-item subnav__item">
                                    <a class="subnav-item__link" href="{{ node.get_absolute_url }}">
                                        <span>{{ node.name }}</span>

                                        {% if not node.is_leaf_node %}
                                            <svg class="subnav-item__icon" width="11" height="6" viewBox="0 0 11 6" fill="none" xmlns="http://www.w3.org/2000/svg">
                                                <path d="M1.39661 0.936523L5.85261 5.32223L10.3104 0.936523" stroke-linecap="round" stroke-linejoin="round" />
                                            </svg>
                                        {% endif %}
                                    </a>

                                    {% if not node.is_leaf_node %}
                                        <div class="subnav subnav-item__subnav">
                                            <ul class="subnav__list">
                                                {{ children }}
                                            </ul>
                                        </div>
                                    {% endif %}
                                </li>
                            {% endrecursetree %}
                        </ul>
                    </div>
                {% endif %} -->
            </li>

            <li class="nav-item nav__item">
                <a class="nav-item__link" href="{% url 'marketing:delivery-and-payment' %}">
                    Доставка и оплата
                </a>
            </li>

            <li class="nav-item nav__item">
                <a class="nav-item__link" href="{% url 'marketing:return' %}">
                    Возврат
                </a>
            </li>

            <li class="nav-item nav__item">
                <router-link to="/about" class="nav-item__link">
                    О нас
                </router-link>
            </li>

            <li class="nav-item nav__item">
                <a class="nav-item__link" href="{% url 'marketing:contact' %}">
                    Контакты
                </a>
            </li>
        </ul>
    </nav>
</template>

<script>
    export default {
        name: "SiteNav",
    };
</script>

<style lang="scss" scoped>
    .nav {
        padding-left: 30px;
        border-left: 1px solid var(--color-gold);

        &__list {
            min-height: 38px;
            margin: 0;
            padding: 0;
            display: flex;
            align-items: center;
            list-style: none;
        }

        &__item {
            &:not(:last-child) {
                margin-right: 40px;
            }
        }
    }

    .nav-item {
        position: relative;

        &__link {
            position: relative;
            display: inline-block;
            padding: 3px 0;

            color: #2E2E2E;
            transition: color 0.3s ease;

            font-size: 13px;
            line-height: 16px;
            text-decoration: none;

            &::before,
            &::after {
                content: "";
                position: absolute;
                width: 100%;
                height: 1px;

                background-color: var(--color-gold);
                transform: scaleX(0);
                transition: transform 0.3s ease;
            }

            &::before {
                top: 0;
                left: 0;
                transform-origin: left center;
            }

            &::after {
                bottom: 0;
                right: 0;
                transform-origin: right center;
            }
        }

        &:hover > &__link {
            color: var(--color-gold);

            &::before,
            &::after {
                transform: scaleX(1);
            }
        }


        &__icon {
            margin-top: -2px;

            stroke: var(--color-gray);
            transition: transform 0.3s ease;
        }

        &:hover > &__link &__icon {
            stroke: var(--color-gold);
            transform: rotateZ(180deg);
        }


        &__subnav {
            position: absolute;
            top: 100%;
            left: -20px;
            z-index: 6;

            opacity: 0;
            visibility: hidden;
            transition: opacity 0.3s ease,
                        visibility 0.3s ease;
        }

        &:hover > &__subnav {
            opacity: 1;
            visibility: visible;
        }
    }
</style>
