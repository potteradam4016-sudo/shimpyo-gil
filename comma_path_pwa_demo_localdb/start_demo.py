import http.server, socketserver, socket, webbrowser, os
from pathlib import Path
PORT=8000
BASE=Path(__file__).resolve().parent
os.chdir(BASE)
def ip():
    s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    try:s.connect(("8.8.8.8",80));return s.getsockname()[0]
    except:return "127.0.0.1"
    finally:s.close()
addr=ip()
print("="*60)
print("쉼표길 PWA 데모")
print(f"PC: http://localhost:{PORT}/")
print(f"휴대폰(같은 Wi-Fi): http://{addr}:{PORT}/")
print("공개 배포 후 HTTPS 주소에서는 '앱 설치'가 가능합니다.")
print("="*60)
try:webbrowser.open(f"http://localhost:{PORT}/")
except:pass
with socketserver.TCPServer(("",PORT),http.server.SimpleHTTPRequestHandler) as h:h.serve_forever()
