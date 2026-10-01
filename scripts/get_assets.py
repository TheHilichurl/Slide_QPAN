import urllib.request
import re
import json

def fetch_dainam_images():
    urls = [
        'https://dainam.edu.vn/vi/tin-tuc',
        'https://dainam.edu.vn/vi/khoa-hoc-quan-su',
        'https://dainam.edu.vn/vi/sinh-vien'
    ]
    found = set()
    for u in urls:
        try:
            req = urllib.request.Request(u, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
            txt = urllib.request.urlopen(req, timeout=5).read().decode('utf-8', errors='ignore')
            matches = re.findall(r'https://dainam\.edu\.vn/upload/[^\"\'\s>]+\.(?:jpg|png|jpeg)', txt)
            for m in matches:
                found.add(m)
        except Exception as e:
            print('Error on', u, ':', e)
    return list(found)

if __name__ == '__main__':
    imgs = fetch_dainam_images()
    print(f'Found {len(imgs)} images on dainam.edu.vn:')
    for img in imgs[:10]:
        print(img)
