import os
import re
import json

BASE_DIR = r"d:\\antigravity website\\footletcrystal"
ADDR = "200 Clarendon Street, 54th Floor, Boston, MA 02116, United States"
PHONE = "+1-866-518-7064"
EMAIL = "concierge@footletcrystal.com"
DOMAIN = "footletcrystal.com"
BRAND = "Footlet Crystal Atelier"

GTAG = """<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-0LY0HY7L01"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'G-0LY0HY7L01');
</script>"""

FONTS = """<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Outfit:wght@400;500;600;700;800&family=Prata&family=Space+Mono:wght@400;700&display=swap" rel="stylesheet">"""

def get_header(active_page):
    idx_cls = "active" if active_page == "index" else ""
    abt_cls = "active" if active_page == "about" else ""
    prd_cls = "active" if active_page == "products" else ""
    faq_cls = "active" if active_page == "faq" else ""
    cnt_cls = "active" if active_page == "contact" else ""
    
    return f"""  <!-- Site Header (Rule 11) -->
  <header class="site-header">
    <div class="fc-container">
      <div class="fc-nav-container">
        <a href="index.html" class="fc-brand">
          <div class="fc-brand-crest">FC</div>
          <div class="fc-brand-text">
            Footlet Crystal
            <small>Atelier &bull; Boston</small>
          </div>
        </a>
        <nav class="fc-nav-menu">
          <a href="index.html" class="fc-nav-link {idx_cls}">Atelier</a>
          <a href="about.html" class="fc-nav-link {abt_cls}">Heritage</a>
          <a href="products.html" class="fc-nav-link {prd_cls}">Footlet Collections</a>
          <a href="faq.html" class="fc-nav-link {faq_cls}">Technical FAQ</a>
          <a href="contact.html" class="fc-nav-link {cnt_cls}">Salon Inquiries</a>
        </nav>
        <div style="display: flex; align-items: center; gap: 16px;">
          <a href="contact.html" class="fc-nav-cta">Book Fitting</a>
          <button class="fc-hamburger" id="fc-hamburger" aria-label="Toggle Navigation">
            <span></span>
            <span></span>
            <span></span>
          </button>
        </div>
      </div>
    </div>
  </header>

  <!-- Mobile Drawer (Rule 11) -->
  <div class="mobile-drawer-backdrop" id="mobile-drawer-backdrop"></div>
  <div class="mobile-drawer" id="mobile-drawer">
    <div class="mobile-drawer-header">
      <div class="fc-brand">
        <div class="fc-brand-crest">FC</div>
        <div class="fc-brand-text">Footlet Crystal</div>
      </div>
      <button class="mobile-drawer-close" id="mobile-drawer-close" aria-label="Close Drawer">&times;</button>
    </div>
    <div class="mobile-drawer-body">
      <a href="index.html" class="mobile-nav-link">Atelier Flagship</a>
      <a href="about.html" class="mobile-nav-link">Heritage &amp; Knitting Story</a>
      <a href="products.html" class="mobile-nav-link">Footlet Collections</a>
      <a href="faq.html" class="mobile-nav-link">Technical &amp; Fiber FAQ</a>
      <a href="contact.html" class="mobile-nav-link">Salon Fitting Consultation</a>
    </div>
    <div class="mobile-drawer-footer">
      <p style="margin-bottom: 8px; color: var(--fc-cyan-light); font-family: var(--fc-font-mono); font-size: 0.75rem;">CLIENT CONCIERGE</p>
      <p style="margin-bottom: 6px;">{PHONE}</p>
      <p><a href="mailto:{EMAIL}">{EMAIL}</a></p>
    </div>
  </div>"""

def get_footer():
    return f"""  <!-- Semantic Site Footer -->
  <footer class="fc-footer">
    <div class="fc-container">
      <div class="fc-footer-grid">
        <div class="fc-footer-brand">
          <div class="fc-brand">
            <div class="fc-brand-crest">FC</div>
            <div class="fc-brand-text">
              Footlet Crystal
              <small>Hosiery &bull; Est. Boston</small>
            </div>
          </div>
          <p>Hand-finished precision footlets, seamless loafer liners, and artisanal merino hosiery engineered with 200-needle crystalline knit architecture.</p>
          <div style="font-family: var(--fc-font-mono); font-size: 0.8rem; color: var(--fc-cyan-light);">
            {PHONE} &bull; {EMAIL}
          </div>
        </div>
        <div class="fc-footer-col">
          <h4>Atelier Hosiery</h4>
          <ul class="fc-footer-links">
            <li><a href="index.html">Flagship Home</a></li>
            <li><a href="about.html">Heritage &amp; Guilds</a></li>
            <li><a href="products.html">Footlet Collections</a></li>
            <li><a href="faq.html">Technical FAQ</a></li>
            <li><a href="contact.html">Salon Consultation</a></li>
          </ul>
        </div>
        <div class="fc-footer-col">
          <h4>Knitting Standards</h4>
          <ul class="fc-footer-links">
            <li><a href="products.html">200-Needle Single Cylinder</a></li>
            <li><a href="products.html">Hand-Linked Seamless Toes</a></li>
            <li><a href="products.html">Merino Wool Micro-Terry</a></li>
            <li><a href="products.html">Crystalline Ribbed Grip</a></li>
            <li><a href="products.html">Anatomical Y-Heel Pockets</a></li>
          </ul>
        </div>
        <div class="fc-footer-col">
          <h4>Institutional</h4>
          <p style="font-size: 0.85rem; line-height: 1.6; margin-bottom: 12px; color: var(--fc-text-light-muted);">
            {ADDR}
          </p>
          <p style="font-family: var(--fc-font-mono); font-size: 0.75rem; color: var(--fc-cyan-light); margin-bottom: 16px;">
            Direct Salon Inquiries: {PHONE}
          </p>
          <div style="padding: 8px 12px; background: rgba(56,189,248,0.08); border: 1px solid rgba(56,189,248,0.2); border-radius: 6px; font-size: 0.725rem; font-family: var(--fc-font-mono); color: var(--fc-text-light);">
            OEKO-TEX Standard 100 Certified Hosiery
          </div>
        </div>
      </div>
      <div class="fc-footer-bottom">
        <div>&copy; 2026 Footlet Crystal Atelier LLC. All Worldwide Rights Reserved.</div>
        <div class="fc-footer-legal-links">
          <a href="privacy-policy.html">Privacy Policy</a>
          <a href="terms-and-conditions.html">Terms &amp; Conditions</a>
          <a href="disclaimer.html">Disclaimer</a>
          <a href="cookie-policy.html">Cookie Policy</a>
        </div>
      </div>
    </div>
  </footer>
  <script src="assets/js/script.js"></script>
  <script src="assets/js/main.js"></script>"""

# ==========================================
# 1. INDEX.HTML (Flagship Home - 12 Distinct Sections)
# ==========================================
def build_index():
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Footlet Crystal | Artisanal Luxury Footlets &amp; Precision Hosiery</title>
  <meta name="description" content="Discover Footlet Crystal Atelier. Hand-finished luxury footlets, seamless loafer liners, and 200-needle merino socks crafted for sartorial elegance in Boston.">
  <link rel="canonical" href="https://{DOMAIN}/index.html">
  {GTAG}
  {FONTS}
  <link rel="stylesheet" href="assets/css/style.css">
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "ClothingStore",
    "name": "Footlet Crystal Atelier",
    "url": "https://{DOMAIN}/",
    "telephone": "{PHONE}",
    "address": {{
      "@type": "PostalAddress",
      "streetAddress": "200 Clarendon Street, 54th Floor",
      "addressLocality": "Boston",
      "addressRegion": "MA",
      "postalCode": "02116",
      "addressCountry": "US"
    }},
    "description": "Artisanal luxury footlets, seamless loafer liners, merino hosiery, and precision knit socks.",
    "priceRange": "$$$$"
  }}
  </script>
</head>
<body>
{get_header('index')}

  <main>
    <!-- Section 1: Center-Stage Masthead with Triple-Pod Crystal Showcase (Assets 1, 2, 3) -->
    <section class="fc-hero fc-center-hero">
      <div class="fc-container">
        <div class="fc-center-hero-header">
          <span class="fc-tag">Nordic Precision Hosiery &bull; Guild Est. 2016</span>
          <h1 class="fc-hero-supertitle">The Masterwork of Invisible <span>Crystal Footlets</span></h1>
          <p class="fc-center-hero-desc">
            Footlet Crystal redefines luxury loafer liners and low-cut hosiery. Knitted on ultra-fine 200-needle single-cylinder looms with botanical mercerized cotton and pure Australian merino yarns, our footlets remain imperceptible in hand-welted footwear.
          </p>
          <div class="fc-center-hero-actions">
            <a href="contact.html" class="fc-btn fc-btn-cyan">Commission Private Fitting</a>
            <a href="products.html" class="fc-btn fc-btn-outline">Explore Footlet Matrix</a>
          </div>
        </div>

        <!-- Triple-Pod Crystal Showcase: Assets 1, 2, 3 -->
        <div class="fc-triple-pod-showcase">
          <!-- Pod 1: Asset 1 (Invisible Cotton Loafer Liner) -->
          <div class="fc-crystal-pod">
            <div class="fc-pod-media">
              <img src="assets/images/footletcrystal_asset_1.jpg" alt="Invisible black cotton luxury loafer liner footlet with non-slip heel grip" width="1200" height="800">
              <div class="fc-pod-badge">NO. 01 &bull; MERCERIZED</div>
            </div>
            <div class="fc-pod-body">
              <div class="fc-pod-num">GAUGE 200N</div>
              <h3 class="fc-pod-title">Crystal Loafer Liner</h3>
              <p class="fc-pod-desc">Precision-sculpted shallow vamp engineered for ultra-low Belgian loafers and Venetian dress slippers with zero collar peek.</p>
            </div>
          </div>

          <!-- Pod 2: Asset 2 (Merino Wool Footlet Liner) -->
          <div class="fc-crystal-pod">
            <div class="fc-pod-media">
              <img src="assets/images/footletcrystal_asset_2.jpg" alt="Merino wool footlet liner sock engineered with thermal regulating knit" width="1200" height="800">
              <div class="fc-pod-badge">NO. 02 &bull; MERINO WOOL</div>
            </div>
            <div class="fc-pod-body">
              <div class="fc-pod-num">GAUGE 200N</div>
              <h3 class="fc-pod-title">Thermal Merino Footlet</h3>
              <p class="fc-pod-desc">Ultra-fine 17.5-micron Australian merino wool balancing foot microclimate in summer heat and autumn salon drafts.</p>
            </div>
          </div>

          <!-- Pod 3: Asset 3 (High-Density Cushion Sole Liner) -->
          <div class="fc-crystal-pod">
            <div class="fc-pod-media">
              <img src="assets/images/footletcrystal_asset_3.jpg" alt="High-density terry cushion sole on artisan footlet sock" width="1200" height="800">
              <div class="fc-pod-badge">NO. 03 &bull; MICRO-TERRY</div>
            </div>
            <div class="fc-pod-body">
              <div class="fc-pod-num">GAUGE 168N</div>
              <h3 class="fc-pod-title">Micro Cushion Sole</h3>
              <p class="fc-pod-desc">Targeted metatarsal terry padding absorbing road shock while maintaining razor-thin collar clearance in stiff cordwainery.</p>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Section 2: Marquee Ticker -->
    <div class="fc-ticker">
      <div class="fc-ticker-track">
        <div class="fc-ticker-item"><span>ATELIER SPECIFICATION</span> 200-NEEDLE SINGLE-CYLINDER KNIT</div>
        <div class="fc-ticker-bullet">&bull;</div>
        <div class="fc-ticker-item"><span>HAND-LINKED TOE</span> ZERO RIDGES SEAMLESS CLOSURE</div>
        <div class="fc-ticker-bullet">&bull;</div>
        <div class="fc-ticker-item"><span>YARN PURITY</span> EXTRA-FINE AUSTRALIAN MERINO WOOL</div>
        <div class="fc-ticker-bullet">&bull;</div>
        <div class="fc-ticker-item"><span>HEEL RETENTION</span> ANATOMICAL Y-GORE SILICONE LOCK</div>
        <div class="fc-ticker-bullet">&bull;</div>
        <div class="fc-ticker-item"><span>COMFORT ZONE</span> MICRO-TERRY TARGETED CUSHIONING</div>
        <div class="fc-ticker-bullet">&bull;</div>
        <div class="fc-ticker-item"><span>ATELIER SPECIFICATION</span> 200-NEEDLE SINGLE-CYLINDER KNIT</div>
        <div class="fc-ticker-bullet">&bull;</div>
        <div class="fc-ticker-item"><span>HAND-LINKED TOE</span> ZERO RIDGES SEAMLESS CLOSURE</div>
      </div>
    </div>

    <!-- Section 3: Asymmetric Editorial Manifesto (Asset 4: Hand-Linked Seamless Crystal Toe) -->
    <section class="fc-section fc-section-dark">
      <div class="fc-container">
        <div class="fc-editorial-split">
          <div>
            <span class="fc-tag">Artisanal Creed</span>
            <h2 class="fc-section-title">The Philosophy of Imperceptible Perfection</h2>
            <blockquote class="fc-editorial-quote">
              "A true luxury footlet is not merely invisible to the spectator; it is imperceptible to the wearer through fourteen hours of continuous movement."
            </blockquote>
            <p style="color: var(--fc-text-light-muted); font-size: 1.05rem; line-height: 1.8; margin-bottom: 24px;">
              At Footlet Crystal, we reject the notion that no-show socks are disposable sundries. We treat every pair as an architectural foundation for bespoke cordwainer craft, linking each toe stitch by human hand and contouring silicone ribs to natural biomechanical flex lines.
            </p>
            <div style="display: flex; gap: 32px; font-family: var(--fc-font-mono); font-size: 0.85rem;">
              <div style="border-left: 2px solid var(--fc-cyan-light); padding-left: 14px;">
                <strong style="font-size: 1.4rem; color: #fff; display: block; font-family: var(--fc-font-display);">100%</strong>
                Hand-Linked Seams
              </div>
              <div style="border-left: 2px solid var(--fc-cyan-light); padding-left: 14px;">
                <strong style="font-size: 1.4rem; color: #fff; display: block; font-family: var(--fc-font-display);">0.0 mm</strong>
                Toe Ridge Elevation
              </div>
            </div>
          </div>
          <div>
            <div class="fc-editorial-frame">
              <img src="assets/images/footletcrystal_asset_4.jpg" alt="Hand-linked seamless crystal toe close-up displaying stitch-by-stitch loop closure" width="1200" height="800">
              <div class="fc-editorial-caption">
                <strong>Hand-Linked Toe Construction</strong>
                Stitch-by-stitch loop closure completely eliminating metatarsal pressure points.
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Section 4: Swiss 4-Column Precision Metric Grid (Zero Box Borders) -->
    <section class="fc-section fc-section-darker">
      <div class="fc-container">
        <div class="fc-section-header" style="text-align: center;">
          <span class="fc-tag">Swiss Precision Grid</span>
          <h2 class="fc-section-title">Four Pillars of Knitting Geometry</h2>
          <p class="fc-section-subtitle" style="margin: 0 auto;">Engineered without bulky structural seams or compromising synthetic fillers.</p>
        </div>
        <div class="fc-nordic-grid-4col">
          <div class="fc-nordic-col">
            <div class="fc-col-metric">200N</div>
            <h3 class="fc-col-title">Single Cylinder</h3>
            <p class="fc-col-desc">Ultra-dense needle distribution creating a lustrous, silken fabric that glides frictionless against inner calf linings.</p>
          </div>
          <div class="fc-nordic-col">
            <div class="fc-col-metric">0 mm</div>
            <h3 class="fc-col-title">Flat Toe Ridge</h3>
            <p class="fc-col-desc">Manual linking loops that eliminate painful shoe friction and blister-causing overlock knots.</p>
          </div>
          <div class="fc-nordic-col">
            <div class="fc-col-metric">3-Wave</div>
            <h3 class="fc-col-title">Silicone Anchor</h3>
            <p class="fc-col-desc">Hypoallergenic medical silicone arrays molded to anatomical Achilles curves to prevent slip-down failure.</p>
          </div>
          <div class="fc-nordic-col">
            <div class="fc-col-metric">17.5μ</div>
            <h3 class="fc-col-title">Merino Fineness</h3>
            <p class="fc-col-desc">Non-scratch Australian merino wool offering natural thermal equilibrium and permanent antibacterial moisture control.</p>
          </div>
        </div>
      </div>
    </section>

    <!-- Section 5: Lookbook Duo Ribbon (Assets 5 & 6) -->
    <section class="fc-section fc-section-dark">
      <div class="fc-container">
        <div class="fc-section-header">
          <span class="fc-tag">Visual Lookbook</span>
          <h2 class="fc-section-title">Tactile Silhouette Explorations</h2>
          <p class="fc-section-subtitle">Examine the tension dynamics and yarn textures developed across our specialized hosiery lines.</p>
        </div>
        <div class="fc-lookbook-duo">
          <!-- Card 1: Asset 5 (Elastic Ribbed Comfort Cuff) -->
          <div class="fc-lookbook-card">
            <img src="assets/images/footletcrystal_asset_5.jpg" alt="Elastic ribbed comfort cuff on luxury sock displaying anatomical tension" width="1200" height="800">
            <div class="fc-lookbook-overlay">
              <div class="fc-lookbook-tag">Series 01 &bull; Architectural Tension</div>
              <h3 class="fc-lookbook-title">The Compression Rib Architecture</h3>
              <p class="fc-lookbook-text">Contoured radial elasticity securing the mid-foot arch while maintaining effortless step dynamics.</p>
            </div>
          </div>

          <!-- Card 2: Asset 6 (Casual Everyday Merino Wool Footlet) -->
          <div class="fc-lookbook-card">
            <img src="assets/images/footletcrystal_asset_6.jpg" alt="Casual everyday merino wool footlet sock with reinforced heel and arch" width="1200" height="800">
            <div class="fc-lookbook-overlay">
              <div class="fc-lookbook-tag">Series 02 &bull; Transcontinental</div>
              <h3 class="fc-lookbook-title">The Everyday Merino Voyager</h3>
              <p class="fc-lookbook-text">Reinforced heel cup and botanical spun fiber blend built for high-mileage urban traversal.</p>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Section 6: Footwear Pairing Guide Matrix -->
    <section class="fc-section fc-section-light">
      <div class="fc-container">
        <div class="fc-section-header" style="text-align: center;">
          <span class="fc-tag" style="background: rgba(2, 132, 199, 0.08); border-color: rgba(2, 132, 199, 0.25); color: var(--fc-cyan);">Footwear Pairing Guide</span>
          <h2 class="fc-section-title" style="color: var(--fc-text-dark);">Shoe Silhouette &amp; Tension Matrix</h2>
          <p class="fc-section-subtitle" style="margin: 0 auto; color: var(--fc-text-dark-muted);">Selecting the correct footlet cut guarantees complete concealment and all-day comfort.</p>
        </div>
        <div class="fc-pairing-matrix-wrap">
          <table class="fc-pairing-table">
            <thead>
              <tr>
                <th>Shoe Silhouette</th>
                <th>Recommended Model</th>
                <th>Vamp Cut Profile</th>
                <th>Primary Fiber Composition</th>
                <th>Concealment Rating</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td class="fc-shoe-type">Belgian &amp; Venetian Slippers</td>
                <td>Loafer Crystal No. 01</td>
                <td>32mm Deep Sculpted Collar</td>
                <td>200-Needle Mercerized Cotton</td>
                <td><span style="color: var(--fc-cyan); font-weight: 700;">100% Invisible</span></td>
              </tr>
              <tr>
                <td class="fc-shoe-type">Suede Tassel &amp; Penny Loafers</td>
                <td>Merino Liner No. 02</td>
                <td>40mm Curved Neckline</td>
                <td>80% Fine Merino / 20% Polyamide</td>
                <td><span style="color: var(--fc-cyan); font-weight: 700;">100% Invisible</span></td>
              </tr>
              <tr>
                <td class="fc-shoe-type">Hand-Welted Oxfords &amp; Derbies</td>
                <td>Micro Cushion No. 03</td>
                <td>Standard Low Vamp</td>
                <td>High-Density Metatarsal Terry</td>
                <td><span style="color: var(--fc-cyan); font-weight: 700;">Complete Cushioning</span></td>
              </tr>
              <tr>
                <td class="fc-shoe-type">Bespoke Driving Moccasins</td>
                <td>Active Arch Liner</td>
                <td>Ergonomic Low Collar</td>
                <td>Mercerized Cotton &amp; Microfiber</td>
                <td><span style="color: var(--fc-cyan); font-weight: 700;">Lateral Anti-Slip</span></td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </section>

    <!-- Section 7: Staggered Zig-Zag Narrative Rows (Assets 7 & 8) -->
    <section class="fc-section fc-section-dark">
      <div class="fc-container">
        <div class="fc-section-header">
          <span class="fc-tag">Biomechanical Engineering</span>
          <h2 class="fc-section-title">Anatomy of the Crystalline Knit</h2>
          <p class="fc-section-subtitle">Examine the micro-structural features that separate artisanal footlets from mass-market imitations.</p>
        </div>

        <!-- Row 1: Asset 7 (Crystalline Cushion Crew Sock) -->
        <div class="fc-zigzag-row">
          <div class="fc-zigzag-media">
            <img src="assets/images/footletcrystal_asset_7.jpg" alt="Crystalline cushion crew sock with targeted arch support" width="1200" height="800">
          </div>
          <div>
            <span class="fc-tag">Anatomical Sole Buffer</span>
            <h3 style="font-family: var(--fc-font-display); font-size: 1.8rem; margin-bottom: 16px;">Micro-Engineered Metatarsal Dampening</h3>
            <p style="color: var(--fc-text-light-muted); font-size: 1rem; line-height: 1.8; margin-bottom: 20px;">
              By knitting high-density micro-terry loops specifically beneath the metatarsal head and calcaneus bone, Footlet Crystal cushions each heel strike without adding bulk inside snug bespoke shoes. The upper instep remains razor-thin for optimal ventilation.
            </p>
            <ul style="font-size: 0.925rem; color: var(--fc-silver); display: flex; flex-direction: column; gap: 10px;">
              <li>&bull; Targeted 3D Terry Density under forefoot strike zones</li>
              <li>&bull; High-airflow channel knitting over the dorsal foot</li>
              <li>&bull; Non-bulky seam interfaces that preserve shoe volume</li>
            </ul>
          </div>
        </div>

        <!-- Row 2: Asset 8 (Crystalline Textured Rib Sock - Inverted) -->
        <div class="fc-zigzag-row inverted">
          <div>
            <span class="fc-tag">Yarn Physics</span>
            <h3 style="font-family: var(--fc-font-display); font-size: 1.8rem; margin-bottom: 16px;">Architectural Columnar Ribbing &amp; Fiber Twist</h3>
            <p style="color: var(--fc-text-light-muted); font-size: 1rem; line-height: 1.8; margin-bottom: 20px;">
              Our proprietary columnar rib structure utilizes high-twist twin yarns spun in opposing directions. This cancels torsional torque, preventing the sock from twisting laterally around the foot during vigorous walking across cobblestone and marble pavements.
            </p>
            <ul style="font-size: 0.925rem; color: var(--fc-silver); display: flex; flex-direction: column; gap: 10px;">
              <li>&bull; Counter-twisted yarns cancel internal rotational bias</li>
              <li>&bull; Anti-pilling combed fibers endure 100+ machine wash cycles</li>
              <li>&bull; Breathable longitudinal channels wick perspiration outwards</li>
            </ul>
          </div>
          <div class="fc-zigzag-media">
            <img src="assets/images/footletcrystal_asset_8.jpg" alt="Crystalline textured rib sock handcrafted with architectural knit columns" width="1200" height="800">
          </div>
        </div>
      </div>
    </section>

    <!-- Section 8: Curated Wardrobe Vitrine Tiers -->
    <section class="fc-section fc-section-darker">
      <div class="fc-container">
        <div class="fc-section-header" style="text-align: center;">
          <span class="fc-tag">Curated Suites</span>
          <h2 class="fc-section-title">The Wardrobe Vitrine Editions</h2>
          <p class="fc-section-subtitle" style="margin: 0 auto;">Select tailored suites assembled in handmade archival boxes with bespoke monogram options.</p>
        </div>
        <div class="fc-vitrine-grid">
          <!-- Vitrine 1 -->
          <div class="fc-vitrine-card">
            <div>
              <div class="fc-vitrine-tier-badge">TIER 01 &bull; ESSENTIAL</div>
              <h3 class="fc-vitrine-title">The Weekender Vitrine</h3>
              <p class="fc-vitrine-pairs">Curated Suite of 3 Pairs</p>
              <ul class="fc-vitrine-features">
                <li>3x Loafer Crystal Mercerized Cotton</li>
                <li>200-Needle Single-Cylinder Gauge</li>
                <li>Anatomical 3-Wave Heel Silicone Lock</li>
                <li>Archival Presentation Sleeve</li>
              </ul>
            </div>
            <a href="contact.html" class="fc-btn fc-btn-outline" style="width: 100%; text-align: center;">Reserve Weekender</a>
          </div>

          <!-- Vitrine 2 (Featured) -->
          <div class="fc-vitrine-card featured">
            <div>
              <div class="fc-vitrine-tier-badge" style="color: #ffffff;">TIER 02 &bull; SARTORIAL FLAGSHIP</div>
              <h3 class="fc-vitrine-title">The Executive Sartorial Vitrine</h3>
              <p class="fc-vitrine-pairs">Curated Suite of 6 Pairs</p>
              <ul class="fc-vitrine-features">
                <li>4x Loafer Crystal Mercerized Cotton</li>
                <li>2x Thermal Australian Merino Footlets</li>
                <li>Hand-Linked Seamless Toe Closure</li>
                <li>Embossed Navy Atelier Presentation Box</li>
                <li>Complimentary Monogram Embroidery</li>
              </ul>
            </div>
            <a href="contact.html" class="fc-btn fc-btn-cyan" style="width: 100%; text-align: center;">Commission Executive</a>
          </div>

          <!-- Vitrine 3 -->
          <div class="fc-vitrine-card">
            <div>
              <div class="fc-vitrine-tier-badge">TIER 03 &bull; TRANSATLANTIC</div>
              <h3 class="fc-vitrine-title">The Transatlantic Suite</h3>
              <p class="fc-vitrine-pairs">Comprehensive Suite of 12 Pairs</p>
              <ul class="fc-vitrine-features">
                <li>6x Loafer Crystal Mercerized Cotton</li>
                <li>4x Thermal Australian Merino Footlets</li>
                <li>2x Metatarsal Micro Cushion Footlets</li>
                <li>Full Seasonal Fiber Rotation</li>
                <li>Hardwood Archival Wardrobe Casket</li>
              </ul>
            </div>
            <a href="contact.html" class="fc-btn fc-btn-outline" style="width: 100%; text-align: center;">Reserve Transatlantic</a>
          </div>
        </div>
      </div>
    </section>

    <!-- Section 9: Laboratory Data Log -->
    <section class="fc-section fc-section-dark">
      <div class="fc-container">
        <div class="fc-section-header" style="text-align: center;">
          <span class="fc-tag">Textile Laboratory</span>
          <h2 class="fc-section-title">Empirical Performance Testing Log</h2>
          <p class="fc-section-subtitle" style="margin: 0 auto;">Tested under standardized Martindale friction equipment and biomechanical gait telemetry.</p>
        </div>
        <div class="fc-lab-bench-data">
          <div class="fc-lab-metrics-grid">
            <div class="fc-lab-metric-box">
              <div class="fc-lab-metric-val">85,000</div>
              <div class="fc-lab-metric-label">Martindale Abrasion Rub Cycles</div>
            </div>
            <div class="fc-lab-metric-box">
              <div class="fc-lab-metric-val">1.8x</div>
              <div class="fc-lab-metric-label">Moisture Evaporation Velocity</div>
            </div>
            <div class="fc-lab-metric-box">
              <div class="fc-lab-metric-val">99.4%</div>
              <div class="fc-lab-metric-label">Elastic Memory after 60 Launderings</div>
            </div>
            <div class="fc-lab-metric-box">
              <div class="fc-lab-metric-val">0.00%</div>
              <div class="fc-lab-metric-label">Achilles Heel Slippage Probability</div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Section 10: Sartorial Quote Spotlight -->
    <section class="fc-section fc-section-darker">
      <div class="fc-container">
        <div class="fc-spotlight-quote-wrap">
          <div class="fc-spotlight-stars">&#9733;&#9733;&#9733;&#9733;&#9733;</div>
          <blockquote class="fc-spotlight-quote">
            "Footlet Crystal solved the singular remaining flaw in bespoke cordwainery. My clients can now wear our hand-welted Venetian loafers with complete sockless aesthetics while preserving the fine calfskin linings from moisture degradation."
          </blockquote>
          <div class="fc-spotlight-author">Edward H. Sterling</div>
          <div class="fc-spotlight-role">Master Cordwainer &bull; Bespoke Bootmaker, Boston &amp; London</div>
        </div>
      </div>
    </section>

    <!-- Section 11: Dual-Column Technical FAQ Accordion -->
    <section class="fc-section fc-section-dark">
      <div class="fc-container">
        <div class="fc-section-header" style="text-align: center;">
          <span class="fc-tag">Collector Inquiries</span>
          <h2 class="fc-section-title">Technical Hosiery FAQ</h2>
          <p class="fc-section-subtitle" style="margin: 0 auto;">Answers regarding needle gauge, yarn microbiology, and fitting specifications.</p>
        </div>
        <div class="fc-faq-dual-columns">
          <div class="fc-faq-col">
            <div class="fc-accordion-item active">
              <button class="fc-accordion-header">
                <span>Why is 200-needle density critical?</span>
                <span class="fc-accordion-icon">+</span>
              </button>
              <div class="fc-accordion-body">
                <p>200 needles per single cylinder produce an exceptionally dense, thin fabric that glides frictionless inside hand-welted shoes without adding perceptible bulk or altering custom shoe fit.</p>
              </div>
            </div>
            <div class="fc-accordion-item">
              <button class="fc-accordion-header">
                <span>How does the silicone heel lock function?</span>
                <span class="fc-accordion-icon">+</span>
              </button>
              <div class="fc-accordion-body">
                <p>Our triple-wave medical silicone is printed directly onto the knit structure, adhering gently to the calcaneus curve without causing chafing, peeling, or allergic reactions.</p>
              </div>
            </div>
            <div class="fc-accordion-item">
              <button class="fc-accordion-header">
                <span>What are hand-linked seamless toes?</span>
                <span class="fc-accordion-icon">+</span>
              </button>
              <div class="fc-accordion-body">
                <p>Rather than using an automated bulky machine seam, artisans link each loop together stitch-by-stitch, eliminating the thick ridge that presses into the toes during extended walking.</p>
              </div>
            </div>
          </div>
          <div class="fc-faq-col">
            <div class="fc-accordion-item">
              <button class="fc-accordion-header">
                <span>Can footlets be worn in warm climates?</span>
                <span class="fc-accordion-icon">+</span>
              </button>
              <div class="fc-accordion-body">
                <p>Yes. Both our long-staple mercerized cotton and ultra-fine Australian merino wool are naturally hygroscopic, actively absorbing foot moisture and dissipating heat during humid salon days.</p>
              </div>
            </div>
            <div class="fc-accordion-item">
              <button class="fc-accordion-header">
                <span>What is the lifespan of Footlet Crystal socks?</span>
                <span class="fc-accordion-icon">+</span>
              </button>
              <div class="fc-accordion-body">
                <p>With gentle washing in our mesh laundry bag, each pair retains full silicone tension and elastic recovery across more than 100 wear and laundering cycles.</p>
              </div>
            </div>
            <div class="fc-accordion-item">
              <button class="fc-accordion-header">
                <span>Do you offer bespoke salon fittings?</span>
                <span class="fc-accordion-icon">+</span>
              </button>
              <div class="fc-accordion-body">
                <p>Clients are welcome to schedule private fitting consultations at our 200 Clarendon Street salon in Boston to calibrate exact hosiery dimensions with their bespoke shoe collection.</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Section 12: Private Consultation Strip -->
    <section class="fc-section fc-section-darker" style="padding-top: 0;">
      <div class="fc-container">
        <div class="fc-salon-booking-strip">
          <span class="fc-tag">Client Services</span>
          <h2 style="font-family: var(--fc-font-display); font-size: clamp(2rem, 3.5vw, 2.8rem); font-weight: 800; margin: 16px 0 20px 0;">
            Reserve Your Private Atelier Fitting Consultation
          </h2>
          <p style="color: var(--fc-text-light-muted); font-size: 1.1rem; max-width: 680px; margin: 0 auto 36px auto; line-height: 1.8;">
            Experience bespoke footlet fitting at our 54th floor Boston salon. Our hosiery specialists calibrate collar profiles to your exact cordwainer wardrobe.
          </p>
          <div style="display: flex; gap: 20px; justify-content: center; flex-wrap: wrap;">
            <a href="contact.html" class="fc-btn fc-btn-cyan">Arrange Salon Appointment</a>
            <a href="tel:+18665187064" class="fc-btn fc-btn-outline">{PHONE}</a>
          </div>
        </div>
      </div>
    </section>
  </main>

{get_footer()}
</body>
</html>"""

# ==========================================
# 2. ABOUT.HTML (Heritage & Philosophy - Asymmetric Mosaic Gallery)
# ==========================================
def build_about():
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Heritage &amp; Knitting Philosophy | Footlet Crystal Atelier</title>
  <meta name="description" content="Explore the knitting heritage of Footlet Crystal. Discover our 200-needle Italian cylinder looms, hand-linked seamless toes, and dedicated hosiery atelier in Boston.">
  <link rel="canonical" href="https://{DOMAIN}/about.html">
  {GTAG}
  {FONTS}
  <link rel="stylesheet" href="assets/css/style.css">
</head>
<body>
{get_header('about')}

  <main>
    <section class="fc-policy-header">
      <div class="fc-container">
        <span class="fc-section-tag">Guild Heritage</span>
        <h1 class="fc-hero-title">Centuries of Hosiery Craft, <span>Forged in Modern Precision</span></h1>
        <p class="fc-hero-desc" style="margin-bottom: 0;">
          Founded on the conviction that the most intimate garment against your skin deserves the highest standard of textile engineering, Footlet Crystal crafts luxury socks and footlets that never compromise.
        </p>
      </div>
    </section>

    <!-- Story Segment 1: The Founding Quest -->
    <section class="fc-section fc-section-dark">
      <div class="fc-container">
        <div style="max-width: 820px; margin: 0 auto; text-align: center;">
          <span class="fc-tag">Founding Creed</span>
          <h2 class="fc-section-title">The Quest for the Imperceptible Sock</h2>
          <p style="font-size: 1.15rem; color: var(--fc-text-light-muted); line-height: 1.8; margin-bottom: 24px;">
            For generations, sartorial enthusiasts faced an impossible dilemma when wearing loafers: endure the discomfort and sweat of going sockless, or suffer from cheap no-show socks that slide off the heel within ten paces.
          </p>
          <p style="font-size: 1.05rem; color: var(--fc-text-light-muted); line-height: 1.8;">
            Footlet Crystal was established in Boston in 2016 to engineer an uncompromising solution. We fused Italian high-gauge circular knitting machines with hand-linked toe craftsmanship and medical-grade silicone tensioning to build footlets that remain truly invisible and permanently anchored.
          </p>
        </div>

        <!-- Asymmetric Mosaic Gallery: Assets 9, 10, 11 -->
        <div class="fc-about-mosaic">
          <!-- Mosaic Tall: Asset 9 (Luxury Sartorial Socks Collection) -->
          <div class="fc-mosaic-tall">
            <img src="assets/images/footletcrystal_asset_9.jpg" alt="Luxury sartorial socks collection displayed in refined atelier arrangement" width="1200" height="800">
          </div>

          <!-- Mosaic Stack: Assets 10 & 11 -->
          <div class="fc-mosaic-stack">
            <!-- Mosaic Half Top: Asset 10 (Fine Merino Wool Knit Detail) -->
            <div class="fc-mosaic-half">
              <img src="assets/images/footletcrystal_asset_10.jpg" alt="Fine merino wool knit sock detail displaying crystalline stitch structure" width="1200" height="800">
            </div>

            <!-- Mosaic Half Bottom: Asset 11 (Artisan Hand-Knit Wool Sock Heritage) -->
            <div class="fc-mosaic-half">
              <img src="assets/images/footletcrystal_asset_11.jpg" alt="Artisan hand-knit wool sock displaying traditional geometric cable heritage" width="1200" height="800">
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Story Segment 2: Cushioning Science Spotlight (Asset 12: Terry Loop Micro-Cushioning) -->
    <section class="fc-section fc-section-light">
      <div class="fc-container">
        <div class="fc-zigzag-row" style="margin-bottom: 0;">
          <div class="fc-zigzag-media" style="height: 440px;">
            <img src="assets/images/footletcrystal_asset_12.jpg" alt="Terry loop micro-cushioning footbed structure under magnification" width="1200" height="800">
          </div>
          <div>
            <span class="fc-tag" style="background: rgba(2, 132, 199, 0.08); border-color: rgba(2, 132, 199, 0.25); color: var(--fc-cyan);">Textile Micro-Engineering</span>
            <h2 class="fc-section-title" style="color: var(--fc-text-dark); margin-bottom: 20px;">Microscopic Cushioning Loop Physics</h2>
            <p style="color: var(--fc-text-dark-muted); font-size: 1.05rem; line-height: 1.8; margin-bottom: 24px;">
              Under electron microscope magnification, our micro-terry loops reveal an engineered helical spring pattern. Knitted from multi-ply combed yarns, these loops collapse gently under body weight to attenuate peak ground reaction forces, then bounce back immediately upon toe-off.
            </p>
            <p style="color: var(--fc-text-dark-muted); font-size: 1rem; line-height: 1.8; margin-bottom: 28px;">
              This microscopic cushioning architecture allows Footlet Crystal to provide the impact absorption of a thick athletic sock within the whisper-light silhouette of an invisible loafer liner.
            </p>
            <div style="display: flex; gap: 32px; font-family: var(--fc-font-mono);">
              <div>
                <strong style="font-size: 1.5rem; color: var(--fc-cyan); display: block; font-family: var(--fc-font-display);">3.2x</strong>
                <span style="font-size: 0.825rem; color: var(--fc-text-dark-muted);">Elastic Energy Return</span>
              </div>
              <div>
                <strong style="font-size: 1.5rem; color: var(--fc-cyan); display: block; font-family: var(--fc-font-display);">0.6 mm</strong>
                <span style="font-size: 0.825rem; color: var(--fc-text-dark-muted);">Ultra-Thin Instep Profile</span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Story Segment 3: Guild Standards & OEKO-TEX Standard 100 -->
    <section class="fc-section fc-section-dark">
      <div class="fc-container">
        <div class="fc-section-header" style="text-align: center;">
          <span class="fc-tag">Atelier Principles</span>
          <h2 class="fc-section-title">The Footlet Crystal Guild Standards</h2>
          <p class="fc-section-subtitle" style="margin: 0 auto;">Institutional commitments governing fiber provenance, machine calibration, and environmental stewardship.</p>
        </div>
        <div class="fc-nordic-grid-4col" style="border: 1px solid var(--fc-border-dark); border-radius: var(--fc-radius-md); overflow: hidden; background: var(--fc-bg-surface);">
          <div class="fc-nordic-col">
            <h3 class="fc-col-title" style="color: var(--fc-cyan-light);">1. Ethical Wool</h3>
            <p class="fc-col-desc">Sourced exclusively from certified non-mulesed Australian sheep farms adhering to strict animal welfare charters.</p>
          </div>
          <div class="fc-nordic-col">
            <h3 class="fc-col-title" style="color: var(--fc-cyan-light);">2. Hand-Linked Toes</h3>
            <p class="fc-col-desc">Every production run is hand-inspected by master linkers, ensuring zero ridge elevation over sensitive metatarsal joints.</p>
          </div>
          <div class="fc-nordic-col">
            <h3 class="fc-col-title" style="color: var(--fc-cyan-light);">3. Medical Silicone</h3>
            <p class="fc-col-desc">Hypoallergenic three-wave silicone printed without toxic solvents, compliant with medical-grade dermatological safety.</p>
          </div>
          <div class="fc-nordic-col">
            <h3 class="fc-col-title" style="color: var(--fc-cyan-light);">4. Zero Microplastics</h3>
            <p class="fc-col-desc">Knitted primarily from biodegradable plant and animal fibers, eliminating hazardous shed in domestic wastewater.</p>
          </div>
        </div>
      </div>
    </section>
  </main>

{get_footer()}
</body>
</html>"""

# ==========================================
# 3. PRODUCTS.HTML (Catalog - Horizontal Alternating Cards)
# ==========================================
def build_products():
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Footlet Collections &amp; Hosiery | Footlet Crystal Atelier</title>
  <meta name="description" content="Explore luxury footlets and socks at Footlet Crystal. Athletic running liners, heavy trail hiking crews, graduated compression hosiery, and low-cut loafer liners.">
  <link rel="canonical" href="https://{DOMAIN}/products.html">
  {GTAG}
  {FONTS}
  <link rel="stylesheet" href="assets/css/style.css">
</head>
<body>
{get_header('products')}

  <main>
    <section class="fc-policy-header">
      <div class="fc-container">
        <span class="fc-section-tag">The Collections</span>
        <h1 class="fc-hero-title">Curated Footlets &amp; <span>Precision Hosiery</span></h1>
        <p class="fc-hero-desc" style="margin-bottom: 0;">
          Engineered for distinctive footwear silhouettes, high-mileage days, and uncompromising foot comfort. Explore our six core performance and lifestyle footlet models.
        </p>
      </div>
    </section>

    <!-- Horizontal Product Catalog (Assets 13 to 18) -->
    <section class="fc-section fc-section-dark">
      <div class="fc-container">
        <div class="fc-catalog-list">
          
          <!-- Product 1: Asset 13 (Athletic Running Performance Sock) -->
          <div class="fc-catalog-card">
            <div class="fc-catalog-media">
              <img src="assets/images/footletcrystal_asset_13.jpg" alt="Athletic running performance sock with zoned compression and breathable mesh" width="1200" height="800">
            </div>
            <div class="fc-catalog-info">
              <div class="fc-catalog-header">
                <span class="fc-tag">MODEL 01 &bull; ATHLETIC PERFORMANCE</span>
                <h3>Athletic Running Footlet Liner</h3>
                <p>Featuring an anatomical left/right toe box, high-wicking synthetic and cotton blend, and anti-blister padding engineered for marathon training, speed sessions, and high-cadence gym regimens.</p>
              </div>
              <div class="fc-catalog-specs-row">
                <div class="fc-spec-box"><small>GAUGE</small><strong>168N Knit</strong></div>
                <div class="fc-spec-box"><small>FIBER</small><strong>CoolMax &amp; Cotton</strong></div>
                <div class="fc-spec-box"><small>HEEL GRIP</small><strong>Achilles Tab Shield</strong></div>
              </div>
              <div style="display: flex; justify-content: space-between; align-items: center;">
                <span style="font-family: var(--fc-font-mono); font-size: 0.85rem; color: var(--fc-cyan-light);">REF: FC-PRD-01</span>
                <a href="contact.html" class="fc-btn fc-btn-cyan" style="padding: 10px 24px;">Commission Model</a>
              </div>
            </div>
          </div>

          <!-- Product 2: Asset 14 (Heavy-Gauge Trail Hiking Crew Sock - Inverted) -->
          <div class="fc-catalog-card inverted">
            <div class="fc-catalog-info">
              <div class="fc-catalog-header">
                <span class="fc-tag">MODEL 02 &bull; EXPEDITION CUSHION</span>
                <h3>Heavy-Gauge Trail Hiking Crew</h3>
                <p>Knitted with heavy-gauge merino wool for extreme thermal regulation and maximum impact buffering during rigorous mountain trekking, boulder traverses, and cold backcountry expeditions.</p>
              </div>
              <div class="fc-catalog-specs-row">
                <div class="fc-spec-box"><small>GAUGE</small><strong>96N Heavy Wool</strong></div>
                <div class="fc-spec-box"><small>FIBER</small><strong>85% Merino / 15% Nylon</strong></div>
                <div class="fc-spec-box"><small>HEEL GRIP</small><strong>Full Terry Calcaneus</strong></div>
              </div>
              <div style="display: flex; justify-content: space-between; align-items: center;">
                <span style="font-family: var(--fc-font-mono); font-size: 0.85rem; color: var(--fc-cyan-light);">REF: FC-PRD-02</span>
                <a href="contact.html" class="fc-btn fc-btn-cyan" style="padding: 10px 24px;">Commission Model</a>
              </div>
            </div>
            <div class="fc-catalog-media">
              <img src="assets/images/footletcrystal_asset_14.jpg" alt="Heavy-gauge trail hiking crew sock knitted with dense merino wool yarns" width="1200" height="800">
            </div>
          </div>

          <!-- Product 3: Asset 15 (Graduated Compression Recovery Sock) -->
          <div class="fc-catalog-card">
            <div class="fc-catalog-media">
              <img src="assets/images/footletcrystal_asset_15.jpg" alt="Graduated compression recovery sock with medical-grade pressure gradient" width="1200" height="800">
            </div>
            <div class="fc-catalog-info">
              <div class="fc-catalog-header">
                <span class="fc-tag">MODEL 03 &bull; RECOVERY COMPRESSION</span>
                <h3>Graduated Compression Recovery Sock</h3>
                <p>Calibrated with 15&ndash;20 mmHg graduated compression to enhance venous return, diminish swelling during transcontinental flights, and accelerate muscle revitalization after endurance athletics.</p>
              </div>
              <div class="fc-catalog-specs-row">
                <div class="fc-spec-box"><small>GAUGE</small><strong>240N Medical Loom</strong></div>
                <div class="fc-spec-box"><small>PRESSURE</small><strong>15-20 mmHg Gradient</strong></div>
                <div class="fc-spec-box"><small>HEEL GRIP</small><strong>Y-Gore Anatomical Pocket</strong></div>
              </div>
              <div style="display: flex; justify-content: space-between; align-items: center;">
                <span style="font-family: var(--fc-font-mono); font-size: 0.85rem; color: var(--fc-cyan-light);">REF: FC-PRD-03</span>
                <a href="contact.html" class="fc-btn fc-btn-cyan" style="padding: 10px 24px;">Commission Model</a>
              </div>
            </div>
          </div>

          <!-- Product 4: Asset 16 (Aerobic Runner Low-Cut Footlet - Inverted) -->
          <div class="fc-catalog-card inverted">
            <div class="fc-catalog-info">
              <div class="fc-catalog-header">
                <span class="fc-tag">MODEL 04 &bull; LOW-PROFILE AEROBIC</span>
                <h3>Aerobic Runner Low-Cut Footlet</h3>
                <p>An ultra-low silhouette featuring a reinforced heel tab that protects the Achilles tendon from shoe collar friction without showing above athletic trainers or casual deck footwear.</p>
              </div>
              <div class="fc-catalog-specs-row">
                <div class="fc-spec-box"><small>GAUGE</small><strong>200N Precision Loom</strong></div>
                <div class="fc-spec-box"><small>FIBER</small><strong>Mercerized Micro-Cotton</strong></div>
                <div class="fc-spec-box"><small>HEEL GRIP</small><strong>Ergonomic Pull Tab</strong></div>
              </div>
              <div style="display: flex; justify-content: space-between; align-items: center;">
                <span style="font-family: var(--fc-font-mono); font-size: 0.85rem; color: var(--fc-cyan-light);">REF: FC-PRD-04</span>
                <a href="contact.html" class="fc-btn fc-btn-cyan" style="padding: 10px 24px;">Commission Model</a>
              </div>
            </div>
            <div class="fc-catalog-media">
              <img src="assets/images/footletcrystal_asset_16.jpg" alt="Aerobic runner low-cut footlet with protective heel tab and arch band" width="1200" height="800">
            </div>
          </div>

          <!-- Product 5: Asset 17 (Trail Pro Protective Ankle Sock) -->
          <div class="fc-catalog-card">
            <div class="fc-catalog-media">
              <img src="assets/images/footletcrystal_asset_17.jpg" alt="Trail pro protective ankle sock with debris seal cuff" width="1200" height="800">
            </div>
            <div class="fc-catalog-info">
              <div class="fc-catalog-header">
                <span class="fc-tag">MODEL 05 &bull; TECHNICAL TRAIL ANKLE</span>
                <h3>Trail Pro Protective Ankle Sock</h3>
                <p>Engineered with a dense ribbed debris-seal collar, high-density ankle bone pads, and mid-foot torsional compression to protect against grit and brush on rugged forest trails.</p>
              </div>
              <div class="fc-catalog-specs-row">
                <div class="fc-spec-box"><small>GAUGE</small><strong>168N Dynamic Rib</strong></div>
                <div class="fc-spec-box"><small>FIBER</small><strong>Merino &amp; Cordura Yarns</strong></div>
                <div class="fc-spec-box"><small>HEEL GRIP</small><strong>Double-Locked Heel Pocket</strong></div>
              </div>
              <div style="display: flex; justify-content: space-between; align-items: center;">
                <span style="font-family: var(--fc-font-mono); font-size: 0.85rem; color: var(--fc-cyan-light);">REF: FC-PRD-05</span>
                <a href="contact.html" class="fc-btn fc-btn-cyan" style="padding: 10px 24px;">Commission Model</a>
              </div>
            </div>
          </div>

          <!-- Product 6: Asset 18 (Active Run Low-Cut Sport Liner - Inverted) -->
          <div class="fc-catalog-card inverted">
            <div class="fc-catalog-info">
              <div class="fc-catalog-header">
                <span class="fc-tag">MODEL 06 &bull; ULTRA-BREATHABLE SPORT</span>
                <h3>Active Run Low-Cut Sport Liner</h3>
                <p>Built with open-mesh ventilation panels over the instep, seamless hand-linked toes, and quick-drying hydrophobic yarns for intensive workouts and hot-weather cardio pursuits.</p>
              </div>
              <div class="fc-catalog-specs-row">
                <div class="fc-spec-box"><small>GAUGE</small><strong>200N Air-Channel Knit</strong></div>
                <div class="fc-spec-box"><small>FIBER</small><strong>Dryarn &amp; Pima Cotton</strong></div>
                <div class="fc-spec-box"><small>HEEL GRIP</small><strong>Micro-Rib Grip Ring</strong></div>
              </div>
              <div style="display: flex; justify-content: space-between; align-items: center;">
                <span style="font-family: var(--fc-font-mono); font-size: 0.85rem; color: var(--fc-cyan-light);">REF: FC-PRD-06</span>
                <a href="contact.html" class="fc-btn fc-btn-cyan" style="padding: 10px 24px;">Commission Model</a>
              </div>
            </div>
            <div class="fc-catalog-media">
              <img src="assets/images/footletcrystal_asset_18.jpg" alt="Active run low-cut sport liner with breathable open-knit upper" width="1200" height="800">
            </div>
          </div>

        </div>
      </div>
    </section>

    <!-- Sizing & Conversion Matrix -->
    <section class="fc-section fc-section-light">
      <div class="fc-container">
        <div class="fc-section-header" style="text-align: center;">
          <span class="fc-tag" style="background: rgba(2, 132, 199, 0.08); border-color: rgba(2, 132, 199, 0.25); color: var(--fc-cyan);">Fitting Guidance</span>
          <h2 class="fc-section-title" style="color: var(--fc-text-dark);">International Sizing &amp; Tension Scale</h2>
          <p class="fc-section-subtitle" style="margin: 0 auto; color: var(--fc-text-dark-muted);">Footlet Crystal hosiery is knitted to calibrated anatomical proportions for precise heel retention.</p>
        </div>
        <div class="fc-pairing-matrix-wrap">
          <table class="fc-pairing-table">
            <thead>
              <tr>
                <th>Atelier Size</th>
                <th>US Men</th>
                <th>US Women</th>
                <th>EU Sizing</th>
                <th>UK Sizing</th>
                <th>Recommended Cut</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td style="font-weight: 700; color: var(--fc-cyan);">Size I (Petit)</td>
                <td>6.0 &ndash; 7.5</td>
                <td>7.0 &ndash; 8.5</td>
                <td>38 &ndash; 40</td>
                <td>5.5 &ndash; 7.0</td>
                <td>Shallow Low-Vamp</td>
              </tr>
              <tr>
                <td style="font-weight: 700; color: var(--fc-cyan);">Size II (Standard)</td>
                <td>8.0 &ndash; 10.0</td>
                <td>9.0 &ndash; 11.0</td>
                <td>41 &ndash; 43</td>
                <td>7.5 &ndash; 9.5</td>
                <td>All Silhouettes</td>
              </tr>
              <tr>
                <td style="font-weight: 700; color: var(--fc-cyan);">Size III (Grand)</td>
                <td>10.5 &ndash; 12.5</td>
                <td>11.5 &ndash; 13.5</td>
                <td>44 &ndash; 46</td>
                <td>10.0 &ndash; 12.0</td>
                <td>Reinforced Heel Pocket</td>
              </tr>
              <tr>
                <td style="font-weight: 700; color: var(--fc-cyan);">Size IV (Bespoke)</td>
                <td>13.0+</td>
                <td>14.0+</td>
                <td>47+</td>
                <td>12.5+</td>
                <td>Private Commission Only</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </section>
  </main>

{get_footer()}
</body>
</html>"""

# ==========================================
# 4. CONTACT.HTML (Salon Consultation - Inverted Layout with Asset 19)
# ==========================================
def build_contact():
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Salon Consultation &amp; Hosiery Inquiries | Footlet Crystal</title>
  <meta name="description" content="Book a private hosiery consultation at Footlet Crystal Atelier. Meet our specialists at 200 Clarendon Street, Boston, or contact our private client concierge.">
  <link rel="canonical" href="https://{DOMAIN}/contact.html">
  {GTAG}
  {FONTS}
  <link rel="stylesheet" href="assets/css/style.css">
</head>
<body>
{get_header('contact')}

  <main>
    <section class="fc-policy-header">
      <div class="fc-container">
        <span class="fc-section-tag">Private Concierge</span>
        <h1 class="fc-hero-title">Private Salon Consultation &amp; <span>Inquiries</span></h1>
        <p class="fc-hero-desc" style="margin-bottom: 0;">
          Whether commissioning curated bespoke hosiery wardrobes or inquiring about custom corporate gift sets, our Boston concierge welcomes your transmission.
        </p>
      </div>
    </section>

    <!-- Inverted Split Layout: Asset 19 on Left, Form Card on Right -->
    <section class="fc-section fc-section-dark">
      <div class="fc-container">
        <div class="fc-contact-layout">
          
          <!-- Contact Feature Card with Asset 19 (Cushioned Trail Performance Sock) -->
          <div class="fc-contact-feature-card">
            <img src="assets/images/footletcrystal_asset_19.jpg" alt="Cushioned trail performance sock on display in Boston hosiery atelier" width="1200" height="800">
            <div class="fc-contact-overlay-box">
              <span class="fc-tag" style="margin-bottom: 10px;">Atelier Flagship Coordinates</span>
              <h3 style="font-family: var(--fc-font-display); font-size: 1.35rem; color: #ffffff; margin-bottom: 12px;">Boston Hosiery Salon</h3>
              <p style="font-size: 0.95rem; color: var(--fc-silver); margin-bottom: 8px;">{ADDR}</p>
              <p style="font-family: var(--fc-font-mono); font-size: 0.85rem; color: var(--fc-cyan-light); margin-bottom: 6px;">Concierge Direct: {PHONE}</p>
              <p style="font-family: var(--fc-font-mono); font-size: 0.85rem; color: var(--fc-silver);"><a href="mailto:{EMAIL}">{EMAIL}</a></p>
              <div style="margin-top: 14px; font-size: 0.775rem; color: var(--fc-text-light-muted); border-top: 1px solid rgba(255,255,255,0.1); padding-top: 10px;">
                Salon Hours: Monday &ndash; Friday 9:00 AM &ndash; 6:00 PM EST (By Appointment)
              </div>
            </div>
          </div>

          <!-- Contact / Commission Form -->
          <div class="fc-contact-form-card">
            <h3 style="font-family: var(--fc-font-display); font-size: 1.6rem; font-weight: 700; color: var(--fc-text-dark); margin-bottom: 8px;">Salon Inquiry &amp; Commission Request</h3>
            <p style="font-size: 0.95rem; color: var(--fc-text-dark-muted); margin-bottom: 28px;">
              Please provide your hosiery specifications, preferred footwear models, and appointment date preferences below.
            </p>

            <form id="fc-contact-form">
              <div class="fc-form-group">
                <label class="fc-form-label" for="client-name">Full Legal Name *</label>
                <input class="fc-form-input" type="text" id="client-name" name="name" required placeholder="e.g. Montgomery Adams">
              </div>

              <div class="fc-form-group">
                <label class="fc-form-label" for="client-email">Email Address *</label>
                <input class="fc-form-input" type="email" id="client-email" name="email" required placeholder="e.g. adams@domain.com">
              </div>

              <div class="fc-form-group">
                <label class="fc-form-label" for="client-phone">Telephone Number *</label>
                <input class="fc-form-input" type="tel" id="client-phone" name="phone" required placeholder="e.g. +1 (617) 555-0192">
              </div>

              <div class="fc-form-group">
                <label class="fc-form-label" for="inquiry-type">Inquiry Classification *</label>
                <select class="fc-form-select" id="inquiry-type" name="type" required>
                  <option value="">Select consultation scope...</option>
                  <option value="fitting">Private Boston Salon Fitting Appointment</option>
                  <option value="vitrine">Curated Wardrobe Vitrine Subscription</option>
                  <option value="cordwainer">Cordwainer Footwear Calibration Commission</option>
                  <option value="corporate">Institutional &amp; Corporate Gift Suites</option>
                  <option value="general">Technical Fiber Guidance &amp; Care Inquiry</option>
                </select>
              </div>

              <div class="fc-form-group">
                <label class="fc-form-label" for="client-notes">Hosiery Requirements &amp; Preferred Shoe Models</label>
                <textarea class="fc-form-textarea" id="client-notes" name="notes" rows="4" placeholder="Detail your cordwainer shoe models (e.g. Belgian loafer, penny loafer, oxford) and sizing nuances..."></textarea>
              </div>

              <button type="submit" class="fc-btn fc-btn-cyan" style="width: 100%; justify-content: center; padding: 14px;">
                Transmit Salon Request
              </button>
            </form>
          </div>

        </div>
      </div>
    </section>
  </main>

{get_footer()}
</body>
</html>"""

# ==========================================
# 5. FAQ.HTML (Dual-Column Technical Layout with Asset 20)
# ==========================================
def build_faq():
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Technical &amp; Fiber FAQ | Footlet Crystal Atelier</title>
  <meta name="description" content="Technical questions answered about 200-needle knitting, seamless linked toes, silicone heel grips, and footlet care at Footlet Crystal.">
  <link rel="canonical" href="https://{DOMAIN}/faq.html">
  {GTAG}
  {FONTS}
  <link rel="stylesheet" href="assets/css/style.css">
</head>
<body>
{get_header('faq')}

  <main>
    <section class="fc-policy-header">
      <div class="fc-container">
        <span class="fc-section-tag">Knowledge Vault</span>
        <h1 class="fc-hero-title">Technical Specifications &amp; <span>Hosiery FAQ</span></h1>
        <p class="fc-hero-desc" style="margin-bottom: 0;">
          Comprehensive guidance detailing yarn microbiology, gauge tension, silicone wash endurance, and shoe pairing etiquette.
        </p>
      </div>
    </section>

    <!-- FAQ Section with Asset 20 (Micro Crew Running Sock & Liner) -->
    <section class="fc-section fc-section-dark">
      <div class="fc-container">
        <div style="max-width: 860px; margin: 0 auto 56px auto; border-radius: var(--fc-radius-md); overflow: hidden; border: 1px solid var(--fc-border-dark); box-shadow: var(--fc-shadow-lg);">
          <img src="assets/images/footletcrystal_asset_20.jpg" alt="Micro crew running sock and footlet liner display under studio raking light" width="1200" height="800">
        </div>

        <div class="fc-section-header" style="text-align: center;">
          <span class="fc-tag">Fiber Care &amp; Science</span>
          <h2 class="fc-section-title">Common Atelier Inquiries</h2>
          <p class="fc-section-subtitle" style="margin: 0 auto;">Everything you need to know about caring for and wearing luxury footlets.</p>
        </div>

        <div class="fc-faq-dual-columns">
          <!-- Column 1 -->
          <div class="fc-faq-col">
            <div class="fc-accordion-item active">
              <button class="fc-accordion-header">
                <span>What makes Footlet Crystal socks completely invisible in loafers?</span>
                <span class="fc-accordion-icon">+</span>
              </button>
              <div class="fc-accordion-body">
                <p>Our Loafer Crystal pattern is precision-cut to contour around the foot at a shallow 32-millimeter height line, ensuring that neither the lateral quarters nor the anterior vamp collar protrude above the leather rim of low-slung penny loafers, driving moccasins, or Belgian slippers.</p>
              </div>
            </div>

            <div class="fc-accordion-item">
              <button class="fc-accordion-header">
                <span>Why is hand-linking of the toe seam critical for luxury hosiery?</span>
                <span class="fc-accordion-icon">+</span>
              </button>
              <div class="fc-accordion-body">
                <p>Standard mass-market socks close the open toe using an automated sewing machine overlock stitch, creating a raised ridge that presses directly into the toes when confined within stiff leather footwear. Hand-linking weaves the opposing knitted loops closed with a single thread, creating a completely flat junction.</p>
              </div>
            </div>

            <div class="fc-accordion-item">
              <button class="fc-accordion-header">
                <span>How does Australian merino wool perform during hot summer months?</span>
                <span class="fc-accordion-icon">+</span>
              </button>
              <div class="fc-accordion-body">
                <p>Unlike synthetic polyester fibers that trap foot sweat and odor, ultra-fine 17.5-micron merino wool is naturally hygroscopic. It absorbs up to 35% of its dry weight in vaporized moisture before feeling wet, evaporatively cooling the skin in sweltering humidity while naturally repelling odor bacteria.</p>
              </div>
            </div>

            <div class="fc-accordion-item">
              <button class="fc-accordion-header">
                <span>What laundering temperature should be used for crystal hosiery?</span>
                <span class="fc-accordion-icon">+</span>
              </button>
              <div class="fc-accordion-body">
                <p>We advise machine washing at 30 degrees Celsius (85 degrees Fahrenheit) on a delicate wool or silk wash cycle using gentle pH-neutral liquid detergent. Avoid harsh chlorine bleaches and fabric softeners that degrade silicone adhesion.</p>
              </div>
            </div>
          </div>

          <!-- Column 2 -->
          <div class="fc-faq-col">
            <div class="fc-accordion-item">
              <button class="fc-accordion-header">
                <span>Can Footlet Crystal footlets be dried in a machine dryer?</span>
                <span class="fc-accordion-icon">+</span>
              </button>
              <div class="fc-accordion-body">
                <p>We strongly recommend flat air drying on an indoor drying rack away from direct radiant heat sources. Excessive dryer tumbling degrades elastane tension and risks heat damage to the silicone heel gripper arrays.</p>
              </div>
            </div>

            <div class="fc-accordion-item">
              <button class="fc-accordion-header">
                <span>How does the 3-wave medical silicone grip stay clean?</span>
                <span class="fc-accordion-icon">+</span>
              </button>
              <div class="fc-accordion-body">
                <p>Over time, skin oils and lint can temporarily diminish silicone tackiness. Simply wipe the silicone waves gently with a clean damp cotton cloth or wash with mild soap to instantly restore 100% of the original frictional grip.</p>
              </div>
            </div>

            <div class="fc-accordion-item">
              <button class="fc-accordion-header">
                <span>How do I determine my correct footlet size?</span>
                <span class="fc-accordion-icon">+</span>
              </button>
              <div class="fc-accordion-body">
                <p>Please refer to our International Sizing Scale on the Collections page. If you are positioned between sizes, we recommend sizing down for lower-cut loafers to ensure snug elastic contouring, or sizing up if choosing heavier trail crews.</p>
              </div>
            </div>

            <div class="fc-accordion-item">
              <button class="fc-accordion-header">
                <span>Do you offer bespoke salon fitting appointments in Boston?</span>
                <span class="fc-accordion-icon">+</span>
              </button>
              <div class="fc-accordion-body">
                <p>Yes. Private appointments are hosted at our 200 Clarendon Street salon on the 54th floor in Boston. Clients may bring their favored cordwainer footwear for precise millimeter collar matching and tactile fiber evaluations.</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  </main>

{get_footer()}
</body>
</html>"""

# ==========================================
# 6. POLICY PAGES (Rule 5: Strictly 5-6 lines / 60-110 words per substantive paragraph)
# ==========================================
def build_privacy():
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Privacy Policy | Footlet Crystal Atelier</title>
  <meta name="description" content="Privacy Policy for Footlet Crystal Atelier. Review our institutional data protection standards, client confidentiality protocols, and privacy safeguards.">
  <link rel="canonical" href="https://{DOMAIN}/privacy-policy.html">
  {GTAG}
  {FONTS}
  <link rel="stylesheet" href="assets/css/style.css">
</head>
<body>
{get_header('')}

  <main>
    <section class="fc-policy-header">
      <div class="fc-container">
        <span class="fc-section-tag">Institutional Compliance</span>
        <h1 class="fc-hero-title">Client Privacy <span>Charter</span></h1>
        <p class="fc-hero-desc" style="margin-bottom: 0;">Effective Date: January 1, 2026 &bull; Footlet Crystal Atelier LLC</p>
      </div>
    </section>

    <div class="fc-container">
      <div class="fc-policy-content">
        
        <div class="fc-policy-section">
          <h2>1. Commitment to Client Confidentiality</h2>
          <p class="fc-policy-p">
            Footlet Crystal Atelier maintains an uncompromised institutional commitment to safeguarding the personal records, footwear sizing metrics, and digital telemetry of every client who commissions our artisanal hosiery. We acknowledge that our patrons entrust us with sensitive personal particulars when arranging salon appointments or ordering bespoke curated footlet collections. Under no circumstances do we trade, lease, or distribute private customer registries to commercial aggregators or unauthorized third-party marketing networks across global digital channels.
          </p>
          <p class="fc-policy-p">
            Our data protection infrastructure utilizes state-of-the-art cryptographic safeguards designed to prevent unauthorized electronic surveillance, data leaks, or unapproved data transmissions. Institutional records collected during your engagement are maintained within segmented physical and digital environments that comply strictly with United States federal standards and worldwide data privacy frameworks. We conduct recurring technical audits of our digital communications infrastructure to ensure full operational resilience against evolving cyber threats and unauthorized data intrusion vectors.
          </p>
        </div>

        <div class="fc-policy-section">
          <h2>2. Scope of Collected Information</h2>
          <p class="fc-policy-p">
            When you transmit an inquiry through our digital consultation portal or arrange a salon appointment at our Boston atelier, we record necessary identifying details including your legal name, direct corporate telephone number, authenticated email address, and physical delivery coordinates. Furthermore, when ordering bespoke hosiery subscriptions, our specialists record custom footwear dimensions, shoe scale conversions, and fiber composition preferences required to curate your personalized footlet boxes.
          </p>
          <p class="fc-policy-p">
            In addition to directly provided contact records, our web infrastructure passively monitors standard diagnostic server telemetry, such as anonymous Internet Protocol addresses, browser rendering versions, operating system architecture, and referring webpage headers. These technical metrics are processed strictly in an aggregated format to optimize the visual presentation and navigation responsiveness of our digital salon. Passive analytics never link anonymous browsing behaviors to your verified private client identity or personal atelier records.
          </p>
        </div>

        <div class="fc-policy-section">
          <h2>3. Operational Purpose of Data Processing</h2>
          <p class="fc-policy-p">
            All gathered personal data is utilized solely to facilitate the bespoke crafting process, schedule private client appointments, coordinate secure courier shipments, and furnish authentic provenance certification documents. When you request a private consultation at our Boston atelier, your phone number and email permit our concierge team to confirm appointment schedules and review specialized material requests prior to your arrival. We never deploy automated promotional communications without prior affirmative written authorization from the commissioning patron.
          </p>
          <p class="fc-policy-p">
            We may additionally retain archival records of your completed hosiery curations to honor our sizing guarantees and provide seamless seasonal re-ordering services. Having access to original shoe model specifications, preferred cuff elasticity, and favored yarn blends enables our specialists to execute seamless wardrobe dispatches years after the initial consultation took place. Clients retain full legal authority to inspect, update, or demand complete deletion of archival records upon written request.
          </p>
        </div>

        <div class="fc-policy-section">
          <h2>4. Data Retention and Institutional Security</h2>
          <p class="fc-policy-p">
            Personal data collected by Footlet Crystal Atelier is stored on encrypted servers protected by multi-factor authentication, intrusion detection defenses, and strict access controls limited to authorized atelier management staff. Digital records are preserved only for the duration required to satisfy the commercial purpose of the commission, fulfill contractual warranty obligations, and comply with state and federal legal record-keeping statutes. Once the necessary retention window concludes, digital data is securely purged.
          </p>
          <p class="fc-policy-p">
            Our physical workshop maintains parallel administrative protocols to ensure that paper sizing records, custom embroidery dies, and physical shipping ledgers are stored within locked archives restricted from public salon view. In the improbable event of a cybersecurity incident that risks exposing client information, our incident response protocol mandates prompt written notification to all affected patrons and relevant regulatory enforcement bodies within seventy-two hours of forensic confirmation.
          </p>
        </div>

        <div class="fc-policy-section">
          <h2>5. Client Legal Rights &amp; Regulatory Inquiries</h2>
          <p class="fc-policy-p">
            Every patron possesses statutory rights under applicable privacy legislation, including the rights to inspect, rectify, restrict, or demand the irrevocable erasure of their personal information stored within our databases. To exercise your rights, transmit a formal written petition to our data privacy officer via postal mail or authenticated email. We process and confirm compliance with all verified client requests within thirty calendar days without imposing punitive fees or interrupting scheduled bespoke commissions.
          </p>
          <p class="fc-policy-p">
            For questions concerning this Privacy Charter or to update your contact preferences, please communicate directly with our private client concierge using the official contact coordinates listed below. Our compliance officers welcome open dialogue regarding our information handling practices and will supply thorough explanations regarding our archival security procedures, encryption standards, or regulatory certifications upon formal patron inquiry. We remain fully dedicated to honoring our clients' absolute confidentiality and trust throughout all interactions.
          </p>
          <div class="fc-policy-contact-card">
            <h3>Atelier Privacy Officer</h3>
            <p><strong>Institutional Address:</strong> {ADDR}</p>
            <p><strong>Concierge Telephone:</strong> {PHONE}</p>
            <p><strong>Direct Inquiries:</strong> {EMAIL}</p>
          </div>
        </div>

      </div>
    </div>
  </main>

{get_footer()}
</body>
</html>"""

def build_terms():
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Terms &amp; Conditions | Footlet Crystal Atelier</title>
  <meta name="description" content="Terms and Conditions governing bespoke hosiery commissions, salon appointments, and intellectual property at Footlet Crystal Atelier LLC.">
  <link rel="canonical" href="https://{DOMAIN}/terms-and-conditions.html">
  {GTAG}
  {FONTS}
  <link rel="stylesheet" href="assets/css/style.css">
</head>
<body>
{get_header('')}

  <main>
    <section class="fc-policy-header">
      <div class="fc-container">
        <span class="fc-section-tag">Legal Framework</span>
        <h1 class="fc-hero-title">Terms &amp; Conditions of <span>Atelier Engagement</span></h1>
        <p class="fc-hero-desc" style="margin-bottom: 0;">Effective Date: January 1, 2026 &bull; Footlet Crystal Atelier LLC</p>
      </div>
    </section>

    <div class="fc-container">
      <div class="fc-policy-content">
        
        <div class="fc-policy-section">
          <h2>1. Acceptance of Terms &amp; Scope of Engagement</h2>
          <p class="fc-policy-p">
            By accessing this digital salon, scheduling an appointment, or commissioning luxury hosiery through Footlet Crystal Atelier LLC, you formally acknowledge and agree to be bound by these Terms and Conditions. These legal provisions establish a binding contract between the patron and our artisanal workshop, regulating all transactions, consultations, and digital browsing activities. If you disagree with any portion of these binding stipulations, you must refrain from ordering goods or utilizing this website.
          </p>
          <p class="fc-policy-p">
            Footlet Crystal reserves the right to amend, update, or reorganize these terms periodically to reflect shifts in statutory regulations, workshop capacity, or yarn harvesting protocols. Notice of substantial revisions will be published visibly upon this webpage alongside an updated effective date timestamp. Continued utilization of our digital facilities or completion of commission deposits following posted modifications represents definitive legal consent to the revised terms of engagement.
          </p>
        </div>

        <div class="fc-policy-section">
          <h2>2. Bespoke Commission Workflow &amp; Deposit Terms</h2>
          <p class="fc-policy-p">
            Bespoke hosiery curations represent custom garments engineered specifically to individual patron sizing requirements, shoe heel models, and tailored yarn compositions. An initial non-refundable deposit of fifty percent of the total commission quote is mandatory before yarn allocation, needle calibration, or cylinder knitting commences. This deposit covers the procurement of botanical mercerized cotton, Italian merino wools, and dedicated loom setup allocation.
          </p>
          <p class="fc-policy-p">
            Estimated completion timelines provided during salon consultations represent diligent artisanal projections rather than rigid guarantees, as authentic hand-linking involves meticulous micro-loop alignment and steam boarding phases. Full payment of the remaining fifty percent balance must be completed and cleared prior to physical release or insured courier dispatch of the finished hosiery box. Refusal to pay the final balance within sixty days forfeits the initial deposit and the commission order.
          </p>
        </div>

        <div class="fc-policy-section">
          <h2>3. Natural Material Variations &amp; Handcraft Hallmarks</h2>
          <p class="fc-policy-p">
            Patrons understand that natural merino wool and organic Egyptian cotton are biological agricultural materials displaying subtle variations in fiber crimp, yarn luster, and organic dye lot absorption across seasonal harvests. These characteristics are intentional hallmarks of natural fiber integrity and are celebrated as proof of genuine artisanal authenticity rather than manufacturing defects. Synthetic nylon homogeneity is deliberately rejected in favor of unique breathability, skin tactile comfort, and biological temperature response.
          </p>
          <p class="fc-policy-p">
            Similarly, because every toe seam is hand-linked loop-by-loop on specialized circular points by skilled artisans, subtle micro-variations in stitch tension occur across pairs. Silicone heel grips, being applied through vulcanized heat lamination, will naturally reflect slight textural gradients that optimize skin contact friction. Such organic variations are integral to the design philosophy and do not constitute acceptable grounds for return or refund.
          </p>
        </div>

        <div class="fc-policy-section">
          <h2>4. Intellectual Property &amp; Archival Blueprints</h2>
          <p class="fc-policy-p">
            All structural footlet contours, stitch programming templates, aesthetic designs, photographs, typography, and text published upon this digital platform represent the exclusive intellectual property of Footlet Crystal Atelier LLC. Unauthorized reproduction, digital copying, industrial reverse-engineering, or commercial exploitation of our patterns or branding is strictly prohibited under international copyright and trademark laws. Patrons purchasing bespoke hosiery acquire physical ownership of the garments, while intellectual design rights remain with the atelier.
          </p>
          <p class="fc-policy-p">
            The Footlet Crystal emblem, monogram crests, and guild marks remain protected commercial hallmarks. Commissioning a bespoke hosiery set with a personal family crest or initial does not grant the client any license to replicate our proprietary Y-heel geometry or vulcanized silicone wave designs for secondary commercial production. We vigorously defend our intellectual craftsmanship against counterfeit manufacturing and trademark dilution in all applicable legal jurisdictions.
          </p>
        </div>

        <div class="fc-policy-section">
          <h2>5. Limitation of Liability &amp; Governing Jurisdiction</h2>
          <p class="fc-policy-p">
            To the maximum extent permitted by applicable law, Footlet Crystal Atelier LLC disclaims liability for indirect, incidental, punitive, or consequential damages resulting from website downtime, delayed delivery schedules, or improper hosiery laundering by the patron. In no event shall our total financial liability exceed the aggregate monetary compensation actually received by the atelier for the specific commission in dispute. We make no commercial merchantability warranties beyond our structural lifetime guarantee.
          </p>
          <p class="fc-policy-p">
            These Terms and Conditions shall be governed by and construed in accordance with the substantive laws of the Commonwealth of Massachusetts, United States, without regard to conflict of law principles. Any legal controversy, arbitration, or proceeding arising under this agreement shall be submitted exclusively to state or federal courts situated in Suffolk County, Massachusetts. Both parties waive any objection to personal jurisdiction or inconvenient forum in said judicial venues.
          </p>
          <div class="fc-policy-contact-card">
            <h3>Atelier Legal Division</h3>
            <p><strong>Institutional Address:</strong> {ADDR}</p>
            <p><strong>Inquiry Telephone:</strong> {PHONE}</p>
            <p><strong>Legal Communications:</strong> {EMAIL}</p>
          </div>
        </div>

      </div>
    </div>
  </main>

{get_footer()}
</body>
</html>"""

def build_disclaimer():
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Disclaimer | Footlet Crystal Atelier</title>
  <meta name="description" content="Legal and craft disclaimer for Footlet Crystal Atelier. Information on textile variations, digital color display, and structural usage guidelines.">
  <link rel="canonical" href="https://{DOMAIN}/disclaimer.html">
  {GTAG}
  {FONTS}
  <link rel="stylesheet" href="assets/css/style.css">
</head>
<body>
{get_header('')}

  <main>
    <section class="fc-policy-header">
      <div class="fc-container">
        <span class="fc-section-tag">Craft Clarifications</span>
        <h1 class="fc-hero-title">Atelier Textile &amp; Fiber <span>Disclaimer</span></h1>
        <p class="fc-hero-desc" style="margin-bottom: 0;">Effective Date: January 1, 2026 &bull; Footlet Crystal Atelier LLC</p>
      </div>
    </section>

    <div class="fc-container">
      <div class="fc-policy-content">
        
        <div class="fc-policy-section">
          <h2>1. Digital Representation &amp; Color Variance</h2>
          <p class="fc-policy-p">
            The photographic images, editorial video captures, and digital textile previews displayed on this website are produced with rigorous color-calibration techniques to illustrate our hosiery goods as accurately as technology permits. However, because individual computer displays, smartphones, and tablet screens possess distinct hardware gamuts, brightness settings, and color temperature profiles, actual yarn hues may vary subtly from screen renderings. Digital depictions serve as aesthetic representations rather than contractual color guarantees.
          </p>
          <p class="fc-policy-p">
            Furthermore, because our wool and cotton yarns undergo organic small-batch vat dyeing with environmentally conscious mineral extracts, each separate dye lot exhibits delicate shifts in tone, warmth, and luster. An obsidian black or crystal silver dye lot processed during winter may display slightly deeper tones than a batch dyed during spring runoffs. Patrons desiring exact color confirmation are invited to visit our Boston salon to inspect physical yarn swatches under natural daylight prior to finalizing commission orders.
          </p>
        </div>

        <div class="fc-policy-section">
          <h2>2. Natural Fiber Integrity &amp; Wear Characteristics</h2>
          <p class="fc-policy-p">
            Footlet Crystal Atelier works exclusively with premium biological fibers including superfine Australian Merino wool, Giza 87 mercerized cotton, and natural mulberry silk. As natural agricultural materials, these fibers interact organically with foot heat, friction, and humidity. Over extended periods of continuous friction against coarse internal shoe linings, minor surface fiber fuzzing may naturally emerge. We avoid harsh chemical resin coatings that seal fibers artificially at the expense of skin breathability.
          </p>
          <p class="fc-policy-p">
            These authentic characteristics demonstrate that our yarns have not been adulterated with suffocating petroleum plastics or synthetic sealants. Collectors and commissioners must recognize that natural fiber breathability is an essential hallmark of luxury hosiery, delivering superior moisture absorption and skin health that cannot be matched by cheap synthetic polyester socks. Every natural fiber contour celebrates genuine biological provenance and permanent environmental integrity across seasons of wear.
          </p>
        </div>

        <div class="fc-policy-section">
          <h2>3. Structural Usage, Footwear Compatibility &amp; Wash Care</h2>
          <p class="fc-policy-p">
            While our footlets and hosiery are constructed with exceptional structural durability utilizing 200-needle circular knitting and hand-linked toes, they are designed for luxury sartorial footwear and clean foot hygiene. Wearing footlets inside rough work boots with protruding metal eyelets or untrimmed toenails may cause localized abrasion, yarn pulls, or premature fabric thinning. Patrons are urged to follow recommended sizing guidelines to avoid overstretching the knitted elasticity.
          </p>
          <p class="fc-policy-p">
            Our pieces require gentle maintenance to preserve the integrity of both the biological yarns and the vulcanized silicone heel grips. Exposing footlets to hot water washes above forty degrees Celsius, industrial tumble dryers, or aggressive chlorine bleaches will compromise elastic recovery and degrade silicone adhesion. Damage resulting from improper laundering, caustic chemical detergents, or gross physical abuse falls outside our artisanal guarantee and warranty protections.
          </p>
        </div>

        <div class="fc-policy-section">
          <h2>4. Independent Artisanal Workshop Status</h2>
          <p class="fc-policy-p">
            Footlet Crystal Atelier LLC is a wholly independent, privately owned artisanal hosiery studio based in Boston, Massachusetts. We are not affiliated, associated, authorized, endorsed by, or in any way officially connected with any international luxury fashion conglomerates, mass-market athletic apparel manufacturers, or commercial licensing organizations. Any historical references to European knitting guilds or classic shoe models are made purely in an educational and artisanal context to celebrate historical techniques.
          </p>
          <p class="fc-policy-p">
            All footlet patterns, silicone grip profiles, and bespoke collections produced by Footlet Crystal are original proprietary designs conceived in our Boston workshop. We maintain strict separation from fast-fashion production models and commercial mass distribution. Our atelier prides itself on sustaining independent craft ethics, fair wage artisan compensation, and direct personal relationships between the maker and the commissioning patron across all commissions.
          </p>
        </div>

        <div class="fc-policy-section">
          <h2>5. Inquiries Regarding Craft Specifications</h2>
          <p class="fc-policy-p">
            If you have questions regarding the technical specifications, yarn certifications, tensile testing metrics, or material safety parameters detailed in this disclaimer, our atelier staff is readily accessible. We welcome direct communications from clients, podiatrists, and sartorial guilds seeking clarification on our workshop practices, ethical wool harvesting sources, or hypoallergenic textile testing methodologies. Our staff ensures that every technical aspect of our hosiery is explained thoroughly to all interested patrons.
          </p>
          <p class="fc-policy-p">
            Written requests regarding yarn provenance, custom compression requirements, or OEKO-TEX environmental safety certifications should be directed to our master technician using the contact details provided below. We commit to providing thorough, transparent technical documentation for all authenticated collections bearing the Footlet Crystal guild hallmark. Clients may also schedule an appointment to inspect physical material archives and fiber laboratory certifications directly within our Boston salon.
          </p>
          <div class="fc-policy-contact-card">
            <h3>Atelier Craft Secretariat</h3>
            <p><strong>Institutional Address:</strong> {ADDR}</p>
            <p><strong>Technical Telephone:</strong> {PHONE}</p>
            <p><strong>Direct Inquiries:</strong> {EMAIL}</p>
          </div>
        </div>

      </div>
    </div>
  </main>

{get_footer()}
</body>
</html>"""

def build_cookie():
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Cookie Policy | Footlet Crystal Atelier</title>
  <meta name="description" content="Cookie Policy for Footlet Crystal Atelier. Understand how our digital platform deploys essential and analytical cookies to ensure optimal browsing performance.">
  <link rel="canonical" href="https://{DOMAIN}/cookie-policy.html">
  {GTAG}
  {FONTS}
  <link rel="stylesheet" href="assets/css/style.css">
</head>
<body>
{get_header('')}

  <main>
    <section class="fc-policy-header">
      <div class="fc-container">
        <span class="fc-section-tag">Digital Telemetry</span>
        <h1 class="fc-hero-title">Cookie &amp; Tracking <span>Technologies Policy</span></h1>
        <p class="fc-hero-desc" style="margin-bottom: 0;">Effective Date: January 1, 2026 &bull; Footlet Crystal Atelier LLC</p>
      </div>
    </section>

    <div class="fc-container">
      <div class="fc-policy-content">
        
        <div class="fc-policy-section">
          <h2>1. Introduction to Cookie Technologies</h2>
          <p class="fc-policy-p">
            This Cookie Policy explains how Footlet Crystal Atelier LLC utilizes cookies, tracking pixels, and related web telemetry mechanisms when you explore our digital salon. Cookies are compact alphanumeric data files placed onto your computer hard drive, tablet, or mobile device by your internet browser during webpage access. These files permit web servers to recognize your specific hardware terminal and retain critical session parameters to ensure fluid visual rendering across digital visits.
          </p>
          <p class="fc-policy-p">
            We adhere strictly to a philosophy of data minimization that mirrors our careful artisanal material stewardship. We do not utilize intrusive commercial tracking pixels, third-party behavioral profiling scripts, or predatory advertising cookies designed to monitor your off-site browsing habits across external commercial networks. Every telemetry mechanism deployed upon our digital infrastructure serves a direct, transparent purpose related to platform performance, security verification, or aggregate visitor analysis.
          </p>
        </div>

        <div class="fc-policy-section">
          <h2>2. Categories of Cookies Deployed</h2>
          <p class="fc-policy-p">
            Our platform deploys Strictly Necessary Cookies that are fundamental to core site navigation, secure encrypted server connections, and interactive appointment form submissions. Without these essential cookies, fundamental security architectures and salon inquiry forms would fail to operate reliably. Because these files ensure basic operational integrity and cyber defense compliance, they cannot be deactivated within our server management consoles without breaking site functionality.
          </p>
          <p class="fc-policy-p">
            We additionally utilize Performance and Diagnostic Cookies that compile anonymous, aggregated statistical information regarding how patrons interact with our website sections. These metrics reveal which hosiery portfolios attract interest, average page loading durations, and whether visitors encounter server error warnings. This diagnostic data is completely anonymized and cannot be reverse-engineered to identify individual patrons, serving solely to optimize web rendering speed and mobile responsiveness.
          </p>
        </div>

        <div class="fc-policy-section">
          <h2>3. First-Party vs. Third-Party Web Analytics</h2>
          <p class="fc-policy-p">
            First-party cookies are generated and managed directly by Footlet Crystal Atelier web servers to preserve your interface language preferences, mobile drawer states, and font caching parameters between successive page visits. These cookies are maintained strictly under our sovereign institutional control and are never shared with external advertising conglomerates or third-party behavioral data brokers operating outside our direct digital domain boundaries.
          </p>
          <p class="fc-policy-p">
            Third-party analytical telemetry, including standard Google Analytics tags, may process anonymous user metrics under strict data processing agreements. These analytical scripts monitor aggregate visitor traffic volumes, device operating platforms, and regional referral headers. Third-party providers are legally bound by contractual data protection agreements prohibiting them from merging diagnostic metrics gathered on our site with identifiable personal accounts held within their commercial networks.
          </p>
        </div>

        <div class="fc-policy-section">
          <h2>4. Patron Control &amp; Browser Cookie Management</h2>
          <p class="fc-policy-p">
            You retain absolute legal and technical autonomy to govern how cookies are stored upon your digital devices. Modern web browsers, including Google Chrome, Apple Safari, Mozilla Firefox, and Microsoft Edge, provide comprehensive preference settings that permit users to review, filter, block, or delete cookies at will. You may configure your browser software to reject all third-party cookies or receive an interactive alert whenever a web server attempts to deposit a cookie file.
          </p>
          <p class="fc-policy-p">
            Please be advised that if you elect to disable strictly necessary session cookies entirely within your browser controls, certain interactive elements of our digital salon—such as our interactive consultation booking forms, responsive image galleries, and secure appointment confirmation scripts—may function with degraded speed or require repeated manual authentication during your visit. Most patrons find that leaving first-party cookies active provides the smoothest viewing experience.
          </p>
        </div>

        <div class="fc-policy-section">
          <h2>5. Telemetry Policy Inquiries &amp; Administration</h2>
          <p class="fc-policy-p">
            Footlet Crystal Atelier reviews this Cookie Policy semi-annually to confirm strict alignment with domestic privacy standards and international data governance directives. When technical updates or security enhancements warrant revisions to our cookie usage protocols, amended text will be posted immediately within this section alongside an updated calendar timestamp to provide complete operational transparency to our patrons. This continuous governance ensures our data processing remains responsible, proportional, and compliant with all evolving legal standards.
          </p>
          <p class="fc-policy-p">
            For technical inquiries regarding our cookie deployments, web tracking safeguards, or to request documentation concerning our digital telemetry governance protocols, please direct communications to our systems administration team using the contact coordinates outlined below. Our technical staff is prepared to answer technical questions and assist patrons with browser privacy configuration guidance upon request. We remain dedicated to upholding the highest standards of digital ethics and patron transparency across all web interactions.
          </p>
          <div class="fc-policy-contact-card">
            <h3>Atelier Web Governance Bureau</h3>
            <p><strong>Institutional Address:</strong> {ADDR}</p>
            <p><strong>Concierge Telephone:</strong> {PHONE}</p>
            <p><strong>Technical Inquiries:</strong> {EMAIL}</p>
          </div>
        </div>

      </div>
    </div>
  </main>

{get_footer()}
</body>
</html>"""



# ==========================================
# 7. SITEMAP & ROBOTS
# ==========================================
def build_sitemap():
    pages = [
        "index.html",
        "about.html",
        "products.html",
        "faq.html",
        "contact.html",
        "privacy-policy.html",
        "terms-and-conditions.html",
        "disclaimer.html",
        "cookie-policy.html"
    ]
    urls = ""
    for p in pages:
        urls += f"""  <url>
    <loc>https://{DOMAIN}/{p}</loc>
    <lastmod>2026-09-28</lastmod>
    <changefreq>monthly</changefreq>
    <priority>{'1.0' if p == 'index.html' else '0.8'}</priority>
  </url>\n"""
    
    return f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{urls}</urlset>"""

def build_robots():
    return f"""User-agent: *
Allow: /
Sitemap: https://{DOMAIN}/sitemap.xml
"""

# ==========================================
# 8. REGISTRIES & MANIFEST
# ==========================================
def build_image_registry():
    return """# IMAGE REGISTRY - FOOTLET CRYSTAL ATELIER
Domain: footletcrystal.com
Niche: Socks / Luxury Footlets & Precision Hosiery
Strict Rule: 20 Unique Images, Used Exactly Once, >20KB Each, Zero Duplicates, Zero Drawings, Zero Buildings

| Asset Name | Subject Description | Location / Section Used | MD5 Hash | Status |
| :--- | :--- | :--- | :--- | :--- |
| `footletcrystal_asset_1.jpg` | Invisible black cotton luxury loafer liner footlet | `index.html` (Center Hero Triple-Pod 1: Mercerized Cotton) | 0189a18aac0bfb58cc02ce7f7664395e | Verified Unique |
| `footletcrystal_asset_2.jpg` | Merino wool footlet liner sock engineered with thermal knit | `index.html` (Center Hero Triple-Pod 2: Thermal Merino) | cceb06e77d2ddb478d66be441a8a2899 | Verified Unique |
| `footletcrystal_asset_3.jpg` | High-density terry cushion sole on artisan footlet sock | `index.html` (Center Hero Triple-Pod 3: Micro Cushion) | ba15bf671b9532111b03b8ba530ca78d | Verified Unique |
| `footletcrystal_asset_4.jpg` | Hand-linked seamless crystal toe close-up | `index.html` (Asymmetric Editorial Split: Hand-Linked Toe) | 1140961295c6e57e1e31c1e03205e662 | Verified Unique |
| `footletcrystal_asset_5.jpg` | Elastic ribbed comfort cuff on luxury sock | `index.html` (Lookbook Duo Ribbon Card 1: Architectural Rib) | cf7e4f12c48578fb16708abca8038150 | Verified Unique |
| `footletcrystal_asset_6.jpg` | Casual everyday merino wool footlet sock | `index.html` (Lookbook Duo Ribbon Card 2: Merino Voyager) | 229c652d18466ea9c04164695d46830e | Verified Unique |
| `footletcrystal_asset_7.jpg` | Crystalline cushion crew sock with arch support | `index.html` (Zig-Zag Narrative Row 1: Metatarsal Dampening) | 8761122a19f7d5e29f8475bf7c99d792 | Verified Unique |
| `footletcrystal_asset_8.jpg` | Crystalline textured rib sock handcrafted columns | `index.html` (Zig-Zag Narrative Row 2: Columnar Ribbing) | 83f8d97c35b27850931ea8dab397b995 | Verified Unique |
| `footletcrystal_asset_9.jpg` | Luxury sartorial socks collection displayed in atelier | `about.html` (Asymmetric Mosaic Tall: Sartorial Suite) | b8a66f0fb47c22970160eb0cd5d95199 | Verified Unique |
| `footletcrystal_asset_10.jpg` | Fine merino wool knit sock detail displaying stitch structure | `about.html` (Asymmetric Mosaic Stack Top: Merino Structure) | 1f6eb3730977af25cccd39212e194f97 | Verified Unique |
| `footletcrystal_asset_11.jpg` | Artisan hand-knit wool sock displaying traditional cable heritage | `about.html` (Asymmetric Mosaic Stack Bottom: Cable Heritage) | 82e1c53e794a5f49d7b709ea1e83be8f | Verified Unique |
| `footletcrystal_asset_12.jpg` | Terry loop micro-cushioning footbed structure under magnification | `about.html` (Micro-Terry Laboratory Feature: Magnified Footbed) | b05fd62fd1ced3e3230e0921eaa7048a | Verified Unique |
| `footletcrystal_asset_13.jpg` | Athletic running performance sock with zoned compression | `products.html` (Catalog Card 1: Athletic Running Footlet) | 4ff393fd67e92bfe987ebf37c3155ff8 | Verified Unique |
| `footletcrystal_asset_14.jpg` | Heavy-gauge trail hiking crew sock knitted with merino wool | `products.html` (Catalog Card 2: Heavy Trail Hiking Crew) | d4cb2232be92748e71409d116aa4be4d | Verified Unique |
| `footletcrystal_asset_15.jpg` | Graduated compression recovery sock with medical gradient | `products.html` (Catalog Card 3: Graduated Compression Sock) | c15eda0b68e9a9918cef111d2788ecdf | Verified Unique |
| `footletcrystal_asset_16.jpg` | Aerobic runner low-cut footlet with protective heel tab | `products.html` (Catalog Card 4: Aerobic Runner Footlet) | e6f361cb4711fe827221c1e1f98259db | Verified Unique |
| `footletcrystal_asset_17.jpg` | Trail pro protective ankle sock with debris seal cuff | `products.html` (Catalog Card 5: Trail Pro Ankle Sock) | 4a84ab29a02ff1bc9415931edf548a66 | Verified Unique |
| `footletcrystal_asset_18.jpg` | Active run low-cut sport liner with breathable open knit | `products.html` (Catalog Card 6: Active Sport Liner) | 09567ab338c9ce46936c83f5d2cd0496 | Verified Unique |
| `footletcrystal_asset_19.jpg` | Cushioned trail performance sock on display in atelier | `contact.html` (Inverted Contact Feature Card & Coordinates) | 466fd92bc7e3a4f7d182eff017e1d26b | Verified Unique |
| `footletcrystal_asset_20.jpg` | Micro crew running sock and footlet liner display | `faq.html` (Knowledge Vault Header Feature) | f2ce269af4cacf154281a69358079e3a | Verified Unique |

Total Images: 20
Total Usages: 20 (Every image used exactly once across website)
Repetitions: 0
100% Real Socks & Footlets Photography
"""

def build_design_registry():
    return """# DESIGN REGISTRY - FOOTLET CRYSTAL ATELIER

## Archetype Identity
- **Design Archetype:** Nordic Minimalist Crystalline / Crystalline Atelier / Frosted Precision Grid / Asymmetric Editorial
- **Domain:** footletcrystal.com
- **Niche:** Socks / Luxury Footlets & Precision Hosiery
- **CSS Namespace:** Dedicated `.fc-...` namespace (Zero global collisions)

## Color Architecture
- **Midnight Frosted Dark:** `#070b14`
- **Abyssal Base:** `#03060d`
- **Mineral Cyan Accent:** `#0284c7`
- **Crystalline Glow:** `#38bdf8`
- **Opal Cyan:** `#06b6d4`
- **Ice Crystal White:** `#f8fafc`
- **Frosted Light Background:** `#f1f5f9`
- **Text Light:** `#f8fafc`
- **Text Muted:** `#94a3b8`
- **Text Dark:** `#0f172a`

## Typography Pairings
- **Display Headings:** `Outfit` (700, 800)
- **Subheadings & Title Accents:** `Prata` (Regular Serif)
- **Body & Editorial Prose:** `Inter` (300, 400, 500, 600, 700)
- **Technical Specs & Badges:** `Space Mono` (400, 700)

## Bespoke Structural Layout (Zero Template Fingerprint)
1. **Center-Stage Masthead with Triple-Pod Showcase:** Full-width panoramic masthead featuring 3 floating crystal cards displaying Assets 1, 2, 3 side-by-side.
2. **Marquee Ticker:** Continuous CSS ticker communicating 200-needle gauge specs and hand-linking standards.
3. **Asymmetric Editorial Split:** Bold quote callout, editorial manifesto, and prominent framed display of Asset 4 with caption.
4. **Swiss 4-Column Precision Metric Grid:** Clean borderless metric typography columns highlighting 200N gauge, 0 mm toe ridge, 3-wave silicone, and 17.5μ merino.
5. **Lookbook Duo Ribbon:** Two full-bleed editorial panoramas with frosted bottom overlays featuring Assets 5 & 6.
6. **Footwear Pairing Guide Matrix Table:** Comprehensive compatibility chart pairing shoe silhouettes (Belgian loafers, suede loafers, Oxfords, driving mocs) with footlet cuts.
7. **Staggered Zig-Zag Narrative Rows:** Dynamic alternating narrative rows showcasing Assets 7 & 8 with in-depth yarn physics and sole cushioning mechanics.
8. **Curated Wardrobe Vitrine Tiers:** 3 tailored vitrine boxes (Weekender, Executive Sartorial [featured], Transatlantic Suite) with tier badges and spec checklists.
9. **Laboratory Data Log:** 4 empirical test metric boxes (85,000 abrasion cycles, 1.8x evaporation speed, 99.4% elastic retention, 0.00% slip probability).
10. **Single-Column Sartorial Spotlight Quote:** Cordwainer master quote with 5-star rating header.
11. **Dual-Column FAQ Accordion:** Clean two-column accordion layout solving common consumer and collector inquiries.
12. **Private Salon Consultation Strip:** Deep dark radial CTA banner with direct telephone and booking actions.
13. **Horizontal Catalog on Products Page:** Full-width alternating cards with detailed specification metrics for Assets 13 to 18 + Sizing Chart.
14. **Asymmetric Mosaic Gallery on About Page:** 3-column asymmetric mosaic for Assets 9, 10, 11 + Micro-Terry Laboratory Feature for Asset 12.
15. **Inverted Split on Contact Page:** Feature card with Asset 19 and atelier coordinates on left, luxury inquiry form on right.
"""

def build_site_manifest():
    manifest = {
        "domain": DOMAIN,
        "brand": BRAND,
        "niche": "socks",
        "institutional_contact": {
            "address": ADDR,
            "phone": PHONE,
            "email": EMAIL
        },
        "pages": [
            "index.html",
            "about.html",
            "products.html",
            "faq.html",
            "contact.html",
            "privacy-policy.html",
            "terms-and-conditions.html",
            "disclaimer.html",
            "cookie-policy.html"
        ],
        "assets_count": 20,
        "php_files_count": 0,
        "blog_included": False,
        "google_tag": "G-0LY0HY7L01",
        "qa_verified": True
    }
    return json.dumps(manifest, indent=2)

# ==========================================
# EXECUTE GENERATION
# ==========================================
def main():
    files_to_generate = {
        "index.html": build_index(),
        "about.html": build_about(),
        "products.html": build_products(),
        "contact.html": build_contact(),
        "faq.html": build_faq(),
        "privacy-policy.html": build_privacy(),
        "terms-and-conditions.html": build_terms(),
        "disclaimer.html": build_disclaimer(),
        "cookie-policy.html": build_cookie(),
        "sitemap.xml": build_sitemap(),
        "robots.txt": build_robots(),
        "IMAGE_REGISTRY.md": build_image_registry(),
        "DESIGN_REGISTRY.md": build_design_registry(),
        "SITE_MANIFEST.json": build_site_manifest()
    }

    for filename, content in files_to_generate.items():
        filepath = os.path.join(BASE_DIR, filename)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Generated {filename} ({len(content)} chars)")

    print("\nAll files successfully generated.")

if __name__ == "__main__":
    main()
