# This is a simple python app that translates a given subnet to its available IP addresses.

from flask import Flask, request, jsonify
from ipaddress import ip_network, AddressValueError

app = Flask(__name__)


@app.route('/subnet')
def subnet_to_ips():
    subnet = request.args.get('subnet')
    if not subnet:
        return jsonify(error='No subnet provided.'), 400

    try:
        ip_addresses = [str(ip) for ip in ip_network(subnet).hosts()]
    except (ValueError, AddressValueError) as e:
        return jsonify(error=str(e)), 400

    return {
        "subnet": subnet,
        "available_ips": ip_addresses
    }


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
