(async () => {
  try {
    await initAuth();

    const account = getAccount();
    const claims = await getIdTokenClaimsForAccount(account);
    const email = getEmailClaimValue(claims);

    if (email) {
      // Create and append chat-ai element only after successful auth
      const chatAi = document.createElement("chat-ai");
      chatAi.id = "chat-ai";
      chatAi.setAttribute("app-name", "IPExplorer");
      chatAi.setAttribute("api-url", "http://localhost:5001");
      chatAi.setAttribute("tnc-url", "https://ipuser.dev.bespin.arm.com/vfae-terms-and-conditions");
      chatAi.setAttribute("login-on-load", "true");
      chatAi.setAttribute("stream", "false");
      chatAi.setAttribute("login-hint", email);
      chatAi.setAttribute("redirect-url", window.location.origin + "/");
      
      document.body.appendChild(chatAi);
      window.chatAiRef = chatAi;
    }
  } catch (error) {
    console.warn("Unable to authenticate:", error);
  }
})();
