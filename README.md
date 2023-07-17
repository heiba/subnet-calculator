# Subnet Calculator
This project is a web server application that translates a given subnet to its available IP addresses, implemented in Python using Flask and Nginx, and configured with SSL using self-signed certificates.

## Requirements

- Docker
- Docker Compose

## Instructions

Follow the steps below to run the project:

**1. Clone the repository:**

```bash
git clone https://github.com/heiba/subnet-calculator.git
cd subnet-calculator
```

**2. Generate a self-signed certificate:**

If you don't have a certificate already, you can generate a self-signed certificate using OpenSSL:

```bash
openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout selfsigned.key -out selfsigned.crt
```

This will create `selfsigned.key` and `selfsigned.crt` files. Please note that browsers will show a warning when accessing a site secured with a self-signed certificate.

**3. Build and run the Docker services:**

```bash
docker-compose up --build
```

This command will build the Docker images and start the containers for the Flask app and Nginx.

**4. Access the application:**

Open a web browser and navigate to `https://localhost/subnet?subnet=192.168.1.0/24` (or https://<your-server-ip>/subnet?subnet=192.168.1.0/24 if you're running Docker on a remote machine).

You will likely see a warning about the self-signed certificate. You will need to accept the warning to proceed to the website. The web page should return a JSON object listing the available IP addresses in the provided subnet.

## Troubleshooting

If you run into issues, please verify the following:

- Docker and Docker Compose are properly installed on your machine.
- The Docker services are running correctly. You can check this with `docker ps`.
- The self-signed certificate and key files are in the root directory of the project.
- The volume paths in the `docker-compose.yml` file and the certificate paths in the `nginx.conf` file are correct.

## Design Choices

### Web Server: Nginx

Nginx was chosen as the web server as it serves the purpose of a reverse proxy server, and its documentation and implementation are straight forward.

Nginx is renowned for its efficiency and low memory consumption.  Nginx also supports SSL with minimum configuration.  Finally, Nginx's strong community enables us to troubelshoot issues relatively quicker.

### Application Server: Gunicorn

Gunicorn ("Green Unicorn") is a Python WSGI (Web Server Gateway Interface) HTTP Server that's easy to set up and works excellently with Flask applications. It was chosen as the application server for this project due to its compatibility with our application's technology stack and its lightweight and unopinionated nature.

Gunicorn facilitates the communication between our Flask application and Nginx, allowing the web server to interface with the application using the WSGI (Web Server Gateway Interface) protocol. This choice also simplifies the configuration process, as Gunicorn is straightforward to set up and requires minimal additional configuration.

### Web Framework: Flask

Flask is a lightweight and easy-to-use web framework for Python. Its minimalistic, modular and flexible design was a key factor in our choice. With Flask, we have the freedom to choose exactly what components we want to use, making it perfect for a small, focused application like ours.

Flask's simplicity also makes it easy to get our application up and running quickly, and its compatibility with Gunicorn and Nginx makes it a good fit for this project.

### Containerization: Docker

Docker was chosen to simplify the deployment of our application and its dependencies. By using Docker, we can ensure our application runs in the same environment across any platform, making it easier to develop, test, and deploy.

Docker's integration with many CI/CD platforms and cloud providers is also a significant advantage, as it allows us to easily scale and distribute our application.

### Orchestration: Docker Compose

Docker Compose was chosen as our orchestration tool for its simplicity and ease of use in development environments. Docker Compose allows us to define our multi-container application using a simple YAML file, and manage the entire application lifecycle (start, stop, rebuild services, etc.) with a single command.

This is particularly useful for local development and testing, as it allows developers to quickly and easily replicate the application's production environment on their local machine. While Docker Compose can be used in production, in more complex deployments a more powerful orchestration tool like Kubernetes may be preferable.

### Python Library: ipaddress

We chose to use the built-in ipaddress Python library to handle the subnet to IP address translation because of its comprehensive feature set for creating, manipulating, and operating on IPv4 and IPv6 addresses and networks. This library simplifies the task of converting a subnet to its available IP addresses and helps ensure that the IP addresses we generate are valid and correctly formatted.

The ipaddress library is included in the standard Python library and does not require any extra installation, which is an added benefit. It provides a rich set of features to work with: network and address validity checks, iteration over hosting IPs, network and broadcast addresses, etc.

## Security Considerations

If this server was deployed in an infrastructure, there are several security concerns we should consider:

### Use of Self-Signed Certificates
In this project, we used self-signed certificates to enable SSL. In a real-world production environment, self-signed certificates can pose a security risk as they do not provide the level of trust that certificates issued by a Certificate Authority (CA) would. Self-signed certificates will trigger warnings in most web browsers, leading to a poor user experience and potential loss of trust from users. For production environments, we recommend using certificates issued by a well-known CA.

### Regular Patching and Updates
The server's underlying software components (such as Nginx, Gunicorn, Flask, and the operating system itself) should be regularly updated to ensure any known vulnerabilities are patched. Regular patch management can greatly reduce the risk of exploitation.

### Monitoring and Logging
There should be robust monitoring and logging in place to detect any malicious activity or anomalies. This includes network monitoring, application monitoring, and intrusion detection systems.

## Integration in a Microservices Architecture
Integrating this server into a distributed, microservices-oriented, and containerized architecture would involve several steps:

### Dockerization
We have already containerized the individual services (the Flask application and Nginx) using Docker. Containers are the preferred way to package and deploy services in a microservices architecture due to their isolation, portability, and reproducibility.

### Orchestrating Services
Currently, we are using Docker compose to run the 3 containers.

In a distributed environment with multiple microservices, we would use an orchestration tool such as Kubernetes or Docker Swarm. These tools help manage, scale, and maintain the containers. Services can be defined, and their replicas can be managed efficiently using declarative syntax. These tools also offer robust solutions for service discovery, load balancing, and zero-downtime deployments.

### Centralized Logging and Monitoring
Monitoring and logging should be centralized, as microservices could be spread across multiple nodes. Tools like Prometheus for monitoring and the ELK Stack (Elasticsearch, Logstash, Kibana) or DataDog for log management could be used.