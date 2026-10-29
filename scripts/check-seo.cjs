// Focused regressions for course differentiation, contextual links and privacy-safe counters.
'use strict';
const assert=require('node:assert/strict'),fs=require('node:fs'),vm=require('node:vm');
const data=JSON.parse(fs.readFileSync('content/course-seo.json'));
const intros=new Set();
for(const [key,c] of Object.entries(data)){
 const file='egitim/'+(key==='index'?'':key+'/')+'index.html';const html=fs.readFileSync(file,'utf8');
 assert(html.includes(c.intro),file+' intro');assert(html.includes(c.h1),file+' heading');
 assert(!html.includes('+12 Saat Ortalama'),file+' stale fixed duration');
 assert(!html.includes('Aile hekimliğinden Ücretsiz'),file+' unsupported free report');
 assert(!html.includes('online ve yüz yüze ders seçenekleri'),file+' unsupported services');
 assert(html.includes('course-seo-faq'),file+' visible questions');
 const doc=JSON.parse(html.match(/<script type="application\/ld\+json">(.*?)<\/script>/s)[1]);
 const service=doc['@graph'].find(x=>x['@type']==='Service');assert.equal(service.name,c.h1);
 const page=doc['@graph'].find(x=>x['@type']==='WebPage');assert.equal(page.description,c.description);assert.equal(page.name,c.title);
 intros.add(c.intro);
}
assert.equal(intros.size,8);
let guides=0;for(const d of fs.readdirSync('rehber',{withFileTypes:true})){if(!d.isDirectory())continue;const p='rehber/'+d.name+'/index.html';if(!fs.existsSync(p))continue;const s=fs.readFileSync(p,'utf8');assert.equal((s.match(/<!-- related course start -->/g)||[]).length,1,p);guides++;}assert.equal(guides,50);

const measure=require('../api/olcum.js');let logs=[];const original=console.info;console.info=m=>logs.push(JSON.parse(m));
function request(body,origin='https://uslusurucukursu.com',method='POST'){const req={method,headers:{origin,'content-type':'application/json'},body};const res={headers:{},setHeader(k,v){this.headers[k]=v;},end(){}};return measure(req,res).then(()=>res.statusCode);}
(async()=>{
 const event={event:'phone_click',page:'/egitim/motor-a2/',channel:'search',placement:'content'};
 assert.equal(await request(event),204);assert.equal(logs.length,1);assert.deepEqual(Object.keys(logs[0]).sort(),['metric','event','page','channel','placement'].sort());
 assert.equal(await request({...event,phone:'05321234568'}),400);assert.equal(await request({...event,page:'/anything?name=private'}),400);assert.equal(await request({...event,event:'form_success'}),400);assert.equal(await request(event,'https://attacker.invalid'),403);assert.equal(await request(event,undefined,'GET'),405);assert.equal(logs.length,1);
 // Successful leads are recorded by the delivery handler, never a public client claim.
 const delivery=require('../api/iletisim.js'), originalFetch=global.fetch;
 const oldKey=process.env.RESEND_API_KEY,oldTo=process.env.CONTACT_TO;
 process.env.RESEND_API_KEY='test-only';process.env.CONTACT_TO='test@example.invalid';
 let sent=0;global.fetch=async()=>{sent++;return {ok:true,status:200};};
 const req={method:'POST',headers:{origin:'https://uslusurucukursu.com','content-type':'application/json','x-forwarded-for':'test-fixture'},body:{source:'form',lang:'tr',name:'Ayşe Yılmaz',phone:'05321234568',email:'',topic:'kayit',message:'Kayıt hakkında bilgi almak istiyorum',kvkk:true,t:10000,website:''}};
 const res={setHeader(){},end(){}};
 try{await delivery(req,res);assert.equal(res.statusCode,200);assert.equal(sent,1);const accepted=logs.find(x=>x.metric==='uslu_lead_delivery');assert.deepEqual(accepted,{metric:'uslu_lead_delivery',source:'form',lang:'tr',channel:'unmeasured',status:'accepted'});assert(!JSON.stringify(accepted).includes('Ayşe'));}
 finally{global.fetch=originalFetch;if(oldKey===undefined)delete process.env.RESEND_API_KEY;else process.env.RESEND_API_KEY=oldKey;if(oldTo===undefined)delete process.env.CONTACT_TO;else process.env.CONTACT_TO=oldTo;}
 console.info=original;
 function browserFixture(privacy={},referrer='https://www.google.com/search?q=private+query',storedChannel=null){const out=[],listeners={};const body={};const context={location:{hostname:'uslusurucukursu.com',pathname:'/egitim/motor-a2/',href:'https://uslusurucukursu.com/egitim/motor-a2/',origin:'https://uslusurucukursu.com'},document:{referrer:referrer,addEventListener:(k,fn)=>listeners[k]=fn},sessionStorage:{getItem:()=>storedChannel,setItem(){}},navigator:{...privacy,sendBeacon:(url,blob)=>{out.push(blob);return true;}},window:{},URL,Blob};vm.runInNewContext(fs.readFileSync('assets/js/seo-events.js','utf8'),context);return {context,out,listeners};}
 let b=browserFixture();const anchor={closest:()=>null,getAttribute:()=> 'https://wa.me/905320685647?text=PRIVATE-MESSAGE'};const e={target:{closest:()=>anchor}};b.listeners.click(e);b.listeners.click(e);assert.equal(b.out.length,1);const payload=JSON.parse(await b.out[0].text());assert.equal(payload.channel,'search');assert.equal(payload.event,'whatsapp_click');assert(!JSON.stringify(payload).includes('PRIVATE'));assert(!JSON.stringify(payload).includes('private'));
 b.context.window.usluWhatsAppOpened();assert.equal(b.out.length,2);assert.equal(JSON.parse(await b.out[1].text()).event,'whatsapp_auto_open');
 b=browserFixture({},'https://uslusurucukursu.com/rehber/','search');b.listeners.click(e);assert.equal(JSON.parse(await b.out[0].text()).channel,'search');
 b=browserFixture({doNotTrack:'1'});assert.equal(b.listeners.click,undefined);b=browserFixture({globalPrivacyControl:true});assert.equal(b.listeners.click,undefined);
 console.log('PASS: 8 distinct courses, 50 contextual guide sections, event allowlists, no input/query leakage, deduplication, DNT/GPC');
})().catch(e=>{console.info=original;console.error(e);process.exitCode=1;});
