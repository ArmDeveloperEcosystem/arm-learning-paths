(async () => {
  const banner = document.getElementById("ai-sign-in-banner");
  const alertElement = document.getElementById("ai-sign-in-alert");
  if (!banner || !alertElement) return;

  alertElement.addEventListener("visibleChange", (event) => {
    if (event.detail?.visible === false) {
      banner.hidden = true;
    }
  });

  try {
    await initAuth();
    banner.hidden = isUserSignedIn();
  } catch (error) {
    console.warn("Unable to check Arm ID sign-in status:", error);
    banner.hidden = false;
  }
})();
