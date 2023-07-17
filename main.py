# This is a simple python app that translates a given subnet to its available IP addresses. Running on Docker,
# exposed via nginx.

from flask import Flask, request
from ipaddress import ip_network

app = Flask(__name__)


@app.route('/subnet')
def subnet_to_ips():
    subnet = request.args.get('subnet')
    ip_addresses = [str(ip) for ip in ip_network(subnet).hosts()]
    return {
        "subnet": subnet,
        "available_ips": ip_addresses
    }


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
