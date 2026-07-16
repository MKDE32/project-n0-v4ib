#!/usr/bin/env python3

from dnslib.server import DNSServer, BaseResolver
from dnslib import DNSRecord
import requests


# Google DoH per IP
DOH_URL = "https://8.8.8.8/dns-query"


class DoHResolver(BaseResolver):

    def resolve(self, request, handler):

        # DNS Anfrage in Wire Format
        query = request.pack()

        headers = {
            "Host": "dns.google",
            "Content-Type": "application/dns-message",
            "Accept": "application/dns-message"
        }

        try:
            response = requests.post(
                DOH_URL,
                headers=headers,
                data=query,
                timeout=5,
                verify=True
            )

            response.raise_for_status()

            # Antwort wieder als DNS Paket zurückgeben
            reply = DNSRecord.parse(response.content)

            print(
                f"[+] {request.q.qname} "
                f"{request.q.qtype}"
            )

            return reply


        except Exception as e:

            print(
                f"[!] DoH Fehler: {e}"
            )

            # Fehlerantwort erzeugen
            reply = request.reply()
            reply.header.rcode = 2  # SERVFAIL

            return reply



if __name__ == "__main__":

    resolver = DoHResolver()

    server = DNSServer(
        resolver,
        port=53,
        address="127.0.0.1"
    )

    print(
        "[*] DNS DoH Proxy läuft auf 127.0.0.1:53"
    )

    server.start()
