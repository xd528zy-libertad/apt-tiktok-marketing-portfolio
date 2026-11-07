"""CSV export and SVG chart helpers; standard library only."""
import csv
import html

def safe_cell(value):
    # Prevent copied public text from becoming a spreadsheet formula on export.
    if isinstance(value, str) and value.startswith(('=', '+', '-', '@', '\t', '\r')):
        return "'" + value
    return value

def write_csv(path, fields, rows):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open('w', encoding='utf-8-sig', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fields, extrasaction='ignore')
        writer.writeheader()
        writer.writerows({k: safe_cell(v) for k, v in row.items()} for row in rows)

def chart(path, title, subtitle, entries, percent=False):
    height = max(270, 150 + 46 * len(entries))
    parts = [f'<svg xmlns="http://www.w3.org/2000/svg" width="1100" height="{height}" viewBox="0 0 1100 {height}" role="img" aria-label="{html.escape(title)}">',
             '<rect width="100%" height="100%" fill="#faf9f6"/>',
             '<g font-family="Arial, sans-serif" fill="#222b39">',
             f'<text x="30" y="42" font-size="23" font-weight="bold">{html.escape(title)}</text>',
             f'<text x="30" y="72" font-size="13">{html.escape(subtitle)}</text>']
    if not entries:
        parts += ['<text x="30" y="150" font-size="20">No eligible observations yet.</text>',
                  '<text x="30" y="180" font-size="15">Collect and verify public videos before interpreting performance.</text>']
    else:
        maximum = max([value for _, value, _ in entries if value is not None] + [0]) or 1
        for i, (label, value, n) in enumerate(entries):
            y = 115 + 46 * i
            parts.append(f'<text x="30" y="{y+17}" font-size="13">{html.escape(label)}</text>')
            if value is None:
                parts.append(f'<text x="430" y="{y+17}" font-size="13">Unavailable (valid n={n}; need 3)</text>')
            else:
                width = value / maximum * 470
                display = f'{value:.2%}' if percent else f'{value:g}'
                parts += [f'<rect x="430" y="{y}" width="{width:.2f}" height="24" rx="3" fill="#7465a8"/>',
                          f'<text x="{440+width:.2f}" y="{y+17}" font-size="13">{display} | n={n}</text>']
    parts.append('</g></svg>')
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text('\n'.join(parts), encoding='utf-8')
