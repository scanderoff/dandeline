<template>
    <section class="content">
        <div class="content__container page__container">
            <div class="section-header">
                <h1 class="section-header__title">
                    {{ heading }}
                </h1>
            </div>

            {% if ancestors is not None %}
                <div class="breadcrumbs content__breadcrumbs">
                    <ul class="breadcrumbs__list">
                        <li class="breadcrumbs__item">
                            <a class="breadcrumbs__link" href="{% url 'marketing:homepage' %}">
                                Главная
                            </a>
                        </li>
                        {% for category in ancestors %}
                            <li class="breadcrumbs__item">
                                {% if not forloop.last %}
                                    <a class="breadcrumbs__link" href="{{ category.get_absolute_url }}">
                                        {{ category.name }}
                                    </a>
                                {% else %}
                                    <span class="breadcrumbs__link">
                                        {{ category.name }}
                                    </span>
                                {% endif %}
                            </li>
                        {% empty %}
                            <li class="breadcrumbs__item">
                                <a class="breadcrumbs__link" href="{% url 'catalog:products' %}">
                                    Каталог
                                </a>
                            </li>
                        {% endfor %}
                    </ul>
                </div>
            {% endif %}

            <div v-if="messages" class="messages content__messages">
                <ul class="messages__list">
                    <li
                        v-for="(message, index) in messages"
                        :key="index"
                        class="message messages__item"
                    >
                        {{ message }}
                    </li>
                </ul>
            </div>

            <div class="content__wrapper">
                {% block sidebar %}{% endblock %}

                <div class="content__inner">
                    {% block content %}{% endblock %}
                </div>
            </div>
        </div>
    </section>
</template>

<script>
    export default {
        name: "ContentSection",

        props: {
            heading: {
                type: String,
                required: true,
            },

            messages: {
                type: Array,
                required: false,
            },
        },
    };
</script>

<style lang="scss" scoped></style>
