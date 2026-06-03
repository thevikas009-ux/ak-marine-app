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
html_content = """
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
  <ul class="nav-links
