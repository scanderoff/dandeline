class Typewriter {
    constructor(element, words, wait = 3000) {
        this.element = element;
        this.words = words;
        this.wait = wait;
        this.text = "";
        this.wordIndex = 0;
        this.isDeleting = false;

        this.type();
    }

    type() {
        const index = this.wordIndex % this.words.length;
        const fullText = this.words[index];

        if (this.isDeleting) {
            this.text = fullText.slice(0, this.text.length - 1);
        } else {
            this.text = fullText.slice(0, this.text.length + 1);
        }

        this.element.textContent = this.text;

        let speed = 100;

        if (this.isDeleting) {
            speed *= 0.5;
        }

        if (!this.isDeleting && this.text === fullText) {
            speed = this.wait;

            this.isDeleting = true;
        } else if (this.isDeleting && this.text === "") {
            this.isDeleting = false;

            ++this.wordIndex;

            speed = 500;
        }

        setTimeout(() => this.type(), speed);
    }
}


export default Typewriter;
