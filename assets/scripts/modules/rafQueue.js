class RafQueue {
    static instance = null;

    container = new Set();
    requestId = 0;

    constructor() {
        if (RafQueue.instance) {
            return RafQueue.instance;
        }

        RafQueue.instance = this;
    }

    enqueue(callback) {
        this.container.add(callback);

        if (this.requestId === 0) {
            this.run();
        }
    }

    dequeue(callback) {
        this.container.delete(callback);

        if (this.container.size === 0) {
            this.stop();
        }
    }

    run() {
        const loop = (now) => {
            for (const callback of this.container) {
                callback(now);
            }

            this.requestId = requestAnimationFrame(loop);
        };

        this.requestId = requestAnimationFrame(loop);
    }

    stop() {
        cancelAnimationFrame(this.requestId);
        this.requestId = 0;
    }
}


export default new RafQueue();
