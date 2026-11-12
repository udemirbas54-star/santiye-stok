import base64, gzip, json, urllib.request

old = urllib.request.urlopen('https://raw.githubusercontent.com/udemirbas54-star/santiye-stok/main/index.html').read().decode('utf-8').replace('\r\n','\n').split('\n')
ops = json.loads(gzip.decompress(base64.b64decode(open('p.b64').read().strip())).decode('utf-8'))
out = []
for op in ops:
    if op.startswith('@'):
        s, c = map(int, op[1:].split(':'))
        out.extend(old[s:s+c])
    else:
        out.append(op[1:])
res = '\n'.join(out)
open('index.html', 'w', encoding='utf-8').write(res)
print('PATCH_OK_LEN:', len(res))
