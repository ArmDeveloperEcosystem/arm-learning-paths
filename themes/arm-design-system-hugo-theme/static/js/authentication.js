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





// ----------------------------------------------------------------------
//                 Authentication Functions
// ----------------------------------------------------------------------

function ensureDigitalDataRoot() {
  if (!window.digitalData || typeof window.digitalData !== "object") {
    window.digitalData = {};
  }
  return window.digitalData;
}

function getFirstClaimValue(claims, keys) {
  if (!claims) return undefined;
  for (const key of keys) {
    const value = claims[key];
    if (value !== undefined && value !== null && value !== "") {
      return value;
    }
  }
  return undefined;
}

function getClaimValueBySuffix(claims, suffixes) {
  if (!claims) return undefined;

  const claimKeys = Object.keys(claims);
  for (const suffix of suffixes) {
    const suffixLower = suffix.toLowerCase();
    const matchedKey = claimKeys.find((key) => key.toLowerCase().endsWith(suffixLower));
    if (matchedKey) {
      const value = claims[matchedKey];
      if (value !== undefined && value !== null && value !== "") {
        return value;
      }
    }
  }

  return undefined;
}

function getEmailClaimValue(claims) {
  const value = getFirstClaimValue(claims, [
    "signInNames.emailAddress",
    "email",
    "preferred_username",
    "emails"
  ]);

  if (Array.isArray(value)) {
    return value.find(Boolean);
  }
  return value;
}

function normalizeToArray(value) {
  if (Array.isArray(value)) return value.filter(Boolean);
  if (typeof value === "string") {
    const trimmed = value.trim();
    if (trimmed.startsWith("[") && trimmed.endsWith("]")) {
      try {
        const parsed = JSON.parse(trimmed);
        if (Array.isArray(parsed)) {
          return parsed.filter(Boolean);
        }
      } catch (error) {
        // Fall through to comma-split parsing.
      }
    }

    // Support comma-separated claim formats and single-value strings.
    return value
      .split(",")
      .map((item) => item.trim())
      .filter(Boolean);
  }
  return undefined;
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

function mapClaimsToDigitalData(claims) {
  const email = getEmailClaimValue(claims);
  const canonicalArmId = getFirstClaimValue(claims, [
    "extension_armId",
    "armId",
    "extension_arm_id",
    "extension_canonical_arm_id"
  ]) || getClaimValueBySuffix(claims, [
    "_armid",
    "_arm_id",
    "_canonical_arm_id"
  ]);
  const adpMemberType = getFirstClaimValue(claims, [
    "extension_adp_member_type",
    "adp_member_type"
  ]) || getClaimValueBySuffix(claims, [
    "_adp_member_type"
  ]);
  const adpMemberStatus = getFirstClaimValue(claims, [
    "extension_adp_member_status",
    "adp_member_status"
  ]) || getClaimValueBySuffix(claims, [
    "_adp_member_status"
  ]);
  const companyName = getFirstClaimValue(claims, [
    "extension_company_name",
    "company_name",
    "companyName"
  ]) || getClaimValueBySuffix(claims, [
    "_company_name",
    "_companyname"
  ]);
  const targetStack = normalizeToArray(
    getFirstClaimValue(claims, [
      "extension_target_stack",
      "target_stack",
      "targetStack"
    ]) || getClaimValueBySuffix(claims, [
      "_target_stack",
      "_targetstack"
    ])
  );
  const targetHardware = normalizeToArray(
    getFirstClaimValue(claims, [
      "extension_target_hardware",
      "target_hardware",
      "targetHardware"
    ]) || getClaimValueBySuffix(claims, [
      "_target_hardware",
      "_targethardware"
    ])
  );
  const developerClassification = getFirstClaimValue(claims, [
    "extension_developer_classification",
    "developer_classification"
  ]) || getClaimValueBySuffix(claims, [
    "_developer_classification"
  ]);
  const jobFunction = getFirstClaimValue(claims, [
    "extension_job_function",
    "job_function"
  ]) || getClaimValueBySuffix(claims, [
    "_job_function"
  ]);
  const jobTitle = getFirstClaimValue(claims, [
    "extension_job_title",
    "job_title"
  ]) || getClaimValueBySuffix(claims, [
    "_job_title"
  ]);

  return {
    user_contact_email: email,
    user: {
      full_name: getFirstClaimValue(claims, [
        "name"
      ]),
      first_name: getFirstClaimValue(claims, [
        "given_name"
      ]),
      last_name: getFirstClaimValue(claims, [
        "family_name"
      ]),
      user_id: "ARM123456",
      adp_member_type: adpMemberType,
      adp_member_status: adpMemberStatus,
      company_name: companyName,
      target_stack: targetStack,
      target_hardware: targetHardware,
      developer_classification: developerClassification,
      job_function: jobFunction,
      job_title: jobTitle
    }
  };
}

function pruneEmptyDigitalDataFields(data) {
  const pruned = {};

  if (data.user_contact_email) {
    pruned.user_contact_email = data.user_contact_email;
  }

  if (data.user && typeof data.user === "object") {
    const user = {};
    Object.entries(data.user).forEach(([key, value]) => {
      if (Array.isArray(value) && value.length > 0) {
        user[key] = value;
      } else if (value !== undefined && value !== null && value !== "") {
        user[key] = value;
      }
    });

    if (Object.keys(user).length > 0) {
      pruned.user = user;
    }
  }

  return pruned;
}

function clearDigitalDataUser() {
  const digitalData = ensureDigitalDataRoot();
  delete digitalData.user_contact_email;
  delete digitalData.user;
}

async function updateDigitalDataForCurrentUser() {
  const account =
    msalInstance.getActiveAccount() ||
    msalInstance.getAllAccounts()[0];

  if (!account) {
    clearDigitalDataUser();
    return;
  }

  const claims = await getIdTokenClaimsForAccount(account);
  if (!claims) {
    clearDigitalDataUser();
    return;
  }

  const mappedData = mapClaimsToDigitalData(claims);
  const prunedData = pruneEmptyDigitalDataFields(mappedData);
  const digitalData = ensureDigitalDataRoot();
  delete digitalData.user_contact_email;
  delete digitalData.user;
  Object.assign(digitalData, prunedData);

  console.log("Auth claims available for analytics mapping:", Object.keys(claims));
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
