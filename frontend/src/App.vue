<template>
    <PageHeader/>

    <router-view/>

    <PageFooter/>

    <!-- <PagePopups/> -->
</template>

<script>
    import PageHeader from "@/components/PageHeader.vue";
    import PageFooter from "@/components/PageFooter.vue";

    export default {
        name: "App",

        components: {
            PageHeader,
            PageFooter,
        },
    };
</script>

<style lang="scss">
    :root {
        --container-side-padding: 15px;
        --container-width: 1170px;
        --container-max-width: calc(var(--container-width) + 2*var(--container-side-padding));

        --color-black: #000;
        --color-gray: #888;
        --color-gold: #AF996B;
        --color-error: #E1372F;
        --color-white: #FFF;
    }

    .page {
        overflow-x: hidden;

        &.locked {
            padding-right: var(--scrollbar-width);
            overflow-y: hidden;

            .fixed {
                padding-right: var(--scrollbar-width);

                @media (max-width: 1200px) {
                    padding-right: 0;
                }
            }
        }

        #app,
        &__body {
            display: flex;
            flex-direction: column;
            min-height: 100vh;
            margin: 0;

            text-rendering: optimizeSpeed;
        }

        &__main {
            flex-grow: 1;
        }
    }

    .page {
        &__body {
            color: var(--color-gray);

            font-family: "Lato";
            font-size: 14px;
            line-height: 17px;
        }

        &__container {
            box-sizing: border-box;
            width: 100%;
            height: 100%;
            max-width: var(--container-max-width);
            margin: 0 auto;
            padding-right: var(--container-side-padding);
            padding-left: var(--container-side-padding);
        }
    }

    .link {
        color: inherit;

        text-decoration: none;

        transition: border-color 0.3s ease,
                    color 0.3s ease;

        &:hover {
            border-color: var(--color-gold);
            color: var(--color-gold);
        }
    }

    .btn {
        box-sizing: border-box;
        border: none;
        outline: none;
        padding: 11px;

        background-image: none;
        color: var(--color-white);
        cursor: pointer;

        font: inherit;
        font-size: 17px;
        line-height: 20px;
        text-align: center;
        text-decoration: none;


        &[disabled] {
            opacity: 0.4;
            cursor: not-allowed;
        }


        &--gold {
            background-color: var(--color-gold);
        }

        &--gray {
            background-color: var(--color-gray);
        }
    }

    .section-header {
        text-align: center;

        &__title {
            margin: 0;

            color: #000000;

            font-size: 32px;
            font-weight: 600;
            line-height: 38px;
        }

        &__subtitle {
            margin-top: 11px;

            color: var(--color-gray);

            font-size: 13px;
            line-height: 16px;
        }
    }
</style>
