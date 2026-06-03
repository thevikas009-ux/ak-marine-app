import streamlit as st
import streamlit.components.v1 as components

# 1. Page Configuration
st.set_page_config(page_title="AK Mehra – Fiberglass & Boat Specialists", layout="wide")

# 2. FULL SCREEN & GAP FIX
st.markdown("""
    <style>
        #MainMenu, header, footer { visibility: hidden; height: 0px; }
        .block-container { padding: 0rem !important; max-width: 100% !important; }
        iframe { display: block; border: none; width: 100% !important; }
    </style>
""", unsafe_allow_html=True)

# 3. COMPLETE SOURCE CODE (ALL DATA RESTORED)
html_content = r"""
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>AK Mehra Marine</title>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,600;1,400&family=Jost:wght@300;400;500&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://unpkg.com/leaflet/dist/leaflet.css"/>
<style>
  *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
  :root { --navy: #0d2640; --navy-mid: #153352; --blue: #1a5f8a; --sky: #5ba4cf; --sky-light: #a8d4f0; --cream: #f5f0e8; --gold: #c8a96e; --white: #ffffff; }
  html { scroll-behavior: smooth; }
  body { font-family: 'Jost', sans-serif; background: var(--cream); color: #0d1f33; overflow-x: hidden; }

  /* NAV */
  nav { position: fixed; top: 0; left: 0; right: 0; z-index: 1000; background: rgba(13,38,64,0.98); display: flex; align-items: center; justify-content: space-between; padding: 0 5vw; height: 64px; border-bottom: 1px solid rgba(91,164,207,0.25); }
  .nav-brand { font-family: 'Cormorant Garamond', serif; font-size: 1.5rem; font-weight: 600; color: var(--sky-light); }
  .nav-links { display: flex; gap: 2rem; list-style: none; }
  .nav-links a { color: rgba(255,255,255,0.7); text-decoration: none; font-size: 0.8rem; text-transform: uppercase; letter-spacing: 1px; }

  /* HERO */
  .hero { min-height: 100vh; background: linear-gradient(160deg, var(--navy) 0%, var(--navy-mid) 55%, var(--blue) 100%); display: flex; align-items: center; padding: 100px 5vw 60px; position: relative; }
  .hero-inner { max-width: 1200px; margin: 0 auto; display: grid; grid-template-columns: 1fr 1fr; gap: 4rem; align-items: center; }
  .hero h1 { font-family: 'Cormorant Garamond', serif; font-size: clamp(3rem, 5vw, 5rem); color: #fff; line-height: 1.1; }
  .hero h1 em { font-style: italic; color: var(--sky-light); }
  .hero-stats { display: grid; grid-template-columns: 1fr 1fr; gap: 1px; margin-top: 2rem; background: rgba(91,164,207,0.2); }
  .stat-item { background: rgba(13,38,64,0.6); padding: 1rem; text-align: center; }
  .stat-num { font-family: 'Cormorant Garamond', serif; font-size: 2rem; color: var(--sky-light); font-weight: 600; }
  .stat-label { font-size: 0.7rem; color: #fff; opacity: 0.7; text-transform: uppercase; }
  .hero-photo-frame { width: 100%; max-width: 400px; aspect-ratio: 3/4; padding: 10px; border: 1px solid rgba(255,255,255,0.1); margin: 0 auto; }
  .hero-photo-frame img { width: 100%; height: 100%; object-fit: cover; }

  /* SECTIONS */
  section { padding: 5rem 5vw; }
  .section-title { font-family: 'Cormorant Garamond', serif; font-size: 2.5rem; color: var(--navy); margin-bottom: 2rem; }
  
  /* SERVICES - ALL 6 RESTORED */
  .services-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 20px; }
  .service-card { background: #fff; padding: 30px; border-radius: 8px; border-top: 4px solid var(--navy); box-shadow: 0 5px 15px rgba(0,0,0,0.05); }
  .service-card h3 { font-size: 2rem; color: var(--navy); margin-bottom: 10px; }

  /* ABOUT BADGE */
  .exp-badge { display: flex; align-items: center; gap: 1rem; padding: 1.5rem; border: 1px solid #ddd; margin: 1rem 0; }
  .exp-num { font-size: 3rem; font-family: serif; color: var(--blue); }

  /* GALLERY MOVING */
  #gallery { background: var(--navy); overflow: hidden; padding: 4rem 0; }
  .gallery-grid { display: flex; gap: 20px; width: max-content; animation: scrollGallery 40s linear infinite; }
  .gallery-item { width: 300px; height: 220px; flex-shrink: 0; border-radius: 10px; overflow: hidden; }
  .gallery-item img { width: 100%; height: 100%; object-fit: cover; }
  @keyframes scrollGallery { 0% { transform: translateX(0); } 100% { transform: translateX(-50%); } }

  /* CONTACT INFO WITH EMAIL RESTORED */
  .contact-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 3rem; }
  .info-row { display: flex; align-items: flex-start; gap: 1rem; padding: 1rem 0; border-bottom: 1px solid #eee; }
  .icon-box { width: 40px; height: 40px; background: var(--navy); display: flex; align-items: center; justify-content: center; border-radius: 4px; flex-shrink: 0; }
  .icon-box svg { width: 20px; fill: var(--sky-light); }
  .info-text h4 { font-size: 0.8rem; color: var(--blue); text-transform: uppercase; }
  .info-text a { color: var(--navy); text-decoration: none; font-weight: 500; }

  /* MAP */
  #map { height: 450px; width: 100%; border-radius: 10px; border: 1px solid #ddd; }

  footer { background: var(--navy); color: #fff; padding: 2rem; text-align: center; opacity: 0.5; font-size: 0.8rem; }
</style>
</head>
<body>

<nav>
  <div class="nav-brand">A K Mehra</div>
  <ul class="nav-links">
    <li><a href="#about">About</a></li>
    <li><a href="#services">Services</a></li>
    <li><a href="#gallery">Gallery</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><button id="admin-login-btn" style="background:none; border:1px solid var(--gold); color:var(--gold); padding:4px 10px; cursor:pointer;">Admin</button></li>
  </ul>
</nav>

<section class="hero">
  <div class="hero-inner">
    <div>
      <p style="color:var(--sky); letter-spacing:3px;">EST. SINCE 1990</p>
      <h1>Masters of<br><em>Fiberglass</em><br>& the Sea</h1>
      <p style="color:rgba(255,255,255,0.7); margin: 1.5rem 0;">Over 35 years of expertise in fishing boat manufacturing and structural marine repairs in Maharashtra.</p>
      <div class="hero-stats">
        <div class="stat-item"><div class="stat-num">35+</div><div class="stat-label">Years Exp</div></div>
        <div class="stat-item"><div class="stat-num">07</div><div class="stat-label">Services</div></div>
        <div class="stat-item"><div class="stat-num">100%</div><div class="stat-label">Quality</div></div>
        <div class="stat-item"><div class="stat-num">∞</div><div class="stat-label">Clients</div></div>
      </div>
      <a href="#contact" style="display:inline-block; margin-top:2rem; padding:12px 30px; border:1px solid var(--sky); color:var(--sky-light); text-decoration:none;">GET IN TOUCH</a>
    </div>
    <div class="hero-photo-frame">
      <img src="https://images.unsplash.com/photo-1559136555-9303baea8ebd?w=500" alt="Boat Builder">
      <div style="text-align:center; color:#fff; margin-top:10px;">
        <p style="font-family:serif; font-size:1.2rem;">A.K. Mehra</p>
        <span style="font-size:0.7rem; color:var(--sky);">Founder & Chief Builder</span>
      </div>
    </div>
  </div>
</section>

<section id="about" style="background:#fff;">
  <div class="section-title">35+ Years of Maritime Excellence</div>
  <div style="display:grid; grid-template-columns:1fr 1fr; gap:3rem;">
    <div>
      <div class="exp-badge">
        <div class="exp-num">35</div>
        <p><strong>Years of Active Service</strong><br>Crafting resilient vessels for Indian waters.</p>
      </div>
    </div>
    <p style="line-height:1.8; color:#666;">Based in Bhayandar, Maharashtra, we specialize in high-end fiberglass reinforcement, gel coats, and structural restorations that withstand the harshest sea environments.</p>
  </div>
</section>

<section id="services">
  <h2 class="section-title">Our Marine Services</h2>
  <div class="services-grid">
    <div class="service-card"><h3>01</h3><h4>New Boat Manufacturing</h4><p>Custom fiberglass fishing boats built for durability.</p></div>
    <div class="service-card"><h3>02</h3><h4>Repair & Maintenance</h4><p>Complete structural restoration and leak repairs.</p></div>
    <div class="service-card"><h3>03</h3><h4>Gelcoat Finishing</h4><p>Professional seawater protection coating.</p></div>
    <div class="service-card"><h3>04</h3><h4>Fish Storage Tanks</h4><p>Marine grade fiberglass tanks for catch storage.</p></div>
    <div class="service-card"><h3>05</h3><h4>Reinforcement</h4><p>Structural strengthening and hull modifications.</p></div>
    <div class="service-card"><h3>06</h3><h4>Cabin Fitting</h4><p>Custom boat ice boxes and interior cabin work.</p></div>
  </div>
</section>

<section id="locations" style="background:#fff; text-align:center;">
  <h2 class="section-title">Work Locations</h2>
  <p style="font-size:1.2rem; color:var(--blue); letter-spacing:1px;">Uran • Gorai • Ratnagiri • Porbandar • Mangrul • Alibaug</p>
</section>

<section id="gallery">
  <div class="gallery-grid" id="dynamic-gallery"></div>
</section>

<section id="contact" style="background:#fff;">
  <h2 class="section-title">Connect with Us</h2>
  <div class="contact-grid">
    <div>
      <div class="info-row">
        <div class="icon-box"><svg viewBox="0 0 24 24"><path d="M12 2C8.13 2 5 5.13 5 9c0 5.25 7 13 7 13s7-7.75 7-13c0-3.87-3.13-7-7-7z"/></svg></div>
        <div class="info-text"><h4>Workshop</h4><p>Bhayandar West, Near Uttan Marine Area, Maharashtra</p></div>
      </div>
      <div class="info-row">
        <div class="icon-box"><svg viewBox="0 0 24 24"><path d="M6.62 10.79c1.44 2.83 3.76 5.14 6.59 6.59l2.2-2.2c.27-.27.67-.36 1.02-.24 1.12.37 2.33.57 3.57.57.55 0 1 .45 1 1V20c0 .55-.45 1-1 1-9.39 0-17-7.61-17-17 0-.55.45-1 1-1h3.5c.55 0 1 .45 1 1 0 1.25.2 2.45.57 3.57.11.35.03.74-.25 1.02l-2.2 2.2z"/></svg></div>
        <div class="info-text"><h4>Call / WhatsApp</h4><p><a href="tel:+918655411098">+91 86554 11098</a></p></div>
      </div>
      <div class="info-row">
        <div class="icon-box"><svg viewBox="0 0 24 24"><path d="M20 4H4c-1.1 0-1.99.9-1.99 2L2 18c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 4l-8 5-8-5V6l8 5 8-5v2z"/></svg></div>
        <div class="info-text"><h4>Email Address</h4><p><a href="mailto:arun.mehra401105@gmail.com">arun.mehra401105@gmail.com</a></p></div>
      </div>
    </div>
    <div id="map"></div>
  </div>
</section>

<section id="admin-upload" style="display:none; padding:2rem; background:#eee;">
  <h3>Admin: Upload Assets</h3>
  <input type="file" id="admin-file-input" multiple style="margin:1rem 0;">
  <button id="upload-submit-btn" style="padding:10px 20px; background:var(--navy); color:#fff; border:none; cursor:pointer;">Upload to Gallery</button>
</section>

<footer>© 2026 AK Mehra Fiberglass Specialists. All Rights Reserved.</footer>

<script src="https://unpkg.com/leaflet/dist/leaflet.js"></script>
<script>
  // MAP
  const map = L.map('map').setView([19.3090, 72.7850], 7);
  L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png').addTo(map);
  const locs = [
    {n:"Bhayandar HQ", c:[19.3090, 72.7850]}, {n:"Uran", c:[18.8770, 72.9430]},
    {n:"Gorai", c:[19.2372, 72.7811]}, {n:"Ratnagiri", c:[16.9902, 73.3120]},
    {n:"Alibaug", c:[18.6585, 72.8777]}, {n:"Mangrul", c:[15.8640, 73.6520]}, {n:"Porbandar", c:[21.6417, 69.6093]}
  ];
  locs.forEach(l => L.marker(l.c).addTo(map).bindPopup(l.n));

  // GALLERY
  const initial = [
    "https://images.unsplash.com/photo-1567899378494-47b22a2ae96a?w=400",
    "https://images.unsplash.com/photo-1544551763-46a013bb70d5?w=400",
    "https://images.unsplash.com/photo-1517524206127-48bbd363f3d7?w=400",
    "https://images.unsplash.com/photo-1505242844900-33230a1bf64c?w=400",
    "https://images.unsplash.com/photo-1454496522488-7a8e488e8606?w=400"
  ];
  let adminPics = JSON.parse(localStorage.getItem('ak_pics')) || [];
  function render() {
    const grid = document.getElementById('dynamic-gallery');
    const all = [...adminPics, ...initial, ...adminPics, ...initial];
    grid.innerHTML = all.map(src => `<div class="gallery-item"><img src="${src}"></div>`).join('');
  }
  render();

  // ADMIN
  document.getElementById('admin-login-btn').onclick = () => {
    if(prompt("Password:") === "mehra123") {
      document.getElementById('admin-upload').style.display = "block";
      window.location.hash = "#admin-upload";
    }
  };

  document.getElementById('upload-submit-btn').onclick = () => {
    const files = document.getElementById('admin-file-input').files;
    let count = 0;
    Array.from(files).forEach(f => {
      const r = new FileReader();
      r.onload = (e) => {
        adminPics.unshift(e.target.result);
        localStorage.setItem('ak_pics', JSON.stringify(adminPics));
        count++;
        if(count === files.length) { render(); alert("Uploaded!"); }
      };
      r.readAsDataURL(f);
    });
  };
</script>
</body>
</html>
"""

# 4. FINAL RENDER (Height set to cover content)
components.html(html_content, height=4800, scrolling=True)
