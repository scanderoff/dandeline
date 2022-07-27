<template>
    <div class="popups">
        <div id="requestPopup" class="popup">
            <form class="request-form popup-window popup__window" action="{% url 'marketing:leave-contact' %}" method="POST" name="requestForm">
                <button class="popup__closer" type="button">
                    <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" fill="none" viewBox="0 0 18 18">
                        <path stroke="#888" stroke-width="1.5" d="m1.153 1.524 15.892 15.892M.99 17.415 16.882 1.523"></path>
                    </svg>
                </button>

                <div class="form__step form__step--default active">
                    <div class="section-header request-form__header">
                        <h6 class="section-header__title">
                            Заказать звонок
                        </h6>
                        <div class="section-header__subtitle">
                            Укажите ваш номер телефона
                            и мы перезвоним в течение 10 минут
                        </div>
                    </div>

                    <label class="input input--2 request-form__input">
                        {{ contact_form.name }}
                    </label>

                    <label class="input input--2 request-form__input">
                        {{ contact_form.phone }}
                    </label>

                    <button class="btn btn--gold request-form__btn" type="submit">
                        Заказать звонок
                    </button>

                    <img class="request-form__image" src="{% static 'images/popup-window/grass.png' %}" alt="Grass">
                </div>

                <div class="form__step form__step--success">
                    <div class="section-header request-form__header">
                        <h6 class="section-header__title">
                            Заявка успешно отправлена
                        </h6>
                        <div class="section-header__subtitle">
                            Ожидайте звонка
                        </div>
                    </div>
                </div>
            </form>
        </div>
    </div>
</template>

<script>
export default {

};
</script>

<style lang="scss" scoped>

</style>
