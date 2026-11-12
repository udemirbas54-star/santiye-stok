import base64, zlib, gzip

raw_b64 = open('p.b64').read().strip()
print('RAW_B64_LEN:', len(raw_b64))

data = base64.b64decode(raw_b64)
print('DATA_LEN:', len(data))

d = zlib.decompressobj(16 + zlib.MAX_WBITS)
out = b''
for i in range(len(data)):
    try:
        out += d.decompress(data[i:i+1])
    except Exception as e:
        print(f"FAILED AT BYTE {i}/{len(data)}: {e}")
        break
print('DECOMPRESSED SO FAR:', len(out))
