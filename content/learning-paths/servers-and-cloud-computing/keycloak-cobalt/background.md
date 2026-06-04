---
title: Understand Keycloak on Azure Cobalt 100
weight: 2

layout: "learningpathall"
---

## Why run Keycloak on Azure Cobalt 100

Keycloak on Arm-based Azure Cobalt 100 processors delivers scalable and efficient identity and access management for modern cloud-native applications. Azure Cobalt 100 processors provide dedicated physical cores per vCPU, which helps deliver predictable performance for authentication workloads, user management, and OAuth2/OpenID Connect flows.

Keycloak benefits from the strong multi-core performance and energy efficiency of Arm-based Azure infrastructure, making it well suited for enterprise authentication systems, API security, and cloud-native identity platforms.

## Azure Cobalt 100 Arm-based processor

Azure’s Cobalt 100 is Microsoft’s first-generation, in-house Arm-based processor. Built on Arm Neoverse N2, Cobalt 100 is a 64-bit CPU that delivers strong performance and energy efficiency for cloud-native, scale-out Linux workloads. These workloads include web and application servers, data analytics, open-source databases, and caching systems. Running at 3.4 GHz, Cobalt 100 allocates a dedicated physical core for each vCPU, ensuring consistent and predictable performance.

To learn more, see the Microsoft blog [Announcing the preview of new Azure VMs based on the Azure Cobalt 100 processor](https://techcommunity.microsoft.com/blog/azurecompute/announcing-the-preview-of-new-azure-vms-based-on-the-azure-cobalt-100-processor/4146353).

## How Keycloak improves authentication and identity management

Keycloak is an open-source Identity and Access Management (IAM) platform that simplifies authentication and authorization for applications and services.

Keycloak supports modern authentication standards such as:

- OAuth2
- OpenID Connect (OIDC)
- SAML

Keycloak provides centralized authentication, allowing users to log in once and securely access multiple applications using Single Sign-On (SSO).

Keycloak integrates with web applications, APIs, Kubernetes platforms, microservices, and enterprise identity systems, making it ideal for securing cloud-native workloads.

To learn more, see the official [Keycloak documentation](https://www.keycloak.org/documentation).

Keycloak provides several important capabilities for authentication and security management:

- Single Sign-On (SSO): Enables users to authenticate once and access multiple applications securely.
- Centralized Identity Management: Manages users, roles, groups, and authentication policies from a single platform.
- OAuth2 and OpenID Connect Support: Simplifies secure API and application authentication workflows.
- Multi-factor Authentication (MFA): Improves account security using additional authentication methods.
- User Federation: Integrates with enterprise identity systems such as LDAP and Active Directory.
- Role-Based Access Control (RBAC): Controls user permissions and application access securely.

In this Learning Path, you'll deploy Keycloak on an Azure Cobalt 100 Arm64 virtual machine and configure PostgreSQL as the backend database. You'll create realms, users, and OAuth2/OpenID Connect clients, then integrate a Flask application with Keycloak authentication.

## What you've learned and what's next

You now understand why Azure Cobalt 100 and Keycloak are a strong combination for scalable authentication and identity management workloads. Next, you'll create the virtual machine that will run Keycloak and the Flask OAuth2 demo application throughout this Learning Path.
