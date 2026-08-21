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
      chatAi.setAttribute("title", "Arm Virtual Assistant");
      chatAi.setAttribute("current-page", "true");
      chatAi.setAttribute(
        "content",
        `<strong>Discover the right technical content faster</strong><br><br>
         Arm Virtual Assistant helps developers find relevant Learning Paths, tools, and implementation guidance across AI, cloud, and multi-architecture development.<br><br>
         Use of the ARM Virtual FAE is subject to the terms of the <a href="https://ipuser.dev.bespin.arm.com/vfae-terms-and-conditions" target="_blank" rel="noopener noreferrer"><strong>ARM Virtual FAE Terms and Conditions of Use</strong></a>.`
      );
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
