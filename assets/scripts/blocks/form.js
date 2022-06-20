class Form {
    constructor(element) {
        this.container = element;
        this.submitBtn = element.querySelector("[type=submit]");

        this.listenEvents();
    }

    listenEvents() {
        this.container.addEventListener("submit", this.onSubmit.bind(this));
        this.container.addEventListener("reset", this.onReset.bind(this));
    }

    onSubmit(event) {
        event.preventDefault();

        const data = new FormData(this.container);

        this.submitBtn.disabled = true;

        fetch("send.php", {
            method: "POST",
            body: data,
        })
            .then(response => response.text())
            .then(result => {
                this.submitBtn.disabled = false;

                if (result !== "Success") {
                    return;
                }


                this.container.reset();
            })
        ;
    }

    onReset(event) {

    }
}


export default Form;
