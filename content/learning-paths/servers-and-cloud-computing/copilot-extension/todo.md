# TODO

## Tasks by Person

### Joe:

- [x] copy extension code to new ArmDeveloperEcosystem repo, clean up extension
- [ ] Flask Webapp
- [ ] Deployment LP
- [ ] Requirements section

### Avin:

- [ ] Creating GitHub App
- [ ] Vector Database
- [ ] Configuring GitHub App

## Jason:

- [x] Python hello world extension LP

## Learning Path flow

- 1 Requirements
    - Install needed developer tools / SDKs 
        - Python (version?)
        - Python local environment + package install
    - Ensure have the example repo cloned 
- 10 Creating GitHub App
    - Creating the extension in UI
    - Getting application ID and client secret for Flask web app
- 20 Flask webapp / API
    - oauth2 implementation (refresher)
        - Link to previous learning path    
    - agent endpoint
        - RAG augmentations
        - Create client ID/secret
    - marketplace endpoint (optional step, if users want to deploy to the marketplace)
- 30 Vector database
    - What is a vector database
    - Describe FAISS, and why it is the fastest similarity search algorithm (efficient ANN, in-memory)
    - Mention that deploying a static in-memory vector store in every instance prevents a centralized bottleneck when scaling
    - bin file generation
- 40 Deployment (AWS only)
    - Disclaimers "There are a lot of ways to run a flask app"
    - Link to other learning path for full explanation
- 50 Configuring GitHub App
    - input callback endpoints
        - get URLs from LP #2, that are specfied in Route 53
    - optional: registering the extension with marketplace
- 100 Next steps
