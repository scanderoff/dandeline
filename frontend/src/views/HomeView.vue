<template>
    <main class="page__main">
        <HeroSection/>

        <CategoriesSection/>

        <NewSection/>
    </main>
</template>

<script>
    import HeroSection from "@/components/HeroSection.vue";
    import CategoriesSection from "@/components/CategoriesSection.vue";
    import NewSection from "@/components/NewSection.vue";

    export default {
        name: "HomeView",

        components: {
            HeroSection,
            CategoriesSection,
            NewSection,
        },
    };
</script>
