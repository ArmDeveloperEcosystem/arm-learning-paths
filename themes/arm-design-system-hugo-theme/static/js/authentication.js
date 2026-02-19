// ----------------------------------------------------------------------
//                 Azure AD B2C Configuration
// ----------------------------------------------------------------------
const POLICY          = "b2c_1a_arm_accounts.susi";
const CLIENT_ID       = "20ede7b2-aeb1-43d4-81f9-fc1b7fbfca5e";

// Change these in CI/CD pipeline depending on target environment
const TENANT_DOMAIN   = "armb2ctest.onmicrosoft.com";
const TENANT_ID       = "f15a8617-9b4e-41dd-8614-adea42784599";
const B2C_DOMAIN      = "account.arm.com";

const REDIRECT_URI    = window.location.origin + "/";
//const REDIRECT_URI    = "http://localhost/";
// const REDIRECT_URI = "https://internal.learn.arm.com/"
// const REDIRECT_URI = "https://learn.arm.com/";

const AUTHORITY = `https://${B2C_DOMAIN}/tfp/${TENANT_DOMAIN}/${POLICY}/`;

window.msalConfig = {
  auth: {
    clientId: CLIENT_ID,
    authority: AUTHORITY,
    knownAuthorities: [B2C_DOMAIN],      
    redirectUri: REDIRECT_URI,
    postLogoutRedirectUri: REDIRECT_URI,
    navigateToLoginRequestUrl: true 
  },
  cache: {
    cacheLocation: "sessionStorage", // Switch to localStorage for better persistence across tabs after testing
    storeAuthStateInCookie: false
  }
};

window.loginRequest = {
  authority: AUTHORITY,
  scopes: [
    "openid",
    "profile",
    "offline_access",
    `https://${TENANT_DOMAIN}/${CLIENT_ID}/User.Read`
  ]
};

if (!window.msalInstance) {
    window.msalInstance = new msal.PublicClientApplication(window.msalConfig);
}
const msalInstance = window.msalInstance;

function ensureChatAiLoaded() {
  const host = (window.location.hostname || "").toLowerCase();
  const allowedHosts = new Set([
    "localhost",
    "127.0.0.1",
    "internal.learn.arm.com",
    "learn.arm.com"
  ]);
  const isAllowedHost = allowedHosts.has(host);
  const signedIn = isUserSignedIn();
  const existingWidget = document.querySelector("chat-ai");
  const existingScript = document.querySelector("script[data-chat-ai]");

  if (!isAllowedHost || !signedIn) {
    if (existingWidget) {
      existingWidget.remove();
    }
    if (existingScript) {
      existingScript.remove();
    }
    return;
  }

  if (!existingWidget) {
    const widget = document.createElement("chat-ai");
    widget.setAttribute("app-name", "learning-paths");
    widget.setAttribute("redirect-url", `${window.location.origin}/`);
    document.body.appendChild(widget);
  }

  if (!existingScript) {
    const script = document.createElement("script");
    script.src = "https://content.dev.bespin.arm.com/VirtualFAE/learnarm/stage/chat-ai.js";
    script.defer = true;
    script.setAttribute("data-chat-ai", "true");
    document.head.appendChild(script);
  }
}




// ----------------------------------------------------------------------
//                 Authentication Functions
// ----------------------------------------------------------------------

// Auth Init on pageload
let authInitPromise;
async function initAuth() {
    if (authInitPromise) return authInitPromise; // prevent double init on same page
    authInitPromise = (async () => {
        // await msalInstance.initialize(); // recommended in newer msal-browser docs, but we don't have newest version
    
        const result = await msalInstance.handleRedirectPromise(); // safe to call every load
    
        if (result?.account) {
          msalInstance.setActiveAccount(result.account);
        } else {
          getAccount();
        }
    
        renderAuthInTopNav();
        ensureChatAiLoaded();
      })().catch((e) => {
        console.log("Auth init failed:", e);
        renderAuthInTopNav();
        ensureChatAiLoaded();
      });
    
      return authInitPromise;
}


// Helper function
function getAccount() {
    const accounts = msalInstance.getAllAccounts();
    if (accounts.length) {
      // Optional: pick a deterministic account if multiple
      msalInstance.setActiveAccount(accounts[0]);
      return accounts[0];
    }
    return null;
}
  


// Access signed-in user data, return it in format ads-top-nav expects
function getSignedInNavData() {
  if (!msalInstance) return null;

  const account =
    msalInstance.getActiveAccount() ||
    msalInstance.getAllAccounts()[0];

  if (!account) return null;

  const username =
    account.name ||
    account.username ||
    "Signed in";


  return {
    signInUsername: username,
    ctaBtnLogOff: {
      enableCallback: true,
      label: "Log out",
      url: 'https://developer.arm.com/user-logout' 
    }
  };
}


// Site-wide check for signed-in user
function isUserSignedIn() {
  const account = getAccount();
  return account !== null;
}

// UI update to top nav based on auth state (login or logout options)
function renderAuthInTopNav() {

  const topnav = document.querySelector("arm-top-navigation");
  const signInData = getSignedInNavData();
  if (topnav && signInData) {
      // This signInData will now appear in the top navigation when clicking the user icon
      topnav.signIn(signInData);
  }
  else {
     var loginRegisterData = {
      login: {
        title: "Login",
        description: "Login to your account",
        ctaBtn: {
          enableCallback: true,
          label: "Login",
          url: "####",
        },
      },
      register: {
        ctaBtn: {
          enableCallback: false,
          label: "register-label",
          url: "https://developer.arm.com/register",
        },
      },
    };
    topnav.loginRegister(loginRegisterData);
    // Add a message to inform the user about the registration option
    console.log("User is not signed in. Displaying login and registration options.");
  }

}




// ----------------------------------------------------------------------
//                 Auth Callback hooks in top nav
// ----------------------------------------------------------------------
document.addEventListener('arm-account-signout', (event) => {
    var shadowRoot = document.querySelector('arm-top-navigation').shadowRoot;
    if (shadowRoot) {
  
    const signOutButton = shadowRoot.querySelector('.js-signout-btn');
      if (signOutButton) {
        signOutButton.innerHTML = "Logging you out...";
      }
      else {
          console.log("Sign-out button not found in DOM.");
      }
    }
    
  const account = getAccount();
  msalInstance.logoutRedirect({
    account,
    authority: AUTHORITY,
    postLogoutRedirectUri: REDIRECT_URI
  });
  ensureChatAiLoaded();

});

document.addEventListener('arm-account-signin', (event) => {
  
  var shadowRoot = document.querySelector('arm-top-navigation').shadowRoot;
  if (shadowRoot) {

      const signInButton = shadowRoot.querySelector('.c-utility-navigation-login__sign-in-button');
    if (signInButton) {
        signInButton.innerHTML = "Redirecting to login...";
    }
    else {
        console.log("Sign-in button not found in DOM.");
    }
  }


  msalInstance.loginRedirect({   // single-window login
    ...loginRequest
  });
});

document.addEventListener("arm-top-navigation-ready", function (e) {
  // Need to reset theme as arm-top-navigation may override it
  const htmlElement = document.documentElement; 
  htmlElement.setAttribute("theme", "dark"); 

  renderAuthInTopNav();
});



// ----------------------------------------------------------------------
//                 Page Boot
// ----------------------------------------------------------------------
(async () => {
  await initAuth();   // IMPORTANT: await this before user clicks anything

})();
