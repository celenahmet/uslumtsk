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
            // Oynarken arka planda yarış hissi: hız çizgileri (Ahmet 30.09). Yalnız video oynarken akar.
            const area=frame.closest('.video-area');
            if (area && !area.querySelector('.video-race') && !matchMedia('(prefers-reduced-motion: reduce)').matches) {
                const race=document.createElement('div');
                race.className='video-race'; race.setAttribute('aria-hidden','true');
                for (let i=0;i<16;i++) {
                    const line=document.createElement('span');
                    if (i%4===1) line.className='is-red';
                    line.style.top=(4+i*6)+'%';
                    line.style.width=(70+(i*53)%190)+'px';
                    line.style.animationDuration=(0.7+((i*37)%9)/10)+'s';
                    line.style.animationDelay=(-((i*29)%10)/10)+'s';
                    race.appendChild(line);
                }
                area.prepend(race);
            }
            video.addEventListener('play', ()=>area?.classList.add('is-racing'));
            ['pause','ended'].forEach(name=>video.addEventListener(name, ()=>area?.classList.remove('is-racing')));
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
