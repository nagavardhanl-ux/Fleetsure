# -*- coding: utf-8 -*-
"""
Fleetsure Hero Section HTML (Streamlined, Clear & Focused)
"""

def get_c(C, sec, elem, default=""):
    try:
        val = C[sec][elem]['content']
        if not val:
            return default
        return val.replace(chr(183), '&middot;').replace('·', '&middot;')
    except KeyError:
        return default

def get_header_html():
    # Header completely removed per user request
    return ""

def get_hero_html(C):
    eyebrow = get_c(C, '1. HERO', 'Eyebrow', 'Fleetsure by AIQoD')
    h1 = get_c(C, '1. HERO', 'H1', 'Know every vehicle is legal before it leaves the yard')
    subline = get_c(C, '1. HERO', 'Subline', '')
    primary_cta = get_c(C, '1. HERO', 'Primary CTA', 'Book a demo')
    secondary_cta = get_c(C, '1. HERO', 'Secondary CTA', 'Talk to our team')
    trust_line = get_c(C, '1. HERO', 'Trust line', 'Running with fleet operators today on the AIQoD platform.')

    return f"""
  <!-- =======================================================================
       1. HERO SECTION (Clean, Clear & Impactful)
       ========================================================================= -->
  <section class="hero-section" id="hero">
    <div class="container hero-split">
      <div class="hero-left">
        <div class="eyebrow">
          <span class="eyebrow-dot"></span>
          {eyebrow}
        </div>
        <h1 class="hero-title">
          <span class="hero-product-title">Fleetsure</span>
          <span class="hero-tagline-title">{h1}</span>
        </h1>
        <p>{subline}</p>
        <div class="btn-group">
          <button class="btn btn-brand" onclick="openDemoModal()">{primary_cta}</button>
          <a href="#contact" class="btn btn-outline">{secondary_cta}</a>
        </div>
        <div class="hero-trust">
          <svg width="18" height="18" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z"></path></svg>
          {trust_line}
        </div>
      </div>

      <!-- Hero Dashboard Console Card (Simplified, Clear & Uncluttered) -->
      <div class="hero-right">
        <div class="product-preview-card">
          <div class="preview-topbar">
            <div class="window-controls">
              <span class="win-dot red"></span>
              <span class="win-dot yellow"></span>
              <span class="win-dot green"></span>
            </div>
            <div class="preview-screen-title">
              <svg width="15" height="15" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z"></path></svg>
              Fleetsure Fleet Compliance Console
            </div>
            <span class="example-data-tag">Example data</span>
          </div>

          <div class="hero-console-body">
            <!-- 3 Key Metrics: Clear & Punchy -->
            <div class="hero-metric-strip" style="grid-template-columns: repeat(3, 1fr); margin-bottom: 20px;">
              <div class="hero-metric-box val-green">
                <div class="label">Legal &amp; Road Ready</div>
                <div class="val">136 Vehicles</div>
              </div>
              <div class="hero-metric-box val-amber">
                <div class="label">Expiring &lt;15d</div>
                <div class="val">8 Documents</div>
              </div>
              <div class="hero-metric-box val-red">
                <div class="label">State Challans</div>
                <div class="val">₹38,500</div>
              </div>
            </div>

            <!-- Clear, Legible Fleet List (3 Highlighted Vehicles) -->
            <div style="display:flex; flex-direction:column; gap:10px;">
              <!-- Vehicle 1 -->
              <div style="background:var(--surface); border:1px solid var(--line); border-radius:8px; padding:12px 14px; display:flex; justify-content:space-between; align-items:center;">
                <div>
                  <div style="font-weight:700; color:var(--heading); font-size:14px;">MH-12-RN-4821</div>
                  <div style="font-size:11.5px; color:var(--muted); margin-top:2px;">Pune North &middot; Owned 32ft Container</div>
                </div>
                <div style="display:flex; gap:6px; align-items:center;">
                  <span class="status-pill valid">&bull; RC Valid</span>
                  <span class="status-pill expiring">&bull; Insurance 7d</span>
                </div>
              </div>

              <!-- Vehicle 2 -->
              <div style="background:var(--surface); border:1px solid var(--line); border-radius:8px; padding:12px 14px; display:flex; justify-content:space-between; align-items:center;">
                <div>
                  <div style="font-weight:700; color:var(--heading); font-size:14px;">DL-01-AX-9942</div>
                  <div style="font-size:11.5px; color:var(--muted); margin-top:2px;">Delhi NCR &middot; Leased Tractor Trailer</div>
                </div>
                <div style="display:flex; gap:6px; align-items:center;">
                  <span class="status-pill valid">&bull; All Legal</span>
                  <span class="status-pill valid">&bull; Nil Challans</span>
                </div>
              </div>

              <!-- Vehicle 3 -->
              <div style="background:var(--surface); border:1px solid var(--line); border-radius:8px; padding:12px 14px; display:flex; justify-content:space-between; align-items:center;">
                <div>
                  <div style="font-weight:700; color:var(--heading); font-size:14px;">KA-05-MM-3310</div>
                  <div style="font-size:11.5px; color:var(--muted); margin-top:2px;">Bengaluru &middot; Vendor 16T Multi-Axle</div>
                </div>
                <div style="display:flex; gap:6px; align-items:center;">
                  <span class="status-pill expired">&bull; DL Lapsed</span>
                  <span class="status-pill expiring">&bull; ₹2,000 Fine</span>
                </div>
              </div>
            </div>

            <!-- Slide-in Alert -->
            <div class="hero-slide-alert" style="margin-top:16px;">
              <div class="alert-left">
                <svg width="16" height="16" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z"></path></svg>
                <span>Automated Alert: Insurance renewal due in 7 days (MH-12-RN-4821)</span>
              </div>
              <span class="example-data-tag">WhatsApp &amp; Email Sent</span>
            </div>

            <!-- Clean interstate challan summary -->
            <div class="hero-challan-strip" style="margin-top:12px;">
              <span style="color:var(--muted); font-weight:600;">Interstate Challans:</span>
              <div class="challan-states-row">
                <span class="state-chip">MH: ₹14,500</span>
                <span class="state-chip">DL: ₹8,000</span>
                <span class="state-chip">KA: ₹11,000</span>
                <span class="state-chip">TN: ₹5,000</span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
    """
