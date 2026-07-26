"""
Regenerates the sample files used for local preview/download testing when
MinIO credentials are not configured (see views._is_minio_mock).

Not imported by the app at runtime — run manually if these files ever need
to be regenerated:

    venv\\Scripts\\python.exe catalogue\\mock_data\\generate_assets.py
"""
import struct
import zlib
from pathlib import Path

FILES_DIR = Path(__file__).resolve().parent / 'files'


def _png_chunk(tag, data):
    return (
        struct.pack('>I', len(data))
        + tag
        + data
        + struct.pack('>I', zlib.crc32(tag + data) & 0xFFFFFFFF)
    )


def make_sample_photo(path, width=400, height=300):
    """A simple gradient PNG standing in for a real site photo/orthophoto."""
    raw = bytearray()
    for y in range(height):
        raw.append(0)  # filter type: none
        for x in range(width):
            r = int(255 * x / width)
            g = int(255 * y / height)
            b = 180
            raw += bytes([r, g, b])

    compressed = zlib.compress(bytes(raw), 9)
    ihdr = struct.pack('>IIBBBBB', width, height, 8, 2, 0, 0, 0)
    png = (
        b'\x89PNG\r\n\x1a\n'
        + _png_chunk(b'IHDR', ihdr)
        + _png_chunk(b'IDAT', compressed)
        + _png_chunk(b'IEND', b'')
    )
    path.write_bytes(png)


def make_sample_report(path):
    """A minimal, valid single-page PDF standing in for a real report."""
    content = (
        b'BT /F1 18 Tf 72 700 Td (Sample PDF Preview) Tj ET\n'
        b'BT /F1 12 Tf 72 670 Td (Kent Ground Investigation Report - mock data) Tj ET\n'
        b'BT /F1 10 Tf 72 650 Td '
        b'(Set PYCSW_STAC_URL and MinIO credentials in .env for the real document.) Tj ET\n'
    )

    objects = {
        1: b'<< /Type /Catalog /Pages 2 0 R >>',
        2: b'<< /Type /Pages /Kids [3 0 R] /Count 1 >>',
        3: (
            b'<< /Type /Page /Parent 2 0 R /MediaBox [0 0 612 792] '
            b'/Resources << /Font << /F1 5 0 R >> >> /Contents 4 0 R >>'
        ),
        4: b'<< /Length %d >>\nstream\n' % len(content) + content + b'endstream',
        5: b'<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica >>',
    }

    buf = bytearray(b'%PDF-1.4\n')
    offsets = {}
    for num in range(1, 6):
        offsets[num] = len(buf)
        buf += f'{num} 0 obj\n'.encode() + objects[num] + b'\nendobj\n'

    xref_offset = len(buf)
    buf += f'xref\n0 {len(objects) + 1}\n'.encode()
    buf += b'0000000000 65535 f \n'
    for num in range(1, 6):
        buf += f'{offsets[num]:010d} 00000 n \n'.encode()
    buf += b'trailer\n<< /Size 6 /Root 1 0 R >>\nstartxref\n'
    buf += f'{xref_offset}\n'.encode()
    buf += b'%%EOF'

    path.write_bytes(bytes(buf))


if __name__ == '__main__':
    FILES_DIR.mkdir(parents=True, exist_ok=True)
    make_sample_photo(FILES_DIR / 'sample_photo.png')
    make_sample_report(FILES_DIR / 'sample_report.pdf')
    print(f'Wrote sample_photo.png and sample_report.pdf to {FILES_DIR}')
