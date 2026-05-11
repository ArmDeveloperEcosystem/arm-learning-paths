---
# ================================================================================
#       FIXED, DO NOT MODIFY THIS FILE
# ================================================================================
weight: 21
title: "Next Steps"
layout: "learningpathall"
---

## Where to go next

From this baseline you can extend the deployment in a few directions:

- swap Zenoh dev mode for [Zenoh with TLS](https://github.com/arm/device-connect/tree/main/packages/device-connect-server#secure--zenoh-tls) using the `generate_tls_certs.sh` script in `security_infra/`
- swap to a NATS backend with [JWT authentication](https://github.com/arm/device-connect/tree/main/packages/device-connect-server#authenticated--nats-jwt-auth) for per-device credentials
- explore the [multi-tenant deployment](https://github.com/arm/device-connect/tree/main/packages/device-connect-server#multi-tenant-deployment) flow when several teams or workshops share the same infrastructure
- replace the simulated number-generator with a real sensor or robot driver using the same `DeviceDriver` pattern from the edge SDK
