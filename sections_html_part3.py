# -*- coding: utf-8 -*-
"""
Fleetsure Sections 10-14, Footer & Modals HTML (Streamlined & Clean)
"""

def get_views_html(C):
    h2 = C['10. WHAT YOU CAN SEE']['H2']['content']
    content = C['10. WHAT YOU CAN SEE']['Content']['content']
    panel_label = C['10. WHAT YOU CAN SEE']['Panel']['content']

    return f"""
  <!-- =======================================================================
       10. WHAT YOU CAN SEE
       ========================================================================= -->
  <section id="reporting">
    <div class="container">
      <div class="section-header">
        <h2>{h2}</h2>
        <p class="prose-760">{content}</p>
      </div>

      <!-- 2 x 2 Dashboard Grid: Simple & High Clarity -->
      <div class="dashboard-2x2-grid">
        <!-- Panel 1: Fleet Status -->
        <div class="dash-panel">
          <div class="dash-panel-header">
            <span>Fleet-Wide Compliance Health</span>
            <span class="example-data-tag">All Depots</span>
          </div>
          <div class="dash-panel-body">
            <div style="font-size:28px; font-weight:800; color:#34D399; margin-bottom:4px;">97.3% Valid</div>
            <div style="font-size:13.5px; color:var(--text); margin-bottom:16px;">136 out of 148 fleet vehicles active and 100% legal on the road today.</div>
            <div style="display:flex; flex-direction:column; gap:8px; font-size:13px;">
              <div style="display:flex; justify-content:space-between; padding:8px 12px; background:var(--surface); border-radius:6px;">
                <span>Owned Fleet (104 vehicles)</span>
                <span style="color:#34D399; font-weight:700;">99.0% Compliant</span>
              </div>
              <div style="display:flex; justify-content:space-between; padding:8px 12px; background:var(--surface); border-radius:6px;">
                <span>Vendor &amp; Leased (44 vehicles)</span>
                <span style="color:#FBBF24; font-weight:700;">93.2% Compliant</span>
              </div>
            </div>
          </div>
        </div>

        <!-- Panel 2: Expiring Soon -->
        <div class="dash-panel">
          <div class="dash-panel-header">
            <span>Documents Expiring Soon</span>
            <span class="example-data-tag">30 &middot; 15 &middot; 7 Days</span>
          </div>
          <div class="dash-panel-body">
            <div style="font-size:28px; font-weight:800; color:#FBBF24; margin-bottom:4px;">8 Reminders Active</div>
            <div style="font-size:13.5px; color:var(--text); margin-bottom:16px;">Alerts already sent to depot leads. Renewals handled ahead of time.</div>
            <div style="display:flex; flex-direction:column; gap:8px; font-size:13px;">
              <div style="display:flex; justify-content:space-between; padding:8px 12px; background:var(--surface); border-radius:6px;">
                <span>MH-12-RN-4821 (Commercial Insurance)</span>
                <span style="color:#F87171; font-weight:700;">7 Days Left</span>
              </div>
              <div style="display:flex; justify-content:space-between; padding:8px 12px; background:var(--surface); border-radius:6px;">
                <span>DL-01-AX-9942 (PUC Certificate)</span>
                <span style="color:#FBBF24; font-weight:700;">12 Days Left</span>
              </div>
            </div>
          </div>
        </div>

        <!-- Panel 3: Challans by State -->
        <div class="dash-panel">
          <div class="dash-panel-header">
            <span>Interstate Challans</span>
            <span class="example-data-tag">Grouped By State</span>
          </div>
          <div class="dash-panel-body">
            <div style="font-size:28px; font-weight:800; color:#F87171; margin-bottom:4px;">₹38,500 Total</div>
            <div style="font-size:13.5px; color:var(--text); margin-bottom:16px;">Fines caught early across states before late fees and court penalties.</div>
            <div style="display:flex; flex-direction:column; gap:8px; font-size:13px;">
              <div style="display:flex; justify-content:space-between; padding:8px 12px; background:var(--surface); border-radius:6px;">
                <span>Maharashtra Highways (6 challans)</span>
                <span style="color:#F87171; font-weight:700;">₹14,500</span>
              </div>
              <div style="display:flex; justify-content:space-between; padding:8px 12px; background:var(--surface); border-radius:6px;">
                <span>Karnataka Border (3 challans)</span>
                <span style="color:#F87171; font-weight:700;">₹11,000</span>
              </div>
            </div>
          </div>
        </div>

        <!-- Panel 4: Document Storage & History -->
        <div class="dash-panel">
          <div class="dash-panel-header">
            <span>Government Checks &amp; Audit Vault</span>
            <span class="example-data-tag">Audit Ready</span>
          </div>
          <div class="dash-panel-body">
            <div style="font-size:28px; font-weight:800; color:var(--brand-light); margin-bottom:4px;">100% Verified</div>
            <div style="font-size:13.5px; color:var(--text); margin-bottom:16px;">Every document authenticated against government records.</div>
            <div style="display:flex; flex-direction:column; gap:8px; font-size:13px;">
              <div style="display:flex; justify-content:space-between; padding:8px 12px; background:var(--surface); border-radius:6px;">
                <span>Vehicle Registrations (RC)</span>
                <span style="color:#34D399; font-weight:700;">VAHAN Verified</span>
              </div>
              <div style="display:flex; justify-content:space-between; padding:8px 12px; background:var(--surface); border-radius:6px;">
                <span>Driver Licences (DL)</span>
                <span style="color:#34D399; font-weight:700;">Sarathi Verified</span>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- 4 High-Level Metric Cards -->
      <div class="dashboard-metrics-strip">
        <div class="metric-panel-card">
          <div class="metric-panel-title">Fleet Compliance Rate</div>
          <div class="metric-panel-val" style="color:var(--accent-green);">97.3%</div>
          <div class="metric-panel-desc">Road-legal across all states</div>
        </div>
        <div class="metric-panel-card">
          <div class="metric-panel-title">Active Depots</div>
          <div class="metric-panel-val">5 Hubs</div>
          <div class="metric-panel-desc">Pune, Mumbai, Delhi, BLR, Chennai</div>
        </div>
        <div class="metric-panel-card">
          <div class="metric-panel-title">Early Alerts</div>
          <div class="metric-panel-val" style="color:#F59E0B;">30 &middot; 15 &middot; 7d</div>
          <div class="metric-panel-desc">Dispatched via WhatsApp &amp; Email</div>
        </div>
        <div class="metric-panel-card">
          <div class="metric-panel-title">Vehicle Hardware</div>
          <div class="metric-panel-val" style="color:var(--brand-light);">Zero</div>
          <div class="metric-panel-desc">No tracking devices or OBD units</div>
        </div>
      </div>
    </div>
  </section>
    """

def get_compare_html(C):
    h2 = C['11. BUILT FOR COMPLIANCE, NOT A GPS SUITE']['H2']['content']
    c1_h = C['11. BUILT FOR COMPLIANCE, NOT A GPS SUITE']['Card 1 - Heading']['content']
    c1_c = C['11. BUILT FOR COMPLIANCE, NOT A GPS SUITE']['Card 1 - Content']['content']
    c2_h = C['11. BUILT FOR COMPLIANCE, NOT A GPS SUITE']['Card 2 - Heading']['content']
    c2_c = C['11. BUILT FOR COMPLIANCE, NOT A GPS SUITE']['Card 2 - Content']['content']
    ttv = C['11. BUILT FOR COMPLIANCE, NOT A GPS SUITE']['Time to value']['content']

    return f"""
  <!-- =======================================================================
       11. BUILT FOR COMPLIANCE, NOT A GPS SUITE
       ========================================================================= -->
  <section class="bg-surface" id="compliance-vs-gps">
    <div class="container">
      <div class="section-header text-center prose-760" style="margin:0 auto 36px;">
        <h2>{h2}</h2>
      </div>

      <div class="config-cards-grid">
        <!-- Card 1: GPS and telematics suites -->
        <div class="config-card config-card-muted">
          <div>
            <h3>{c1_h}</h3>
            <p>{c1_c}</p>
            <ul style="list-style:none; margin-top:20px; display:flex; flex-direction:column; gap:12px; font-size:14px; color:var(--muted);">
              <li style="display:flex; align-items:center; gap:8px;">
                <span style="color:#EF4444;"><svg width="16" height="16" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M6 18L18 6M6 6l12 12"></path></svg></span>
                Needs hardware fitted to every vehicle
              </li>
              <li style="display:flex; align-items:center; gap:8px;">
                <span style="color:#EF4444;"><svg width="16" height="16" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M6 18L18 6M6 6l12 12"></path></svg></span>
                Months of rollout and fleet disruption
              </li>
              <li style="display:flex; align-items:center; gap:8px;">
                <span style="color:#EF4444;"><svg width="16" height="16" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M6 18L18 6M6 6l12 12"></path></svg></span>
                Document compliance is just an afterthought module
              </li>
            </ul>
          </div>
        </div>

        <!-- Card 2: Fleetsure -->
        <div class="config-card config-card-highlight">
          <div class="highlight-badge">Dedicated Compliance &amp; Challans</div>
          <div>
            <h3 style="color:var(--heading);">{c2_h}</h3>
            <p style="color:#E2E8F0;">{c2_c}</p>
            <ul style="list-style:none; margin-top:20px; display:flex; flex-direction:column; gap:12px; font-size:14px; color:#F1F5F9;">
              <li style="display:flex; align-items:center; gap:8px;">
                <span style="color:#10B981;"><svg width="16" height="16" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M5 13l4 4L19 7"></path></svg></span>
                Zero hardware &mdash; 100% software &amp; AI agents
              </li>
              <li style="display:flex; align-items:center; gap:8px;">
                <span style="color:#10B981;"><svg width="16" height="16" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M5 13l4 4L19 7"></path></svg></span>
                Go live today: upload documents, set alert rules, switch on
              </li>
              <li style="display:flex; align-items:center; gap:8px;">
                <span style="color:#10B981;"><svg width="16" height="16" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M5 13l4 4L19 7"></path></svg></span>
                Challans tracked across every state on one screen
              </li>
            </ul>
          </div>
        </div>
      </div>

      <!-- Time to value strip -->
      <div class="time-to-value-strip">
        <svg width="18" height="18" fill="none" stroke="currentColor" viewBox="0 0 24 24" style="display:inline; vertical-align:middle; margin-right:6px;"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M13 10V3L4 14h7v7l9-11h-7z"></path></svg>
        {ttv}
      </div>
    </div>
  </section>
    """

def get_included_html(C):
    h2 = C['12. WHAT IS INCLUDED']['H2']['content']
    
    t1 = C['12. WHAT IS INCLUDED']['Document tracking']['content']
    t2 = C['12. WHAT IS INCLUDED']['Government record check']['content']
    t3 = C['12. WHAT IS INCLUDED']['Secure storage']['content']
    
    t4 = C['12. WHAT IS INCLUDED']['Expiry alerts']['content']
    t5 = C['12. WHAT IS INCLUDED']['Compliance dashboard']['content']
    t6 = C['12. WHAT IS INCLUDED']['Multi-location view']['content']
    
    t7 = C['12. WHAT IS INCLUDED']['Challan management']['content']
    t8 = C['12. WHAT IS INCLUDED']['Asset status tracking']['content']

    return f"""
  <!-- =======================================================================
       12. WHAT IS INCLUDED
       ========================================================================= -->
  <section class="included-section" id="included">
    <div class="container">
      <div class="section-header text-center prose-760" style="margin:0 auto 36px;">
        <h2>{h2}</h2>
      </div>

      <div class="included-grid">
        <!-- Group 1: Track -->
        <div class="included-phase-header">
          <span class="included-phase-title">Track</span>
          <div class="included-phase-line"></div>
        </div>

        <div class="included-tile">
          <div class="included-icon-box">
            <svg width="20" height="20" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"></path></svg>
          </div>
          <div class="included-heading">Document tracking</div>
          <div class="included-desc">{t1}</div>
        </div>

        <div class="included-tile">
          <div class="included-icon-box">
            <svg width="20" height="20" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z"></path></svg>
          </div>
          <div class="included-heading">Government record check</div>
          <div class="included-desc">{t2}</div>
        </div>

        <div class="included-tile">
          <div class="included-icon-box">
            <svg width="20" height="20" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 15v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2-2H6a2 2 0 00-2 2v6a2 2 0 002 2zm10-10V7a4 4 0 00-8 0v4h8z"></path></svg>
          </div>
          <div class="included-heading">Secure storage</div>
          <div class="included-desc">{t3}</div>
        </div>

        <!-- Group 2: Alert and see -->
        <div class="included-phase-header">
          <span class="included-phase-title">Alert and see</span>
          <div class="included-phase-line"></div>
        </div>

        <div class="included-tile">
          <div class="included-icon-box">
            <svg width="20" height="20" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 17h5l-1.405-1.405A2.032 2.032 0 0118 14.158V11a6.002 6.002 0 00-4-5.659V5a2 2 0 10-4 0v.341C7.67 6.165 6 8.388 6 11v3.159c0 .538-.214 1.055-.595 1.436L4 17h5m6 0v1a3 3 0 11-6 0v-1m6 0H9"></path></svg>
          </div>
          <div class="included-heading">Expiry alerts</div>
          <div class="included-desc">{t4}</div>
        </div>

        <div class="included-tile">
          <div class="included-icon-box">
            <svg width="20" height="20" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z"></path></svg>
          </div>
          <div class="included-heading">Compliance dashboard</div>
          <div class="included-desc">{t5}</div>
        </div>

        <div class="included-tile">
          <div class="included-icon-box">
            <svg width="20" height="20" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3.055 11H5a2 2 0 012 2v1a2 2 0 002 2 2 2 0 012 2v2.945M8 3.935V5.5A2.5 2.5 0 0010.5 8h.5a2 2 0 012 2 2 2 0 104 0 2 2 0 012-2h1.064M15 20.488V18a2 2 0 012-2h3.064M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>
          </div>
          <div class="included-heading">Multi-location view</div>
          <div class="included-desc">{t6}</div>
        </div>

        <!-- Group 3: Manage -->
        <div class="included-phase-header">
          <span class="included-phase-title">Manage</span>
          <div class="included-phase-line"></div>
        </div>

        <div class="included-tile">
          <div class="included-icon-box">
            <svg width="20" height="20" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8c-1.657 0-3 .895-3 2s1.343 2 3 2 3 .895 3 2-1.343 2-3 2m0-8c1.11 0 2.08.402 2.599 1M12 8V7m0 1v8m0 0v1m0-1c-1.11 0-2.08-.402-2.599-1M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>
          </div>
          <div class="included-heading">Challan management</div>
          <div class="included-desc">{t7}</div>
        </div>

        <div class="included-tile">
          <div class="included-icon-box">
            <svg width="20" height="20" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 11H5m14 0a2 2 0 012 2v6a2 2 0 01-2 2H5a2 2 0 01-2-2v-6a2 2 0 012-2m14 0V9a2 2 0 00-2-2M5 11V9a2 2 0 012-2m0 0V5a2 2 0 012-2h6a2 2 0 012 2v2M7 7h10"></path></svg>
          </div>
          <div class="included-heading">Asset status tracking</div>
          <div class="included-desc">{t8}</div>
        </div>
      </div>
    </div>
  </section>
    """

def get_faq_html(C, faqs):
    h2 = C['13. FAQ']['H2']['content']

    items_html = ""
    for idx, f in enumerate(faqs, 1):
        items_html += f"""
        <details class="faq-item" id="faq-item-{idx}">
          <summary class="faq-question">
            <span>{f['q']}</span>
            <span class="faq-icon">+</span>
          </summary>
          <div class="faq-answer">
            <p>{f['a']}</p>
          </div>
        </details>
        """

    return f"""
  <!-- =======================================================================
       13. FAQ SECTION
       ========================================================================= -->
  <section class="faq-section" id="faq">
    <div class="container">
      <div class="section-header text-center prose-760" style="margin:0 auto 32px;">
        <h2>{h2}</h2>
      </div>

      <!-- FAQ Search -->
      <div class="faq-search-wrap">
        <svg class="faq-search-icon" width="18" height="18" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"></path></svg>
        <input type="text" id="faq-search-input" class="faq-search-input" placeholder="Search questions on documents, challans, alerts..." oninput="filterFAQs()">
      </div>

      <div class="faq-accordion" id="faq-accordion-list">
        {items_html}
      </div>
    </div>
  </section>
    """

def get_final_cta_html(C):
    h2 = C['14. FINAL CTA']['H2']['content']
    content = C['14. FINAL CTA']['Content']['content']
    primary_cta = C['14. FINAL CTA']['Primary CTA']['content']
    secondary_cta = C['14. FINAL CTA']['Secondary CTA']['content']

    return f"""
  <!-- =======================================================================
       14. FINAL CTA SECTION (Site finishes cleanly here)
       ========================================================================= -->
  <section class="closing-band" id="contact">
    <div class="container prose-680">
      <h2>{h2}</h2>
      <p class="closing-line">{content}</p>
      <div class="closing-buttons">
        <button class="btn btn-contrast-solid" onclick="openDemoModal()">{primary_cta}</button>
        <a href="/contact-us" class="btn btn-contrast-outline">{secondary_cta}</a>
      </div>
    </div>
  </section>
    """

def get_footer_html(C):
    # Completely removed per user request
    return ""

def get_modals_html():
    return """
  <!-- =======================================================================
       INTERACTIVE DEMO MODAL
       ========================================================================= -->
  <div class="modal-backdrop" id="demo-modal" onclick="closeModalOnBackdrop(event, 'demo-modal')">
    <div class="modal-card">
      <div class="modal-header">
        <h3>Book a 20-Minute Fleetsure Demo</h3>
        <button class="modal-close-btn" onclick="closeDemoModal()">&times;</button>
      </div>
      <div class="modal-body">
        <p style="font-size:13.5px; color:var(--text); margin-bottom:18px;">
          Bring a sample of your fleet's vehicles. In twenty minutes, see Fleetsure track their documents, show live status and pull their challans onto one screen.
        </p>
        <form id="demo-booking-form" onsubmit="handleDemoSubmit(event)">
          <div class="form-group">
            <label for="demo-name">Full Name *</label>
            <input type="text" id="demo-name" class="form-control" placeholder="e.g. Rajesh Kumar" required>
          </div>
          <div class="form-group">
            <label for="demo-email">Work Email *</label>
            <input type="email" id="demo-email" class="form-control" placeholder="name@company.com" required>
          </div>
          <div class="form-group">
            <label for="demo-company">Company / Fleet Name *</label>
            <input type="text" id="demo-company" class="form-control" placeholder="e.g. Apex Logistics India" required>
          </div>
          <div class="form-group">
            <label for="demo-fleet-size">Fleet Size (Vehicles) *</label>
            <select id="demo-fleet-size" class="form-control" required>
              <option value="10-50">10 &ndash; 50 Vehicles</option>
              <option value="51-200" selected>51 &ndash; 200 Vehicles</option>
              <option value="201-500">201 &ndash; 500 Vehicles</option>
              <option value="500+">500+ Vehicles (Enterprise)</option>
            </select>
          </div>
          <div style="margin-top:24px;">
            <button type="submit" class="btn btn-brand" style="width:100%;">Schedule 20-Min Live Walkthrough</button>
          </div>
          <div style="text-align:center; font-size:11.5px; color:var(--muted); margin-top:10px;">
            No hardware to fit. Upload, set alert rules, and switch on.
          </div>
        </form>
      </div>
    </div>
  </div>
    """
