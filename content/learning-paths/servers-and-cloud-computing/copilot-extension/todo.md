# TODO

## Tasks by Person

### Joe:

- [ ] copy extension code to new ArmDeveloperEcosystem repo, clean up extension
- [ ] Flask Webapp
- [ ] Deployment

### Avin:

- [ ] Vector Database
- [ ] Configuring with GitHub

## Learning Path flow

- What is a GitHub Copilot Extension
    - What can it do
    - What it can't do (What data is transmitted)
    - Overview of flow (flask app, etc)
- Requirements
    - Install needed developer tools / SDKs 
        - NOTE: Don't mention CDK, will handle in deployment section
        - Python (version?)
        - Python local environment + package install
    - Clone the example repo 
- Walk through the main elements
    - Flask webapp / API
        - oauth2 implementation
        - agent endpoint
        - marketplace endpoint
    - Vector database
        - What is a vector database
        - bin file generation
    - Deployment (AWS only)
        - Disclaimers "There are a lot of ways to run a flask app"
        - CDK Setup / Install
        - Run CDK code
- Configuring with GitHub
    - Creating the extension in UI
    - Create client ID/secret
    - input callback endpoints
    - optional: registering the extension with marketplace