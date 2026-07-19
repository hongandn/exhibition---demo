import json
from pathlib import Path
p = Path('wikidata-item.ipynb')
nb = json.loads(p.read_text(encoding='utf-8'))
print('cells', len(nb.get('cells', [])))
for idx, cell in enumerate(nb.get('cells', [])):
    if cell.get('cell_type') == 'code':
        print('CELL', idx)
        src = ''.join(cell.get('source', []))
        if 'bindings = fetch_sparql_bindings' in src or 'item_id' in src:
            print(src)
        for out in cell.get('outputs', []):
            if 'data' in out:
                print('OUTPUT DATA KEYS', list(out['data'].keys()))
                if 'text/plain' in out['data']:
                    print('TEXT/PLAIN', ''.join(out['data']['text/plain']))
                if 'text/html' in out['data']:
                    print('TEXT/HTML', ''.join(out['data']['text/html'])[:4000])
            if 'text' in out:
                print('TEXT', ''.join(out['text']))
