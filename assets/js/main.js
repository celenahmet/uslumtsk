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
            $(el).owlCarousel({loop: false, margin: partner ? 50 : 30, nav: false, dots: !partner, autoplay: false,
                responsive: {0: {items: partner ? 2 : 1}, 600: {items: 3}, 1000: {items: partner ? 6 : 3}}});
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
