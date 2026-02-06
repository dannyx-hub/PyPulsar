class PyWebViewAPI {
  constructor() {
    this.eventListeners = {};
    window.addEventListener('pypulsar', this.handleMessage.bind(this));
  }

  async call(eventName, payload = {}) {
    if (!window.pywebview || !window.pywebview.api) {
      throw new Error('pywebview API not available');
    }
    try {
      return await window.pywebview.api.pywebview_message(eventName, payload);
    } catch (err) {
      throw new Error(`API call failed: ${err.message}`);
    }
  }

  on(eventName, callback) {
    if (!this.eventListeners[eventName]) {
      this.eventListeners[eventName] = [];
    }
    this.eventListeners[eventName].push(callback);
  }

  handleMessage(event) {
    const detail = event.detail;
    if (detail && detail.event) {
      const { event: eventName, data } = detail;
      if (this.eventListeners[eventName]) {
        this.eventListeners[eventName].forEach(cb => cb(data));
      }
    }
  }
}

export const api = new PyWebViewAPI();