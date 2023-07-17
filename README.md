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