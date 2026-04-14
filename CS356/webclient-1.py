import socket
import time 
import argparse

def main():
    parser = argparse.ArgumentParser(description="Plain HTTP/1.1 client over TCP")
    parser.add_argument("--host",required=True ,help="remote host")
    parser.add_argument("--port", required=True ,type=int, help="remote port")
    parser.add_argument("--path", required=True , help="request path")
    args = parser.parse_args()

    #Request
    request_lines = [
        f"GET {args.path} HTTP/1.1",
        f"Host: {args.host}",
        "User-Agent: cs-ece-356-client/1.0",
        "Connection: close",
        "",
        ""
    ]
    request = "\r\n".join(request_lines)
    print("=== Connection Info ===")
    print(f"Host: {args.host}")
    print(f"Port: {args.port}")

    print("\n=== Request Sent ===")
    print("\r\n".join(request_lines[:-2]))

    #RTT measure start
    t_start = time.time()

    #TCP
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((args.host, args.port))
    sock.sendall(request.encode())

    #Recieve
    response_bytes = b""
    while True:
        chunk = sock.recv(4096)
        if not chunk:
            break
        response_bytes += chunk

    t_end = time.time()
    sock.close()
    total_ms= (t_end - t_start) * 1000

    #Decode
    response = response_bytes.decode("utf-8", errors="replace")
    header_section, _, body = response.partition("\r\n\r\n")
    header_lines = header_section.split("\r\n")
    status_line = header_lines[0]
    headers = header_lines[1:]

    print("\n=== Response Summary ===")
    print(f"Status Line: {status_line}")

    print("\n=== Response Headers ===")
    for header in headers:
        print(header)

    print("\n=== Body Preview (first 200 chars) ===")
    print(body[:200])

    print(f"\n=== Timing ===")
    print(f"Total transaction time: {total_ms:.2f} ms")

if __name__ == "__main__":
    main()