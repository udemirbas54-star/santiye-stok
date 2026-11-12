import base64, zlib, gzip

raw_b64 = open('p.b64').read().strip()
data = base64.b64decode(raw_b64)

d = zlib.decompressobj(16 + zlib.MAX_WBITS)
out = b''
for i in range(len(data)):
    try:
        out += d.decompress(data[i:i+1])
    except Exception as e:
        print(f"FAILED AT BYTE {i}/{len(data)}: {e}")
        break
print('DECOMPRESSED LEN:', len(out))
print('LAST 300 CHARS:', out[-300:].decode('utf-8', errors='replace'))
