---
title: Understand Keycloak for identity and access management on Azure Cobalt 100-based virtual machines
description: Learn how Keycloak provides IAM, OAuth2/OpenID Connect, and single sign-on for applications running on Arm-based Azure infrastructure.
weight: 2

layout: "learningpathall"
---

## Why run Keycloak on Azure Cobalt 100

Keycloak delivers scalable and efficient identity and access management for modern cloud-native applications. Azure Cobalt 100 processors provide dedicated physical cores per vCPU, which helps deliver predictable performance for authentication workloads, user management, and OAuth2/OpenID Connect (OIDC) flows.

Keycloak benefits from the strong multi-core performance and energy efficiency of Arm-based Azure infrastructure, making it well suited for enterprise authentication systems, API security, and cloud-native identity platforms.

## Azure Cobalt 100 Arm-based processor

Azure’s Cobalt 100 is Microsoft’s first-generation, in-house Arm-based processor. Built on Arm Neoverse N2, Cobalt 100 is a 64-bit CPU that delivers strong performance and energy efficiency for cloud-native, scale-out Linux workloads. 

Running at 3.4 GHz, Cobalt 100 allocates a dedicated physical core for each vCPU, ensuring consistent and predictable performance.

To learn more, see the Microsoft blog [Announcing the preview of new Azure VMs based on the Azure Cobalt 100 processor](https://techcommunity.microsoft.com/blog/azurecompute/announcing-the-preview-of-new-azure-vms-based-on-the-azure-cobalt-100-processor/4146353).

## How Keycloak provides authentication and identity management

Keycloak is an open-source identity and access management (IAM) platform that simplifies authentication and authorization for applications and services.

Keycloak supports modern authentication standards such as OAuth2, OIDC, and Security Asserion Markup Language (SAML). It integrates with web applications, APIs, Kubernetes platforms, microservices, and enterprise identity systems, making it ideal for securing cloud-native workloads.

Keycloak provides several important capabilities for authentication and security management. With single sign-on (SSO) support, you can authenticate once and access multiple applications without logging in again. 

With centralized identity management, you can manage users, roles, groups, and authentication policies from a single platform. With OAuth2 and OpenID Connect support, you get simplified secure API and application authentication workflows.

Keycloak also supports multi-factor authentication (MFA) for stronger account security, user federation for integrating with enterprise identity systems such as LDAP and Active Directory, and role-based access control (RBAC) to control user permissions and application access.

To learn more about Keycloak, see the official [Keycloak documentation](https://www.keycloak.org/documentation).

## What you've learned and what's next

You've now learned why Azure Cobalt 100 and Keycloak are a strong combination for scalable authentication and identity management workloads. You also learned how Keycloak provides support for centralized identity management.

Next, you'll create a virtual machine on Azure that you'll use to run Keycloak and a Flask OAuth2 demo application.
