import json, base64, sys
from pathlib import Path

logs = Path(r"C:\Users\omeat\.cursor\browser-logs")
dst = Path(sys.argv[1])
src = max(logs.glob("cdp-response-Page.captureScreenshot-*.json"), key=lambda p: p.stat().st_mtime)
obj = json.loads(src.read_text(encoding="utf-8"))

def find_data(o):
    if isinstance(o, dict):
        if "data" in o and isinstance(o["data"], str) and len(o["data"]) > 100:
            return o["data"]
        for v in o.values():
            r = find_data(v)
            if r:
                return r
    elif isinstance(o, list):
        for v in o:
            r = find_data(v)
            if r:
                return r
    return None

raw = base64.b64decode(find_data(obj))
dst.parent.mkdir(parents=True, exist_ok=True)
dst.write_bytes(raw)
print(f"{src.name} -> {dst} ({len(raw)} bytes)")
