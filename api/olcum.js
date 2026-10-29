// First-party engagement counters. Never log input values, URL queries, referrers,
// IP addresses, visitor IDs, or WhatsApp message text. Vercel keeps runtime logs;
// these are event totals, not unique visitors, phone calls or registrations.
'use strict';
const pages = new Set(require('./_seo-pages.json'));
const events = new Set(['phone_click','whatsapp_click','whatsapp_auto_open']);
const channels = new Set(['search','social','referral','direct','internal']);
const placements = new Set(['header','footer','assistant','content']);
let windowStart = 0, count = 0;
module.exports = async function(req,res) {
 res.setHeader('Cache-Control','no-store');res.setHeader('X-Robots-Tag','noindex');
 const reply=(code)=>{res.statusCode=code;res.end();};
 if(req.method!=='POST'){res.setHeader('Allow','POST');return reply(405);}
 if(req.headers.origin!=='https://uslusurucukursu.com')return reply(403);
 if(!String(req.headers['content-type']||'').startsWith('application/json'))return reply(415);
 if(Number(req.headers['content-length']||0)>1024)return reply(413);
 let body=req.body;
 try{
  if(body===undefined){let raw='';for await(const chunk of req){raw+=chunk;if(Buffer.byteLength(raw)>1024)return reply(413);}body=raw;}
  if(typeof body==='string')body=JSON.parse(body);
 }catch(_){return reply(400);}
 if(!body||typeof body!=='object'||Array.isArray(body))return reply(400);
 if(Object.keys(body).some(k=>!['event','page','channel','placement'].includes(k)))return reply(400);
 if(!events.has(body.event)||!pages.has(body.page)||!channels.has(body.channel)||!placements.has(body.placement))return reply(400);
 // Instance-wide volume cap; no identifying rate-limit key is collected.
 if(Date.now()-windowStart>=60000){windowStart=Date.now();count=0;}
 if(++count>300)return reply(429);
 console.info(JSON.stringify({metric:'uslu_engagement',event:body.event,page:body.page,channel:body.channel,placement:body.placement}));
 return reply(204);
};
