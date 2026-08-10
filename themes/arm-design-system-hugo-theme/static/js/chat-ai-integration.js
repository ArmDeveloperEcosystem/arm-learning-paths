(async () => {
  try {
    await initAuth();

    const account = getAccount();
    const claims = await getIdTokenClaimsForAccount(account);
    const email = getEmailClaimValue(claims);
    const chatbotApiUrl = atob(window.chatbotApiUrlEncoded || "");

    if (!chatbotApiUrl) {
      throw new Error("HUGO_CHATBOT_API is not configured");
    }

    if (email) {
      // Create and append chat-ai element only after successful auth
      const chatAi = document.createElement("chat-ai");
      chatAi.id = "chat-ai";
      chatAi.setAttribute("theme", "dark");
      chatAi.setAttribute("app-name", "learning-paths");
      chatAi.setAttribute("api-url", chatbotApiUrl);
      chatAi.setAttribute("tnc-url", "https://ipuser.dev.bespin.arm.com/vfae-terms-and-conditions");
      chatAi.setAttribute("stream", "false");
      chatAi.setAttribute("login-hint", email);
      chatAi.setAttribute("redirect-url", window.location.origin + "/");
      chatAi.setAttribute("login-on-load", "true");
      
      document.body.appendChild(chatAi);
      window.chatAiRef = chatAi;
    }
  } catch (error) {
    console.warn("Unable to authenticate:", error);
  }
})();
