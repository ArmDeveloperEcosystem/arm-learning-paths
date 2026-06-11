// ----------------------------------------------------------------------
//                 Azure AD B2C Configuration
// ----------------------------------------------------------------------
const POLICY          = "b2c_1a_arm_accounts.susi";
const CLIENT_ID       = "8234ed8a-6728-4a0b-bb7d-b2e5933e581d";
const TENANT_DOMAIN   = "armb2c.onmicrosoft.com";
const TENANT_ID       = "1eb62d43-db15-492b-beab-8a32f6d90351";
const B2C_DOMAIN      = "account.arm.com";

const REDIRECT_URI    = window.location.origin + "/";
//const REDIRECT_URI    = "http://localhost/";
// const REDIRECT_URI = "https://internal.learn.arm.com/"
// const REDIRECT_URI = "https://learn.arm.com/";

const AUTHORITY = `https://${B2C_DOMAIN}/tfp/${TENANT_ID}/${POLICY}/`;
const EXPECTED_ISSUER = `${AUTHORITY}v2.0/`;
const LEGACY_TENANT_ISSUER = `https://${B2C_DOMAIN}/${TENANT_ID}/v2.0/`;
const LEGACY_POLICY_ISSUER = `https://${B2C_DOMAIN}/${TENANT_ID}/${POLICY}/v2.0/`;
const OPENID_CONFIGURATION = `${EXPECTED_ISSUER}.well-known/openid-configuration`;
const ALLOWED_ISSUERS = [
  EXPECTED_ISSUER,
  LEGACY_TENANT_ISSUER,
  LEGACY_POLICY_ISSUER
];

window.msalConfig = {
  auth: {
    clientId: CLIENT_ID,
    authority: AUTHORITY,
    knownAuthorities: [B2C_DOMAIN],      
    redirectUri: REDIRECT_URI,
    postLogoutRedirectUri: REDIRECT_URI
  },
  cache: {
    cacheLocation: "sessionStorage", // Switch to localStorage for better persistence across tabs after testing
    storeAuthStateInCookie: false
  },
  system: {
    allowRedirectInIframe: false,
  }
};

window.loginRequest = {
  authority: AUTHORITY,
  scopes: [
    "openid",
  ]
};

if (!window.msalInstance) {
    window.msalInstance = new msal.PublicClientApplication(window.msalConfig);
}
const msalInstance = window.msalInstance;


// ----------------------------------------------------------------------
//                 Authentication Functions
// ----------------------------------------------------------------------

function ensureDigitalDataRoot() {
  if (!window.digitalData || typeof window.digitalData !== "object") {
    window.digitalData = {};
  }
  return window.digitalData;
}

function clearDigitalDataUser() {
  const digitalData = ensureDigitalDataRoot();
  delete digitalData.user_contact_email;
  delete digitalData.user;
}

function getEmailClaimValue(claims) {
  if (!claims) return undefined;

  const value =
    claims["signInNames.emailAddress"] ||
    claims.email ||
    claims.preferred_username ||
    claims.emails;

  const emailValue = Array.isArray(value) ? value.find(Boolean) : value;
  if (typeof emailValue === "string") {
    return emailValue.trim().toLowerCase();
  }

  return undefined;
}

function getPolicyClaimValue(claims) {
  if (!claims) return undefined;
  return claims.tfp || claims.acr;
}

function isExpectedPolicy(claims) {
  const policy = getPolicyClaimValue(claims);
  return typeof policy === "string" &&
    policy.toLowerCase() === POLICY.toLowerCase();
}

function isExpectedIssuer(claims) {
  return ALLOWED_ISSUERS.includes(claims?.iss);
}

function hasTfpIssuer(claims) {
  return claims?.iss === EXPECTED_ISSUER;
}

function isExpectedB2cClaims(claims) {
  return isExpectedPolicy(claims) && isExpectedIssuer(claims);
}

function logIssuerGap(claims) {
  if (hasTfpIssuer(claims)) return;

  const issuer = claims?.iss || "missing";
  console.warn(
    `B2C token issuer is not TFP-scoped. Expected "${EXPECTED_ISSUER}", received "${issuer}".`
  );
}

function clearUnexpectedPolicyAccount(account, claims) {
  const policy = getPolicyClaimValue(claims) || "missing";
  const issuer = claims?.iss || "missing";
  console.log(`Ignoring B2C account with policy "${policy}" and issuer "${issuer}".`);

  const activeAccount = msalInstance.getActiveAccount();
  if (
    activeAccount &&
    account &&
    activeAccount.homeAccountId === account.homeAccountId
  ) {
    msalInstance.setActiveAccount(null);
  }

  clearDigitalDataUser();
}

async function getIdTokenClaimsForAccount(account) {
  if (!account) return null;

  if (account.idTokenClaims && typeof account.idTokenClaims === "object") {
    return account.idTokenClaims;
  }

  try {
    const tokenResponse = await msalInstance.acquireTokenSilent({
      ...window.loginRequest,
      account
    });
    return tokenResponse?.idTokenClaims || null;
  } catch (error) {
    console.log("Unable to acquire token claims silently:", error);
    return null;
  }
}

async function getValidatedAccount() {
  const account =
    msalInstance.getActiveAccount() ||
    msalInstance.getAllAccounts()[0];

  if (!account) return null;

  const claims = await getIdTokenClaimsForAccount(account);
  if (!claims || !isExpectedB2cClaims(claims)) {
    clearUnexpectedPolicyAccount(account, claims);
    return null;
  }

  logIssuerGap(claims);
  msalInstance.setActiveAccount(account);
  return account;
}

async function updateDigitalDataForCurrentUser() {
  const account = await getValidatedAccount();

  if (!account) {
    clearDigitalDataUser();
    return;
  }

  const claims = await getIdTokenClaimsForAccount(account);
  if (!claims) {
    clearDigitalDataUser();
    return;
  }

  const email = getEmailClaimValue(claims);
  const digitalData = ensureDigitalDataRoot();
  delete digitalData.user_contact_email;
  delete digitalData.user;

  if (email) {
    digitalData.user_contact_email = email;
  }
}

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

        await updateDigitalDataForCurrentUser();
    
        renderAuthInTopNav();
      })().catch((e) => {
        console.log("Auth init failed:", e);
        clearDigitalDataUser();
        renderAuthInTopNav();
      });
    
      return authInitPromise;
}


// Helper function
function getAccount() {
    const accounts = msalInstance.getAllAccounts();
    if (accounts.length) {
      const account = accounts.find((cachedAccount) =>
        isExpectedB2cClaims(cachedAccount.idTokenClaims)
      );
      if (account) {
        msalInstance.setActiveAccount(account);
        return account;
      }
    }
    return null;
}
  


// Access signed-in user data, return it in format ads-top-nav expects
function getSignedInNavData() {
  if (!msalInstance) return null;

  const account = getAccount();

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

  clearDigitalDataUser();
    
  const account = getAccount();
  msalInstance.logoutRedirect({
    account,
    authority: AUTHORITY,
    postLogoutRedirectUri: REDIRECT_URI
  });

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
