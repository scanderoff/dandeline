import noUiSlider from "nouislider";


export default class PriceFilter {
    constructor($el) {
        this.$el = $el;
        this.$priceFrom = $el.querySelector(".price-input__field--from");
        this.$priceTo = $el.querySelector(".price-input__field--to");
        this.$slider = $el.querySelector(".price-slider");

        this.initSlider();
    }

    initSlider() {
        // const params = new URLSearchParams(location.search);

        noUiSlider.create(this.$slider, {
            start: [+this.$priceFrom.value, +this.$priceTo.value],
            connect: true,
            range: {
                "min": 0,
                "max": 10_000,
            },
        });

        this.$slider.noUiSlider.on("update", this.onSliderUpdate.bind(this));
    }

    onSliderUpdate(values) {
        const [priceFrom, priceTo] = values;

        this.$priceFrom.value = Math.trunc(priceFrom);
        this.$priceTo.value = Math.trunc(priceTo);
    }
}
