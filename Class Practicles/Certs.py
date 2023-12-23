import ssl
cert = ssl.get_server_certificate(('imap.gmail.com',993))

if not cert:
    print(cert)

