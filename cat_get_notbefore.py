def get_certificate(hostname, port):
    import idna
    from socket import socket
    from OpenSSL import SSL

    sock = socket()
    
    sock.setblocking(True) 
    sock.connect((hostname, port), )
    ctx = SSL.Context(SSL.SSLv23_METHOD)
    ctx.check_hostname = False
    ctx.verify_mode = SSL.VERIFY_NONE

    sock_ssl = SSL.Connection(ctx, sock)
    sock_ssl.set_tlsext_host_name(idna.encode(hostname))  
    sock_ssl.set_connect_state()
    sock_ssl.do_handshake()
    cert = sock_ssl.get_peer_certificate()
    sock_ssl.close()
    sock.close()
    return cert
listurl=[
"https://foundation.shanghai.nyu.edu",
"https://cs.shanghai.nyu.edu",
"https://datascience.shanghai.nyu.edu",
"https://neuro.shanghai.nyu.edu",
"https://cber.shanghai.nyu.edu",
"https://ima.shanghai.nyu.edu",
"https://physics-conference.shanghai.nyu.edu",
"https://econ.shanghai.nyu.edu",
"https://ctl.shanghai.nyu.edu",
"https://arts.shanghai.nyu.edu",
"https://gcs.shanghai.nyu.edu",
"https://nyusps.hospitality-conference.shanghai.nyu.edu",
"https://zaanheh.research.shanghai.nyu.edu",
"https://commencement.shanghai.nyu.edu",
"https://research.shanghai.nyu.edu",
"https://researchsymposium.shanghai.nyu.edu",
"https://staff.shanghai.nyu.edu",
"https://textbooks.shanghai.nyu.edu",
"https://faculty.shanghai.nyu.edu",
"https://students.shanghai.nyu.edu",
"https://stern.shanghai.nyu.edu",
"https://worldlanguages.shanghai.nyu.edu",
"https://cga.shanghai.nyu.edu",
"https://shanghai.nyu.edu",
"https://events.shanghai.nyu.edu",
"https://cdn.shanghai.nyu.edu"]
print (len(listurl))
url=["https://ica.shanghai.nyu.edu"]
#for u in ['https://www.baidu.com/', 'https://mp.weixin.qq.com/', 'https://www.qq.com/']:
for u in url:
    from urllib import parse

    rs = parse.urlparse(u)
    cert = get_certificate(rs.hostname, int(rs.port or 443))
    print(u)
    #print('\ttime:', cert.get_notBefore(), '~', cert.get_notAfter())
    print (cert.get_notBefore()[0:8])
    print (cert.get_notAfter()[0:8])
