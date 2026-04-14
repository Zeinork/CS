import socket
import ssl
import time
import argparse


def main():
    parser = argparse.ArgumentParser(description="HTTP/1.1 client over TCP with optional TLS")
    parser.add_argument("--host", required=True, help="Remote host")
    parser.add_argument("--port", required=True, type=int, help="Remote port")
    parser.add_argument("--path", required=True, help="Request path")
    parser.add_argument("--tls", action="store_true", help="Enable TLS (HTTPS)")
    args = parser.parse_args()

    # request
    request_lines = [
        f"GET {args.path} HTTP/1.1",
        f"Host: {args.host}",
        "User-Agent: cs-ece-356-client/1.0",
        "Connection: close",
        "",
        "",
    ]
    request = "\r\n".join(request_lines)

    #formating
    print("=== Connection Info ===")
    print(f"Host: {args.host}")
    print(f"Port: {args.port}")
    print(f"TLS enabled: {args.tls}")

    print("\n=== Request Sent ===")
    print("\r\n".join(request_lines[:-2]))

    # TCP connect 
    t_tcp_start = time.time()
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((args.host, args.port))
    t_tcp_end = time.time()
    tcp_ms = (t_tcp_end - t_tcp_start) * 1000

    cipher_info = None

    if args.tls:
        # handshake
        context = ssl.create_default_context()
        t_tls_start = time.time()
        sock = context.wrap_socket(sock, server_hostname=args.host)
        t_tls_end = time.time()
        tls_ms = (t_tls_end - t_tls_start) * 1000

        # cipher
        cipher_name, tls_version, key_bits = sock.cipher()
        cipher_info = f"{cipher_name} ({tls_version}, {key_bits}-bit)"
    else:
        tls_ms = None

    if args.tls:
        print("\n=== TLS Info ===")
        print(f"Cipher: {cipher_info}")

    # SR and RR
    t_transfer_start = time.time()
    sock.sendall(request.encode())

    response_bytes = b""
    while True:
        chunk = sock.recv(4096)
        if not chunk:
            break
        response_bytes += chunk

    t_transfer_end = time.time()
    sock.close()

    transfer_ms = (t_transfer_end - t_transfer_start) * 1000

    if args.tls:
        total_ms = tcp_ms + tls_ms + transfer_ms
    else:
        total_ms = tcp_ms + transfer_ms

    # decode and parse
    response = response_bytes.decode("utf-8", errors="replace")
    header_section, _, body = response.partition("\r\n\r\n")
    header_lines = header_section.split("\r\n")

    status_line = header_lines[0]
    response_headers = header_lines[1:]

    print("\n=== Response Summary ===")
    print(f"Status Line: {status_line}")

    print("\n=== Response Headers ===")
    for header in response_headers:
        print(header)

    print("\n=== Body Preview (first 200 chars) ===")
    print(body[:200])

    print("\n=== Timing ===")
    if args.tls:
        print(f"TCP connect time: {tcp_ms:.2f} ms")
        print(f"TLS handshake time: {tls_ms:.2f} ms")
        print(f"Response transfer time: {transfer_ms:.2f} ms")
        print(f"Total transaction time: {total_ms:.2f} ms")
    else:
        print(f"Total transaction time: {total_ms:.2f} ms")


if __name__ == "__main__":
    main()