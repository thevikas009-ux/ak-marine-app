import streamlit as st
import streamlit.components.v1 as components

# 1. Page Configuration
st.set_page_config(
    page_title="AK Mehra – Fiberglass & Boat Specialists", 
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. GAP & FRAME KILLER: Streamlit ke default frame, body padding aur scrollbars ko khatam karne ke liye CSS
st.markdown("""
    <style>
        /* Streamlit ke standard borders aur spacing ko target karke delete karna */
        #MainMenu, header, footer {
            visibility: hidden;
            height: 0px !important;
        }
        .stApp {
            background-color: #f5f0e8; /* Body background color match */
        }
        /* Main structural container ka gap hatayein */
        .block-container {
            padding-top: 0rem !important;
            padding-bottom: 0rem !important;
            padding-left: 0rem !important;
            padding-right: 0rem !important;
            max-width: 100% !important;
        }
        /* Frame ke layer ko full screen par setup karna */
        iframe {
            position: absolute;
            top: 0;
            left: 0;
            width: 100% !important;
            height: 100vh !important; /* Viewport height sync taaki background me gap na bane */
            border: none !important;
            margin: 0 !important;
            padding: 0 !important;
            overflow: hidden !important;
        }
    </style>
""", unsafe_allow_html=True)

# 3. Complete Source Code (With Email Icon & Maps Fixed)
html_content = r"""
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
<title>AK Mehra – Fiberglass & Boat Specialists</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,600;1,400&family=Jost:wght@300;400;500&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://unpkg.com/leaflet/dist/leaflet.css"/>

<style>
  *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
  :root {
    --navy: #0d2640; --navy-mid: #153352; --blue: #1a5f8a; --sky: #5ba4cf;
    --sky-light: #a8d4f0; --cream: #f5f0e8; --gold: #c8a96e; --white: #ffffff;
    --text-dark: #0d1f33; --text-muted: #4a6580;
  }
  
  /* Pure body scroll active rakhein taaki frame bar gayab ho sake */
  html, body { 
    height: 100%; 
    background: var(--cream); 
    color: var(--text-dark);
    font-family: 'Jost', sans-serif;
    overflow-x: hidden;
    overflow-y: auto;
  }

  /* FIXED HEADER NAVIGATION */
  nav { 
    position: fixed; top: 0; left: 0; right: 0; z-index: 1000; 
    background: rgba(13,38,64,0.98); 
    display: flex; align-items: center; justify-content: space-between; 
    padding: 0 5vw; height: 64px; 
    border-bottom: 1px solid rgba(91,164,207,0.25); 
  }
  .nav-brand { font-family: 'Cormorant Garamond', serif; font-size: 1.5rem; font-weight: 600; color: var(--sky-light); }
  .nav-links { display: flex; gap: 2rem; list-style: none; align-items: center; }
  .nav-links a { color: rgba(255,255,255,0.7); text-decoration: none; font-size: 0.85rem; text-transform: uppercase; letter-spacing: 0.08em; transition: 0.2s; }
  .nav-links a:hover { color: var(--sky-light); }

  /* HERO SECTION */
  .hero { 
    padding-top: 120px; /* Nav bar overlap fix */
    min-height: 100vh; 
    background: linear-gradient(160deg, var(--navy) 0%, var(--navy-mid) 55%, var(--blue) 100%); 
    display: flex; align-items: center; padding-bottom: 60px; position: relative; 
  }
  .hero-inner { max-width: 1200px; margin: 0 auto; width: 100%; display: grid; grid-template-columns: 1fr 1fr; gap: 4rem; padding: 0 5vw; align-items: center; }
  .hero h1 { font-family: 'Cormorant Garamond', serif; font-size: clamp(3.5rem, 6vw, 5.5rem); color: var(--white); line-height: 1.05; }
  .hero h1 em { font-style: italic; color: var(--sky-light); }
  .hero-cta { display: inline-block; padding: 0.85rem 2.2rem; border: 1px solid var(--sky); color: var(--sky-light); text-decoration: none; text-transform: uppercase; transition: 0.3s; margin-top: 20px; }
  .hero-cta:hover { background: var(--sky); color: var(--navy); }
  .hero-photo-frame { width: 80%; aspect-ratio: 3/4; max-width: 400px; margin: 0 auto; padding: 8px; position: relative; }
  .hero-photo-frame img { width: 100%; height: 100%; object-fit: cover; border-radius: 4px; }

  /* SECTIONS SETUP */
  section { padding: 6rem 5vw; }
  .section-inner { max-width: 1200px; margin: 0 auto; }
  .section-title { font-family: 'Cormorant Garamond', serif; font-size: clamp(2rem, 4vw, 3rem); color: var(--navy); margin-bottom: 2rem; }
  
  .services-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 25px; }
  .service-card { background: #fff; padding: 30px; border-radius: 12px; box-shadow: 0 8px 25px rgba(0,0,0,0.08); border-top: 4px solid #0f3557; transition: 0.3s; }
  .service-card:hover { transform: translateY(-8px); }

  /* INFINITE MOVING AUTOMATED GALLERY */
  #gallery { background: var(--navy); overflow: hidden; }
  .gallery-container { width: 100%; overflow: hidden; position: relative; margin-top: 1rem; }
  .gallery-grid { display: flex; gap: 20px; width: max-content; animation: scrollGallery 35s linear infinite; padding: 20px 0; }
  .gallery-grid:hover { animation-play-state: paused; }
  .gallery-item { width: 300px; height: 220px; flex-shrink: 0; border-radius: 12px; overflow: hidden; position: relative; box-shadow: 0 8px 25px rgba(0,0,0,.25); }
  .gallery-item img { width: 100%; height: 100%; object-fit: cover; }
  @keyframes scrollGallery { 0% { transform: translateX(0); } 100% { transform: translateX(-50%); } }

  /* CONTACT SYSTEM MATRIX */
  .contact-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 5rem; align-items: start; }
  .contact-info-row { display: flex; align-items: flex-start; gap: 1rem; padding: 1.25rem 0; border-bottom: 1px solid rgba(26,95,138,0.1); }
  .contact-icon { width: 40px; height: 40px; background: var(--navy); display: flex; align-items: center; justify-content: center; flex-shrink: 0; border-radius: 4px; }
  .contact-icon svg { width: 18px; height: 18px; fill: var(--sky-light); }
  .contact-info-row h4 { font-size: 0.75rem; text-transform: uppercase; color: var(--blue); margin-bottom: 0.25rem; }
  .contact-info-row p { font-size: 1rem; color: var(--text-dark); }
  .contact-info-row a { color: var(--blue); text-decoration: none; }
  #map { height: 450px; width: 100%; border-radius: 12px; box-shadow: 0 8px 25px rgba(0,0,0,0.05); border: 1px solid rgba(0,0,0,0.1); }

  footer { background: var(--navy); padding: 2.5rem; text-align: center; color: rgba(255,255,255,0.4); }
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
    <li><button id="admin-login-btn" style="background:none; border:1px solid var(--gold); color:var(--gold); padding:5px 12px; cursor:pointer; text-transform:uppercase; font-size:0.8rem; letter-spacing:1px;">Admin Login</button></li>
  </ul>
</nav>

<section class="hero">
  <div class="hero-inner">
    <div>
      <p style="color:var(--sky); letter-spacing: 2px; font-weight:500;">EST. SINCE 1990</p>
      <h1 style="margin-top:10px;">Masters of<br><em>Fiberglass</em><br>& the Sea</h1>
      <p style="color:rgba(255,255,255,0.7); margin-top:20px; line-height:1.7;">AK Mehra brings over 35 years of hands-on expertise in fishing boat manufacturing, custom fiberglass reinforcment, and heavy structural marine repair.</p>
      <a href="#contact" class="hero-cta">Get in Touch</a>
    </div>
    <div class="hero-photo-frame">
      <img src="https://images.unsplash.com/photo-1559136555-9303baea8ebd?w=500" alt="Boat Manufacturing Work">
    </div>
  </div>
</section>

<section id="services">
  <div class="section-inner">
    <h2 class="section-title">Our Marine Services</h2>
    <div class="services-grid">
      <div class="service-card"><h3>01</h3><h4>New Boat Manufacturing</h4><p>Custom fiberglass vessels built with high durability, resilience and coastal standards.</p></div>
      <div class="service-card"><h3>02</h3><h4>Repair & Maintenance</h4><p>Complete structural marine restoration, leak proof patches and preventative servicing.</p></div>
      <div class="service-card"><h3>03</h3><h4>Gelcoat Finishing</h4><p>Premium marine grade protective coating for heavy seawater corrosion resistance.</p></div>
    </div>
  </div>
</section>

<section id="gallery">
  <div class="section-inner">
    <h2 class="section-title" style="color:#fff;">Project Portfolio</h2>
    <div class="gallery-container">
      <div class="gallery-grid" id="dynamic-gallery"></div>
    </div>
  </div>
</section>

<section id="contact">
  <div class="section-inner">
    <h2 class="section-title">Connect with Us</h2>
    <div class="contact-grid">
      <div>
        <div class="contact-info-row">
          <div class="contact-icon"><svg viewBox="0 0 24 24"><path d="M12 2C8.13 2 5 5.13 5 9c0 5.25 7 13 7 13s7-7.75 7-13c0-3.87-3.13-7-7-7zm0 9.5c-1.38 0-2.5-1.12-2.5-2.5s1.12-2.5 2.5-2.5 2.5 1.12 2.5 2.5-1.12 2.5-2.5 2.5z"/></svg></div>
          <div><h4>Workshop Location</h4><p>Bhayandar West, Near Uttan Marine Area / Rai Village, Thane, Maharashtra</p></div>
        </div>
        <div class="contact-info-row">
          <div class="contact-icon"><svg viewBox="0 0 24 24"><path d="M6.62 10.79c1.44 2.83 3.76 5.14 6.59 6.59l2.2-2.2c.27-.27.67-.36 1.02-.24 1.12.37 2.33.57 3.57.57.55 0 1 .45 1 1V20c0 .55-.45 1-1 1-9.39 0-17-7.61-17-17 0-.55.45-1 1-1h3.5c.55 0 1 .45 1 1 0 1.25.2 2.45.57 3.57.11.35.03.74-.25 1.02l-2.2 2.2z"/></svg></div>
          <div><h4>Call / WhatsApp</h4><p><a href="tel:+918655411098">+91 86554 11098</a></p></div>
        </div>
        <div class="contact-info-row">
          <div class="contact-icon"><svg viewBox="0 0 24 24"><path d="M20 4H4c-1.1 0-1.99.9-1.99 2L2 18c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 4l-8 5-8-5V6l8 5 8-5v2z"/></svg></div>
          <div><h4>Email Enquiry</h4><p><a href="mailto:arun.mehra401105@gmail.com">arun.mehra401105@gmail.com</a></p></div>
        </div>
      </div>
      <div id="map"></div>
    </div>
  </div>
</section>

<section id="admin-upload" style="display:none; background:#fff; border-top: 2px solid var(--navy);">
  <div style="max-width:500px; margin: 0 auto; padding: 2rem 0;">
    <h3>Admin: Upload Photos</h3>
    <input type="file" id="admin-file-input" multiple style="margin: 20px 0; width:100%;">
    <button id="upload-submit-btn" class="hero-cta" style="background:var(--navy); color:#fff; width:100%; border:none; padding:1rem; cursor:pointer;">Upload to Gallery</button>
  </div>
</section>

<footer>
  <p>© 2026 AK Mehra Fiberglass Specialists. All Rights Reserved.</p>
</footer>

<script src="https://unpkg.com/leaflet/dist/leaflet.js"></script>
<script>
  // 1. Map Render Engine
  const map = L.map('map').setView([19.3090, 72.7850], 7);
  L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png').addTo(map);
  const locs = [
    {n:"Bhayandar (HQ)", c:[19.3090, 72.7850]},
    {n:"Uran", c:[18.8770, 72.9430]},
    {n:"Gorai", c:[19.2372, 72.7811]},
    {n:"Ratnagiri", c:[16.9902, 73.3120]},
    {n:"Mangrol", c:[21.1217, 70.1162]}
    {n:"Porbandar", c:[21.6417, 69.6293]}
    {n:"Alibaug", c:[18.6585, 72.8777]}
  ];
  locs.forEach(l => L.marker(l.c).addTo(map).bindPopup(`<b>${l.n}</b> Completed Project`));

  // 2. Automated Infinite Gallery Loader
  const initial = [
    "https://images.unsplash.com/photo-1567899378494-47b22a2ae96a?w=400",
    "https://images.unsplash.com/photo-1544551763-46a013bb70d5?w=400",
    "https://images.unsplash.com/photo-1517524206127-48bbd363f3d7?w=400",
    "https://images.unsplash.com/photo-1505242844900-33230a1bf64c?w=400"
  ];
  let adminPics = JSON.parse(localStorage.getItem('ak_pics')) || [];
  function render() {
    const grid = document.getElementById('dynamic-gallery');
    const all = [...adminPics, ...initial, ...adminPics, ...initial];
    grid.innerHTML = all.map(src => `<div class="gallery-item"><img src="${src}"></div>`).join('');
  }
  render();

  // 3. Admin Security Login Panel
  document.getElementById('admin-login-btn').onclick = () => {
    const p = prompt("Enter Password:");
    if(p === "mehra123") {
        document.getElementById('admin-upload').style.display = "block";
        window.location.hash = "#admin-upload";
    }
  };

  // 4. Multiple Image Upload Array Storage
  document.getElementById('upload-submit-btn').onclick = () => {
    const files = document.getElementById('admin-file-input').files;
    let counter = 0;
    if(files.length === 0) return alert("Select files first");
    Array.from(files).forEach(f => {
        const r = new FileReader();
        r.onload = (e) => {
            adminPics.unshift(e.target.result);
            localStorage.setItem('ak_pics', JSON.stringify(adminPics));
            counter++;
            if(counter === files.length) {
              render();
              alert("All photos compiled into storage structure successfully!");
            }
        };
        r.readAsDataURL(f);
    });
  };
</script>
</body>
</html>
"""

# 4. Final Processing Injection
components.html(html_content, height=1000) # Full body viewport handling controls height internally
