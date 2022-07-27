<template>
    <section class="new-section">
        <div class="page__container">
            <div class="section-header new-section__header">
                <h2 class="section-header__title">
                    Новинки
                </h2>
            </div>

            <div class="products">
                <ul class="products__list products__list--4-cols">
                    {% include 'catalog/_product_loop.html' with products=new_products %}
                </ul>

                <div class="products__actions">
                    <a class="btn btn--gold products__more-link" href="{% url 'catalog:products' %}">
                        Больше
                    </a>
                </div>
            </div>
        </div>
    </section>
</template>

<script>
    export default {
        name: "NewSection",
    };
</script>

<style lang="scss" scoped>
    .new-section {
        padding: 29px 0 50px;

        &__header {
            margin-bottom: 38px;
        }
    }
</style>
