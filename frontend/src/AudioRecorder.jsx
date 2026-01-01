import { useRef, useState } from "react";
import { sendAudioBlob } from "./ws";

export default function AudioRecorder() {
  const mediaRecorderRef = useRef(null);
  const [recording, setRecording] = useState(false);

  async function startRecording() {
    const stream = await navigator.mediaDevices.getUserMedia({
      audio: true
    });

    const mediaRecorder = new MediaRecorder(stream, {
      mimeType: "audio/webm"
    });

    mediaRecorderRef.current = mediaRecorder;

    mediaRecorder.ondataavailable = (event) => {
      if (event.data.size > 0) {
        // Send raw Blob directly
        sendAudioBlob(event.data);
      }
    };

    mediaRecorder.start(500);
    setRecording(true);
  }

  function stopRecording() {
    mediaRecorderRef.current?.stop();
    setRecording(false);
  }

  return (
    <div>
      <button onClick={startRecording} disabled={recording}>
        🎙 Start Speaking
      </button>

      <button onClick={stopRecording} disabled={!recording}>
        ⏹ Stop
      </button>
    </div>
  );
}
