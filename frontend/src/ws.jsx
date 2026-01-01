let socket = null;

export function connectWS(onMessage) {
  socket = new WebSocket("ws://localhost:8000/ws/chat");

  socket.onopen = () => {
    console.log("WebSocket connected");
  };

  socket.onmessage = (event) => {
    if (onMessage) {
      onMessage(JSON.parse(event.data));
    }
  };

  socket.onerror = (err) => {
    console.error("WebSocket error", err);
  };
}

export function sendAudioBlob(blob) {
  if (!socket || socket.readyState !== WebSocket.OPEN) return;

  socket.send(blob);
}

export function closeWS() {
  if (socket) socket.close();
}
