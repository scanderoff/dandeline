import ZuckJS from "zuck.js";


let timeIndex = 0;
const shifts = [35, 60, 60*3, 60*60*2, 60*60*25, 60*60*24*4, 60*60*24*10];

function timestamp() {
    const now = new Date();
    const shift = shifts[timeIndex++] || 0;
    const date = new Date( now - shift*1000);

    return date.getTime() / 1000;
}

function initStories() {
    const $stories = document.querySelector(".stories");

    if (!$stories) {
        return;
    }

    const stories = new ZuckJS($stories, {
        skin: "Snapgram",
        openEffect: true,
        reactive: false,
        backNative: true,
        previousTap: true,
        autoFullScreen: false,
        avatars: true,
        list: false,
        cubeEffect: true,
        localStorage: true,

        stories: [
            {
                id: "ramon",
                photo: "https://raw.githubusercontent.com/ramon82/assets/master/zuck.js/users/1.jpg",
                name: "Ramon",
                link: "https://ramon.codes",
                lastUpdated: timestamp(),
                items: [
                    ZuckJS.buildItem("ramon-1", "photo", 3, "https://raw.githubusercontent.com/ramon82/assets/master/zuck.js/stories/1.jpg", "https://raw.githubusercontent.com/ramon82/assets/master/zuck.js/stories/1.jpg", "", false, false, timestamp()),
                    ZuckJS.buildItem("ramon-2", "video", 0, "https://raw.githubusercontent.com/ramon82/assets/master/zuck.js/stories/2.mp4", "https://raw.githubusercontent.com/ramon82/assets/master/zuck.js/stories/2.jpg", "", false,  false, timestamp()),
                    ZuckJS.buildItem("ramon-3", "photo", 3, "https://raw.githubusercontent.com/ramon82/assets/master/zuck.js/stories/3.png", "https://raw.githubusercontent.com/ramon82/assets/master/zuck.js/stories/3.png", "https://ramon.codes", "Visit my Portfolio", false, timestamp())
                ]
            },
            {
                id: "gorillaz",
                photo: "https://raw.githubusercontent.com/ramon82/assets/master/zuck.js/users/2.jpg",
                name: "Gorillaz",
                link: "",
                lastUpdated: timestamp(),
                items: [
                    ZuckJS.buildItem("gorillaz-1", "video", 0, "https://raw.githubusercontent.com/ramon82/assets/master/zuck.js/stories/4.mp4", "https://raw.githubusercontent.com/ramon82/assets/master/zuck.js/stories/4.jpg", "", false, false, timestamp()),
                    ZuckJS.buildItem("gorillaz-2", "photo", 3, "https://raw.githubusercontent.com/ramon82/assets/master/zuck.js/stories/5.jpg", "https://raw.githubusercontent.com/ramon82/assets/master/zuck.js/stories/5.jpg", "", false, false, timestamp()),
                ]
            },
            {
                id: "ladygaga",
                photo: "https://raw.githubusercontent.com/ramon82/assets/master/zuck.js/users/3.jpg",
                name: "Lady Gaga",
                link: "",
                lastUpdated: timestamp(),
                items: [
                    ZuckJS.buildItem("ladygaga-1", "photo", 5, "https://raw.githubusercontent.com/ramon82/assets/master/zuck.js/stories/6.jpg", "https://raw.githubusercontent.com/ramon82/assets/master/zuck.js/stories/6.jpg", "", false, false, timestamp()),
                    ZuckJS.buildItem("ladygaga-2", "photo", 3, "https://raw.githubusercontent.com/ramon82/assets/master/zuck.js/stories/7.jpg", "https://raw.githubusercontent.com/ramon82/assets/master/zuck.js/stories/7.jpg", "http://ladygaga.com", false, false, timestamp()),
                ]
            },
            {
                id: "starboy",
                photo: "https://raw.githubusercontent.com/ramon82/assets/master/zuck.js/users/4.jpg",
                name: "The Weeknd",
                link: "",
                lastUpdated: timestamp(),
                items: [
                    ZuckJS.buildItem("starboy-1", "photo", 5, "https://raw.githubusercontent.com/ramon82/assets/master/zuck.js/stories/8.jpg", "https://raw.githubusercontent.com/ramon82/assets/master/zuck.js/stories/8.jpg", "", false, false, timestamp())
                ]
            },
            {
                id: "riversquomo",
                photo: "https://raw.githubusercontent.com/ramon82/assets/master/zuck.js/users/5.jpg",
                name: "Rivers Cuomo",
                link: "",
                lastUpdated: timestamp(),
                items: [
                    ZuckJS.buildItem("riverscuomo", "photo", 10, "https://raw.githubusercontent.com/ramon82/assets/master/zuck.js/stories/9.jpg", "https://raw.githubusercontent.com/ramon82/assets/master/zuck.js/stories/9.jpg", "", false, false, timestamp())
                ]
            },
            {
                id: "ramon2",
                photo: "https://raw.githubusercontent.com/ramon82/assets/master/zuck.js/users/1.jpg",
                name: "Ramon",
                link: "https://ramon.codes",
                lastUpdated: timestamp(),
                items: [
                    ZuckJS.buildItem("ramon-1", "photo", 3, "https://raw.githubusercontent.com/ramon82/assets/master/zuck.js/stories/1.jpg", "https://raw.githubusercontent.com/ramon82/assets/master/zuck.js/stories/1.jpg", "", false, false, timestamp()),
                    ZuckJS.buildItem("ramon-2", "video", 0, "https://raw.githubusercontent.com/ramon82/assets/master/zuck.js/stories/2.mp4", "https://raw.githubusercontent.com/ramon82/assets/master/zuck.js/stories/2.jpg", "", false,  false, timestamp()),
                    ZuckJS.buildItem("ramon-3", "photo", 3, "https://raw.githubusercontent.com/ramon82/assets/master/zuck.js/stories/3.png", "https://raw.githubusercontent.com/ramon82/assets/master/zuck.js/stories/3.png", "https://ramon.codes", "Visit my Portfolio", false, timestamp())
                ]
            },

            // {
            //     id: "add-review",
            //     photo: "images/stories/add-review.jpg",
            //     name: "Оставьте свой отзыв",
            //     link: "https://vk.com/dandelineshop",
            //     lastUpdated: timestamp(),
            //     items: [],
            // },
        ],
    });
}

export default initStories;
