(async () => {
  const chatAi = document.getElementById("chat-ai");
  if (!chatAi) return;

  // Plain JavaScript equivalent of React's ref={chatAiRef}.
  window.chatAiRef = chatAi;

  try {
    await initAuth();

    const account = getAccount();
    const claims = await getIdTokenClaimsForAccount(account);
    const email = getEmailClaimValue(claims);

    if (email) {
      chatAi.setAttribute("login-hint", email);
    }
  } catch (error) {
    console.warn("Unable to set the chatbot login hint:", error);
  }
})();
