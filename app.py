import streamlit as st
import streamlit.components.v1 as components

# 1. Page Configuration and Padding Fix
st.set_page_config(page_title="AK Mehra – Fiberglass & Boat Specialists", layout="wide")

# Streamlit ka default padding hatane ke liye CSS
st.markdown("""
    <style>
        .block-container {
            padding-top: 0rem;
            padding-bottom: 0rem;
            padding-left: 0rem;
            padding-right: 0rem;
        }
        iframe {
            display: block;
        }
    </style>
""", unsafe_allow_html=True)

# 2. Updated HTML Content (CSS Fixes Included)
html_content = r"""
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,600;1,400&family=Jost:wght@300;400;500&display=swap" rel="stylesheet">
<style>
  *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
  :root {
    --navy: #0d2640; --navy-mid: #153352; --blue: #1a5f8a; --sky: #5ba4cf;
    --sky-light: #a8d4f0; --cream: #f5f0e8; --gold: #c8a96e; --white: #ffffff;
  }
  body {
    font-family: 'Jost', sans-serif;
    background: var(--cream);
    overflow-x: hidden;
  }

  /* GAP FIX: Hero height ko fix kiya gaya hai */
  .hero { 
    min-height: 700px; /* 100vh ki jagah fixed height taaki gap na aaye */
    background: linear-gradient(160deg, var(--navy) 0%, var(--navy-mid) 55%, var(--blue) 100%); 
    display: flex; align-items: center; padding: 80px 5vw; position: relative; 
  }
  
  nav { position: fixed; top: 0; left: 0; right: 0; z-index: 100; background: rgba(13,38,64,0.97); display: flex; align-items: center; justify-content: space-between; padding: 0 5vw; height: 64px; }
  .nav-brand { font-family: 'Cormorant Garamond', serif; font-size: 1.5rem; color: var(--sky-light); }
  .nav-links { display: flex; gap: 2rem; list-style: none; }
  .nav-links a { color: #fff; text-decoration: none; font-size: 0.8rem; text-transform: uppercase; }

  .hero-inner { max-width: 1200px; margin: 0 auto; display: grid; grid-template-columns: 1fr 1fr; gap: 2rem; }
  .hero h1 { font-family: 'Cormorant Garamond', serif; font-size: 4rem; color: #fff; line-height: 1.1; }
  .hero-desc { color: rgba(255,255,255,0.7); margin: 20px 0; }
  
  section { padding: 4rem 5vw; } /* Padding thoda kam kiya takki content paas dikhe */
  .section-title { font-family: 'Cormorant Garamond', serif; font-size: 2.5rem; color: var(--navy); margin-bottom: 2rem; }

  .services-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 20px; }
  .service-card { background: #fff; padding: 30px; border-radius: 8px; border-top: 4px solid var(--navy); }

  .gallery-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(250px, 1fr)); gap: 15px; }
  .gallery-item img { width: 100%; border-radius: 8px; }

  footer { background: var(--navy); color: #fff; padding: 2rem; text-align: center; }
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
  </ul>
</nav>

<section class="hero">
  <div class="hero-inner">
    <div>
      <h1>Masters of Fiberglass & the Sea</h1>
      <p class="hero-desc">Trusted boat builders with 35+ years of experience in Maharashtra.</p>
      <a href="#contact" style="background: var(--sky); color: white; padding: 12px 24px; text-decoration: none; border-radius: 4px;">Get in Touch</a>
    </div>
    <div style="text-align: center;">
      <img src="https://images.unsplash.com/photo-1559136555-9303baea8ebd?w=400" style="border-radius: 10px; width: 300px;">
    </div>
  </div>
</section>

<section id="services">
  <h2 class="section-title">Our Services</h2>
  <div class="services-grid">
    <div class="service-card"><h3>01</h3><h4>Boat Manufacturing</h4><p>Custom fiberglass vessels built for Indian waters.</p></div>
    <div class="service-card"><h3>02</h3><h4>Repair & Maintenance</h4><p>High-quality fiberglass restoration.</p></div>
    <div class="service-card"><h3>03</h3><h4>Gelcoat Finishing</h4><p>Premium finish for long-lasting protection.</p></div>
  </div>
</section>

<section id="locations" style="background: #fff;">
  <h2 class="section-title">Work Locations</h2>
  <p>Uran • Gorai • Ratnagiri • Porbandar • Mangrul • Alibaug</p>
</section>

<footer>
  <p>&copy; 2026 AK Mehra Fiberglass Specialists</p>
</footer>

</body>
</html>
"""

# 3. HTML Render Fix
# height ko thoda kam kiya aur scrolling enable ki takki sahi dikhe
components.html(html_content, height=2500, scrolling=True)
