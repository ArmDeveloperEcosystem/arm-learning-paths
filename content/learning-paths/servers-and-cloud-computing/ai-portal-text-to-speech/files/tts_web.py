#!/usr/bin/env python3
"""FastAPI browser interface for the Qwen3-TTS ONNX cloud example."""

from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
import tempfile
import time
import uuid
from pathlib import Path
from threading import Lock
from typing import Annotated

import uvicorn
from fastapi import FastAPI, File, Form, HTTPException, UploadFile
from fastapi.responses import FileResponse, HTMLResponse


MAX_TEXT_CHARACTERS = 1_000
MAX_UPLOAD_BYTES = 50 * 1024 * 1024
COPY_CHUNK_BYTES = 1024 * 1024


HTML_PAGE = """<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Text-to-Speech Studio</title>
  <style>
    :root {
      color-scheme: light;
      font-family: Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
      color: #172033;
      background: #f3f6f9;
    }
    * { box-sizing: border-box; }
    body {
      margin: 0;
      min-height: 100vh;
      background: linear-gradient(180deg, #f8fafc 0%, #eef3f7 100%);
    }
    main {
      width: min(1040px, calc(100% - 2rem));
      margin: 0 auto;
      padding: 2.5rem 0;
    }
    header {
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 1rem;
      margin-bottom: 1.25rem;
    }
    h1 {
      margin: 0;
      font-size: clamp(1.8rem, 4vw, 2.5rem);
      line-height: 1.1;
      letter-spacing: -0.035em;
    }
    h2 { margin: 0 0 1rem; font-size: 1.05rem; }
    .subtitle { margin: 0.4rem 0 0; color: #596579; }
    .status {
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 0.5rem;
      min-width: 7rem;
      padding: 0.55rem 1rem;
      border: 1px solid #a9dfc0;
      border-radius: 999px;
      color: #17643a;
      background: #eaf8f0;
      font-weight: 700;
    }
    .status::before {
      width: 0.55rem;
      height: 0.55rem;
      border-radius: 50%;
      background: currentColor;
      content: "";
    }
    .status[data-state="working"] {
      border-color: #c4b5fd;
      color: #5b21b6;
      background: #f3efff;
    }
    .status[data-state="error"] {
      border-color: #f3b4b4;
      color: #a61b1b;
      background: #fff0f0;
    }
    .grid {
      display: grid;
      grid-template-columns: minmax(0, 1.15fr) minmax(0, 0.85fr);
      gap: 1rem;
      align-items: start;
    }
    .panel {
      padding: clamp(1.25rem, 3vw, 2rem);
      border: 1px solid #d6dee8;
      border-radius: 0.8rem;
      background: #fff;
      box-shadow: 0 1rem 2.5rem rgb(43 57 78 / 10%);
    }
    label, .field-label {
      display: block;
      margin-bottom: 0.55rem;
      color: #465267;
      font-weight: 700;
    }
    textarea {
      width: 100%;
      min-height: 9rem;
      resize: vertical;
      padding: 1rem;
      border: 1px solid #c9d3df;
      border-radius: 0.5rem;
      color: inherit;
      background: #fff;
      font: inherit;
      line-height: 1.5;
    }
    textarea:focus, input:focus-visible, button:focus-visible, a:focus-visible {
      border-color: #246bfd;
      outline: 3px solid rgb(36 107 253 / 18%);
      outline-offset: 2px;
    }
    .field { margin-top: 1rem; }
    .row, .reference-actions {
      display: flex;
      align-items: center;
      flex-wrap: wrap;
      gap: 0.65rem;
      margin-top: 0.8rem;
    }
    button, .download {
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 0.5rem;
      min-height: 2.65rem;
      padding: 0.7rem 1.1rem;
      border: 0;
      border-radius: 0.45rem;
      color: #fff;
      background: #246bfd;
      font: inherit;
      font-weight: 750;
      text-decoration: none;
      cursor: pointer;
    }
    button svg, .download svg {
      width: 1.05rem;
      height: 1.05rem;
      flex: 0 0 auto;
    }
    button:hover, .download:hover { background: #1858d5; }
    button.secondary {
      border: 1px solid #c9d3df;
      color: #263247;
      background: #fff;
    }
    button.secondary:hover { background: #f3f6f9; }
    button.quiet {
      min-height: 2.25rem;
      padding: 0.45rem 0.7rem;
      border: 1px solid transparent;
      color: #68758a;
      background: transparent;
      font-size: 0.88rem;
    }
    button.quiet:hover {
      border-color: #f1c7c7;
      color: #a61b1b;
      background: #fff5f5;
    }
    .record-button[data-recording="true"] {
      border-color: #f0b7b7;
      color: #a61b1b;
      background: #fff1f1;
    }
    .record-button[data-recording="true"]:hover { background: #ffe8e8; }
    .record-button .stop-icon { display: none; }
    .record-button[data-recording="true"] .microphone-icon { display: none; }
    .record-button[data-recording="true"] .stop-icon { display: block; }
    .recording-time {
      min-width: 2.4rem;
      margin-left: 0.1rem;
      padding-left: 0.55rem;
      border-left: 1px solid #e7b1b1;
      font-variant-numeric: tabular-nums;
    }
    button:disabled { cursor: progress; opacity: 0.62; }
    .generate { width: 100%; margin-top: 1rem; }
    audio { width: 100%; margin-top: 0.5rem; }
    .reference-summary {
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 0.8rem;
      margin-top: 0.9rem;
      padding: 0.85rem;
      border: 1px solid #d8e0e9;
      border-radius: 0.6rem;
      background: #f8fafc;
    }
    .reference-meta {
      display: flex;
      align-items: center;
      min-width: 0;
      gap: 0.7rem;
    }
    .audio-badge {
      display: grid;
      width: 2.35rem;
      height: 2.35rem;
      flex: 0 0 auto;
      place-items: center;
      border-radius: 50%;
      color: #246bfd;
      background: #eaf1ff;
    }
    .audio-badge svg { width: 1.15rem; height: 1.15rem; }
    .reference-copy { min-width: 0; }
    .reference-name {
      display: block;
      overflow: hidden;
      color: #263247;
      font-size: 0.92rem;
      text-overflow: ellipsis;
      white-space: nowrap;
    }
    .reference-detail {
      display: block;
      margin-top: 0.15rem;
      color: #758196;
      font-size: 0.8rem;
    }
    .hint, .metrics {
      color: #68758a;
      font-size: 0.9rem;
      line-height: 1.45;
    }
    .hint { margin: 0.55rem 0 0; }
    .metrics {
      min-height: 4.5rem;
      margin: 1rem 0 0;
      padding: 0.9rem;
      border: 1px solid #d6dee8;
      border-radius: 0.5rem;
      background: #f8fafc;
      white-space: pre-wrap;
    }
    .placeholder {
      display: grid;
      min-height: 10rem;
      place-items: center;
      padding: 1rem;
      border: 1px dashed #c9d3df;
      border-radius: 0.5rem;
      color: #8792a5;
      text-align: center;
    }
    .placeholder svg {
      width: 2.2rem;
      height: 2.2rem;
      margin-bottom: 0.65rem;
      color: #a3adbc;
    }
    .placeholder span { display: block; }
    [hidden] { display: none !important; }
    @media (max-width: 760px) {
      main { padding: 1.25rem 0; }
      header { align-items: flex-start; flex-direction: column; }
      .grid { grid-template-columns: 1fr; }
      .status { min-width: 0; }
    }
  </style>
</head>
<body>
  <main>
    <header>
      <div>
        <h1>Text-to-Speech Studio</h1>
        <p class="subtitle">Qwen3-TTS voice cloning with ONNX Runtime on AWS Graviton</p>
      </div>
      <div class="status" id="status" data-state="ready" role="status">Ready</div>
    </header>

    <div class="grid">
      <section class="panel" aria-labelledby="input-heading">
        <h2 id="input-heading">Create speech</h2>

        <label for="text">Text to synthesize</label>
        <textarea id="text" maxlength="1000" placeholder="Enter the sentence you want spoken...">Hello, this is a voice-cloning test running on AWS Graviton.</textarea>

        <div class="field">
          <div class="field-label">Reference voice</div>
          <input id="reference-file" type="file" accept="audio/*" hidden>
          <div class="reference-actions">
            <button class="secondary" id="upload" type="button">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
                <path d="M12 16V4"></path>
                <path d="m7.5 8.5 4.5-4.5 4.5 4.5"></path>
                <path d="M5 14v4a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2v-4"></path>
              </svg>
              <span>Upload audio</span>
            </button>
            <button class="secondary record-button" id="record" type="button" data-recording="false">
              <svg class="microphone-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
                <rect x="9" y="3" width="6" height="11" rx="3"></rect>
                <path d="M5.5 11.5a6.5 6.5 0 0 0 13 0"></path>
                <path d="M12 18v3"></path>
                <path d="M9 21h6"></path>
              </svg>
              <svg class="stop-icon" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">
                <rect x="6" y="6" width="12" height="12" rx="2"></rect>
              </svg>
              <span id="record-label">Record</span>
              <span class="recording-time" id="recording-time" hidden>0:00</span>
            </button>
          </div>
          <p class="hint">Use a clean recording of one speaker whose permission you have.</p>
          <div class="reference-summary" id="reference-summary" hidden>
            <div class="reference-meta">
              <span class="audio-badge" aria-hidden="true">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round">
                  <path d="M4 13v-2"></path>
                  <path d="M8 17V7"></path>
                  <path d="M12 20V4"></path>
                  <path d="M16 16V8"></path>
                  <path d="M20 13v-2"></path>
                </svg>
              </span>
              <span class="reference-copy">
                <strong class="reference-name" id="reference-name"></strong>
                <span class="reference-detail" id="reference-detail"></span>
              </span>
            </div>
            <button class="quiet" id="discard" type="button" aria-label="Discard reference audio">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
                <path d="M4 7h16"></path>
                <path d="M9 7V4h6v3"></path>
                <path d="m6.5 7 1 13h9l1-13"></path>
                <path d="M10 11v5"></path>
                <path d="M14 11v5"></path>
              </svg>
              <span>Discard</span>
            </button>
          </div>
          <audio id="reference-preview" controls hidden></audio>
        </div>

        <button class="generate" id="generate" type="button">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" aria-hidden="true">
            <path d="M4 13v-2"></path>
            <path d="M8 16V8"></path>
            <path d="M12 19V5"></path>
            <path d="M16 16V8"></path>
            <path d="M20 13v-2"></path>
          </svg>
          <span id="generate-label">Generate speech</span>
        </button>
      </section>

      <section class="panel" aria-labelledby="output-heading">
        <h2 id="output-heading">Generated speech</h2>
        <div class="placeholder" id="placeholder">
          <div>
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
              <path d="M11 5 6 9H3v6h3l5 4V5Z"></path>
              <path d="M15 9.5a4 4 0 0 1 0 5"></path>
              <path d="M18 7a7 7 0 0 1 0 10"></path>
            </svg>
            <span>Your generated audio will appear here.</span>
          </div>
        </div>
        <div id="result" hidden>
          <audio id="output-audio" controls></audio>
          <div class="row">
            <a class="download" id="download" href="#" download="generated_voice.wav">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
                <path d="M12 4v12"></path>
                <path d="m7.5 11.5 4.5 4.5 4.5-4.5"></path>
                <path d="M5 20h14"></path>
              </svg>
              <span>Download WAV</span>
            </a>
          </div>
        </div>
        <p class="metrics" id="metrics" aria-live="polite">Ready for text and a reference recording.</p>
      </section>
    </div>
  </main>

  <script>
    const textInput = document.querySelector("#text");
    const fileInput = document.querySelector("#reference-file");
    const uploadButton = document.querySelector("#upload");
    const recordButton = document.querySelector("#record");
    const recordLabel = document.querySelector("#record-label");
    const recordingTime = document.querySelector("#recording-time");
    const discardButton = document.querySelector("#discard");
    const generateButton = document.querySelector("#generate");
    const generateLabel = document.querySelector("#generate-label");
    const referenceSummary = document.querySelector("#reference-summary");
    const referenceName = document.querySelector("#reference-name");
    const referenceDetail = document.querySelector("#reference-detail");
    const referencePreview = document.querySelector("#reference-preview");
    const outputAudio = document.querySelector("#output-audio");
    const downloadLink = document.querySelector("#download");
    const placeholder = document.querySelector("#placeholder");
    const resultPanel = document.querySelector("#result");
    const status = document.querySelector("#status");
    const metrics = document.querySelector("#metrics");

    let referenceFile = null;
    let referenceUrl = null;
    let outputUrl = null;
    let recorder = null;
    let recordingStream = null;
    let recordingChunks = [];
    let recordingInterval = null;
    let recordingStartedAt = 0;
    let generating = false;

    function setStatus(label, state) {
      status.textContent = label;
      status.dataset.state = state;
    }

    function isRecording() {
      return recorder && recorder.state === "recording";
    }

    function updateControls() {
      const recording = isRecording();
      generateButton.disabled = generating || recording;
      uploadButton.disabled = generating || recording;
      recordButton.disabled = generating;
      discardButton.disabled = generating || recording;
      fileInput.disabled = generating || recording;
      generateLabel.textContent = generating ? "Generating..." : "Generate speech";
    }

    function setBusy(busy) {
      generating = busy;
      updateControls();
    }

    function formatFileSize(bytes) {
      if (bytes < 1024 * 1024) return Math.max(1, Math.round(bytes / 1024)) + " KB";
      return (bytes / (1024 * 1024)).toFixed(1) + " MB";
    }

    function formatRecordingTime() {
      const seconds = Math.floor((Date.now() - recordingStartedAt) / 1000);
      const minutes = Math.floor(seconds / 60);
      return minutes + ":" + String(seconds % 60).padStart(2, "0");
    }

    function stopRecordingTimer() {
      if (recordingInterval) clearInterval(recordingInterval);
      recordingInterval = null;
      recordingTime.hidden = true;
      recordingTime.textContent = "0:00";
      recordButton.dataset.recording = "false";
      recordLabel.textContent = "Record";
    }

    function stopRecordingStream() {
      if (recordingStream) {
        recordingStream.getTracks().forEach(track => track.stop());
        recordingStream = null;
      }
    }

    function selectReference(file, source) {
      referenceFile = file;
      referenceName.textContent = file.name;
      referenceDetail.textContent = source + " - " + formatFileSize(file.size);
      if (referenceUrl) URL.revokeObjectURL(referenceUrl);
      referenceUrl = URL.createObjectURL(file);
      referencePreview.src = referenceUrl;
      referencePreview.hidden = false;
      referenceSummary.hidden = false;
      setStatus("Ready", "ready");
    }

    function discardReference() {
      referenceFile = null;
      fileInput.value = "";
      if (referenceUrl) URL.revokeObjectURL(referenceUrl);
      referenceUrl = null;
      referencePreview.pause();
      referencePreview.removeAttribute("src");
      referencePreview.load();
      referencePreview.hidden = true;
      referenceSummary.hidden = true;
      referenceName.textContent = "";
      referenceDetail.textContent = "";
      metrics.textContent = "Ready for text and a reference recording.";
      setStatus("Ready", "ready");
    }

    uploadButton.addEventListener("click", () => fileInput.click());

    fileInput.addEventListener("change", () => {
      if (fileInput.files && fileInput.files[0]) {
        selectReference(fileInput.files[0], "Uploaded audio");
      }
    });

    discardButton.addEventListener("click", discardReference);

    recordButton.addEventListener("click", async () => {
      if (isRecording()) {
        recorder.stop();
        return;
      }

      if (!navigator.mediaDevices || !window.MediaRecorder) {
        metrics.textContent = "Browser recording is unavailable. Upload an audio file instead.";
        setStatus("Error", "error");
        return;
      }

      try {
        recordingStream = await navigator.mediaDevices.getUserMedia({audio: true});
        recordingChunks = [];
        recorder = new MediaRecorder(recordingStream);
        recorder.addEventListener("dataavailable", event => {
          if (event.data.size > 0) recordingChunks.push(event.data);
        });
        recorder.addEventListener("stop", () => {
          const mimeType = recorder.mimeType || "audio/webm";
          const extension = mimeType.includes("ogg") ? "ogg" : "webm";
          const blob = new Blob(recordingChunks, {type: mimeType});
          selectReference(
            new File([blob], "browser_reference." + extension, {type: mimeType}),
            "Browser recording"
          );
          stopRecordingStream();
          stopRecordingTimer();
          recorder = null;
          updateControls();
          metrics.textContent = "Recording ready. Select Generate speech when you are ready.";
        });
        recorder.start();
        recordingStartedAt = Date.now();
        recordingTime.textContent = "0:00";
        recordingTime.hidden = false;
        recordButton.dataset.recording = "true";
        recordLabel.textContent = "Stop";
        recordingInterval = setInterval(() => {
          recordingTime.textContent = formatRecordingTime();
        }, 250);
        updateControls();
        metrics.textContent = "Recording reference audio...";
        setStatus("Recording", "working");
      } catch (error) {
        stopRecordingStream();
        stopRecordingTimer();
        recorder = null;
        updateControls();
        metrics.textContent = "Microphone access failed: " + error.message;
        setStatus("Error", "error");
      }
    });

    async function readError(response) {
      try {
        const body = await response.json();
        return body.detail || "Generation failed.";
      } catch {
        return await response.text() || "Generation failed.";
      }
    }

    generateButton.addEventListener("click", async () => {
      const text = textInput.value.trim();
      if (!text) {
        textInput.focus();
        setStatus("Enter text", "error");
        return;
      }
      if (!referenceFile) {
        uploadButton.focus();
        setStatus("Add a voice", "error");
        return;
      }

      const form = new FormData();
      form.append("text", text);
      form.append("reference_audio", referenceFile, referenceFile.name);

      setBusy(true);
      setStatus("Generating", "working");
      metrics.textContent = "The ONNX cascade is generating speech. This can take several minutes.";

      try {
        const response = await fetch("/generate", {method: "POST", body: form});
        if (!response.ok) throw new Error(await readError(response));

        const audioBlob = await response.blob();
        if (outputUrl) URL.revokeObjectURL(outputUrl);
        outputUrl = URL.createObjectURL(audioBlob);
        outputAudio.src = outputUrl;
        downloadLink.href = outputUrl;
        placeholder.hidden = true;
        resultPanel.hidden = false;

        const seconds = response.headers.get("X-Generation-Seconds");
        metrics.textContent = seconds
          ? "Generation completed in " + Number(seconds).toFixed(1) + " seconds."
          : "Generation completed.";
        setStatus("Ready", "ready");
      } catch (error) {
        metrics.textContent = "Request failed: " + error.message;
        setStatus("Error", "error");
      } finally {
        setBusy(false);
      }
    });
  </script>
</body>
</html>
"""


class Qwen3OnnxAdapter:
    """Translate the web request into the supplied Qwen3-TTS runner command."""

    def __init__(self, model_dir: Path, threads: int) -> None:
        self.model_dir = model_dir.resolve()
        self.threads = threads
        self.runner_path = self.model_dir / "onnx_tts_runner.py"
        self.ffmpeg = shutil.which("ffmpeg")

    def validate(self) -> None:
        required = [
            self.runner_path,
            self.model_dir / "onnx_cascade_driver.py",
            self.model_dir / "text_path_config.json",
            self.model_dir / "text_path_weights.npz",
        ]
        missing = [path.name for path in required if not path.is_file()]
        if missing:
            raise FileNotFoundError(
                "The model directory is missing: " + ", ".join(missing)
            )
        if self.ffmpeg is None:
            raise FileNotFoundError(
                "ffmpeg was not found. Install it with: sudo apt install ffmpeg"
            )
        if self.threads < 1:
            raise ValueError("--threads must be at least 1")

    def normalize_reference(self, source: Path, destination: Path) -> None:
        result = subprocess.run(
            [
                self.ffmpeg,
                "-nostdin",
                "-hide_banner",
                "-loglevel",
                "error",
                "-y",
                "-i",
                str(source),
                "-ac",
                "1",
                "-ar",
                "24000",
                str(destination),
            ],
            capture_output=True,
            text=True,
        )
        if result.returncode != 0:
            detail = (result.stderr or result.stdout or "Unsupported audio file").strip()
            raise ValueError("Reference-audio conversion failed: " + detail[-1200:])

    def synthesize(self, text: str, reference_wav: Path, output_wav: Path) -> None:
        result = subprocess.run(
            [
                sys.executable,
                str(self.runner_path),
                "--text",
                text,
                "--ref-audio",
                str(reference_wav),
                "--out",
                str(output_wav),
                "--intra-op-threads",
                str(self.threads),
            ],
            cwd=self.model_dir,
            capture_output=True,
            text=True,
        )
        if result.returncode != 0:
            detail = (result.stderr or result.stdout or "Unknown runner error").strip()
            raise RuntimeError("Speech generation failed: " + detail[-3000:])
        if not output_wav.is_file():
            raise RuntimeError("The runner completed without creating the output WAV file.")


def copy_upload(upload: UploadFile, destination: Path) -> None:
    written = 0
    with destination.open("wb") as output:
        while True:
            chunk = upload.file.read(COPY_CHUNK_BYTES)
            if not chunk:
                break
            written += len(chunk)
            if written > MAX_UPLOAD_BYTES:
                raise HTTPException(
                    status_code=413,
                    detail="The reference recording must be smaller than 50 MB.",
                )
            output.write(chunk)
    if written == 0:
        raise HTTPException(status_code=400, detail="The reference recording is empty.")


def prune_outputs(output_dir: Path, keep: int = 20) -> None:
    outputs = sorted(
        output_dir.glob("speech_*.wav"),
        key=lambda path: path.stat().st_mtime,
        reverse=True,
    )
    for old_output in outputs[keep:]:
        old_output.unlink(missing_ok=True)


def create_app(adapter: Qwen3OnnxAdapter) -> FastAPI:
    app = FastAPI(title="Text-to-Speech Studio")
    generation_lock = Lock()
    output_dir = adapter.model_dir / "web_outputs"
    output_dir.mkdir(exist_ok=True)

    @app.get("/", response_class=HTMLResponse)
    def index() -> str:
        return HTML_PAGE

    @app.post("/generate", response_class=FileResponse)
    def generate(
        text: Annotated[str, Form()],
        reference_audio: Annotated[UploadFile, File()],
    ) -> FileResponse:
        text = text.strip()
        if not text:
            raise HTTPException(status_code=400, detail="Enter text to synthesize.")
        if len(text) > MAX_TEXT_CHARACTERS:
            raise HTTPException(
                status_code=400,
                detail="Keep the text under 1,000 characters.",
            )
        if not generation_lock.acquire(blocking=False):
            raise HTTPException(
                status_code=409,
                detail="Another generation is already running. Try again when it finishes.",
            )

        try:
            suffix = Path(reference_audio.filename or "").suffix.lower()
            if not suffix or len(suffix) > 10:
                suffix = ".audio"

            with tempfile.TemporaryDirectory(
                prefix="tts_request_",
                dir=output_dir,
            ) as temporary_directory:
                temporary = Path(temporary_directory)
                uploaded_audio = temporary / ("reference" + suffix)
                normalized_wav = temporary / "reference_24khz.wav"
                copy_upload(reference_audio, uploaded_audio)

                try:
                    adapter.normalize_reference(uploaded_audio, normalized_wav)
                except ValueError as error:
                    raise HTTPException(status_code=400, detail=str(error)) from error

                output_wav = output_dir / ("speech_" + uuid.uuid4().hex + ".wav")
                start = time.perf_counter()
                try:
                    adapter.synthesize(text, normalized_wav, output_wav)
                except RuntimeError as error:
                    raise HTTPException(status_code=500, detail=str(error)) from error
                elapsed = time.perf_counter() - start

            prune_outputs(output_dir)
            return FileResponse(
                output_wav,
                media_type="audio/wav",
                filename="generated_voice.wav",
                headers={"X-Generation-Seconds": f"{elapsed:.3f}"},
            )
        finally:
            generation_lock.release()

    return app


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Serve the Qwen3-TTS ONNX example through FastAPI."
    )
    parser.add_argument(
        "--model-dir",
        type=Path,
        default=Path.cwd(),
        help="Directory containing onnx_tts_runner.py and the ONNX model package",
    )
    parser.add_argument("--threads", type=int, default=4)
    parser.add_argument("--host", default="127.0.0.1")
    parser.add_argument("--port", type=int, default=8000)
    args = parser.parse_args()

    adapter = Qwen3OnnxAdapter(args.model_dir, args.threads)
    adapter.validate()
    uvicorn.run(create_app(adapter), host=args.host, port=args.port)


if __name__ == "__main__":
    main()
