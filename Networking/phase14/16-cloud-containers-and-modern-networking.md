
# Phase 14: Cloud, Containers, and Modern Networking

## 32. Cloud Networking Fundamentals

### 32.1 What Is Cloud Networking?

Cloud networking is the process of connecting cloud-based resources—such as virtual machines, databases, containers, applications, and storage—through virtual networks.

In traditional networking, physical routers, switches, and cables connect devices. In cloud networking, much of this infrastructure is created and managed virtually through a cloud provider.

Popular cloud platforms include:

- Amazon Web Services (AWS)
- Microsoft Azure
- Google Cloud Platform (GCP)

**Example:**

Suppose you build a web application with:
- A frontend hosted on a public-facing server.
- A backend API running on a private server.
- A database accessible only by the backend.

Cloud networking allows these components to communicate while controlling which systems can access them.

**Why it matters in cybersecurity:**

Incorrect cloud networking configurations can expose databases, APIs, virtual machines, and internal services to the public internet.

---

### 32.2 Virtual Private Cloud (VPC/VNet)

A Virtual Private Cloud (VPC) is an isolated virtual network created inside a cloud platform.

It allows you to define:
- IP address ranges.
- Subnets.
- Routing rules.
- Network access controls.
- Connections between cloud resources.

Different cloud providers use different names:

| Cloud provider | Virtual network name |
|---|---|
| AWS | Virtual Private Cloud (VPC) |
| Microsoft Azure | Virtual Network (VNet) |
| Google Cloud | Virtual Private Cloud (VPC) |

**Example:**

You create a VPC with the following IP range:

`10.0.0.0/16`

Inside this network, you can create smaller subnets:

- `10.0.1.0/24` — Public subnet.
- `10.0.2.0/24` — Private application subnet.
- `10.0.3.0/24` — Private database subnet.

The VPC provides a logical boundary for organizing and controlling network communication.

**Security importance:**

A VPC helps isolate cloud resources, but creating one does not automatically make every resource secure. You must configure routing, access controls, and service exposure correctly.

---

### 32.3 Public and Private Subnets

A subnet is a smaller logical network created inside a larger network.

Cloud environments commonly use two subnet categories.

#### Public subnet

A public subnet is a subnet whose route table provides a path to an internet gateway.

Resources in it may be reachable from the internet if they also have:
- A suitable public IP address.
- Permissive security rules.
- A service listening on the relevant port.

Examples:
- Public web servers.
- Internet-facing load balancers.
- Public-facing application gateways.

#### Private subnet

A private subnet does not have a direct route to an internet gateway for general inbound internet access.

Resources in it are typically used for:
- Databases.
- Internal APIs.
- Application servers.
- Background processing systems.

Private resources may still access the internet through a NAT gateway when the routing and security rules permit it.

**Example architecture:**

```text
                 INTERNET
                    |
                    |
             Internet Gateway
                    |
             PUBLIC SUBNET
                    |
             Load Balancer
                    |
             PRIVATE SUBNET
                    |
              Backend API
                    |
             PRIVATE SUBNET
                    |
                Database
```

**Security best practice:**

Do not place databases and internal services in publicly accessible network configurations unless there is a specific, justified requirement.

---

### 32.4 Internet Gateways

An Internet Gateway (IGW) is a cloud networking component that allows communication between a VPC and the public internet.

In AWS, an internet gateway:
- Connects to a VPC.
- Provides internet connectivity for eligible resources.
- Works with route tables.
- Supports inbound and outbound communication when other network and security conditions allow it.

**Example route:**

```text
Destination: 0.0.0.0/0
Target: Internet Gateway
```

`0.0.0.0/0` represents all IPv4 destinations.

This route sends traffic destined for external IPv4 networks toward the internet gateway.

**Important:**

Attaching an internet gateway to a VPC does not automatically make every resource publicly accessible. Public addressing, routing, and security rules also matter.

---

### 32.5 NAT Gateways

NAT stands for Network Address Translation.

A NAT gateway allows resources in a private subnet to initiate connections to external networks without allowing unsolicited internet connections to be initiated directly toward those private resources through that NAT gateway.

**Example:**

A private application server needs to:
- Download software updates.
- Retrieve packages.
- Contact an external API.

However, you do not want the server to accept direct inbound connections from the public internet.

A NAT gateway can provide the required outbound connectivity.

```text
             INTERNET
                 |
          Internet Gateway
                 |
            NAT Gateway
                 |
           PRIVATE SUBNET
                 |
           Application VM
```

**Difference between Internet Gateway and NAT Gateway:**

| Internet Gateway | NAT Gateway |
|---|---|
| Provides internet connectivity for eligible public resources | Provides outbound connectivity for private resources |
| Can support inbound and outbound traffic | Does not allow unsolicited inbound connections through the NAT gateway |
| Used with public subnet routing | Commonly used by private subnet routing |

**Security importance:**

A NAT gateway reduces the need to give private resources public IP addresses. However, outbound access should still be controlled where possible.

---

### 32.6 Route Tables

A route table contains rules that determine where network traffic should go.

Each route typically contains:
- Destination: The target IP range.
- Target: Where the traffic should be forwarded.

**Example:**

| Destination | Target |
|---|---|
| `10.0.0.0/16` | Local VPC |
| `0.0.0.0/0` | Internet Gateway |

Another example for a private subnet:

| Destination | Target |
|---|---|
| `10.0.0.0/16` | Local VPC |
| `0.0.0.0/0` | NAT Gateway |

**How routing works:**

Suppose a server sends traffic to `8.8.8.8`.

1. The operating system sends the packet to its configured network gateway.
2. The cloud network evaluates the applicable route table.
3. The route matching the destination determines the next hop.
4. The packet is forwarded if network and security controls permit it.

Cloud route tables generally use longest-prefix matching when multiple routes match a destination.

**Security importance:**

Incorrect routes can expose internal systems, break connectivity, or send traffic through an unintended network path.

---

### 32.7 Security Groups

A security group is a virtual firewall associated with cloud resources or network interfaces.

In AWS, security groups are stateful.

This means that when an allowed connection is established, its response traffic is automatically permitted without requiring a separate reverse-direction rule.

Security groups commonly control:
- Inbound traffic.
- Outbound traffic.
- Protocols.
- Port ranges.
- Source or destination IP ranges.
- References to other security groups.

**Example inbound rules:**

| Protocol | Port | Source | Purpose |
|---|---:|---|---|
| TCP | 443 | `0.0.0.0/0` | Public HTTPS |
| TCP | 22 | Trusted administrator IP | SSH administration |
| TCP | 3306 | Backend security group | Database access |

**Security best practices:**

- Avoid allowing SSH from `0.0.0.0/0`.
- Avoid exposing database ports publicly.
- Allow only necessary ports.
- Prefer security-group references for internal application communication.
- Review unused and overly permissive rules.

**Important:** Security-group behavior differs across cloud providers. Do not assume every provider implements identical firewall semantics.

---

### 32.8 Network ACLs (NACLs)

A Network Access Control List (NACL) is a network-level access control mechanism.

In AWS, NACLs operate at the subnet level and are stateless.

They can control:
- Inbound traffic.
- Outbound traffic.
- Protocols.
- Port ranges.
- Source and destination IP addresses.

Because they are stateless, you must consider both directions of a connection.

**Security groups vs NACLs:**

| Feature | Security Group | Network ACL |
|---|---|---|
| Scope | Resource/network interface | Subnet |
| Stateful | Yes | No |
| Rules | Allow rules | Allow and deny rules |
| Return traffic | Automatically permitted for tracked connections | Must be permitted separately |
| Main purpose | Control resource-level access | Add subnet-level traffic controls |

**Example:**

You can use a NACL to deny traffic from a particular IP range at the subnet boundary.

A security group can then restrict which resources accept specific application connections.

**Best practice:** Use layered security controls rather than depending on only one network filtering mechanism.

---

### 32.9 Cloud Load Balancers

A load balancer distributes incoming network traffic across multiple servers or application instances.

Its purpose is to improve:
- Availability.
- Scalability.
- Performance.
- Fault tolerance.

**Example:**

```text
              INTERNET
                  |
             LOAD BALANCER
              /        \
             /          \
        SERVER 1      SERVER 2
             \          /
              \        /
                DATABASE
```

If one server becomes unhealthy, a load balancer may stop sending new traffic to it and direct traffic to healthy instances.

**Common load balancer types:**

| Type | Description |
|---|---|
| Application Load Balancer | Works at the application layer, commonly HTTP/HTTPS |
| Network Load Balancer | Handles network-level traffic such as TCP and UDP |
| Gateway Load Balancer | Used for certain network appliance and traffic-inspection architectures |

**Security importance:**

- Configure HTTPS/TLS correctly.
- Restrict direct access to backend servers.
- Validate health-check endpoints.
- Avoid exposing administrative interfaces.
- Configure trusted proxy handling correctly.
- Review access logs.

A load balancer is not automatically a Web Application Firewall (WAF).

---

### 32.10 Private Endpoints

A private endpoint allows a resource to be accessed through private network connectivity rather than requiring access over the public internet.

For example, an application running inside a VPC may need to communicate with a cloud storage service.

Instead of sending that traffic over a public endpoint, you may configure private connectivity supported by the cloud provider.

Examples include:
- AWS PrivateLink and VPC endpoints.
- Azure Private Link.
- Google Cloud Private Service Connect.

**Benefits:**

- Reduces public internet exposure.
- Helps keep service communication within private network paths.
- Supports network isolation requirements.
- Makes it easier to apply controlled access policies.

**Important:**

Private connectivity does not automatically guarantee authorization. Identity permissions, endpoint policies, and application-level security must also be configured.

---

### 32.11 DNS in Cloud Environments

DNS (Domain Name System) translates domain names into IP addresses.

Cloud platforms provide DNS services for:
- Public domain resolution.
- Private network name resolution.
- Service discovery.
- Load balancer addresses.
- Internal application communication.

**Example:**

A web application might use:

```text
www.example.com       -> Public load balancer
api.example.com       -> Backend API
db.internal           -> Private database address
```

The actual resolution behavior depends on the DNS records, private DNS configuration, network, and cloud provider.

**Public DNS vs private DNS:**

| Public DNS | Private DNS |
|---|---|
| Resolves names for public access | Resolves names within configured private networks |
| Can be queried from the internet | Usually restricted to associated networks or resolvers |
| Used for public websites | Used for internal services |

**Security risks:**

- Accidentally publishing internal DNS records.
- Exposing sensitive hostnames.
- Incorrect DNS configurations.
- DNS records pointing to unintended public resources.

**Best practice:** Keep internal service names and records in appropriately restricted private DNS zones.

---

### 32.12 Cloud Network Logging

Cloud network logging records information about network activity.

It helps security teams understand:
- Which resources communicated.
- Where traffic originated.
- Which destination was contacted.
- Which ports and protocols were used.
- Whether traffic was accepted or rejected.

Examples:

- AWS VPC Flow Logs.
- Azure Network Watcher flow logs.
- Google Cloud VPC Flow Logs.

**Example flow-log-style record:**

```text
srcaddr=10.0.1.15
dstaddr=10.0.2.20
srcport=51520
dstport=443
protocol=6
action=ACCEPT
```

Here:
- `srcaddr` = Source IP.
- `dstaddr` = Destination IP.
- `srcport` = Source port.
- `dstport` = Destination port.
- `protocol=6` = TCP.
- `action=ACCEPT` = Traffic was accepted by the recorded network control.

The exact fields and format depend on the cloud provider.

**Security importance:**

Network logs can help investigate:
- Unexpected outbound connections.
- Repeated connection attempts.
- Unusual traffic patterns.
- Unexpected access to sensitive services.
- Possible data exfiltration.

**Important:** Flow logs generally record connection metadata, not the complete contents of packets.

---

### 32.13 Cloud Firewall Concepts

A cloud firewall controls network traffic entering, leaving, or moving between cloud resources.

It can provide:
- IP-based filtering.
- Port and protocol filtering.
- Application-aware inspection.
- Threat detection.
- Traffic logging.
- Centralized network security policies.

Cloud security controls may exist at multiple levels:

1. Network interface or resource level.
2. Subnet level.
3. VPC/VNet level.
4. Centralized network inspection layer.
5. Application layer through a WAF.

**Cloud firewall vs WAF:**

| Cloud firewall | Web Application Firewall |
|---|---|
| Primarily controls network traffic | Focuses on HTTP/HTTPS application requests |
| Can filter IPs, ports, protocols, and other traffic attributes | Can inspect web requests for application-layer attack patterns |
| Protects network boundaries and workloads | Helps protect web applications and APIs |

A WAF may help detect or block common web attacks such as SQL injection and cross-site scripting, depending on its configuration and rules.

---

### 32.14 Publicly Exposed Services

A publicly exposed service is a cloud resource or application endpoint that can be reached from the public internet.

Examples:
- Public web servers.
- Public APIs.
- Exposed SSH services.
- Public database endpoints.
- Unrestricted storage or administration interfaces.

**Why is this dangerous?**

An exposed service can become an attack entry point when it has:
- Weak authentication.
- Unpatched software.
- Misconfigured permissions.
- Vulnerable application code.
- Unnecessary open ports.

**Example of a risky configuration:**

```text
Database: Publicly accessible
Port: 3306
Source: 0.0.0.0/0
```

This makes the database network-accessible from anywhere, subject to other controls.

**Safer configuration:**

```text
Database: Private subnet
Port: 3306
Allowed source: Backend application security group
```

**Cloud security checklist:**

- Identify public IP addresses.
- Review open ports.
- Check publicly accessible databases.
- Review storage access policies.
- Remove unused public endpoints.
- Restrict administrative access.
- Monitor unexpected exposure changes.

---

### 32.15 Least-Privilege Network Access

Least privilege means granting only the minimum access required to perform a task.

In cloud networking, this means:
- Allow only required ports.
- Restrict sources and destinations.
- Avoid unnecessary public access.
- Separate application and database networks.
- Limit outbound connections where practical.
- Review permissions regularly.

**Example:**

Instead of allowing every server to communicate with the database:

```text
Allow: 0.0.0.0/0
Port: 3306
```

Allow only the backend application:

```text
Allow source: Backend security group
Port: 3306
Protocol: TCP
```

**Why it matters in AppSec:**

If an attacker compromises a web application, network restrictions can reduce the attacker's ability to reach unrelated internal services.

This is called limiting lateral movement.

---

## 32.16 Practical Cloud Networking Example

Consider a three-tier web application.

**Architecture:**

```text
                       INTERNET
                           |
                    INTERNET GATEWAY
                           |
                    PUBLIC SUBNET
                           |
                    LOAD BALANCER
                           |
                    PRIVATE SUBNET
                           |
                     BACKEND API
                           |
                    PRIVATE SUBNET
                           |
                        DATABASE
```

**Suggested network design:**

| Component | Network placement | Access |
|---|---|---|
| Load balancer | Public subnet | HTTPS from internet |
| Backend API | Private subnet | Only from load balancer or approved internal services |
| Database | Private subnet | Only from backend API |
| Administration | Restricted management path | Authorized administrators only |

**Security controls:**

1. Use HTTPS for public application traffic.
2. Keep databases private.
3. Restrict database access to the backend.
4. Avoid unrestricted SSH access.
5. Enable network flow logging.
6. Use private endpoints where appropriate.
7. Review firewall and security-group rules.
8. Monitor public exposure.

**Learning exercise:**

Draw this architecture yourself and identify:
- Which resources need internet access?
- Which resources should remain private?
- Which ports are required?
- Which components should communicate with the database?
- Where should network logging be enabled?

You can later build this architecture in a cloud free-tier or sandbox environment. Check current pricing and free-tier limits before creating resources.

---

## 33. Container Networking

### 33.1 What Are Containers?

A container is a lightweight, isolated environment that packages an application together with its required dependencies.

Containers share the host operating system's kernel but have isolated processes and other resources.

They commonly include:
- Application code.
- Runtime.
- Libraries.
- Dependencies.
- Configuration.

**Example:**

A Node.js application may require:
- Node.js runtime.
- Express.
- Application source code.
- Environment configuration.

Instead of installing everything manually on every server, you can package the application into a container image.

Popular container technologies include:
- Docker.
- containerd.
- Podman.

**Container vs Virtual Machine:**

| Container | Virtual Machine |
|---|---|
| Shares the host OS kernel | Runs a guest operating system |
| Usually lightweight | Usually uses more resources |
| Starts quickly in many cases | Often takes longer to start |
| Isolated processes and resources | Isolated virtual machine environment |
| Commonly packaged as images | Commonly packaged as VM images |

**Important:** Containers provide isolation, but they are not equivalent to completely separate physical machines. Their security depends on runtime configuration, kernel security, privileges, and other controls.

---

### 33.2 Docker Bridge Networks

A Docker bridge network allows containers on the same bridge network to communicate with one another.

Docker creates a default bridge network, and users can also create custom bridge networks.

**Example:**

```bash
docker network create app-network
```

Run two containers on that network:

```bash
docker run -d --name app1 --network app-network nginx
docker run -d --name app2 --network app-network nginx
```

Inspect the network:

```bash
docker network inspect app-network
```

List networks:

```bash
docker network ls
```

**How it works:**

```text
             HOST MACHINE
                  |
             DOCKER BRIDGE
               /      \
              /        \
        CONTAINER 1  CONTAINER 2
```

Containers connected to the same user-defined bridge network can generally communicate using container names as DNS names.

For example, a container on `app-network` may reach the other container using:

```text
http://app2
```

The application must still listen on the relevant port, and its own firewall or configuration must permit communication.

**Security importance:**

Custom bridge networks help separate groups of containers. Avoid putting unrelated or sensitive services on the same network without a reason.

---

### 33.3 Host Networking

Host networking allows a container to use the host's network namespace rather than receiving its own separate network namespace.

Example:

```bash
docker run --rm --network host nginx
```

In this mode:
- The container shares the host's network interfaces.
- Port publishing with `-p` is generally unnecessary and ignored.
- Services can bind directly to host network ports.
- Network isolation is reduced.

**Bridge vs host networking:**

| Bridge networking | Host networking |
|---|---|
| Uses a separate container network namespace | Shares the host network namespace |
| Supports Docker port publishing | Port publishing is not needed |
| Provides network separation | Reduces network separation |
| Common for application containers | Used for particular performance or networking requirements |

**Security warning:**

Host networking can increase the impact of a compromised container because it has access to the host's network environment. Use it only when necessary.

---

### 33.4 Port Publishing

Containers can listen on internal ports that are not automatically exposed to the host or the public internet.

Docker port publishing maps a host port to a container port.

**Syntax:**

```bash
docker run -d -p HOST_PORT:CONTAINER_PORT nginx
```

**Example:**

```bash
docker run -d --name web -p 8080:80 nginx
```

This maps:
- Host port: `8080`.
- Container port: `80`.

You can access the application locally at:

```text
http://localhost:8080
```

Check running containers:

```bash
docker ps
```

View container port mappings:

```bash
docker port web
```

**Binding to a specific host interface:**

```bash
docker run -d -p 127.0.0.1:8080:80 nginx
```

This binds the published port to the host's loopback interface, rather than all host interfaces.

**Security importance:**

Be careful with this configuration:

```bash
docker run -d -p 8080:80 nginx
```

Depending on the host and firewall configuration, this may make the service reachable through external host interfaces.

Before publishing a port, ask:
- Does this service need to be reachable from outside the host?
- Should access be limited to localhost?
- Is authentication enabled?
- Is the exposed application secure?

---

### 33.5 Container-to-Container Communication

Containers can communicate over a shared Docker network.

For example, consider:
- A frontend container.
- A backend container.
- A database container.

```text
             DOCKER NETWORK
          ____________________
         |                    |
         |   FRONTEND         |
         |       |            |
         |       v            |
         |    BACKEND         |
         |       |            |
         |       v            |
         |    DATABASE        |
         |____________________|
```

Create a network:

```bash
docker network create my-app
```

Start a database container:

```bash
docker run -d \
  --name database \
  --network my-app \
  -e POSTGRES_PASSWORD=change-me \
  postgres
```

For a real deployment, use a securely managed secret rather than putting a real password directly in shell history or a command line.

A backend container on the same network can connect to the database using the hostname:

```text
database
```

The application would use the database's internal port and the appropriate credentials.

**Important concepts:**

- Containers on the same network can communicate according to the network and application configuration.
- Containers on separate networks are isolated by default unless connected through an appropriate path.
- A database does not need to publish its port to the host just to communicate with another container on the same network.

---

### 33.6 DNS Within Container Networks

Docker provides DNS-based service discovery on user-defined networks.

This allows containers to locate other containers by name.

**Example:**

Suppose you have:

```text
frontend
backend
database
```

If all three containers share a user-defined network, the frontend may communicate with the backend using:

```text
http://backend:3000
```

The backend may communicate with the database using:

```text
database:5432
```

These are examples; the actual ports depend on the applications.

**Why use container DNS?**

Without service discovery, an application might need to use a container's IP address directly.

Container IP addresses can change when containers are recreated. Using service names is generally more convenient and reliable.

**Security considerations:**

- Do not expose internal service names unnecessarily.
- Separate services into appropriate networks.
- Protect internal services with authentication.
- Do not assume that network membership alone provides application authorization.

---

### 33.7 Docker Compose Networking

Docker Compose is a tool for defining and running multi-container applications using a YAML configuration file.

It is commonly used for local development and testing.

**Example `compose.yaml`:**

```yaml
services:
  frontend:
    image: nginx
    ports:
      - "8080:80"
    networks:
      - frontend-network

  backend:
    image: node:22-alpine
    command: ["node", "-e", "require('http').createServer((req,res)=>res.end('API')).listen(3000)"]
    networks:
      - frontend-network
      - database-network

  database:
    image: postgres
    environment:
      POSTGRES_USER: appuser
      POSTGRES_PASSWORD: change-me
      POSTGRES_DB: appdb
    networks:
      - database-network

networks:
  frontend-network:
  database-network:
```

This is a basic learning example. A real deployment should use securely managed credentials, pinned image versions, persistent storage, and suitable application configuration.

Start the services:

```bash
docker compose up -d
```

List services:

```bash
docker compose ps
```

View logs:

```bash
docker compose logs
```

Stop and remove the containers and networks:

```bash
docker compose down
```

**How networking works here:**

- Frontend and backend share `frontend-network`.
- Backend and database share `database-network`.
- Frontend and database are not directly connected through a shared network.
- The backend can communicate with the database using the hostname `database`.

**Security importance:**

Separating networks helps limit unnecessary communication between application components.

---

### 33.8 Container Isolation

Container isolation means restricting how a container interacts with:
- Other containers.
- The host operating system.
- Host files and directories.
- Network interfaces.
- System resources.

Common isolation mechanisms include:

**1. Namespaces**

Linux namespaces isolate resources such as:
- Process IDs.
- Network interfaces.
- Mount points.
- Hostnames.
- Users.

**2. Control groups (cgroups)**

Cgroups control and monitor resource usage, such as:
- CPU.
- Memory.
- Processes.
- I/O resources.

**3. Linux capabilities**

Linux capabilities divide traditional root privileges into smaller individual permissions.

Containers can be granted only the capabilities they require.

**4. Seccomp**

Seccomp can restrict which system calls a process is allowed to make.

**5. AppArmor and SELinux**

These security mechanisms can enforce additional restrictions on what processes are allowed to do.

**Security best practices:**

- Avoid running containers as root when unnecessary.
- Drop unnecessary Linux capabilities.
- Use read-only filesystems where practical.
- Apply CPU and memory limits.
- Avoid privileged containers.
- Keep container images updated.
- Restrict host filesystem mounts.

---

### 33.9 Network Exposure and Misconfiguration

Container networking misconfiguration can expose services unintentionally.

**Common examples:**

1. Publishing database ports to all host interfaces.
2. Using host networking without a clear need.
3. Connecting unrelated services to the same Docker network.
4. Exposing internal administrative APIs.
5. Using weak credentials.
6. Running containers with excessive privileges.
7. Leaving unused containers and services running.
8. Trusting internal network traffic without authentication.

**Example of risky database exposure:**

```bash
docker run -d \
  --name database \
  -p 5432:5432 \
  postgres
```

This publishes the database port on the host's network interfaces by default.

If external access is not needed, do not publish the database port.

Instead, let the backend container communicate with the database over a private Docker network.

**Safer architecture:**

```text
          HOST MACHINE
               |
         FRONTEND CONTAINER
               |
          DOCKER NETWORK
               |
         BACKEND CONTAINER
               |
          DOCKER NETWORK
               |
         DATABASE CONTAINER
```

Only publish the frontend port if external access is required.

**Container security checklist:**

- [ ] Avoid unnecessary published ports.
- [ ] Use private container networks.
- [ ] Avoid privileged mode.
- [ ] Use non-root users where possible.
- [ ] Keep images and packages updated.
- [ ] Use trusted container images.
- [ ] Scan images for known vulnerabilities.
- [ ] Protect secrets.
- [ ] Apply resource limits.
- [ ] Review mounted host directories.

---

### 33.10 Kubernetes Networking — Introduction

Kubernetes is an open-source platform used to manage containerized applications.

It supports:
- Container deployment.
- Scaling.
- Service discovery.
- Load balancing.
- Application recovery.
- Configuration management.

A Kubernetes cluster generally contains:
- Control plane components.
- Worker nodes.
- Pods.
- Services.
- Networking components.

**What is a Pod?**

A Pod is the smallest deployable unit in Kubernetes.

A Pod contains one or more containers that share certain resources, including the Pod's network namespace.

Containers in the same Pod can communicate with each other through `localhost`.

**Kubernetes networking model:**

Kubernetes networking generally provides:
- Communication between containers in the same Pod.
- Communication between Pods.
- Service-based access to Pods.
- Optional external access through configured networking components.

The exact implementation depends on the cluster's Container Network Interface (CNI) plugin and cloud environment.

**Example:**

```text
             KUBERNETES CLUSTER
        ___________________________
       |                           |
       |        WORKER NODE        |
       |                           |
       |       POD 1               |
       |    [Frontend]             |
       |                           |
       |       POD 2               |
       |    [Backend]              |
       |                           |
       |       POD 3               |
       |    [Database]             |
       |___________________________|
```

In a real cluster, Pods may run on different worker nodes.

Kubernetes networking and its CNI plugin handle communication between them.

---

### 33.11 Kubernetes Services and Ingress — Overview

#### Kubernetes Services

A Service provides a stable network endpoint for accessing a group of Pods.

Pods can be recreated or assigned different IP addresses. A Service provides a stable way to reach the selected Pods.

Common Service types:

| Service type | Purpose |
|---|---|
| ClusterIP | Exposes a service inside the cluster |
| NodePort | Exposes a service on a port of each node |
| LoadBalancer | Requests an external load balancer when supported by the environment |
| ExternalName | Maps a service name to an external DNS name |

**Example Service configuration:**

```yaml
apiVersion: v1
kind: Service
metadata:
  name: backend-service
spec:
  selector:
    app: backend
  ports:
    - protocol: TCP
      port: 80
      targetPort: 3000
  type: ClusterIP
```

This creates an internal service that forwards traffic on port 80 to selected backend Pods listening on port 3000.

#### Kubernetes Ingress

Ingress is an API resource that defines HTTP and HTTPS routing rules for accessing services from outside a cluster.

It commonly supports:
- Host-based routing.
- Path-based routing.
- TLS configuration.
- Routing to internal Services.

An Ingress resource generally requires an Ingress controller to implement the rules.

**Example:**

```text
              INTERNET
                  |
             INGRESS
                  |
          __________________
          |                |
      /api path        /app path
          |                |
    BACKEND SERVICE   FRONTEND SERVICE
          |                |
       BACKEND POD      FRONTEND POD
```

**Security considerations:**

- Configure TLS correctly.
- Restrict access to administrative endpoints.
- Validate host and path routing.
- Avoid exposing internal services unnecessarily.
- Apply authentication and authorization at the application layer.
- Keep the Ingress controller updated.

**Important:** Ingress is not itself a firewall or authentication system. Additional controls may be necessary.

---

### 33.12 Kubernetes Network Policies — Overview

A NetworkPolicy is a Kubernetes resource that controls network communication involving selected Pods.

It can define:
- Ingress rules: Which incoming connections are allowed.
- Egress rules: Which outgoing connections are allowed.
- Pod selectors.
- Namespace selectors.
- IP address ranges.
- Ports and protocols.

**Example:**

Suppose you have:
- Frontend Pods.
- Backend Pods.
- Database Pods.

You want:
- Frontend to communicate with backend.
- Backend to communicate with database.
- Frontend not to communicate directly with database.

A suitable network policy can help enforce this separation.

**Conceptual architecture:**

```text
FRONTEND
    |
    | Allowed
    v
BACKEND
    |
    | Allowed
    v
DATABASE

FRONTEND ----------X----------> DATABASE
                 Denied
```

**Important limitations:**

- NetworkPolicy enforcement depends on the cluster's network plugin.
- A policy does not automatically provide application authentication.
- You must account for required DNS and other supporting traffic.
- Policies should be tested after deployment.

**Security importance:**

Network policies help reduce lateral movement if an attacker compromises one application component.

---

## 34. Practical Exercises

### Exercise 1: Understand Cloud Network Architecture

Draw a cloud architecture containing:

- One VPC.
- One public subnet.
- Two private subnets.
- One internet gateway.
- One NAT gateway.
- One load balancer.
- One backend server.
- One database.

Answer these questions:

1. Which component receives public traffic?
2. Which resources should remain private?
3. How does the backend access the database?
4. How can the backend download updates?
5. Which network logs would help investigate suspicious activity?

### Exercise 2: Docker Network Practice

Create a custom Docker network:

```bash
docker network create lab-network
```

Run two containers:

```bash
docker run -d --name web1 --network lab-network nginx

docker run -d --name web2 --network lab-network nginx
```

Inspect the network:

```bash
docker network inspect lab-network
```

Check the containers:

```bash
docker ps
```

Test communication between them:

```bash
docker exec web1 getent hosts web2
```

If the command is unavailable in the image, use another suitable DNS lookup utility or a temporary diagnostic container attached to the same network.

Clean up:

```bash
docker rm -f web1 web2
docker network rm lab-network
```

**Learning objective:** Understand Docker bridge networks and container-name-based DNS resolution.

### Exercise 3: Port Publishing Practice

Run an Nginx container:

```bash
docker run -d --name web-lab -p 127.0.0.1:8080:80 nginx
```

Open:

```text
http://127.0.0.1:8080
```

Inspect its port mapping:

```bash
docker port web-lab
```

Stop and remove it:

```bash
docker rm -f web-lab
```

**Learning objective:** Understand the difference between a container port and a host port, and how binding to localhost limits exposure.

### Exercise 4: Inspect Docker Networks

Run:

```bash
docker network ls
```

Inspect the default bridge:

```bash
docker network inspect bridge
```

Create a custom network and inspect it:

```bash
docker network create test-network
docker network inspect test-network
```

Remove it:

```bash
docker network rm test-network
```

**Learning objective:** Understand Docker network configuration and isolation.

### Exercise 5: Explore Kubernetes Concepts

If you have a local Kubernetes environment such as Minikube or kind, inspect the cluster:

```bash
kubectl get nodes
kubectl get pods -A
kubectl get services -A
kubectl get namespaces
```

Inspect a particular Service:

```bash
kubectl describe service SERVICE_NAME
```

Replace `SERVICE_NAME` with an actual Service in your lab.

**Learning objective:** Understand Pods, Services, namespaces, and cluster networking.

Do not expose a test cluster to the public internet just to complete this exercise.

---

## 35. Cybersecurity Relevance: AppSec, DevSecOps, and Cloud Security

### 35.1 How Cloud Networking Helps AppSec

Application Security (AppSec) focuses on protecting applications from vulnerabilities and attacks.

Cloud networking knowledge helps you understand:

- Where an application is hosted.
- How users reach the application.
- How frontend and backend services communicate.
- How APIs connect to databases.
- Which internal services are exposed.
- How network controls reduce attack impact.

For example, if an attacker exploits a web application, proper network segmentation can help prevent direct access to the database or unrelated internal systems.

### 35.2 How Container Networking Helps AppSec

Modern applications frequently run in containers.

Understanding container networking helps you identify:

- Unexpectedly exposed application ports.
- Internal services reachable without authorization.
- Unnecessary communication between containers.
- Weak network isolation.
- Insecure service-to-service communication.
- Container configuration mistakes.

### 35.3 How Kubernetes Helps DevSecOps

DevSecOps integrates security into software development and deployment workflows.

Kubernetes knowledge is useful for understanding:

- Application deployment.
- Service exposure.
- Ingress routing.
- Network policies.
- Secrets management.
- Container image security.
- Workload isolation.

### 35.4 Important Security Areas to Learn Later

After understanding these networking fundamentals, gradually explore:

1. Cloud IAM and identity permissions.
2. Cloud security posture management.
3. Container image vulnerability scanning.
4. Container runtime security.
5. Kubernetes RBAC.
6. Kubernetes secrets and configuration.
7. Cloud logging and monitoring.
8. Web Application Firewalls.
9. API gateways.
10. Infrastructure as Code security.

These are additional topics. You do not need to master all of them before starting web application security testing.

---

## 36. Quick Revision

| Concept | Meaning |
|---|---|
| Cloud networking | Networking between cloud resources |
| VPC | Isolated virtual network |
| VNet | Azure's virtual network |
| Public subnet | Subnet with a route to an internet gateway |
| Private subnet | Subnet without a direct internet gateway route for general inbound internet access |
| Internet gateway | Connects a VPC to the public internet |
| NAT gateway | Provides outbound connectivity for private resources |
| Route table | Determines where network traffic is forwarded |
| Security group | Resource-level virtual firewall in AWS |
| NACL | Subnet-level stateless network access control in AWS |
| Load balancer | Distributes incoming traffic across resources |
| Private endpoint | Provides private connectivity to a service |
| Cloud flow logs | Record network flow metadata |
| Container | Isolated application environment |
| Docker bridge | Network for container communication |
| Host networking | Container shares the host network namespace |
| Port publishing | Maps a host port to a container port |
| Docker Compose | Defines and runs multi-container applications |
| Container isolation | Restricts interaction with host and other resources |
| Kubernetes | Container orchestration platform |
| Pod | Smallest deployable Kubernetes unit |
| Service | Stable network endpoint for Pods |
| Ingress | Defines external HTTP/HTTPS routing rules |
| NetworkPolicy | Controls Pod network communication |

---

## 37. Interview and Self-Assessment Questions

### Cloud Networking

1. What is cloud networking?
2. What is a VPC?
3. What is the difference between a VPC and a subnet?
4. What is the difference between public and private subnets?
5. What is an internet gateway?
6. What is a NAT gateway?
7. What is the difference between an internet gateway and a NAT gateway?
8. What is a route table?
9. What is a security group?
10. What is a Network ACL?
11. What is the difference between security groups and NACLs?
12. What is a cloud load balancer?
13. What is a private endpoint?
14. What are cloud network flow logs?
15. Why should databases generally remain in private subnets?
16. What does least-privilege network access mean?

### Container Networking

17. What is a container?
18. What is the difference between a container and a virtual machine?
19. What is a Docker bridge network?
20. What is host networking?
21. What is port publishing?
22. What is the difference between a host port and a container port?
23. How do containers communicate with one another?
24. How does Docker DNS work?
25. What is Docker Compose?
26. How does container isolation work?
27. What are Linux namespaces?
28. What are cgroups?
29. Why is running a container as root risky?
30. What is Kubernetes?
31. What is a Kubernetes Pod?
32. What is a Kubernetes Service?
33. What is Ingress?
34. What is a Kubernetes NetworkPolicy?
35. How can network policies reduce lateral movement?

---

## 38. Final Learning Checklist

### Cloud Networking

- [ ] Understand cloud networking.
- [ ] Understand VPC and VNet.
- [ ] Understand public and private subnets.
- [ ] Understand internet gateways.
- [ ] Understand NAT gateways.
- [ ] Understand route tables.
- [ ] Understand security groups.
- [ ] Understand Network ACLs.
- [ ] Understand cloud load balancers.
- [ ] Understand private endpoints.
- [ ] Understand cloud DNS.
- [ ] Understand cloud network logging.
- [ ] Understand cloud firewall concepts.
- [ ] Identify publicly exposed services.
- [ ] Apply least-privilege network access.

### Container Networking

- [ ] Understand containers.
- [ ] Understand Docker bridge networks.
- [ ] Understand host networking.
- [ ] Understand port publishing.
- [ ] Understand container-to-container communication.
- [ ] Understand Docker DNS.
- [ ] Understand Docker Compose networking.
- [ ] Understand container isolation.
- [ ] Identify container network misconfigurations.
- [ ] Understand Kubernetes networking basics.
- [ ] Understand Services and Ingress.
- [ ] Understand NetworkPolicies.

**End of Phase 14.**
