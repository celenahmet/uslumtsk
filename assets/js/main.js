/* Progressive enhancement: load gallery/carousel libraries only when needed. */
(() => {
    'use strict';
    const reducedMotion = matchMedia('(prefers-reduced-motion: reduce)').matches;
    const english = document.documentElement.lang === 'en';
    const scripts = new Map();
    function load(src) {
        if (!scripts.has(src)) scripts.set(src, new Promise((resolve, reject) => {
            const script = document.createElement('script');
            script.src = src; script.onload = resolve; script.onerror = reject;
            document.head.appendChild(script);
        }));
        return scripts.get(src);
    }
    async function plugin(name) {
        await load('/assets/js/jquery-3.6.0.min.js');
        await load('/assets/js/' + name);
        return window.jQuery;
    }
    function nearViewport(elements, init) {
        if (!('IntersectionObserver' in window)) {elements.forEach(init); return;}
        const observer = new IntersectionObserver(entries => entries.forEach(entry => {
            if (entry.isIntersecting) {observer.unobserve(entry.target); init(entry.target);}
        }), {rootMargin: '300px'});
        elements.forEach(el => observer.observe(el));
    }
    nearViewport(document.querySelectorAll('.partner-slider, .testimonial-slider'), async el => {
        try {
            const $ = await plugin('owl.carousel.min.js');
            const partner = el.classList.contains('partner-slider');
            // Logo şeridi eskisi gibi sürekli döner (Uslu + MEB ikişer ikişer, 6 logo);
            // "hareketi azalt" tercihinde dönmez.
            const still = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
            $(el).owlCarousel(partner
                ? {loop: true, margin: 50, nav: false, dots: false, autoplay: !still, autoplayTimeout: 2500,
                   autoplayHoverPause: true, smartSpeed: 800, responsive: {0: {items: 2}, 600: {items: 3}, 1000: {items: 4}}}
                : {loop: false, margin: 30, nav: false, dots: true, autoplay: false,
                   responsive: {0: {items: 1}, 600: {items: 3}, 1000: {items: 3}}});
            el.querySelectorAll('.owl-dot').forEach((button,i) => button.setAttribute('aria-label', english ? `Review group ${i+1}` : `Yorum grubu ${i+1}`));
        } catch {el.style.overflowX = 'auto';}
    });
    document.querySelectorAll('.popup-gallery').forEach(gallery => {
        gallery.addEventListener('click', async event => {
            const anchor = event.target.closest('.popup-img');
            if (!anchor) return;
            event.preventDefault();
            try {
                const $ = await plugin('jquery.magnific-popup.min.js');
                const anchors = [...gallery.querySelectorAll('.popup-img')];
                $.magnificPopup.open({items: anchors.map(a=>({src:a.href})),type:'image',gallery:{enabled:true}}, anchors.indexOf(anchor));
            } catch {location.href = anchor.href;}
        });
    });
    document.querySelectorAll('.popup-youtube, .popup-vimeo, .popup-gmaps').forEach(anchor => anchor.addEventListener('click', async event => {
        event.preventDefault();
        try {const $ = await plugin('jquery.magnific-popup.min.js'); $.magnificPopup.open({items:{src:anchor.href},type:'iframe'});}
        catch {location.href=anchor.href;}
    }));
    nearViewport(document.querySelectorAll('.filter-box'), async el => {
        try {
            const $ = await plugin('isotope.pkgd.min.js');
            const grid = $(el).isotope({itemSelector:'.filter-item',masonry:{columnWidth:1}});
            el.querySelectorAll('img').forEach(img=>img.addEventListener('load',()=>grid.isotope('layout')));
            document.querySelectorAll('.filter-btns [data-filter]').forEach(button=>button.addEventListener('click',()=>{
                grid.isotope({filter:button.dataset.filter});
                button.parentElement.querySelectorAll('.active').forEach(b=>b.classList.remove('active'));
                button.classList.add('active');
            }));
        } catch { /* The unfiltered gallery remains visible. */ }
    });
    nearViewport(document.querySelectorAll('[data-background]'), el=>{el.style.backgroundImage=`url("${el.dataset.background}")`;});
    // Tanıtım videosu: kapak ve video adresi bölüme yaklaşınca verilir; preload="none" olduğu için
    // video dosyası yalnız oynatılınca iner, sayfanın açılışına yük bindirmez.
    // Araç tanıtım videosu: önizleme kareleri bölüme yaklaşınca iner ve yalnız görünürken döner;
    // video YALNIZ oynat'a basınca oluşturulur, öncesinde hiç istek atılmaz.
    document.querySelectorAll('.video-frame[data-video-src]').forEach(frame=>{
        const stage=frame.closest('.video-stage')||frame;
        nearViewport([stage], ()=>stage.querySelectorAll('img[data-src]').forEach(img=>{img.src=img.dataset.src;}));
        if ('IntersectionObserver' in window) new IntersectionObserver(entries=>entries.forEach(entry=>frame.classList.toggle('is-visible', entry.isIntersecting))).observe(frame);
        else frame.classList.add('is-visible');
        frame.querySelector('.video-play')?.addEventListener('click', ()=>{
            const video=document.createElement('video');
            video.src=frame.dataset.videoSrc; video.controls=true; video.playsInline=true; video.preload='auto';
            video.setAttribute('aria-label', frame.dataset.videoLabel||'');
            const first=frame.querySelector('.video-preview img');
            if (first && first.currentSrc) video.poster=first.currentSrc;
            frame.querySelector('.video-screen').appendChild(video);
            frame.classList.add('is-playing');
            // Oynarken bölümün alt şeridinde sakin bir yarış (Ahmet 30.09): paralele yakın 3 şeritli yol,
            // üstünde yukarıdan görünen 3 araç aynı pakette ilerleyip birbirini sollar. Yalnız video
            // oynarken hareket eder; hareket azaltma tercihinde hiç oluşturulmaz. SVG statik, girdi yok.
            const area=frame.closest('.video-area');
            let track=area&&area.querySelector('.video-track');
            if (area && !track && !matchMedia('(prefers-reduced-motion: reduce)').matches) {
                const wave='C 240 {a}, 480 {b}, 720 {c} S 1200 {d}, 1560 {e}';
                const lane=(y)=>`M -140 ${y} `+wave.replace('{a}',y-18).replace('{b}',y+18).replace('{c}',y-2).replace('{d}',y-20).replace('{e}',y);
                const car=(id,body,glass,roof,extra)=>`<g id="${id}"><ellipse cx="2" cy="3" rx="34" ry="15" fill="#000" opacity=".28"/><rect x="-32" y="-14" width="64" height="28" rx="9" fill="${body}"/><path d="M9 -11.5 L17 -9.5 Q20.5 0 17 9.5 L9 11.5 Q11 0 9 -11.5Z" fill="${glass}"/><path d="M-14 -11 L-20 -8.5 Q-22.5 0 -20 8.5 L-14 11 Q-15.5 0 -14 -11Z" fill="${glass}"/><rect x="-13" y="-10.5" width="21" height="21" rx="4" fill="${roof}"/><rect x="5" y="-16.5" width="3" height="3" rx="1" fill="${body}"/><rect x="5" y="13.5" width="3" height="3" rx="1" fill="${body}"/><rect x="28" y="-11" width="3" height="5" rx="1.2" fill="#fff4cc"/><rect x="28" y="6" width="3" height="5" rx="1.2" fill="#fff4cc"/><rect x="-32" y="-11" width="2.5" height="5" rx="1" fill="#e2334f"/><rect x="-32" y="6" width="2.5" height="5" rx="1" fill="#e2334f"/>${extra}</g>`;
                const move=(href,laneId,begin,points)=>`<use href="#${href}"><animateMotion dur="14s" begin="${begin}" repeatCount="indefinite" rotate="auto" calcMode="linear" keyTimes="0;0.33;0.66;1" keyPoints="${points}"><mpath href="#${laneId}"/></animateMotion></use>`;
                const svg=document.createElementNS('http://www.w3.org/2000/svg','svg');
                svg.setAttribute('class','video-track'); svg.setAttribute('aria-hidden','true'); svg.setAttribute('focusable','false');
                svg.setAttribute('viewBox','0 0 1440 170'); svg.setAttribute('preserveAspectRatio','xMidYMax slice');
                svg.innerHTML=`<defs><path id="vt-l1" d="${lane(52)}"/><path id="vt-l2" d="${lane(88)}"/><path id="vt-l3" d="${lane(124)}"/>`
                    +car('vt-uslu','#f4f6f9','#0d2743','#dde3ea','<rect x="-7" y="-7.5" width="7" height="15" rx="1.6" fill="#cb1643"/>')
                    +car('vt-kirmizi','#b3142f','#140c14','#9a1028','')+car('vt-grafit','#56657a','#0c1622','#4a586b','')+'</defs>'
                    +`<path d="${lane(88)}" fill="none" stroke="#fff" stroke-opacity=".035" stroke-width="112"/>`
                    +`<path d="${lane(34)}" fill="none" stroke="#fff" stroke-opacity=".16" stroke-width="2"/><path d="${lane(142)}" fill="none" stroke="#fff" stroke-opacity=".16" stroke-width="2"/>`
                    +`<path d="${lane(70)}" fill="none" stroke="#fff" stroke-opacity=".14" stroke-width="2" stroke-dasharray="22 18"/><path d="${lane(106)}" fill="none" stroke="#fff" stroke-opacity=".14" stroke-width="2" stroke-dasharray="22 18"/>`
                    +move('vt-grafit','vt-l1','-0.7s','0;0.36;0.66;1')+move('vt-uslu','vt-l2','0s','0;0.30;0.63;1')+move('vt-kirmizi','vt-l3','-0.35s','0;0.34;0.70;1');
                area.prepend(svg); track=svg; svg.pauseAnimations?.();
            }
            // Video başlayınca yarış başlar ve video durunca/bitince de sürer (Ahmet 30.09); yalnız bölüm
            // ekrandan çıkınca bekler, geri gelince kaldığı yerden devam eder.
            if (area && track) video.addEventListener('play', ()=>{
                area.classList.add('is-racing'); track.unpauseAnimations?.();
                if ('IntersectionObserver' in window) new IntersectionObserver(entries=>entries.forEach(entry=>{
                    if (entry.isIntersecting) track.unpauseAnimations?.(); else track.pauseAnimations?.();
                })).observe(area);
            }, {once:true});
            video.play().catch(()=>{});
            video.focus({preventScroll:true});
        }, {once:true});
    });
    const top = document.getElementById('scroll-top');
    if (top) {
        const update=()=>{top.style.display=scrollY>100?'inline-block':'none';};
        addEventListener('scroll',update,{passive:true});update();
        top.addEventListener('click',event=>{event.preventDefault();scrollTo({top:0,behavior:reducedMotion?'instant':'smooth'});});
    }
    document.querySelectorAll('#date').forEach(el=>{el.textContent=new Date().getFullYear();});
    // Tawk.to canlı destek kaldırıldı (28.09.2026): yerine WhatsApp teklif asistanı,
    // /assets/js/uslu-widgets.js.
})();
