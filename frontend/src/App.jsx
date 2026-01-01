import { useEffect, useState } from "react";
import AudioRecorder from "./AudioRecorder";
import { connectWS } from "./ws";

export default function App() {
  const [messages, setMessages] = useState([]);

  useEffect(() => {
    connectWS((msg) => {
      setMessages((prev) => [...prev, msg]);
    });
  }, []);

  return (
    <div style={{ padding: "2rem" }}>
      <h2>Voice Tutor (Frontend)</h2>

      <AudioRecorder />

      <h3>Messages from Backend</h3>
      <pre>{JSON.stringify(messages, null, 2)}</pre>
    </div>
  );
}
