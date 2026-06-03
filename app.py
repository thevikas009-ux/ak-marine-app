import streamlit as st
import streamlit.components.v1 as components
import base64
import os

# 1. Page Configuration
st.set_page_config(page_title="AK Mehra – Fiberglass & Boat Specialists", layout="wide")

# Function to load local image and convert to base64
def get_base64_image(image_path):
    if os.path.exists(image_path):
        with open(image_path, "rb") as img_file:
            return "data:image/jpeg;base64," + base64.b64encode(img_file.read()).decode()
    else:
        # Fallback image if local file is missing
        return "https://images.unsplash.com/photo-1559136555-9303baea8ebd?w=600"

# Hero Image path (Folder: images/a.jpg)
hero_img_base64 = get_base64_image("images/a.jpg")

# 2. GAP FIX: Streamlit ka default padding aur frame border hatane ke liye
st.markdown("""
    <style>
        .block-container {
            padding-top: 0rem !important;
            padding-bottom: 0rem !important;
            padding-left: 0rem !important;
            padding-right: 0rem !important;
        }
        iframe {
            display: block;
            border: none;
        }
        #MainMenu, header, footer {
            visibility: hidden;
            height: 0;
        }
    </style>
""", unsafe_allow_html=True)

# 3. Updated HTML Content
html_content = f"""
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
  *, *::before, *::after {{ box-sizing: border-box; margin: 0; padding: 0; }}
  :root {{
    --navy: #0d2640; --navy-mid: #153352; --blue: #1a5f8a; --sky: #5ba4cf;
    --sky-light: #a8d4f0; --cream: #f5f0e8; --gold: #c8a96e; --white: #ffffff;
    --text-dark: #0d1f33; --text-muted: #4a6580;
  }}
  html {{ scroll-behavior: smooth; }}
  body {{ font-family: 'Jost', sans-serif; background: var(--cream); color: var(--text-dark); overflow-x: hidden; }}

  /* NAVIGATION - Header Bada aur Gap Kam */
  nav {{ 
    position: fixed; top: 0; left: 0; right: 0; z-index: 1000; 
    background: rgba(13,38,64,0.98); display: flex; align-items: center; 
    justify-content: space-between; padding: 0 5vw; height: 75px; 
    border-bottom: 1px solid rgba(91,164,207,0.25); 
  }}
  .nav-brand {{ 
    font-family: 'Cormorant Garamond', serif; 
    font-size: 2.2rem; /* Bada Size */
    font-weight: 700; 
    color: var(--sky-light); 
    letter-spacing: 0.05em; 
  }}
  .nav-links {{ display: flex; gap: 2rem; list-style: none; align-items: center; }}
  .nav-links a {{ color: rgba(255,255,255,0.7); text-decoration: none; font-size: 0.9rem; text-transform: uppercase; letter-spacing: 0.08em; }}

  /* HERO SECTION - No Gap below header */
  .hero {{ 
    min-height: 90vh; 
    margin-top: 75px; /* Exact height of nav */
    background: linear-gradient(160deg, var(--navy) 0%, var(--navy-mid) 55%, var(--blue) 100%); 
    display: flex; align-items: center; padding: 40px 5vw; position: relative; overflow: hidden; 
  }}
  .hero-inner {{ max-width: 1200px; margin: 0 auto; width: 100%; display: grid; grid-template-columns: 1fr 1fr; gap: 3rem; align-items: center; }}
  .hero h1 {{ font-family: 'Cormorant Garamond', serif; font-size: clamp(3rem, 5vw, 4.5rem); color: var(--white); line-height: 1.05; }}
  .hero h1 em {{ font-style: italic; color: var(--sky-light); }}
  .hero-cta {{ display: inline-block; padding: 0.85rem 2.2rem; border: 1px solid var(--sky); color: var(--sky-light); text-decoration: none; text-transform: uppercase; transition: 0.3s; margin-top: 25px; }}
  .hero-cta:hover {{ background: var(--sky); color: var(--navy); }}
  
  .hero-photo-frame {{ width: 100%; max-width: 450px; aspect-ratio: 1/1; margin: 0 auto; padding: 8px; position: relative; }}
  .hero-photo-frame img {{ width: 100%; height: 100%; object-fit: cover; border-radius: 50%; border: 4px solid var(--sky); }}

  /* SECTIONS */
  section {{ padding: 5rem 5vw; }}
  .section-title {{ font-family: 'Cormorant Garamond', serif; font-size: clamp(2rem, 4vw, 3rem); color: var(--navy); margin-bottom: 2rem; }}

  /* GALLERY MOVING & DELETE */
  #gallery {{ background: var(--navy); overflow: hidden; position: relative; }}
  .gallery-grid {{ display: flex; gap: 20px; width: max-content; animation: scrollGallery 35s linear infinite; padding: 20px 0; }}
  .gallery-grid:hover {{ animation-play-state: paused; }}
  .gallery-item {{ 
    width: 300px; height: 220px; flex-shrink: 0; border-radius: 12px; 
    overflow: hidden; position: relative; box-shadow: 0 8px 25px rgba(0,0,0,.25); 
  }}
  .gallery-item img {{ width: 100%; height: 100%; object-fit: cover; }}
  
  .del-btn {{ 
    position: absolute; top: 10px; right: 10px; background: red; color: white; 
    border: none; border-radius: 50%; width: 30px; height: 30px; cursor: pointer; 
    z-index: 10; display: none; /* Hidden by default */
  }}
  
  @keyframes scrollGallery {{ 0% {{ transform: translateX(0); }} 100% {{ transform: translateX(-50%); }} }}

  /* CONTACT */
  .contact-grid {{ display: grid; grid-template-columns: 1fr 1fr; gap: 4rem; align-items: start; }}
  .contact-info-row {{ display: flex; align-items: flex-start; gap: 1rem; padding: 1.25rem 0; border-bottom: 1px solid rgba(26,95,138,0.1); }}
  .contact-icon {{ width: 40px; height: 40px; background: var(--navy); display: flex; align-items: center; justify-content: center; flex-shrink: 0; border-radius: 4px; }}
  .contact-icon svg {{ width: 20px; fill: var(--sky-light); }}
  .contact-info-row a {{ color: var(--blue); text-decoration: none; }}
  
  #map {{ height: 450px; width: 100%; border-radius: 12px; border: 1px solid #ddd; }}

  footer {{ background: var(--navy); padding: 2rem; text-align: center; color: rgba(255,255,255,0.4); }}
</style>
</head>
<body>

<nav>
  <div class="nav-brand">A K Mehra</div>
  <ul class="nav-links">
    <li><a href="#services">Services</a></li>
    <li><a href="#gallery">Gallery</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><button id="admin-login-btn" style="background:none; border:1px solid var(--gold); color:var(--gold); padding:5px 12px; cursor:pointer;">Admin Login</button></li>
  </ul>
</nav>

<section class="hero">
  <div class="hero-inner">
    <div>
      <p style="color:var(--sky); letter-spacing: 3px; font-weight:600;">EST. SINCE 1990</p>
      <h1>Masters of<br><em>Fiberglass</em><br>& the Sea</h1>
      <p style="color:rgba(255,255,255,0.7); margin-top:20px; line-height:1.7;">AK Mehra brings over 35 years of hands-on expertise in fishing boat manufacturing and heavy structural marine repair.</p>
      <a href="#contact" class="hero-cta">Get in Touch</a>
    </div>
    <div class="hero-photo-frame">
      <img src="{hero_img_base64}" alt="AK Mehra Boat Work">
    </div>
  </div>
</section>

<section id="services">
  <h2 class="section-title">Our Marine Services</h2>
  <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 20px;">
    <div style="background: #fff; padding: 30px; border-radius: 12px; border-top: 4px solid var(--navy);"><h3>01</h3><h4>Boat Manufacturing</h4><p>Custom fiberglass vessels built with high seawater resistance.</p></div>
    <div style="background: #fff; padding: 30px; border-radius: 12px; border-top: 4px solid var(--navy);"><h3>02</h3><h4>Repair & Maintenance</h4><p>Complete restoration and preventive servicing for all boats.</p></div>
    <div style="background: #fff; padding: 30px; border-radius: 12px; border-top: 4px solid var(--navy);"><h3>03</h3><h4>Gelcoat Finishing</h4><p>Premium protective coating for long-lasting performance.</p></div>
  </div>
</section>

<section id="gallery">
  <h2 class="section-title" style="color:#fff;">Project Gallery</h2>
  <div class="gallery-grid" id="dynamic-gallery"></div>
</section>

<section id="contact">
  <h2 class="section-title">Connect with Us</h2>
  <div class="contact-grid">
    <div>
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
</section>

<section id="admin-upload" style="display:none; background:#fff; border-top: 2px solid var(--navy); padding: 3rem 5vw;">
  <div style="max-width:500px; margin: 0 auto;">
    <h3>Admin: Manage Portfolio</h3>
    <p style="font-size: 0.8rem; color: #666; margin-bottom: 10px;">Select photos to add to gallery:</p>
    <input type="file" id="admin-file-input" multiple style="width:100%; margin-bottom: 20px;">
    <button id="upload-submit-btn" style="background:var(--navy); color:#fff; width:100%; border:none; padding: 12px; cursor:pointer;">UPLOAD PHOTOS</button>
  </div>
</section>

<footer>
  <p>© 2026 AK Mehra Fiberglass Boat Specialists. All Rights Reserved.</p>
</footer>

<script src="https://unpkg.com/leaflet/dist/leaflet.js"></script>
<script>
  // 1. Map Logic - Added Mangrol & Porbandar
  const map = L.map('map').setView([19.3090, 72.7850], 6);
  L.tileLayer('https://{{s}}.tile.openstreetmap.org/{{z}}/{{x}}/{{y}}.png').addTo(map);
  const locs = [
    {{n:"Bhayandar (HQ)", c:[19.3090, 72.7850]}},
    {{n:"Uran", c:[18.8770, 72.9430]}},
    {{n:"Gorai", c:[19.2372, 72.7811]}},
    {{n:"Ratnagiri", c:[16.9902, 73.3120]}},
    {{n:"Alibaug", c:[18.6585, 72.8777]}},
    {{n:"Mangrol", c:[21.1217, 70.1162]}},
    {{n:"Porbandar", c:[21.6417, 69.6293]}}
  ];
  locs.forEach(l => L.marker(l.c).addTo(map).bindPopup(l.n));

  // 2. Gallery Logic with Delete
  const initial = [
    "https://images.unsplash.com/photo-1567899378494-47b22a2ae96a?w=400",
    "https://images.unsplash.com/photo-1544551763-46a013bb70d5?w=400",
    "https://images.unsplash.com/photo-1517524206127-48bbd363f3d7?w=400",
    "https://images.unsplash.com/photo-1505242844900-33230a1bf64c?w=400"
  ];
  
  let adminPics = JSON.parse(localStorage.getItem('ak_pics')) || [];
  let isAdmin = false;

  function deleteImg(index) {{
    if(confirm("Delete this photo?")) {{
        adminPics.splice(index, 1);
        localStorage.setItem('ak_pics', JSON.stringify(adminPics));
        render();
    }}
  }}

  function render() {{
    const grid = document.getElementById('dynamic-gallery');
    // Combine admin pics first so they are deleteable
    let html = adminPics.map((src, i) => `
        <div class="gallery-item">
            <button class="del-btn" onclick="deleteImg(${{i}})" style="display:${{isAdmin?'block':'none'}}">X</button>
            <img src="${{src}}">
        </div>
    `).join('');
    
    // Add initial pics (Non-deleteable)
    html += initial.map(src => `<div class="gallery-item"><img src="${{src}}"></div>`).join('');
    
    // Repeat for infinite animation
    grid.innerHTML = html + html; 
  }}
  render();

  // 3. Admin Login
  document.getElementById('admin-login-btn').onclick = () => {{
    const p = prompt("Enter Admin Password:");
    if(p === "mehra123") {{
        isAdmin = true;
        document.getElementById('admin-upload').style.display = "block";
        const btns = document.querySelectorAll('.del-btn');
        btns.forEach(b => b.style.display = 'block');
        alert("Admin Mode Active: Delete buttons enabled in gallery.");
        window.location.hash = "#admin-upload";
    }}
  }};

  // 4. Upload Logic
  document.getElementById('upload-submit-btn').onclick = () => {{
    const files = document.getElementById('admin-file-input').files;
    if(files.length === 0) return alert("Please select photos");
    
    Array.from(files).forEach(f => {{
        const r = new FileReader();
        r.onload = (e) => {{
            adminPics.unshift(e.target.result);
            localStorage.setItem('ak_pics', JSON.stringify(adminPics));
            render();
        }};
        r.readAsDataURL(f);
    }});
    alert("Photos added to gallery!");
  }};
</script>
</body>
</html>
"""

# 4. Final Render
components.html(html_content, height=4500, scrolling=True)
