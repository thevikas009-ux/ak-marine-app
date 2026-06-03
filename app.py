import streamlit as st
import streamlit.components.v1 as components

# Page ki settings
st.set_page_config(page_title="AK Mehra – Fiberglass & Boat Specialists", layout="wide")

# Aapka HTML content
html_code = """
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
  /* Baki ka aapka pura HTML, CSS, aur Script code jo aapne mujhe bheja tha... */
</style>
</head>
<body>
  <!-- Aapka pura body ka content -->
</body>
</html>
"""

# HTML ko full screen display karne ke liye
components.html(html_code, height=3500, scrolling=True)
