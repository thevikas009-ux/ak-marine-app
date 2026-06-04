<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>AK Mehra – Marine Fiberglass Experts</title>
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700;900&family=DM+Sans:wght@300;400;500;600&display=swap" rel="stylesheet">
<style>
  :root {
    --navy: #0a1f3d;
    --navy-mid: #12336b;
    --gold: #c9a84c;
    --gold-light: #e8c97a;
    --sea: #1a6e8e;
    --sea-light: #2fa4cc;
    --cream: #f5f0e8;
    --white: #ffffff;
    --text: #2c2c2c;
    --text-light: #6b7280;
    --card-bg: #ffffff;
  }
  *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
  html { scroll-behavior: smooth; }
  body { font-family: 'DM Sans', sans-serif; background: var(--navy); color: var(--white); overflow-x: hidden; }

  /* ─── NAV ─── */
  nav {
    position: fixed; top: 0; left: 0; right: 0; z-index: 1000;
    display: flex; align-items: center; justify-content: space-between;
    padding: 18px 6vw;
    background: rgba(10,31,61,0.92);
    backdrop-filter: blur(12px);
    border-bottom: 1px solid rgba(201,168,76,0.2);
    transition: all .3s;
  }
  .nav-logo { font-family: 'Playfair Display', serif; font-size: 1.6rem; color: var(--gold); letter-spacing: 1px; }
  .nav-logo span { color: var(--white); font-size: 0.8rem; display: block; font-family: 'DM Sans', sans-serif; font-weight: 300; letter-spacing: 4px; margin-top: -4px; }
  .nav-links { display: flex; gap: 32px; list-style: none; }
  .nav-links a { color: rgba(255,255,255,0.85); text-decoration: none; font-size: .93rem; letter-spacing: 1px; font-weight: 500; transition: color .2s; }
  .nav-links a:hover { color: var(--gold); }
  .nav-toggle { display: none; flex-direction: column; gap: 5px; cursor: pointer; }
  .nav-toggle span { width: 26px; height: 2px; background: var(--gold); border-radius: 2px; }

  /* ─── HERO ─── */
  #hero {
    min-height: 100vh;
    background: linear-gradient(135deg, var(--navy) 0%, #0d2c5a 50%, #0e3a6e 100%);
    display: flex; flex-direction: column; justify-content: center;
    padding: 120px 6vw 80px;
    position: relative; overflow: hidden;
  }
  .hero-waves { position: absolute; bottom: 0; left: 0; right: 0; height: 120px; opacity: .18; }
  .hero-decor { position: absolute; top: 10%; right: 5%; width: 380px; height: 380px; border-radius: 50%; border: 1px solid rgba(201,168,76,.15); animation: pulse 6s ease-in-out infinite; }
  .hero-decor2 { position: absolute; top: 15%; right: 8%; width: 260px; height: 260px; border-radius: 50%; border: 1px solid rgba(47,164,204,.2); animation: pulse 8s ease-in-out infinite reverse; }
  @keyframes pulse { 0%,100%{transform:scale(1);opacity:.6} 50%{transform:scale(1.08);opacity:1} }
  .hero-badge { display: inline-block; background: rgba(201,168,76,.15); border: 1px solid var(--gold); color: var(--gold); font-size: .78rem; letter-spacing: 3px; padding: 6px 18px; border-radius: 20px; margin-bottom: 24px; animation: fadeUp .8s ease both; }
  .hero h1 { font-family: 'Playfair Display', serif; font-size: clamp(2.8rem,6vw,5.5rem); font-weight: 900; line-height: 1.1; animation: fadeUp .8s .15s ease both; }
  .hero h1 em { font-style: normal; color: var(--gold); }
  .hero-sub { font-size: 1.1rem; color: rgba(255,255,255,.75); margin: 22px 0 36px; max-width: 520px; font-weight: 300; line-height: 1.7; animation: fadeUp .8s .3s ease both; }
  .hero-stats { display: flex; gap: 40px; flex-wrap: wrap; animation: fadeUp .8s .45s ease both; }
  .stat { text-align: center; }
  .stat-num { font-family: 'Playfair Display', serif; font-size: 2.4rem; font-weight: 700; color: var(--gold); line-height: 1; }
  .stat-label { font-size: .78rem; letter-spacing: 2px; color: rgba(255,255,255,.6); margin-top: 4px; }
  .hero-btns { margin-top: 40px; display: flex; gap: 16px; flex-wrap: wrap; animation: fadeUp .8s .6s ease both; }
  .btn-primary { background: var(--gold); color: var(--navy); padding: 14px 32px; border-radius: 6px; font-weight: 600; text-decoration: none; transition: all .25s; font-size: .95rem; }
  .btn-primary:hover { background: var(--gold-light); transform: translateY(-2px); box-shadow: 0 8px 24px rgba(201,168,76,.35); }
  .btn-outline { border: 1.5px solid rgba(255,255,255,.4); color: var(--white); padding: 14px 32px; border-radius: 6px; font-weight: 500; text-decoration: none; transition: all .25s; font-size: .95rem; }
  .btn-outline:hover { border-color: var(--gold); color: var(--gold); }
  @keyframes fadeUp { from{opacity:0;transform:translateY(28px)} to{opacity:1;transform:translateY(0)} }

  /* ─── SECTION BASE ─── */
  section { padding: 90px 6vw; }
  .section-label { font-size: .75rem; letter-spacing: 4px; color: var(--gold); text-transform: uppercase; margin-bottom: 10px; }
  .section-title { font-family: 'Playfair Display', serif; font-size: clamp(1.8rem, 3.5vw, 3rem); font-weight: 700; line-height: 1.2; }
  .section-line { width: 60px; height: 3px; background: var(--gold); border-radius: 2px; margin: 16px 0 40px; }

  /* ─── ABOUT / OWNER ─── */
  #about { background: var(--cream); color: var(--navy); }
  .about-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 60px; align-items: center; }
  .about-text .section-title { color: var(--navy); }
  .about-text p { color: #4a5568; line-height: 1.8; margin-bottom: 16px; font-size: 1rem; }
  .exp-badge { display: inline-flex; align-items: center; gap: 12px; background: var(--navy); color: var(--white); padding: 12px 22px; border-radius: 8px; margin: 16px 0; }
  .exp-badge strong { font-family: 'Playfair Display', serif; font-size: 2rem; color: var(--gold); }
  .owner-card { position: relative; }
  .owner-img-wrap { border-radius: 16px; overflow: hidden; box-shadow: 0 30px 60px rgba(10,31,61,.25); position: relative; background: linear-gradient(135deg, var(--navy) 0%, var(--sea) 100%); min-height: 380px; display: flex; align-items: center; justify-content: center; }
  .owner-placeholder { text-align: center; padding: 40px; }
  .owner-placeholder svg { opacity: .5; }
  .owner-placeholder p { color: rgba(255,255,255,.6); margin-top: 12px; font-size: .85rem; }
  .owner-img-wrap img { width: 100%; height: 100%; object-fit: cover; border-radius: 16px; }
  .owner-tag { position: absolute; bottom: -20px; left: 20px; background: var(--gold); color: var(--navy); padding: 12px 20px; border-radius: 8px; font-weight: 600; font-size: .9rem; box-shadow: 0 8px 24px rgba(201,168,76,.4); }

  /* ─── SERVICES ─── */
  #services { background: #f8fafc; color: var(--navy); }
  #services .section-title { color: var(--navy); }
  .services-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 24px; }
  .service-card { background: var(--white); padding: 32px 28px; border-radius: 14px; border-top: 4px solid var(--navy); box-shadow: 0 4px 20px rgba(0,0,0,.07); transition: all .3s; }
  .service-card:hover { transform: translateY(-6px); box-shadow: 0 16px 40px rgba(10,31,61,.15); border-top-color: var(--gold); }
  .service-num { font-family: 'Playfair Display', serif; font-size: 2rem; color: var(--gold); font-weight: 900; opacity: .5; }
  .service-card h4 { font-size: 1.1rem; font-weight: 600; color: var(--navy); margin: 8px 0; }
  .service-card p { color: #6b7280; font-size: .92rem; line-height: 1.65; }

  /* ─── GALLERY ─── */
  #gallery { background: var(--navy); }
  .gallery-header { display: flex; justify-content: space-between; align-items: flex-end; flex-wrap: wrap; gap: 20px; margin-bottom: 36px; }
  .slider-wrap { position: relative; overflow: hidden; border-radius: 16px; }
  .slider-track { display: flex; transition: transform .6s cubic-bezier(.4,0,.2,1); will-change: transform; }
  .slide { min-width: 100%; position: relative; height: 480px; }
  .slide img { width: 100%; height: 100%; object-fit: cover; border-radius: 16px; }
  .slide-placeholder { width: 100%; height: 100%; background: linear-gradient(135deg, var(--navy-mid), var(--sea)); border-radius: 16px; display: flex; align-items: center; justify-content: center; flex-direction: column; gap: 16px; }
  .slide-placeholder svg { opacity: .3; }
  .slide-placeholder p { color: rgba(255,255,255,.5); font-size: .9rem; }
  .slide-caption { position: absolute; bottom: 0; left: 0; right: 0; background: linear-gradient(to top, rgba(10,31,61,.9) 0%, transparent 100%); padding: 32px 24px 20px; border-radius: 0 0 16px 16px; font-size: .9rem; color: rgba(255,255,255,.85); }
  .slider-btn { position: absolute; top: 50%; transform: translateY(-50%); background: rgba(201,168,76,.9); border: none; color: var(--navy); width: 44px; height: 44px; border-radius: 50%; cursor: pointer; font-size: 1.2rem; display: flex; align-items: center; justify-content: center; z-index: 10; transition: all .2s; }
  .slider-btn:hover { background: var(--gold-light); transform: translateY(-50%) scale(1.1); }
  .slider-btn.prev { left: 16px; }
  .slider-btn.next { right: 16px; }
  .slider-dots { display: flex; justify-content: center; gap: 8px; margin-top: 20px; flex-wrap: wrap; }
  .dot { width: 8px; height: 8px; border-radius: 50%; background: rgba(255,255,255,.3); border: none; cursor: pointer; transition: all .2s; }
  .dot.active { background: var(--gold); width: 24px; border-radius: 4px; }
  .thumbs { display: flex; gap: 12px; margin-top: 16px; overflow-x: auto; padding-bottom: 8px; }
  .thumb { min-width: 80px; height: 60px; border-radius: 8px; object-fit: cover; border: 2px solid transparent; cursor: pointer; transition: all .2s; }
  .thumb.active { border-color: var(--gold); }
  .thumb-placeholder { min-width: 80px; height: 60px; border-radius: 8px; background: rgba(255,255,255,.1); display: flex; align-items: center; justify-content: center; font-size: .65rem; color: rgba(255,255,255,.4); border: 2px solid transparent; cursor: pointer; }
  .thumb-placeholder.active { border-color: var(--gold); }

  /* ─── ADMIN PANEL ─── */
  #admin-section { background: #0e2445; padding: 60px 6vw; }
  .admin-toggle-btn { background: transparent; border: 1.5px solid rgba(201,168,76,.4); color: var(--gold); padding: 10px 24px; border-radius: 6px; cursor: pointer; font-size: .88rem; letter-spacing: 1px; transition: all .2s; }
  .admin-toggle-btn:hover { background: rgba(201,168,76,.1); }
  #admin-panel { display: none; margin-top: 28px; background: rgba(255,255,255,.04); border: 1px solid rgba(201,168,76,.15); border-radius: 14px; padding: 32px; }
  #admin-panel.visible { display: block; animation: fadeUp .4s ease; }
  .admin-login { max-width: 360px; }
  .admin-login h3 { font-family: 'Playfair Display', serif; font-size: 1.4rem; color: var(--gold); margin-bottom: 20px; }
  .form-group { margin-bottom: 16px; }
  .form-group label { display: block; font-size: .85rem; color: rgba(255,255,255,.7); margin-bottom: 6px; }
  .form-group input { width: 100%; padding: 10px 14px; background: rgba(255,255,255,.08); border: 1px solid rgba(255,255,255,.15); border-radius: 6px; color: var(--white); font-size: .95rem; outline: none; transition: border .2s; }
  .form-group input:focus { border-color: var(--gold); }
  .btn-login { background: var(--gold); color: var(--navy); padding: 10px 28px; border: none; border-radius: 6px; font-weight: 600; cursor: pointer; font-size: .95rem; transition: all .2s; }
  .btn-login:hover { background: var(--gold-light); }
  .admin-upload { display: none; }
  .admin-upload.visible { display: block; animation: fadeUp .4s ease; }
  .admin-upload h3 { font-family: 'Playfair Display', serif; color: var(--gold); margin-bottom: 20px; }
  .upload-area { border: 2px dashed rgba(201,168,76,.4); border-radius: 12px; padding: 40px; text-align: center; cursor: pointer; transition: all .2s; }
  .upload-area:hover, .upload-area.dragover { border-color: var(--gold); background: rgba(201,168,76,.05); }
  .upload-area svg { margin: 0 auto 12px; opacity: .5; }
  .upload-area p { color: rgba(255,255,255,.6); font-size: .9rem; }
  #file-input { display: none; }
  .btn-upload { background: var(--sea); color: var(--white); padding: 10px 24px; border: none; border-radius: 6px; font-weight: 600; cursor: pointer; margin-top: 16px; transition: all .2s; }
  .btn-upload:hover { background: var(--sea-light); }
  .preview-list { display: flex; flex-wrap: wrap; gap: 12px; margin-top: 20px; }
  .preview-item { position: relative; width: 90px; height: 70px; border-radius: 8px; overflow: hidden; }
  .preview-item img { width: 100%; height: 100%; object-fit: cover; }
  .preview-item button { position: absolute; top: 2px; right: 2px; background: rgba(220,38,38,.85); border: none; color: white; width: 18px; height: 18px; border-radius: 50%; cursor: pointer; font-size: .7rem; display: flex; align-items: center; justify-content: center; }
  .admin-gallery-list { margin-top: 24px; }
  .admin-gallery-list h4 { font-size: .95rem; color: rgba(255,255,255,.8); margin-bottom: 14px; }
  .gallery-admin-grid { display: flex; flex-wrap: wrap; gap: 12px; }
  .gal-item { position: relative; width: 100px; height: 76px; border-radius: 8px; overflow: hidden; }
  .gal-item img { width: 100%; height: 100%; object-fit: cover; }
  .gal-item .del-btn { position: absolute; top: 3px; right: 3px; background: rgba(220,38,38,.9); border: none; color: white; width: 20px; height: 20px; border-radius: 50%; cursor: pointer; font-size: .7rem; display: flex; align-items: center; justify-content: center; transition: transform .15s; }
  .gal-item .del-btn:hover { transform: scale(1.15); }
  .msg { font-size: .85rem; margin-top: 10px; padding: 8px 14px; border-radius: 6px; }
  .msg.success { background: rgba(34,197,94,.15); color: #4ade80; }
  .msg.error { background: rgba(239,68,68,.15); color: #f87171; }

  /* ─── CONTACT ─── */
  #contact { background: var(--cream); color: var(--navy); }
  #contact .section-title { color: var(--navy); }
  .contact-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 60px; }
  .contact-info p { color: #4a5568; margin-bottom: 24px; line-height: 1.7; }
  .contact-item { display: flex; align-items: flex-start; gap: 14px; margin-bottom: 20px; }
  .contact-icon { width: 42px; height: 42px; background: var(--navy); border-radius: 10px; display: flex; align-items: center; justify-content: center; flex-shrink: 0; }
  .contact-icon svg { width: 20px; height: 20px; }
  .contact-item strong { display: block; font-size: .78rem; letter-spacing: 1px; color: #9ca3af; margin-bottom: 2px; }
  .contact-item span { color: var(--navy); font-weight: 500; }
  .contact-form { display: flex; flex-direction: column; gap: 16px; }
  .cf-input { padding: 12px 16px; border: 1.5px solid #e2e8f0; border-radius: 8px; font-size: .95rem; outline: none; transition: border .2s; font-family: inherit; background: white; }
  .cf-input:focus { border-color: var(--navy); }
  textarea.cf-input { resize: vertical; min-height: 120px; }
  .btn-send { background: var(--navy); color: var(--white); padding: 13px; border: none; border-radius: 8px; font-weight: 600; cursor: pointer; font-size: .95rem; transition: all .2s; }
  .btn-send:hover { background: var(--navy-mid); transform: translateY(-2px); }

  /* ─── FOOTER ─── */
  footer { background: #060f1e; padding: 40px 6vw; text-align: center; border-top: 1px solid rgba(201,168,76,.15); }
  footer p { color: rgba(255,255,255,.4); font-size: .85rem; }
  footer .footer-brand { font-family: 'Playfair Display', serif; font-size: 1.3rem; color: var(--gold); margin-bottom: 10px; }

  /* ─── RESPONSIVE ─── */
  @media (max-width: 768px) {
    .nav-links { display: none; flex-direction: column; position: absolute; top: 100%; left: 0; right: 0; background: var(--navy); padding: 20px; gap: 16px; }
    .nav-links.open { display: flex; }
    .nav-toggle { display: flex; }
    .about-grid, .contact-grid { grid-template-columns: 1fr; }
    .owner-card { order: -1; }
    .slide { height: 280px; }
    .hero-stats { gap: 24px; }
  }
</style>
</head>
<body>

<!-- NAV -->
<nav id="navbar">
  <div class="nav-logo">AK Mehra<span>Marine Fiberglass Experts</span></div>
  <ul class="nav-links" id="nav-links">
    <li><a href="#hero">Home</a></li>
    <li><a href="#about">About</a></li>
    <li><a href="#services">Services</a></li>
    <li><a href="#gallery">Gallery</a></li>
    <li><a href="#contact">Contact</a></li>
  </ul>
  <div class="nav-toggle" onclick="document.getElementById('nav-links').classList.toggle('open')">
    <span></span><span></span><span></span>
  </div>
</nav>

<!-- HERO -->
<section id="hero">
  <div class="hero-decor"></div>
  <div class="hero-decor2"></div>
  <div class="hero-badge">🚢 Trusted Since 1989</div>
  <h1>Crafting the <em>Finest</em><br>Marine Vessels</h1>
  <p class="hero-sub">AK Mehra brings 35+ years of fiberglass mastery to every boat we build, repair, and finish — trusted by fishermen and fleet operators across the coast.</p>
  <div class="hero-stats">
    <div class="stat"><div class="stat-num">35+</div><div class="stat-label">Years Experience</div></div>
    <div class="stat"><div class="stat-num">500+</div><div class="stat-label">Boats Built</div></div>
    <div class="stat"><div class="stat-num">100%</div><div class="stat-label">Quality Assured</div></div>
  </div>
  <div class="hero-btns">
    <a href="#services" class="btn-primary">Our Services</a>
    <a href="#gallery" class="btn-outline">View Gallery</a>
  </div>
  <svg class="hero-waves" viewBox="0 0 1440 120" fill="none" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="none">
    <path d="M0,60 C360,120 1080,0 1440,60 L1440,120 L0,120 Z" fill="white"/>
  </svg>
</section>

<!-- ABOUT -->
<section id="about">
  <div class="about-grid">
    <div class="about-text">
      <div class="section-label">About Us</div>
      <h2 class="section-title">35 Years of Marine Excellence</h2>
      <div class="section-line"></div>
      <p>AK Mehra is a legacy marine fiberglass company founded by a master craftsman with an unmatched passion for the sea. For over three decades, we have been building, repairing, and perfecting marine vessels that withstand the harshest ocean conditions.</p>
      <p>Our expertise spans custom boat manufacturing, structural repairs, premium gelcoat finishing, and specialized marine installations — all executed with the precision and pride that has made us the most trusted name in the business.</p>
      <div class="exp-badge">
        <strong>35+</strong>
        <span>Years of Proven<br>Fiberglass Expertise</span>
      </div>
      <p>Every vessel that leaves our workshop is a testament to quality, durability, and craftsmanship that our clients rely on — season after season.</p>
    </div>
    <div class="owner-card">
      <div class="owner-img-wrap" id="owner-img-wrap">
        <!-- Owner image: replace src below with actual photo path -->
        <!-- <img src="owner.jpg" alt="AK Mehra - Founder"> -->
        <div class="owner-placeholder">
          <svg width="80" height="80" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="1.5"><circle cx="12" cy="8" r="4"/><path d="M4 20c0-4 3.6-7 8-7s8 3 8 7"/></svg>
          <p>Owner Photo<br><small>Place owner.jpg in same folder</small></p>
        </div>
      </div>
      <div class="owner-tag">A.K. Mehra — Founder &amp; Master Craftsman</div>
    </div>
  </div>
</section>

<!-- SERVICES -->
<section id="services">
  <div class="section-label">What We Do</div>
  <h2 class="section-title">Our Marine Services</h2>
  <div class="section-line"></div>
  <div class="services-grid">
    <div class="service-card"><div class="service-num">01</div><h4>Boat Manufacturing</h4><p>Custom fiberglass vessels built with high seawater resistance and precision engineering for long-lasting performance.</p></div>
    <div class="service-card"><div class="service-num">02</div><h4>Repair &amp; Maintenance</h4><p>Complete restoration and preventive servicing for all types of boats — hull repairs, structural work, and full overhauls.</p></div>
    <div class="service-card"><div class="service-num">03</div><h4>Gelcoat Finishing</h4><p>Premium protective coating applications for long-lasting marine performance, shine, and resistance to saltwater damage.</p></div>
    <div class="service-card"><div class="service-num">04</div><h4>Fish Storage Tank</h4><p>Manufacturing and installation of durable fiberglass fish storage tanks designed specifically for marine environments.</p></div>
    <div class="service-card"><div class="service-num">05</div><h4>Reinforcement &amp; Modification</h4><p>Structural strengthening, hull modifications, deck upgrades, and custom marine solutions tailored to your needs.</p></div>
    <div class="service-card"><div class="service-num">06</div><h4>Boat Ice Box &amp; Cabin Fitting</h4><p>Custom ice box fabrication, cabin fitting, interior modifications, and utility installations for optimal comfort at sea.</p></div>
    <div class="service-card"><div class="service-num">07</div><h4>Boat Ice Box &amp; Cabin Making</h4><p>End-to-end custom ice box and cabin making — designed, built, and fitted by our experienced marine craftsmen.</p></div>
  </div>
</section>

<!-- GALLERY -->
<section id="gallery">
  <div class="gallery-header">
    <div>
      <div class="section-label">Our Work</div>
      <h2 class="section-title">Project Gallery</h2>
      <div class="section-line"></div>
    </div>
  </div>
  <div class="slider-wrap">
    <div class="slider-track" id="slider-track"></div>
    <button class="slider-btn prev" onclick="moveSlide(-1)">&#8592;</button>
    <button class="slider-btn next" onclick="moveSlide(1)">&#8594;</button>
  </div>
  <div class="slider-dots" id="slider-dots"></div>
  <div class="thumbs" id="thumbs"></div>
</section>

<!-- ADMIN SECTION -->
<div id="admin-section">
  <div style="display:flex;align-items:center;gap:16px;flex-wrap:wrap;">
    <span style="color:rgba(255,255,255,.5);font-size:.85rem;">Admin Access:</span>
    <button class="admin-toggle-btn" onclick="toggleAdmin()">🔐 Admin Panel</button>
  </div>
  <div id="admin-panel">
    <!-- LOGIN -->
    <div class="admin-login" id="admin-login">
      <h3>Admin Login</h3>
      <div class="form-group">
        <label>Username</label>
        <input type="text" id="admin-user" placeholder="Enter username">
      </div>
      <div class="form-group">
        <label>Password</label>
        <input type="password" id="admin-pass" placeholder="Enter password">
      </div>
      <button class="btn-login" onclick="adminLogin()">Login</button>
      <div id="login-msg" class="msg" style="display:none"></div>
      <p style="margin-top:14px;color:rgba(255,255,255,.4);font-size:.78rem;">Default: admin / akmehra2024</p>
    </div>
    <!-- UPLOAD -->
    <div class="admin-upload" id="admin-upload">
      <h3>📸 Upload Gallery Photos</h3>
      <div class="upload-area" id="upload-area" onclick="document.getElementById('file-input').click()" ondragover="handleDrag(event,true)" ondragleave="handleDrag(event,false)" ondrop="handleDrop(event)">
        <svg width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="1.5" style="display:block;margin:0 auto 12px"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="17 8 12 3 7 8"/><line x1="12" y1="3" x2="12" y2="15"/></svg>
        <p>Click to select photos, or drag &amp; drop here</p>
        <p style="font-size:.78rem;margin-top:6px;color:rgba(255,255,255,.4)">JPG, PNG, WEBP supported</p>
      </div>
      <input type="file" id="file-input" accept="image/*" multiple onchange="handleFiles(this.files)">
      <div class="preview-list" id="preview-list"></div>
      <div style="display:flex;gap:12px;align-items:center;flex-wrap:wrap;margin-top:12px;">
        <button class="btn-upload" onclick="uploadImages()">💾 Save to Gallery</button>
        <button onclick="adminLogout()" style="background:transparent;border:1px solid rgba(255,255,255,.2);color:rgba(255,255,255,.6);padding:10px 18px;border-radius:6px;cursor:pointer;font-size:.85rem;">Logout</button>
      </div>
      <div id="upload-msg" class="msg" style="display:none"></div>
      <div class="admin-gallery-list">
        <h4>Saved Gallery Images</h4>
        <div class="gallery-admin-grid" id="gallery-admin-grid"></div>
      </div>
    </div>
  </div>
</div>

<!-- CONTACT -->
<section id="contact">
  <div class="contact-grid">
    <div class="contact-info">
      <div class="section-label">Get In Touch</div>
      <h2 class="section-title">Contact Us</h2>
      <div class="section-line"></div>
      <p>Have a project in mind? Need a repair estimate? We'd love to hear from you. Reach out and our team will respond promptly.</p>
      <div class="contact-item">
        <div class="contact-icon">
          <svg viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="2"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07A19.5 19.5 0 0 1 4.69 13.5 19.79 19.79 0 0 1 1.61 4.88 2 2 0 0 1 3.59 2.68h3a2 2 0 0 1 2 1.72c.127.96.361 1.903.7 2.81a2 2 0 0 1-.45 2.11L7.91 10.1a16 16 0 0 0 6 6l1.47-1.47a2 2 0 0 1 2.11-.45c.907.339 1.85.573 2.81.7A2 2 0 0 1 22 16.92z"/></svg>
        </div>
        <div><strong>Phone</strong><span>+91 XXXXX XXXXX</span></div>
      </div>
      <div class="contact-item">
        <div class="contact-icon">
          <svg viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="2"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/><polyline points="22,6 12,13 2,6"/></svg>
        </div>
        <div><strong>Email</strong><span>info@akmehra.com</span></div>
      </div>
      <div class="contact-item">
        <div class="contact-icon">
          <svg viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="2"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg>
        </div>
        <div><strong>Location</strong><span>Coastal Workshop, India</span></div>
      </div>
    </div>
    <div>
      <div class="contact-form">
        <input class="cf-input" type="text" placeholder="Your Name" id="cf-name">
        <input class="cf-input" type="tel" placeholder="Phone Number" id="cf-phone">
        <input class="cf-input" type="email" placeholder="Email Address" id="cf-email">
        <textarea class="cf-input" placeholder="Tell us about your project..." id="cf-msg"></textarea>
        <button class="btn-send" onclick="sendMessage()">Send Message →</button>
        <div id="contact-msg" class="msg" style="display:none"></div>
      </div>
    </div>
  </div>
</section>

<!-- FOOTER -->
<footer>
  <div class="footer-brand">AK Mehra</div>
  <p>Marine Fiberglass Experts &nbsp;|&nbsp; Est. 1989 &nbsp;|&nbsp; 35+ Years of Excellence</p>
  <p style="margin-top:8px;">© 2024 AK Mehra. All rights reserved.</p>
</footer>

<script>
// ─── STORAGE KEY ───
const GALLERY_KEY = 'akmehra_gallery';

// ─── GALLERY DATA ───
let galleryImages = [];
let currentSlide = 0;
let slideInterval;

function loadGallery() {
  try {
    const saved = localStorage.getItem(GALLERY_KEY);
    if (saved) galleryImages = JSON.parse(saved);
  } catch(e) { galleryImages = []; }
}

function saveGallery() {
  try { localStorage.setItem(GALLERY_KEY, JSON.stringify(galleryImages)); } catch(e) {}
}

// ─── SLIDER ───
function renderSlider() {
  const track = document.getElementById('slider-track');
  const dots = document.getElementById('slider-dots');
  const thumbsEl = document.getElementById('thumbs');
  track.innerHTML = ''; dots.innerHTML = ''; thumbsEl.innerHTML = '';

  if (galleryImages.length === 0) {
    track.innerHTML = `<div class="slide"><div class="slide-placeholder">
      <svg width="64" height="64" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="1.5"><rect x="3" y="3" width="18" height="18" rx="2"/><circle cx="8.5" cy="8.5" r="1.5"/><polyline points="21 15 16 10 5 21"/></svg>
      <p>Gallery photos will appear here after upload</p></div></div>`;
    return;
  }

  galleryImages.forEach((img, i) => {
    // Slide
    const slide = document.createElement('div');
    slide.className = 'slide';
    slide.innerHTML = `<img src="${img.src}" alt="Gallery ${i+1}"><div class="slide-caption">${img.caption || 'AK Mehra – Marine Work'}</div>`;
    track.appendChild(slide);
    // Dot
    const dot = document.createElement('button');
    dot.className = 'dot' + (i===0?' active':'');
    dot.onclick = () => goToSlide(i);
    dots.appendChild(dot);
    // Thumb
    const thumb = document.createElement('img');
    thumb.src = img.src; thumb.className = 'thumb' + (i===0?' active':'');
    thumb.onclick = () => goToSlide(i);
    thumbsEl.appendChild(thumb);
  });

  goToSlide(0);
  startAuto();
}

function goToSlide(idx) {
  if (galleryImages.length === 0) return;
  currentSlide = (idx + galleryImages.length) % galleryImages.length;
  document.getElementById('slider-track').style.transform = `translateX(-${currentSlide * 100}%)`;
  document.querySelectorAll('.dot').forEach((d,i) => d.classList.toggle('active', i===currentSlide));
  document.querySelectorAll('.thumb, .thumb-placeholder').forEach((t,i) => t.classList.toggle('active', i===currentSlide));
}

function moveSlide(dir) { goToSlide(currentSlide + dir); resetAuto(); }

function startAuto() {
  clearInterval(slideInterval);
  if (galleryImages.length > 1) slideInterval = setInterval(() => goToSlide(currentSlide+1), 4000);
}
function resetAuto() { startAuto(); }

// ─── ADMIN ───
let isAdminOpen = false, isLoggedIn = false;
const ADMIN_USER = 'admin', ADMIN_PASS = 'akmehra2024';
let pendingFiles = [];

function toggleAdmin() {
  isAdminOpen = !isAdminOpen;
  const panel = document.getElementById('admin-panel');
  panel.classList.toggle('visible', isAdminOpen);
}

function adminLogin() {
  const u = document.getElementById('admin-user').value.trim();
  const p = document.getElementById('admin-pass').value;
  const msg = document.getElementById('login-msg');
  if (u === ADMIN_USER && p === ADMIN_PASS) {
    isLoggedIn = true;
    document.getElementById('admin-login').style.display = 'none';
    document.getElementById('admin-upload').classList.add('visible');
    renderAdminGrid();
  } else {
    msg.style.display = 'block'; msg.className = 'msg error'; msg.textContent = 'Invalid credentials.';
  }
}

function adminLogout() {
  isLoggedIn = false;
  document.getElementById('admin-login').style.display = 'block';
  document.getElementById('admin-upload').classList.remove('visible');
  document.getElementById('admin-user').value = '';
  document.getElementById('admin-pass').value = '';
}

function handleDrag(e, over) {
  e.preventDefault();
  document.getElementById('upload-area').classList.toggle('dragover', over);
}
function handleDrop(e) {
  e.preventDefault();
  document.getElementById('upload-area').classList.remove('dragover');
  handleFiles(e.dataTransfer.files);
}

function handleFiles(files) {
  Array.from(files).forEach(file => {
    if (!file.type.startsWith('image/')) return;
    const reader = new FileReader();
    reader.onload = (e) => {
      pendingFiles.push({ src: e.target.result, caption: '' });
      renderPreviews();
    };
    reader.readAsDataURL(file);
  });
}

function renderPreviews() {
  const list = document.getElementById('preview-list');
  list.innerHTML = '';
  pendingFiles.forEach((f, i) => {
    const div = document.createElement('div');
    div.className = 'preview-item';
    div.innerHTML = `<img src="${f.src}" alt="preview"><button onclick="removePending(${i})">✕</button>`;
    list.appendChild(div);
  });
}

function removePending(i) { pendingFiles.splice(i,1); renderPreviews(); }

function uploadImages() {
  const msg = document.getElementById('upload-msg');
  if (pendingFiles.length === 0) {
    msg.style.display='block'; msg.className='msg error'; msg.textContent='Please select at least one image.'; return;
  }
  galleryImages = [...galleryImages, ...pendingFiles];
  saveGallery();
  renderSlider();
  renderAdminGrid();
  pendingFiles = [];
  renderPreviews();
  msg.style.display='block'; msg.className='msg success'; msg.textContent=`✅ ${pendingFiles.length || galleryImages.length} photo(s) saved to gallery!`;
  setTimeout(() => msg.style.display='none', 3500);
}

function renderAdminGrid() {
  const grid = document.getElementById('gallery-admin-grid');
  grid.innerHTML = '';
  if (galleryImages.length === 0) { grid.innerHTML = '<p style="color:rgba(255,255,255,.4);font-size:.85rem;">No images in gallery yet.</p>'; return; }
  galleryImages.forEach((img,i) => {
    const div = document.createElement('div');
    div.className = 'gal-item';
    div.innerHTML = `<img src="${img.src}" alt="gal ${i}"><button class="del-btn" onclick="deleteGalleryImg(${i})">✕</button>`;
    grid.appendChild(div);
  });
}

function deleteGalleryImg(i) {
  if (!confirm('Delete this image from gallery?')) return;
  galleryImages.splice(i,1);
  saveGallery();
  renderSlider();
  renderAdminGrid();
}

// ─── CONTACT ───
function sendMessage() {
  const name = document.getElementById('cf-name').value.trim();
  const phone = document.getElementById('cf-phone').value.trim();
  const msg = document.getElementById('cf-msg').value.trim();
  const cmsg = document.getElementById('contact-msg');
  if (!name || !msg) {
    cmsg.style.display='block'; cmsg.className='msg error'; cmsg.textContent='Please fill name and message.'; return;
  }
  // WhatsApp link as simple contact
  const text = encodeURIComponent(`Hi AK Mehra,\nName: ${name}\nPhone: ${phone}\nMessage: ${msg}`);
  window.open(`https://wa.me/91XXXXXXXXXX?text=${text}`, '_blank');
  cmsg.style.display='block'; cmsg.className='msg success'; cmsg.textContent='✅ Opening WhatsApp... Or call us directly!';
}

// ─── INIT ───
loadGallery();
renderSlider();

// Navbar scroll effect
window.addEventListener('scroll', () => {
  document.getElementById('navbar').style.boxShadow = window.scrollY > 50 ? '0 4px 20px rgba(0,0,0,.4)' : 'none';
});

// Intersection observer for fade-in
const observer = new IntersectionObserver((entries) => {
  entries.forEach(e => { if (e.isIntersecting) { e.target.style.opacity='1'; e.target.style.transform='translateY(0)'; } });
}, { threshold: 0.1 });
document.querySelectorAll('.service-card').forEach(el => {
  el.style.opacity='0'; el.style.transform='translateY(20px)'; el.style.transition='opacity .5s ease, transform .5s ease';
  observer.observe(el);
});
</script>
</body>
</html>
