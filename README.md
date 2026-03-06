# 🚀 EKS Microservices Platform with Istio Service Mesh

This project demonstrates a **production-grade Kubernetes microservices architecture** deployed on AWS using **Amazon EKS and Istio Service Mesh**.

It simulates a real **e-commerce platform** consisting of multiple microservices with advanced traffic management, observability, and secure communication.

---

# 📌 Project Features

✔ Kubernetes microservices architecture
✔ AWS EKS cluster deployment
✔ Istio Service Mesh
✔ Canary deployments (90/10 split)
✔ Advanced traffic control (retries, timeouts, circuit breaker)
✔ Observability stack (Kiali, Prometheus, Grafana, Jaeger)
✔ DNS routing via Route53
✔ Public application access through AWS Load Balancer
✔ GitHub repository for version control

---

# 🏗 Architecture Diagram

```
                      Internet
                          │
                          ▼
                Route53 DNS Record
          app.katakamdevopsplatform.com
                          │
                          ▼
              AWS Network Load Balancer
                          │
                          ▼
                Istio Ingress Gateway
                          │
                          ▼
                 Istio Virtual Service
                          │
                          ▼
          ┌──────────────────────────────────┐
          │           EKS Cluster            │
          │                                  │
          │  product-service (v1 / v2)       │
          │  cart-service                    │
          │  order-service                   │
          │  payment-service                 │
          │  user-service                    │
          │                                  │
          │  Istio Envoy Sidecars            │
          └──────────────────────────────────┘
                          │
                          ▼
                 Observability Stack
     Prometheus → Grafana → Jaeger → Kiali
```

---

# 🧩 Microservices

| Service         | Endpoint    |
| --------------- | ----------- |
| Product Service | `/products` |
| Cart Service    | `/cart`     |
| Order Service   | `/orders`   |
| Payment Service | `/payments` |
| User Service    | `/users`    |

---

# ☁️ Infrastructure Components

| Component  | Purpose                    |
| ---------- | -------------------------- |
| AWS EKS    | Managed Kubernetes         |
| AWS NLB    | External traffic entry     |
| Istio      | Service mesh               |
| Karpenter  | Node autoscaling           |
| Route53    | DNS routing                |
| Prometheus | Metrics collection         |
| Grafana    | Metrics visualization      |
| Jaeger     | Distributed tracing        |
| Kiali      | Service mesh visualization |

---

# 🚀 Phase 1 — Create EKS Cluster

Create cluster using AWS CLI or Terraform.

Verify nodes:

```
kubectl get nodes
```

Expected output:

```
ip-10-0-1-x
ip-10-0-2-x
```

---

# 🚀 Phase 2 — Deploy Microservices

Create namespace:

```
kubectl create namespace ecommerce
```

Deploy services:

```
kubectl apply -f product-service.yaml
kubectl apply -f cart-service.yaml
kubectl apply -f order-service.yaml
kubectl apply -f payment-service.yaml
kubectl apply -f user-service.yaml
```

Verify:

```
kubectl get pods -n ecommerce
```

---

# 🚀 Phase 3 — Install Istio

Install Istio:

```
istioctl install --set profile=demo -y
```

Enable sidecar injection:

```
kubectl label namespace ecommerce istio-injection=enabled
```

Restart deployments:

```
kubectl rollout restart deployment -n ecommerce
```

---

# 🚀 Phase 4 — Configure Istio Gateway

Expose services externally.

```
kubectl apply -f ecommerce-gateway.yaml
```

Verify:

```
kubectl get gateway -n ecommerce
```

---

# 🚀 Phase 5 — VirtualService Routing

Routes requests to services.

Example:

```
/products → product-service
/cart → cart-service
/orders → order-service
/payments → payment-service
/users → user-service
```

Apply:

```
kubectl apply -f virtualservice.yaml
```

---

# 🚀 Phase 6 — Canary Deployment

Two versions of product service.

```
product-service-v1
product-service-v2
```

Traffic split:

```
90% → v1
10% → v2
```

VirtualService example:

```
route:
- destination:
    host: product-service
    subset: v1
  weight: 90

- destination:
    host: product-service
    subset: v2
  weight: 10
```

---

# 🚀 Phase 7 — Observability Setup

Installed tools:

```
Prometheus
Grafana
Jaeger
Kiali
```

Access dashboards:

```
istioctl dashboard kiali
istioctl dashboard grafana
istioctl dashboard prometheus
```

---

# 🚀 Phase 8 — Domain Mapping

Domain used:

```
katakamdevopsplatform.com
```

DNS record:

```
app.katakamdevopsplatform.com
```

Route53 configuration:

```
Type: A
Alias: AWS Network Load Balancer
```

Application access:

```
http://app.katakamdevopsplatform.com/products
```

---

# ⚠ Issues Faced & Fixes

## Issue 1 — Pods stuck in 1/2 state

Cause:

Istio sidecar not injected.

Fix:

```
kubectl label namespace ecommerce istio-injection=enabled
kubectl rollout restart deployment
```

---

## Issue 2 — 503 Service Unavailable

Cause:

VirtualService routing incorrect.

Fix:

Corrected URI match rules.

---

## Issue 3 — Cannot access LoadBalancer

Cause:

Security group blocked traffic.

Fix:

```
aws ec2 authorize-security-group-ingress
```

---

## Issue 4 — DNS not resolving

Cause:

Route53 record pointing to wrong load balancer.

Fix:

Updated alias to correct NLB.

---

## Issue 5 — Too many pods error

Cause:

Node CPU exhausted.

Fix:

Karpenter automatically provisioned new node.

---

# 🔐 Security

Implemented security features:

* mTLS communication between services
* Authorization policies
* Namespace isolation

---

# 📊 Observability

Using Kiali we can visualize service traffic:

```
product-service → cart-service
cart-service → order-service
order-service → payment-service
```

Metrics available:

* Request rate
* Latency
* Error rate

---

# 🎤 5 Minute Interview Explanation

Example answer:

> I implemented a microservices platform on AWS using EKS and Istio Service Mesh.
>
> The application consists of multiple services such as product, cart, order, payment, and user services.
>
> Traffic enters through Route53 DNS and an AWS Network Load Balancer, which forwards requests to the Istio Ingress Gateway.
>
> Istio handles service-to-service communication using Envoy sidecar proxies and enables advanced traffic management like canary deployments and retries.
>
> For observability, I integrated Prometheus, Grafana, Jaeger, and Kiali to monitor metrics, traces, and service topology.
>
> This architecture ensures reliability, security, and controlled rollouts in a production environment.

---

# 💼 Real DevOps Scenarios

### Scenario 1 — Production Deployment

New version deployed using canary strategy:

```
v1 → 90%
v2 → 10%
```

Monitor metrics before full rollout.

---

### Scenario 2 — Service Failure

Istio retries failed requests:

```
retries: 3
timeout: 5s
```

---

### Scenario 3 — Debug latency

Use Jaeger distributed tracing to find slow services.

---

### Scenario 4 — Traffic spike

Karpenter automatically provisions new nodes.

---

### Scenario 5 — Secure communication

Strict mTLS ensures encrypted service communication.

---

# 📈 Future Improvements

Planned enhancements:

* GitOps using ArgoCD
* Automatic canary using Argo Rollouts
* HTTPS with AWS ACM
* Rate limiting
* Chaos engineering

---

# 👨‍💻 Author

Vinod Katakam

DevOps Engineer

This project demonstrates **real-world Kubernetes service mesh architecture with AWS and Istio**.
