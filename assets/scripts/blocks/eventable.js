const Eventable = Base => class extends Base {
    _eventListeners = {};

    _emit(eventName) {
        if (!this._eventListeners[eventName]) {
            this._eventListeners[eventName] = new Set();
        }

        for (const eventHandler of this._eventListeners[eventName]) {
            eventHandler(this);
        }
    }

    on(eventName, eventHandler) {
        if (!this._eventListeners[eventName]) {
            this._eventListeners[eventName] = new Set();
        }

        this._eventListeners[eventName].add(eventHandler);
    }

    off(eventName, eventHandler) {
        if (!this._eventListeners[eventName]) {
            return;
        }

        this._eventListeners[eventName].delete(eventHandler);
    }
};


export default Eventable;
