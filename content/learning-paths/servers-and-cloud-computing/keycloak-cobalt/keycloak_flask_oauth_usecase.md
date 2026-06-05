---
title: Integrate Flask OAuth2 application with Keycloak on Azure Cobalt 100
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Integrate Flask OAuth2 application with Keycloak

### Overview

In this section, you'll configure Keycloak realms, users, and OAuth2/OpenID Connect clients, then integrate a Flask application with Keycloak authentication.

You will learn how to:

- Create realms and users
- Configure OpenID Connect clients
- Build a Flask demo application
- Validate OAuth2/OpenID Connect integration
- Test authentication workflows

## Create a realm

Create a dedicated realm for the Flask OAuth2 demo application.

In the Admin Console:

1. Select **Manage Realms**.
2. Select **Create realm**.
3. Enter `demo-realm` as the realm name.
4. Select **Create**.

![Keycloak Create Realm page showing the configuration of the demo-realm on the Azure Cobalt 100 Arm64 virtual machine before creating the new authentication realm.#center](images/create-realm.png "Keycloak Create Realm configuration page")

## Create a user

Create a user in the `demo-realm` for testing OAuth2 authentication.

Navigate to **Users** and select **Create new user**.

Set the username to `testuser` and select **Create**.

After the user is created, navigate to **Credentials** and select **Set password**.

Enter a password of your choice and disable the temporary password setting.

![Keycloak Create User page showing the configuration of the testuser account inside the demo-realm on the Azure Cobalt 100 Arm64 virtual machine.#center](images/create-user.png "Keycloak user creation page for demo-realm")

## Configure OAuth2 login for the Flask application

This section shows how to configure Keycloak as an OAuth2/OpenID Connect provider and build a Flask application that authenticates users through Keycloak.

### Create an OpenID Connect client

Create a Keycloak client for the Flask application.

Navigate to **Clients** and select **Create client**.

In General Settings, enter:

```text
Client type: OpenID Connect
Client ID: flask-demo
```

Under Capability config:

```text
Client authentication: Off
Authorization: Off
```

Under Login settings, set the Valid redirect URI:

```text
http://YOUR_PUBLIC_IP:5000/*
```

Save the client.

![Keycloak Create Client page showing the OpenID Connect client configuration for the Flask OAuth2 demo application running on the Azure Cobalt 100 Arm64 virtual machine.#center](images/create-client.png "Keycloak OpenID Connect client configuration for Flask demo application")

## Create the Flask demo application

Create a project directory for the Flask OAuth2 application.

```bash
mkdir ~/flask-keycloak-demo
cd ~/flask-keycloak-demo
```

### Create a Python virtual environment

Create and activate a Python virtual environment for dependency isolation.

```bash
python3 -m venv venv
```

Activate the virtual environment.

```bash
source venv/bin/activate
```

### Install Flask dependencies

Install Flask and OAuth-related Python packages.

```bash
pip install flask authlib requests
```

### Create the Flask application

Create a Flask application that implements the OAuth2 authorization code flow with PKCE using authlib. The application connects to Keycloak using the OpenID Connect discovery endpoint.

Replace `YOUR_PUBLIC_IP` with the public IP address of your Azure VM.

```bash
cat > app.py <<'EOF'
import os
from flask import Flask, redirect, url_for, session
from authlib.integrations.flask_client import OAuth

app = Flask(__name__)
app.secret_key = os.urandom(24)

KEYCLOAK_URL = os.environ.get('KEYCLOAK_URL', 'http://YOUR_PUBLIC_IP:8080')
REALM = 'demo-realm'

oauth = OAuth(app)
keycloak = oauth.register(
    name='keycloak',
    client_id='flask-demo',
    client_secret=None,
    server_metadata_url=f'{KEYCLOAK_URL}/realms/{REALM}/.well-known/openid-configuration',
    client_kwargs={
        'scope': 'openid email profile',
        'code_challenge_method': 'S256',
    },
)

@app.route('/')
def home():
    user = session.get('user')
    if user:
        return f'Logged in as: {user.get("preferred_username", user.get("sub"))}'
    return '<a href="/login">Log in with Keycloak</a>'

@app.route('/login')
def login():
    redirect_uri = url_for('auth', _external=True)
    return keycloak.authorize_redirect(redirect_uri)

@app.route('/auth')
def auth():
    token = keycloak.authorize_access_token()
    user = token.get('userinfo')
    session['user'] = user
    return redirect(url_for('home'))

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
EOF
```

## Run the Flask application

Start the Flask application with the Keycloak URL pointing to `localhost`. The Flask application connects to Keycloak locally on the VM. The browser redirects use the public IP automatically, because Keycloak's `hostname` setting controls the URLs returned in the discovery document.

```bash
KEYCLOAK_URL=http://localhost:8080 python app.py
```

Open the application in your browser.

```text
http://YOUR_PUBLIC_IP:5000
```

The home page shows a login link. Select the link to be redirected to the Keycloak login page. After authenticating as `testuser`, you are redirected back to the Flask application and the page displays the logged-in username.

```output
Logged in as: testuser
```

![Flask OAuth2 demo application running on port 5000 and successfully authenticating through Keycloak on the Azure Cobalt 100 Arm64 virtual machine, showing the logged-in username after OAuth2 authentication.#center](images/keycloak-demo.png "Flask OAuth2 demo application authenticated through Keycloak")

## Useful commands

Restart Keycloak.

```bash
sudo systemctl restart keycloak
```

View Keycloak logs.

```bash
sudo journalctl -u keycloak -f
```

Check listening ports.

```bash
sudo ss -tulpn | grep -E '8080|9000|5000'
```

## Common troubleshooting

**Admin console stuck loading:**

Recreate temporary directories and restart Keycloak.

```bash
sudo mkdir -p /opt/keycloak/data/tmp
sudo chown -R keycloak:keycloak /opt/keycloak/data
sudo systemctl restart keycloak
```

### Fix HTTPS required error

If the browser shows an HTTPS required error after logging in, disable SSL enforcement for `demo-realm`. Keycloak enables SSL enforcement per realm by default, so you need to apply this fix to each realm you create.

Log in to the Keycloak database.

```bash
sudo -u postgres psql -d keycloak
```

Disable SSL enforcement for `demo-realm`.

```sql
UPDATE realm
SET ssl_required = 'NONE'
WHERE name = 'demo-realm';
```

Exit PostgreSQL.

```sql
\q
```

Restart Keycloak.

```bash
sudo systemctl restart keycloak
```

### PostgreSQL schema permission issue

If logs show:

```text
permission denied for schema public
```

Connect to the Keycloak database and grant the required permissions.

```bash
sudo -u postgres psql -d keycloak
```

```sql
GRANT ALL ON SCHEMA public TO keycloakuser;
ALTER SCHEMA public OWNER TO keycloakuser;
GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO keycloakuser;
GRANT ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA public TO keycloakuser;
```

Exit PostgreSQL.

```sql
\q
```

Restart Keycloak.

```bash
sudo systemctl restart keycloak
```

## What you've learned

You've completed a full OAuth2/OpenID Connect integration on Azure Cobalt 100 Arm64. The Flask application authenticates users through Keycloak using the authorization code flow with PKCE, exchanging authorization codes for access tokens and retrieving user identity from the OpenID Connect userinfo endpoint.

You can build on this foundation by adding role-based access control in Keycloak, integrating additional applications into the same realm, or replacing the database SSL fix with a proper TLS certificate for production deployments.
