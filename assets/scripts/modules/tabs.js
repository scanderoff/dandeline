class Tabs {
    constructor(element) {
        this.container = element;
        this.currentIdx = 0;

        this.navBtns = [...element.querySelectorAll(".tabs-nav__btn")];
        this.items = element.querySelectorAll(".tabs__item");

        for (const navBtn of this.navBtns) {
            navBtn.addEventListener("click", this);
        }

        let maxHeight = 0;

        for (const item of this.items) {
            const itemHeight = item.offsetHeight;

            if (itemHeight > maxHeight) {
                maxHeight = itemHeight;
            }
        }

        const list = element.querySelector(".tabs__list");
        list.style.minHeight = `${maxHeight}px`;
    }

    handleEvent(event) {
        this.onBtnClick(event);
    }

    onBtnClick({currentTarget: btn}) {
        if (btn.classList.contains("active")) {
            return;
        }

        const idx = this.navBtns.indexOf(btn);
        const item = this.items[idx];

        this.navBtns[this.currentIdx].classList.remove("active");
        this.items[this.currentIdx].classList.remove("active");

        btn.classList.add("active");
        item?.classList.add("active");

        this.currentIdx = idx;
    }
}


export default Tabs;
