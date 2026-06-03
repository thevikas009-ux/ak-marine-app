import streamlit as st
import streamlit.components.v1 as components

# 1. Streamlit Page Settings
st.set_page_config(page_title="AK Mehra – Fiberglass & Boat Specialists", layout="wide")

# 2. GAP FIX: Streamlit ka default padding aur border hatane ke liye CSS
st.markdown("""
    <style>
        /* Top, bottom aur side ki faltu jagah zero karne ke liye */
        .block-container {
            padding-top: 0rem !important;
            padding-bottom: 0rem !important;
            padding-left: 0rem !important;
            padding-right: 0rem !important;
        }
        /* Iframe ke aas paas ka gap hatane ke liye */
        iframe {
            display: block;
            border: none;
        }
        /* Streamlit ka header aur footer chhupane ke liye */
        #MainMenu, header, footer {
            visibility: hidden;
            height: 0;
        }
    </style>
""", unsafe_allow_html=True)

# 3. Aapka Pura Asli HTML Code (Saare Features Ke Sath)
html_content = r"""
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>AK Mehra – Fiberglass & Boat Specialists</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,600;1,400&family=Jost:wght@300;400;500&display=swap" rel="stylesheet">

<link rel="stylesheet" href="https://unpkg.com/leaflet/dist/leaflet.css"/>

<style>
  *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
  :root {
    --navy: #0d2640;
    --navy-mid: #153352;
    --blue: #1a5f8a;
    --sky: #5ba4cf;
    --sky-light: #a8d4f0;
    --cream: #f5f0e8;
    --gold: #c8a96e;
    --white: #ffffff;
    --text-dark: #0d1f33;
    --text-muted: #4a6580;
  }
  html { scroll-behavior: smooth; }
  body {
    font-family: 'Jost', sans-serif;
    font-weight: 300;
    background: var(--cream);
    color: var(--text-dark);
    overflow-x: hidden;
  }

  /* NAV & COMPANY HEADER */
  nav { position: fixed; top: 0; left: 0; right: 0; z-index: 100; background: rgba(13,38,64,0.97); display: flex; align-items: center; justify-content: space-between; padding: 0 5vw; height: 64px; border-bottom: 1px solid rgba(91,164,207,0.25); }  
  .nav-brand { font-family: 'Cormorant Garamond', serif; font-size: 1.5rem; font-weight: 600; color: var(--sky-light); letter-spacing: 0.04em; }
  .nav-links { display: flex; gap: 2rem; list-style: none; align-items: center; }
  .nav-links a { color: rgba(255,255,255,0.7); text-decoration: none; font-size: 0.85rem; letter-spacing: 0.08em; text-transform: uppercase; transition: color 0.2s; }
  .nav-links a:hover { color: var(--sky-light); }

  /* HERO */
  .hero { min-height: 100vh; background: linear-gradient(160deg, var(--navy) 0%, var(--navy-mid) 55%, var(--blue) 100%); display: flex; align-items: center; padding: 80px 5vw 60px; position: relative; overflow: hidden; } 
  .hero::before { content: ''; position: absolute; bottom: -80px; left: -80px; width: 450px; height: 450px; border-radius: 50%; background: radial-gradient(circle, rgba(91,164,207,0.12) 0%, transparent 70%); } 
  .hero::after { content: ''; position: absolute; top: -100px; right: -60px; width: 450px; height: 450px; border-radius: 50%; border: 80px solid rgba(91,164,207,0.08); } 
  .hero-inner { max-width: 1200px; margin: 0 auto; width: 100%; display: grid; grid-template-columns: 1fr 1fr; gap: 4rem; align-items: center; } 
  .hero-tag { font-size: 0.75rem; letter-spacing: 0.15em; text-transform: uppercase; color: var(--sky); margin-bottom: 1.2rem; display: flex; align-items: center; gap: 0.75rem; }
  .hero-tag::before { content: ''; display: inline-block; width: 2rem; height: 1px; background: var(--sky); }
  .hero h1 { font-family: 'Cormorant Garamond', serif; font-size: clamp(3.5rem, 6vw, 5.5rem); font-weight: 600; line-height: 1.05; color: var(--white); margin-bottom: 1.5rem; }
  .hero h1 em { font-style: italic; color: var(--sky-light); }
  .hero-desc { font-size: 1rem; line-height: 1.8; color: rgba(255,255,255,0.65); max-width: 440px; margin-bottom: 2.5rem; }
  .hero-cta { display: inline-block; padding: 0.85rem 2.2rem; border: 1px solid var(--sky); color: var(--sky-light); text-decoration: none; font-size: 0.85rem; letter-spacing: 0.1em; text-transform: uppercase; transition: all 0.25s; background: transparent; }
  .hero-cta:hover { background: var(--sky); color: var(--navy); }
  
  .hero-stats { display: grid; grid-template-columns: 1fr 1fr; gap: 1px; margin-top: 3rem; background: rgba(91,164,207,0.2); border: 1px solid rgba(91,164,207,0.2); }
  .stat-item { background: rgba(13,38,64,0.6); padding: 1.2rem 1.5rem; }
  .stat-num { font-family: 'Cormorant Garamond', serif; font-size: 2.5rem; font-weight: 600; color: var(--sky-light); line-height: 1; }
  .stat-label { font-size: 0.75rem; color: rgba(255,255,255,0.5); text-transform: uppercase; letter-spacing: 0.08em; margin-top: 0.3rem; }
  
  .hero-photo-wrap { position: relative; }
  .hero-photo-frame { width: 80%; aspect-ratio: 3/4; max-width: 400px; margin: 0 auto; padding: 8px; position: relative; }
  .hero-photo-frame img { width: 100%; height: 100%; object-fit: cover; display: block; }
  .hero-photo-name { text-align: center; margin-top: 1.2rem; }
  .hero-photo-name p { font-family: 'Cormorant Garamond', serif; font-size: 1.5rem; color: var(--white); }
  .hero-photo-name span { font-size: 0.78rem; color: var(--sky); letter-spacing: 0.1em; text-transform: uppercase; }

  /* WAVE DIVIDER */
  .wave-divider { display: block; width: 100%; height: 80px; background: var(--navy); }
  .wave-divider svg { display: block; }

  /* SECTION BASE */
  section { padding: 6rem 5vw; }
  .section-inner { max-width: 1200px; margin: 0 auto; }
  .section-label { font-size: 0.72rem; letter-spacing: 0.18em; text-transform: uppercase; color: var(--blue); margin-bottom: 0.75rem; display: flex; align-items: center; gap: 0.6rem; }
  .section-label::before { content: ''; width: 1.5rem; height: 1px; background: var(--blue); }
  .section-title { font-family: 'Cormorant Garamond', serif; font-size: clamp(2rem, 4vw, 3rem); font-weight: 600; color: var(--navy); line-height: 1.2; margin-bottom: 1rem; }

  /* ABOUT */
  #about { background: var(--white); }
  .about-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 5rem; align-items: start; margin-top: 3.5rem; }
  .about-body { font-size: 0.95rem; line-height: 1.9; color: var(--text-muted); }
  .about-body p + p { margin-top: 1rem; }
  .about-highlight { background: var(--navy); color: var(--white); padding: 2rem; margin-top: 2rem; }
  .about-highlight p { font-family: 'Cormorant Garamond', serif; font-size: 1.4rem; font-style: italic; color: var(--sky-light); }
  .experience-badge { display: flex; align-items: center; gap: 1.5rem; padding: 1.5rem; border: 1px solid rgba(26,95,138,0.2); }
  .experience-badge .num { font-family: 'Cormorant Garamond', serif; font-size: 4rem; font-weight: 600; color: var(--blue); line-height: 1; }
  .experience-badge .text { font-size: 0.9rem; color: var(--text-muted); }

  /* SERVICES */
  .services-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 25px; margin-top: 50px; }
  .service-card { background: #fff; padding: 30px; border-radius: 12px; box-shadow: 0 8px 25px rgba(0,0,0,0.08); transition: 0.3s ease; border-top: 4px solid #0f3557; }
  .service-card:hover { transform: translateY(-8px); box-shadow: 0 15px 35px rgba(0,0,0,0.15); }
  .service-card h3 { font-size: 40px; color: #0f3557; margin-bottom: 10px; }
  .service-card h4 { font-size: 22px; margin-bottom: 15px; color: #1b1b1b; }
  .service-card p { color: #666; line-height: 1.7; }

  /* MOVING GALLERY SECTION */
  #gallery { background: var(--navy); overflow: hidden; }
  #gallery .section-title, #gallery .gallery-intro { color: var(--white); }
  .gallery-container { width: 100%; overflow: hidden; margin-top: 2rem; position: relative; }
  
  .gallery-grid { display: flex; gap: 20px; width: max-content; animation: scrollGallery 35s linear infinite; padding: 10px 0; }
  .gallery-grid:hover { animation-play-state: paused; } /* Hover karne par rukega */

  .gallery-item { position: relative; width: 300px; height: 220px; flex-shrink: 0; overflow: hidden; border-radius: 12px; background: var(--navy-mid); box-shadow: 0 8px 25px rgba(0,0,0,.25); }
  .gallery-item img { width: 100%; height: 100%; object-fit: cover; transition: .5s; }
  .gallery-item:hover img { transform: scale(1.08); }
  .gallery-item::after { content: attr(data-location); position: absolute; left: 0; right: 0; bottom: 0; padding: 14px; color: #fff; font-size: 15px; background: linear-gradient(transparent, rgba(0,0,0,.85)); z-index: 2; }

  @keyframes scrollGallery {
    0% { transform: translateX(0); }
    100% { transform: translateX(-50%); } /* Half array scroll automation */
  }

  /* CONTACT & MAP */
  #contact { background: var(--white); }
  .contact-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 5rem; margin-top: 3rem; align-items: start; }
  .contact-info-row { display: flex; align-items: flex-start; gap: 1rem; padding: 1.25rem 0; border-bottom: 1px solid rgba(26,95,138,0.1); }
  .contact-icon { width: 40px; height: 40px; background: var(--navy); display: flex; align-items: center; justify-content: center; flex-shrink: 0; }
  .contact-icon svg { width: 18px; height: 18px; fill: var(--sky-light); }
  
  /* Leaflet Map Styling */
  #map { height: 450px; width: 100%; border-radius: 12px; box-shadow: 0 8px 25px rgba(0,0,0,0.1); border: 1px solid rgba(26,95,138,0.15); }

  /* FOOTER */
  footer { background: var(--navy); padding: 2.5rem 5vw; text-align: center; color: rgba(255,255,255,0.35); }
  .footer-brand { font-family: 'Cormorant Garamond', serif; font-size: 1.2rem; color: var(--sky-light); margin-bottom: 0.5rem; }

  @media (max-width: 768px) {
    .hero-inner, .about-grid, .contact-grid { grid-template-columns: 1fr; gap: 2rem; }
    .hero-photo-wrap, .nav-links { display: none; }
    #map { height: 300px; }
  }
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
    <li><a href="#admin-upload" id="nav-upload-link" style="display:none; color: var(--gold);">Upload (Admin)</a></li>
    <li><button id="admin-login-btn" style="background:none; border:1px solid var(--gold); color:var(--gold); padding:5px 12px; cursor:pointer; font-family:inherit; font-size:0.8rem; text-transform:uppercase; letter-spacing:0.08em;">Admin Login</button></li>
  </ul>
</nav>

<section class="hero">
  <div class="hero-inner">
    <div>
      <p class="hero-tag">Est. Since 1990 · Bhayandar, Maharashtra</p>
      <h1>Masters of<br><em>Fiberglass</em><br>& the Sea</h1>
      <p class="hero-desc">AK Mehra brings over 35 years of hands-on expertise in fishing boat manufacturing, repair, and advanced fiberglass work.</p>
      <a href="#contact" class="hero-cta">Get in Touch</a>
      <div class="hero-stats">
        <div class="stat-item"><div class="stat-num">35+</div><div class="stat-label">Years Experience</div></div>
        <div class="stat-item"><div class="stat-num">06</div><div class="stat-label">Core Services</div></div>
        <div class="stat-item"><div class="stat-num">100%</div><div class="stat-label">Quality</div></div>
        <div class="stat-item"><div class="stat-num">∞</div><div class="stat-label">Satisfied Clients</div></div>
      </div>
    </div>
    <div class="hero-photo-wrap">
      <div class="hero-photo-frame">
        <img src="https://images.unsplash.com/photo-1559136555-9303baea8ebd?w=500" alt="Marine Boat Work">
      </div>
      <div class="hero-photo-name"><p>A.K. Mehra</p><span>Founder & Chief Builder</span></div>
    </div>
  </div>
</section>

<div class="wave-divider">
  <svg viewBox="0 0 1200 120" preserveAspectRatio="none" style="height: 100%; width: 100%; fill: #f5f0e8;">
    <path d="M321.39,56.44c58-10.79,114.16-30.13,172-41.86,82.39-16.72,168.19-17.73,250.45-.39C823.78,31,906.67,72,985.66,92.83c70.05,18.48,146.53,26.09,214.34,3V0H0V120H321.39Z"></path>
  </svg>
</div>

<section id="about">
  <div class="section-inner">
    <div class="about-grid">
      <div>
        <p class="section-label">Legacy of Trust</p>
        <h2 class="section-title">35+ Years of Maritime Excellence</h2>
        <div class="experience-badge">
          <div class="num">35</div>
          <div class="text"><strong>Years of Active Service</strong>Crafting resilient vessels for Indian waters.</div>
        </div>
      </div>
      <div class="about-body">
        <p>Based in the coastal belt of Bhayandar, Maharashtra, AK Mehra has been the backbone of local fishermen since 1990. We specialize in high-end fiberglass reinforcement and structural restorations.</p>
        <div class="about-highlight"><p>"A boat is more than a vessel—it’s a livelihood. We build it to survive the sea."</p></div>
      </div>
    </div>
  </div>
</section>

<section id="services">
  <div class="section-inner">
    <p class="section-label">What We Do</p>
    <h2 class="section-title">Our Marine & Fiberglass Services</h2>
    <div class="services-grid">
      <div class="service-card"><h3>01</h3><h4>New Boat Manufacturing</h4><p>Custom fiberglass fishing boats built with safety and performance.</p></div>
      <div class="service-card"><h3>02</h3><h4>Boat Repairing & Maintenance</h4><p>Complete repair, servicing, and structural restoration.</p></div>
      <div class="service-card"><h3>03</h3><h4>Gelcoat & Finishing</h4><p>Professional gelcoat application for long-lasting protection.</p></div>
      <div class="service-card"><h3>04</h3><h4>Fish Storage Tank</h4><p>Durable fiberglass fish storage tanks designed for marine use.</p></div>
      <div class="service-card"><h3>05</h3><h4>Reinforcement & Modification</h4><p>Structural strengthening, hull modifications, and upgrades.</p></div>
      <div class="service-card"><h3>06</h3><h4>Boat Ice Box Fitting</h4><p>Custom ice box fabrication and utility cabin installation.</p></div>
    </div>
  </div>
</section>

<section id="gallery">
  <div class="section-inner">
    <p class="section-label" style="color: var(--sky);">Our Portfolio</p>
    <h2 class="section-title">Project Gallery</h2>
    <p class="gallery-intro">Explore our latest fiberglass modifications and heavy repair projects running actively across the coast.</p>
    
    <div class="gallery-container">
      <div class="gallery-grid" id="dynamic-gallery">
        </div>
    </div>

    <div style="text-align: center; margin-top: 2rem;">
      <button id="load-more-btn" class="hero-cta" style="cursor: pointer;">Load More Photos</button>
    </div>
  </div>
</section>

<section id="admin-upload" style="display: none; background: var(--white); border-top: 2px solid var(--navy);">
  <div class="section-inner" style="max-width: 600px;">
    <p class="section-label">Admin Control Panel</p>
    <h2 class="section-title">Upload New Photos</h2>
    <div style="background: var(--cream); padding: 2rem; border-radius: 4px; margin-top: 1rem;">
      <div style="margin-bottom: 1.5rem;">
        <label style="display: block; margin-bottom: 0.5rem; font-size: 0.9rem;">Select Images:</label>
        <input type="file" id="admin-file-input" accept="image/*" multiple style="width:100%; padding:0.5rem;">
      </div>
      <div style="margin-bottom: 1.5rem;">
        <label style="display: block; margin-bottom: 0.5rem; font-size: 0.9rem;">Location Name / Title:</label>
        <input type="text" id="admin-img-location" placeholder="e.g. Uran, Gorai, Alibaug" style="width:100%; padding:0.5rem;">
      </div>
      <div style="margin-bottom: 1.5rem;">
        <label style="display: block; margin-bottom: 0.5rem; font-size: 0.9rem;">Layout Style:</label>
        <select id="admin-img-style" style="width: 100%; padding: 0.5rem;">
          <option value="normal">Normal</option>
          <option value="wide">Wide (Takes 2 Columns)</option>
          <option value="tall">Tall (Takes 2 Rows)</option>
        </select>
      </div>
      <button id="upload-submit-btn" class="hero-cta" style="background: var(--navy); color: #fff; width: 100%; border: none; padding: 1rem;">Upload to Live Gallery</button>
    </div>
  </div>
</section>

<section id="contact">
  <div class="section-inner">
    <p class="section-label">Connect with Us</p>
    <h2 class="section-title">Let's Discuss Your Vessel</h2>
    
    <div class="contact-info-row">
          <div class="contact-icon"><svg viewBox="0 0 24 24"><path d="M12 2C8.13 2 5 5.13 5 9c0 5.25 7 13 7 13s7-7.75 7-13c0-3.87-3.13-7-7-7zm0 9.5c-1.38 0-2.5-1.12-2.5-2.5s1.12-2.5 2.5-2.5 2.5 1.12 2.5 2.5-1.12 2.5-2.5 2.5z"/></svg></div>
          <div><h4>Workshop Location</h4><p>Bhayandar West, Near Uttan Marine Area / Rai Village, Thane District, Maharashtra - 401101</p></div>
        </div>

        <div class="contact-info-row">
          <div class="contact-icon"><svg viewBox="0 0 24 24"><path d="M6.62 10.79c1.44 2.83 3.76 5.14 6.59 6.59l2.2-2.2c.27-.27.67-.36 1.02-.24 1.12.37 2.33.57 3.57.57.55 0 1 .45 1 1V20c0 .55-.45 1-1 1-9.39 0-17-7.61-17-17 0-.55.45-1 1-1h3.5c.55 0 1 .45 1 1 0 1.25.2 2.45.57 3.57.11.35.03.74-.25 1.02l-2.2 2.2z"/></svg></div>
          <div><h4>Call / WhatsApp</h4><p><a href="tel:+918655411098" style="color: var(--blue); text-decoration: none;">+91 86554 11098</a></p></div>
        </div>

        <div class="contact-info-row">
          <div class="contact-icon"><svg viewBox="0 0 24 24"><path d="M20 4H4c-1.1 0-1.99.9-1.99 2L2 18c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 4l-8 5-8-5V6l8 5 8-5v2z"/></svg></div>
          <div><h4>Email Address</h4><p><a href="mailto:arun.mehra401105@gmail.com" style="color: var(--blue); text-decoration: none;">arun.mehra401105@gmail.com</a></p></div>
        </div>
        <div class="contact-note"><p><strong>Interactive Map Pointer:</strong> Click on the blue pins in the marine map to see coastal cities where AK Mehra successfully completed flagship projects!</p></div>
      </div>

      <div>
        <div id="map"></div>
      </div>
    </div>
  </div>
</section>

<footer>
  <div class="footer-brand">AK Mehra</div>
  <p>© 2026 AK Mehra Fiberglass & Boat Specialists. All Rights Reserved.</p>
</footer>

<script src="https://unpkg.com/leaflet/dist/leaflet.js"></script>

<script>
  // 1. DYNAMIC & INTERACTIVE GEOMAP ENGINE (With project locations pinned)
  // Bhayandar coordinates as main view point
  const map = L.map('map').setView([19.3090, 72.7850], 7); 
  
  L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '© OpenStreetMap contributors'
  }).addTo(map);

  // Array locations where project work is completed successfully
  const workLocations = [
    { name: "Bhayandar Workshop (HQ)", coords: [19.3090, 72.7850], desc: "Main Boat Manufacturing Hub" },
    { name: "Uran", coords: [18.8770, 72.9430], desc: "Fiberglass Cabins fitted successfully" },
    { name: "Gorai", coords: [19.2372, 72.7811], desc: "Heavy Trawler Hull Overhaul & Repair" },
    { name: "Ratnagiri", coords: [16.9902, 73.3120], desc: "Ice-box Insulation Fabrication Setup" },
    { name: "Alibaug", coords: [18.6585, 72.8777], desc: "Gelcoat Seawater Protection Coating Project" },
    { name: "Mangrul", coords: [15.8640, 73.6520], desc: "Structural Marine Reinforcements" },
    { name: "Porbandar", coords: [21.6417, 69.6093], desc: "Large Scale Fishing Vessel Manufacturing Support" }
  ];

  // Pinned location automation marker generation
  workLocations.forEach(loc => {
    L.marker(loc.coords).addTo(map)
     .bindPopup(`<b>${loc.name}</b><br>${loc.desc}`);
  });

  // 2. LIVE SEAMLESS MOVING AUTOMATED GALLERY LOGIC
  const initialPhotos = [
    { src: "https://images.unsplash.com/photo-1559136555-9303baea8ebd?w=600", loc: "Uran Project" },
    { src: "https://images.unsplash.com/photo-1567899378494-47b22a2ae96a?w=600", loc: "Gorai Coast" },
    { src: "https://images.unsplash.com/photo-1544551763-46a013bb70d5?w=600", loc: "Ratnagiri Heavy Repair" },
    { src: "https://images.unsplash.com/photo-1517524206127-48bbd363f3d7?w=600", loc: "Porbandar Vessel" },
    { src: "https://images.unsplash.com/photo-1505242844900-33230a1bf64c?w=600", loc: "Alibaug Gelcoat Finish" },
    { src: "https://images.unsplash.com/photo-1454496522488-7a8e488e8606?w=600", loc: "Mangrul Dockyard" }
  ];

  let adminPhotos = JSON.parse(localStorage.getItem('ak_mehra_gallery_photos')) || [];
  let combinedPhotos = [...adminPhotos, ...initialPhotos];

  const galleryGrid = document.getElementById('dynamic-gallery');

  function renderMovingGallery() {
    galleryGrid.innerHTML = '';
    // Double array loop for infinite automated slider illusion
    let renderList = [...combinedPhotos, ...combinedPhotos]; 
    
    renderList.forEach(photo => {
      const item = document.createElement('div');
      item.className = 'gallery-item';
      item.setAttribute('data-location', photo.loc || 'AK Mehra Project');
      
      const img = document.createElement('img');
      img.src = photo.src;
      img.loading = 'lazy';
      
      item.appendChild(img);
      galleryGrid.appendChild(item);
    });
  }

  // 3. ADMIN PANEL SECURITY SYSTEM
  const adminLoginBtn = document.getElementById('admin-login-btn');
  const adminUploadSection = document.getElementById('admin-upload');
  const navUploadLink = document.getElementById('nav-upload-link');

  adminLoginBtn.addEventListener('click', () => {
    if (adminLoginBtn.innerText === "LOGOUT") {
      adminUploadSection.style.display = "none";
      navUploadLink.style.display = "none";
      adminLoginBtn.innerText = "ADMIN LOGIN";
      return;
    }

    const pass = prompt("Enter Admin Secret Key Password:");
    if (pass === "mehra123") {
      alert("Welcome Commander! Upload modules are now online.");
      adminUploadSection.style.display = "block";
      navUploadLink.style.display = "block";
      adminLoginBtn.innerText = "LOGOUT";
    } else if (pass !== null) {
      alert("Unauthorized Access Denied.");
    }
  });

  // 4. ADMIN LIVE IMAGE UPLOAD ENGINE
  document.getElementById('upload-submit-btn').addEventListener('click', () => {
    const fileIn = document.getElementById('admin-file-input');
    const locIn = document.getElementById('admin-img-location').value || 'Coastal Project';

    if (fileIn.files.length === 0) {
      alert("Please select at least one marine image asset.");
      return;
    }

    let loaded = 0;
    Array.from(fileIn.files).forEach(file => {
      const reader = new FileReader();
      reader.onload = function(e) {
        adminPhotos.unshift({ src: e.target.result, loc: locIn });
        localStorage.setItem('ak_mehra_gallery_photos', JSON.stringify(adminPhotos));
        
        loaded++;
        if (loaded === fileIn.files.length) {
          combinedPhotos = [...adminPhotos, ...initialPhotos];
          renderMovingGallery();
          alert("Assets successfully updated on live stack!");
          fileIn.value = '';
        }
      }
      reader.readAsDataURL(file);
    });
  });

  // Initial Load Trigger
  renderMovingGallery();
</script>

</body>
</html>
"""

# 4. Pure Frame Height Integration (Auto-Scroll system Enabled)
components.html(html_content, height=4100, scrolling=True)
