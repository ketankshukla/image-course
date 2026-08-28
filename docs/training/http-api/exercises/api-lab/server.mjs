import {createServer} from 'node:http';
import {pathToFileURL} from 'node:url';
export function makeServer() {
  const records = new Map([['1', {id:'1', title:'MCP foundations'}]]);
  let nextId = 2;
  return createServer(async (req,res) => {
    const send = (status, body, headers={}) => {
      res.writeHead(status, {'Content-Type':'application/json', 'Cache-Control':'no-store', ...headers});
      res.end(JSON.stringify(body));
    };
    const url = new URL(req.url,'http://localhost');
    if(url.pathname !== '/lessons') return send(404,{error:{code:'NOT_FOUND',message:'Unknown route'}});
    if(req.method === 'GET') {
      const raw = url.searchParams.get('limit') ?? '10';
      const offset = url.searchParams.get('offset') ?? '0';
      if(!/^([1-9]|10)$/.test(raw) || !/^\d{1,6}$/.test(offset)) return send(400,{error:{code:'INVALID_PAGE',message:'limit 1–10; offset 0–999999'}});
      return send(200,{items:[...records.values()].slice(Number(offset),Number(offset)+Number(raw)),total:records.size});
    }
    if(req.method !== 'POST') return send(405,{error:{code:'METHOD_NOT_ALLOWED',message:'Use GET or POST'}},{Allow:'GET, POST'});
    if(req.headers['content-type']?.split(';')[0].trim() !== 'application/json') return send(415,{error:{code:'JSON_REQUIRED',message:'Send application/json'}});
    let body='';
    try {
      for await(const chunk of req) {
        body+=chunk.toString();
        if(Buffer.byteLength(body)>4096) return send(413,{error:{code:'TOO_LARGE',message:'Body limit is 4096 bytes'}});
      }
      let data;
      try { data=JSON.parse(body); } catch { return send(400,{error:{code:'INVALID_JSON',message:'Body is not valid JSON'}}); }
      if(!data || typeof data.title!=='string' || !data.title.trim() || data.title.trim().length>80) return send(400,{error:{code:'INVALID_TITLE',message:'title must contain 1–80 characters'}});
      const title=data.title.trim();
      if([...records.values()].some(x=>x.title===title)) return send(409,{error:{code:'DUPLICATE_TITLE',message:'This title already exists'}});
      const item={id:String(nextId++),title}; records.set(item.id,item);
      return send(201,item);
    } catch { if(!res.headersSent) send(500,{error:{code:'INTERNAL',message:'Request could not be completed'}}); }
  });
}
if(process.argv[1] && import.meta.url===pathToFileURL(process.argv[1]).href) makeServer().listen(4175,'127.0.0.1',()=>console.log('API Lab http://127.0.0.1:4175/lessons'));
