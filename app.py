import streamlit as st
import streamlit.components.v1 as components

# Streamlit Page Settings (Tab me jo naam dikhega)
st.set_page_config(page_title="AK Mehra – Fiberglass & Boat Specialists", layout="wide")

# Aapka share kiya hua HTML, CSS aur JS code ek sath
html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>AK Mehra – Fiberglass & Boat Specialists</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,600;1,400&family=Jost:wght@300;400;500&display=swap" rel="stylesheet">
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

  /* NAV */
  nav {
    position: fixed; top: 0; left: 0; right: 0; z-index: 100;
    background: rgba(13,38,64,0.97);
    display: flex; align-items: center; justify-content: space-between;
    padding: 0 5vw; height: 64px;
    border-bottom: 1px solid rgba(91,164,207,0.25);
  }
  .nav-brand { font-family: 'Cormorant Garamond', serif; font-size: 1.5rem; font-weight: 600; color: var(--sky-light); letter-spacing: 0.04em; }
  .nav-links { display: flex; gap: 2rem; list-style: none; align-items: center; }
  .nav-links a { color: rgba(255,255,255,0.7); text-decoration: none; font-size: 0.85rem; letter-spacing: 0.08em; text-transform: uppercase; transition: color 0.2s; }
  .nav-links a:hover { color: var(--sky-light); }

  /* HERO */
  .hero {
    min-height: 100vh;
    background: linear-gradient(160deg, var(--navy) 0%, var(--navy-mid) 55%, var(--blue) 100%);
    display: flex; align-items: center;
    padding: 80px 5vw 60px;
    position: relative; overflow: hidden;
  }
  .hero::before {
    content: '';
    position: absolute; bottom: -80px; left: -80px;
    width: 450px; height: 450px;
    border-radius: 50%;
    background: radial-gradient(circle, rgba(91,164,207,0.12) 0%, transparent 70%);
  }
  .hero::after {
    content: '';
    position: absolute; top: -100px; right: -60px;
    width: 450px; height: 450px;
    border-radius: 50%;
    border: 80px solid rgba(91,164,207,0.08);
  }
  .hero-inner { max-width: 1200px; margin: 0 auto; width: 100%; display: grid; grid-template-columns: 1fr 1fr; gap: 4rem; align-items: center; }
  .hero-tag { font-size: 0.75rem; letter-spacing: 0.15em; text-transform: uppercase; color: var(--sky); margin-bottom: 1.2rem; display: flex; align-items: center; gap: 0.75rem; }
  .hero-tag::before { content: ''; display: inline-block; width: 2rem; height: 1px; background: var(--sky); }
  .hero h1 { font-family: 'Cormorant Garamond', serif; font-size: clamp(3.5rem, 6vw, 5.5rem); font-weight: 600; line-height: 1.05; color: var(--white); margin-bottom: 1.5rem; }
  .hero h1 em { font-style: italic; color: var(--sky-light); }
  .hero-desc { font-size: 1rem; line-height: 1.8; color: rgba(255,255,255,0.65); max-width: 440px; margin-bottom: 2.5rem; }
  .hero-cta {
    display: inline-block; padding: 0.85rem 2.2rem;
    border: 1px solid var(--sky); color: var(--sky-light);
    text-decoration: none; font-size: 0.85rem; letter-spacing: 0.1em; text-transform: uppercase;
    transition: all 0.25s;
    background: transparent;
  }
  .hero-cta:hover { background: var(--sky); color: var(--navy); }
  .hero-stats { display: grid; grid-template-columns: 1fr 1fr; gap: 1px; margin-top: 3rem; background: rgba(91,164,207,0.2); border: 1px solid rgba(91,164,207,0.2); }
  .stat-item { background: rgba(13,38,64,0.6); padding: 1.2rem 1.5rem; }
  .stat-num { font-family: 'Cormorant Garamond', serif; font-size: 2.5rem; font-weight: 600; color: var(--sky-light); line-height: 1; }
  .stat-label { font-size: 0.75rem; color: rgba(255,255,255,0.5); text-transform: uppercase; letter-spacing: 0.08em; margin-top: 0.3rem; }
  .hero-photo-wrap { position: relative; }
  .hero-photo-frame {
    width: 80%; aspect-ratio: 3/4; max-width: 400px; margin: 0 auto;
    padding: 8px;
    position: relative;
  }
  .hero-photo-frame img { width: 100%; height: 100%; object-fit: cover; object-position: top; display: block; filter: grayscale(15%); }
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
  .section-sub { font-size: 0.95rem; line-height: 1.8; color: var(--text-muted); max-width: 560px; }

  /* ABOUT */
  #about { background: var(--white); }
  .about-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 5rem; align-items: start; margin-top: 3.5rem; }
  .about-body { font-size: 0.95rem; line-height: 1.9; color: var(--text-muted); }
  .about-body p + p { margin-top: 1rem; }
  .about-highlight { background: var(--navy); color: var(--white); padding: 2rem; margin-top: 2rem; }
  .about-highlight p { font-family: 'Cormorant Garamond', serif; font-size: 1.4rem; font-style: italic; line-height: 1.5; color: var(--sky-light); }
  .experience-badge { display: flex; align-items: center; gap: 1.5rem; padding: 1.5rem; border: 1px solid rgba(26,95,138,0.2); }
  .experience-badge .num { font-family: 'Cormorant Garamond', serif; font-size: 4rem; font-weight: 600; color: var(--blue); line-height: 1; }
  .experience-badge .text { font-size: 0.9rem; color: var(--text-muted); line-height: 1.5; }
  .experience-badge .text strong { display: block; font-size: 1rem; color: var(--navy); font-weight: 500; }

  /* SERVICES */
  #services { background: var(--cream); }
  .services-grid{
      display:grid;
      grid-template-columns:repeat(auto-fit,minmax(300px,1fr));
      gap:25px;
      margin-top:50px;
  }
  .service-card{
      background:#fff;
      padding:30px;
      border-radius:12px;
      box-shadow:0 8px 25px rgba(0,0,0,0.08);
      transition:0.3s ease;
      border-top:4px solid #0f3557;
  }
  .service-card:hover {
      transform:translateY(-8px);
      box-shadow:0 15px 35px rgba(0,0,0,0.15);
  }
  .service-card h3{
      font-size:40px;
      color:#0f3557;
      margin-bottom:10px;
  }
  .service-card h4{
      font-size:22px;
      margin-bottom:15px;
      color:#1b1b1b;
  }
  .service-card p{
      color:#666;
      line-height:1.7;
      margin:0;
  }

  /* GALLERY */
  #gallery { background: var(--navy); }
  #gallery .section-title { color: var(--white); }
  #gallery .section-label { color: var(--sky); }
  #gallery .section-label::before { background: var(--sky); }
  .gallery-intro { font-size: 0.95rem; color: rgba(255,255,255,0.55); margin-top: 1rem; margin-bottom: 3rem; max-width: 500px; }
  .gallery-grid{
      display:flex;
      gap:20px;
      overflow:hidden;
      width:max-content;
      animation:scrollGallery 35s linear infinite;
      padding:10px 0;
  }
  .gallery-item{
      position:relative;
      width:300px;
      height:220px;
      flex-shrink:0;
      overflow:hidden;
      border-radius:12px;
      background:var(--navy-mid);
      box-shadow:0 8px 25px rgba(0,0,0,.25);
  }
  .gallery-item img{
      width:100%;
      height:100%;
      object-fit:cover;
      transition:.5s;
  }
  .gallery-item:hover img{
      transform:scale(1.08);
  }
  @keyframes scrollGallery{
      0% { transform:translateX(0); }
      100% { transform:translateX(-50%); }
  }

  @media(max-width:768px){
      .gallery-item{ width:220px; height:170px; }
  }

  /* CONTACT */
  #contact { background: var(--white); }
  .contact-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 5rem; margin-top: 3rem; align-items: start; }
  .contact-info-row { display: flex; align-items: flex-start; gap: 1rem; padding: 1.25rem 0; border-bottom: 1px solid rgba(26,95,138,0.1); }
  .contact-icon { width: 40px; height: 40px; background: var(--navy); display: flex; align-items: center; justify-content: center; flex-shrink: 0; }
  .contact-icon svg { width: 18px; height: 18px; fill: var(--sky-light); }
  .contact-info-row h4 { font-size: 0.72rem; text-transform: uppercase; letter-spacing: 0.1em; color: var(--blue); margin-bottom: 0.25rem; }
  .contact-info-row p { font-size: 0.95rem; color: var(--text-dark); line-height: 1.6; }
  .contact-info-row a { color: var(--blue); text-decoration: none; }
  .contact-info-row a:hover { text-decoration: underline; }
  .contact-map-placeholder { background: var(--cream); border: 1px solid rgba(26,95,138,0.15); height: 280px; display: flex; align-items: center; justify-content: center; flex-direction: column; gap: 0.5rem; }
  .contact-note { margin-top: 2rem; padding: 1.25rem; background: var(--cream); border-left: 3px solid var(--sky); }
  .contact-note p { font-size: 0.85rem; color: var(--text-muted); line-height: 1.7; }

  /* FOOTER */
  footer { background: var(--navy); padding: 2.5rem 5vw; text-align: center; }
  footer p { color: rgba(255,255,255,0.35); font-size: 0.8rem; letter-spacing: 0.05em; }
  footer .footer-brand { font-family: 'Cormorant Garamond', serif; font-size: 1.2rem; color: var(--sky-light); margin-bottom: 0.5rem; }

  @media (max-width: 768px) {
    .hero-inner { grid-template-columns: 1fr; }
    .hero-photo-wrap { display: none; }
    .about-grid, .contact-grid { grid-template-columns: 1fr; gap: 2rem; }
    .nav-links { display: none; }
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
    <li><button id="admin-login-btn" style="background:none; border:1px solid var(--gold); color:var(--gold); padding:5px 12px; cursor:pointer; font-size:0.8rem; text-transform:uppercase; letter-spacing:0.08em;">Admin Login</button></li>
  </ul>
</nav>

<!-- HERO -->
<section class="hero">
  <div class="hero-inner">
    <div>
      <p class="hero-tag">Est. Since 1990 · Bhayandar, Maharashtra</p>
      <h1>Masters of<br><em>Fiberglass</em><br>& the Sea</h1>
      <p class="hero-desc">AK Mehra brings over 35 years of hands-on expertise in fishing boat manufacturing, repair, and advanced fiberglass work — trusted by fishermen, boat owners, and maritime businesses across the region.</p>
      <a href="#contact" class="hero-cta">Get in Touch</a>
      <div class="hero-stats">
        <div class="stat-item"><div class="stat-num">35+</div><div class="stat-label">Years Experience</div></div>
        <div class="stat-item"><div class="stat-num">7</div><div class="stat-label">Core Services</div></div>
        <div class="stat-item"><div class="stat-num">100%</div><div class="stat-label">Quality Commitment</div></div>
        <div class="stat-item"><div class="stat-num">∞</div><div class="stat-label">Satisfied Clients</div></div>
      </div>
    </div>
    <div class="hero-photo-wrap">
      <div class="hero-photo-frame">
        <!-- Placeholder online image jab tak aap upload na karein -->
        <img src="https://images.unsplash.com/photo-1559136555-9303baea8ebd?w=600" style="width:100%;">
      </div>
      <div class="hero-photo-name">
        <p>A.K. Mehra</p>
        <span>Founder & Chief Builder</span>
      </div>
    </div>
  </div>
</section>

<!-- WAVE DIVIDER -->
<div class="wave-divider">
  <svg viewBox="0 0 1200 120" preserveAspectRatio="none" style="height: 100%; width: 100%; fill: #f5f0e8;">
    <path d="M321.39,56.44c58-10.79,114.16-30.13,172-41.86,82.39-16.72,168.19-17.73,250.45-.39C823.78,31,906.67,72,985.66,92.83c70.05,18.48,146.53,26.09,214.34,3V0H0V120H321.39Z"></path>
  </svg>
</div>

<!-- ABOUT -->
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
        <p>Based in the coastal belt of Bhayandar, Maharashtra, AK Mehra has been the backbone of local fisherman and commercial boat owners since 1990. We specialize in high-end fiberglass reinforcement, high-durability gel coats, and structural restorations that withstand the harshest marine environments.</p>
        <p>Whether it is fabricating a new hull from scratch, upgrading trawler cabins, or executing emergency leak repairs, our team delivers master-level craftsmanship with uncompromised material quality.</p>
        <div class="about-highlight">
          <p>"A boat is more than a vessel—it’s a livelihood. We build it to survive the sea and secure your future."</p>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- SERVICES -->
<section id="services">
  <div class="section-inner">
    <p class="section-label">What We Do</p>
    <h2 class="section-title">Our Marine & Fiberglass Services</h2>
    <div class="services-grid">
      <div class="service-card"><h3>01</h3><h4>New Boat Manufacturing</h4><p>Custom fiberglass fishing boats and marine vessels built with durability, safety, and performance in mind.</p></div>
      <div class="service-card"><h3>02</h3><h4>Boat Repairing & Maintenance</h4><p>Complete repair, servicing, restoration, and preventive maintenance for all types of fiberglass boats.</p></div>
      <div class="service-card"><h3>03</h3><h4>Gelcoat & Finishing</h4><p>Professional gelcoat application, polishing, painting, and premium finishing for long-lasting protection.</p></div>
      <div class="service-card"><h3>04</h3><h4>Fish Storage Tank</h4><p>Manufacturing and installation of durable fiberglass fish storage tanks designed for marine environments.</p></div>
      <div class="service-card"><h3>05</h3><h4>Reinforcement & Modification</h4><p>Structural strengthening, hull modifications, deck upgrades, and custom marine solutions.</p></div>
      <div class="service-card"><h3>06</h3><h4>Boat Ice Box & Cabin Fitting</h4><p>Custom ice box fabrication, cabin fitting, interior modifications, and utility installations.</p></div>
    </div>
  </div>
</section>

<!-- GALLERY -->
<section id="gallery">
  <div class="section-inner">
    <p class="section-label">Our Portfolio</p>
    <h2 class="section-title">Project Gallery</h2>
    <div class="gallery-grid" id="dynamic-gallery">
        <div class="gallery-item"><img src="https://images.unsplash.com/photo-1567899378494-47b22a2ae96a?w=600"></div>
        <div class="gallery-item"><img src="https://images.unsplash.com/photo-1544551763-46a013bb70d5?w=600"></div>
        <div class="gallery-item"><img src="https://images.unsplash.com/photo-1517524206127-48bbd363f3d7?w=600"></div>
    </div>
  </div>
</section>

<!-- LOCATIONS -->
<section id="locations">
  <div class="section-inner">
    <p class="section-label">Work Locations</p>
    <h2 class="section-title">Locations Where We Successfully Completed Projects</h2>
    <p style="margin-top:20px; line-height:2; font-size:1.2rem; color: var(--blue);">
      Uran • Gorai • Ratnagiri • Porbandar • Mangrul • Alibaug
    </p>
  </div>
</section>

<!-- CONTACT -->
<section id="contact">
  <div class="section-inner">
    <p class="section-label">Connect with Us</p>
    <h2 class="section-title">Let's Discuss Your Vessel</h2>
    <div class="contact-grid">
      <div>
        <div class="contact-info-row">
          <div class="contact-icon"><svg viewBox="0 0 24 24"><path d="M12 2C8.13 2 5 5.13 5 9c0 5.25 7 13 7 13s7-7.75 7-13c0-3.87-3.13-7-7-7zm0 9.5c-1.38 0-2.5-1.12-2.5-2.5s1.12-2.5 2.5-2.5 2.5 1.12 2.5 2.5-1.12 2.5-2.5 2.5z"/></svg></div>
          <div><h4>Workshop Location</h4><p>Bhayandar West, Near Uttan Marine Area / Rai Village, Thane District, Maharashtra - 401101</p></div>
        </div>
        <div class="contact-info-row">
          <div class="contact-icon"><svg viewBox="0 0 24 24"><path d="M6.62 10.79c1.44 2.83 3.76 5.14 6.59 6.59l2.2-2.2c.27-.27.67-.36 1.02-.24 1.12.37 2.33.57 3.57.57.55 0 1 .45 1 1V20c0 .55-.45 1-1 1-9.39 0-17-7.61-17-17 0-.55.45-1 1-1h3.5c.55 0 1 .45 1 1 0 1.25.2 2.45.57 3.57.11.35.03.74-.25 1.02l-2.2 2.2z"/></svg></div>
          <div><h4>Call / WhatsApp for Consultation</h4><p><a href="tel:+918655411098">+91 86554 11098</a></p></div>
        </div>
        <div class="contact-info-row">
          <div class="contact-icon"><svg viewBox="0 0 24 24"><path d="M20 4H4c-1.1 0-1.99.9-1.99 2L2 18c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 4l-8 5-8-5V6l8 5 8-5v2z"/></svg></div>
          <div><h4>Email Enquiry</h4><p><a href="mailto:arun.mehra401105@gmail.com">arun.mehra401105@gmail.com</a></p></div>
        </div>
      </div>
      <div class="contact-map-placeholder" style="height:450px; padding:0;">
        <iframe src="https://maps.google.com/maps?q=Bhayandar%20West&t=&z=10&ie=UTF8&iwloc=&output=embed" width="100%" height="100%" style="border:0;" loading="lazy"></iframe>
      </div>
    </div>
  </div>
</section>

<!-- FOOTER -->
<footer>
  <div class="footer-brand">AK Mehra</div>
  <p>&copy; 2026 AK Mehra Fiberglass & Boat Specialists. All Rights Reserved.</p>
</footer>

</body>
</html>
"""

# Is code ki madad se aapka HTML pure webpage par automatic render (bann) jayega
components.html(html_content, height=4200, scrolling=True)
