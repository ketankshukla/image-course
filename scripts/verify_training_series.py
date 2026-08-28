"""Verify local labs and reading artifacts; explicitly exclude unavailable Docker execution."""
from pathlib import Path
import importlib.util
import json
import subprocess
import sys
import threading
from http.server import HTTPServer
from html.parser import HTMLParser
from urllib.request import urlopen
from urllib.error import HTTPError

ROOT=Path(__file__).resolve().parent.parent
TRAINING=ROOT/'docs/training'
def run(args,cwd):
    result=subprocess.run(args,cwd=cwd,text=True,capture_output=True,timeout=60)
    if result.returncode:
        raise AssertionError(result.stdout+result.stderr)
    print(result.stdout.strip())

run(['node','--test','test.mjs'],TRAINING/'http-api/exercises/api-lab')
for slug in ['git-team','databases','identity','configuration','background-jobs','observability','refactoring','performance']:
    run([sys.executable,'lab.py'],TRAINING/slug/'exercises')
run([sys.executable,'test.py'],TRAINING/'codebase/exercises/reader-lab')

spec=importlib.util.spec_from_file_location('container_lab',TRAINING/'docker/exercises/container-lab/app.py')
module=importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
server=HTTPServer(('127.0.0.1',0),module.Handler)
thread=threading.Thread(target=server.serve_forever,daemon=True)
thread.start()
try:
    base=f'http://127.0.0.1:{server.server_port}'
    with urlopen(base+'/health',timeout=5) as response:
        assert response.status==200
        assert json.load(response)=={'status':'ok','service':'container-lab'}
    try: urlopen(base+'/missing',timeout=5)
    except HTTPError as error:
        assert error.code==404
        assert json.load(error)=={'error':'not_found'}
    else: raise AssertionError('Expected 404')
finally:
    server.shutdown();server.server_close();thread.join()
print('PASS: Python container service HTTP behavior. NOT RUN: Docker image build/container execution.')

class Reading(HTMLParser):
    def __init__(self):
        super().__init__();self.images=[];self.links=[];self.ids=set()
    def handle_starttag(self,tag,attrs):
        values=dict(attrs)
        if 'id' in values:self.ids.add(values['id'])
        if tag=='img' and values.get('id')!='diagram-large':self.images.append(values.get('src',''))
        if tag=='a':self.links.append(values.get('href',''))
catalog=json.loads((TRAINING/'series.json').read_text(encoding='utf-8'))
assert len(catalog)==12 and len({x['id'] for x in catalog})==12
for course in catalog:
    source=TRAINING/course['slug']/course['file']
    text=source.read_text(encoding='utf-8')
    assert text.count('## Lesson ')>=6,source
    page=source.with_suffix('.html')
    parsed=Reading();parsed.feed(page.read_text(encoding='utf-8'))
    assert parsed.images and all(x.startswith('data:') for x in parsed.images),page
    assert all(x[1:] in parsed.ids for x in parsed.links if x.startswith('#')),page
index=Reading();index.feed((TRAINING/'START-HERE.html').read_text(encoding='utf-8'))
local=[x for x in index.links if not x.startswith(('#','http:','https:'))]
assert len(local)==15 and all(x.endswith('.html') and (TRAINING/x).is_file() for x in local)
print('PASS: 12 new course editions, embedded diagrams, section anchors, and 15 HTML index links.')
print('Browser simulation requires interaction checks; no full accessibility audit claimed.')
