
function toggleIframeFullscreen(button) {
  const container = button.closest(".iframe-container");

  if (document.fullscreenElement) {
    document.exitFullscreen();
  } else {
    container.requestFullscreen();
  }
}

document.addEventListener("fullscreenchange", () => {
  document.querySelectorAll(".iframe-fullscreen-button").forEach(button => {
    const container = button.closest(".iframe-container");

    button.textContent =
      document.fullscreenElement === container
        ? "Exit full screen"
        : "Full screen";
  });
});

