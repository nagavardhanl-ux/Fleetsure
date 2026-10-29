# -*- coding: utf-8 -*-
"""
Fleetsure Sections HTML Generator
"""

import json

def get_c(C, sec, elem, default=""):
    try:
        val = C[sec][elem]['content']
        if not val:
            return default
        # Replace chr(183) with &middot; if present
        return val.replace(chr(183), '&middot;').replace('·', '&middot;')
    except KeyError:
        return default

def get_header_html():
    return """
  <header class="site-header">
    <div class="container header-container">
      <a href="#hero" class="header-brand">
        <div class="brand-logo-icon">
          <svg width="20" height="20" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.2" d="M9 17a2 2 0 11-4 0 2 2 0 014 0zM19 17a2 2 0 11-4 0 2 2 0 014 0z"></path><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.2" d="M13 16V6a1 1 0 00-1-1H4a1 1 0 00-1 1v10a1 1 0 001 1h1m8-1a1 1 0 01-1 1H9m4-1V8a1 1 0 011-1h2.586a1 1 0 01.707.293l3.414 3.414a1 1 0 01.293.707V16a1 1 0 01-1 1h-1m-6-1a1 1 0 001 1h1M5 17a2 2 0 104 0m-4 0a2 2 0 114 0m6 0a2 2 0 104 0m-4 0a2 2 0 114 0"></path></svg>
        </div>
        <span class="brand-product">Fleetsure</span>
        <span class="brand-badge">Fleet Compliance &amp; Challan Management</span>
      </a>
      <nav class="header-nav">
        <a href="#problem" class="nav-link">The Problem</a>
        <a href="#the-shift" class="nav-link">The Shift</a>
        <a href="#how-it-works" class="nav-link">How It Works</a>
        <a href="#fleet-at-a-glance" class="nav-link">Fleet View</a>
        <a href="#three-teams" class="nav-link">For Teams</a>
        <a href="#expiry-alerts" class="nav-link">Alerts</a>
        <a href="#challans" class="nav-link">Challans</a>
        <a href="#integrations" class="nav-link">Integrations</a>
        <a href="#faq" class="nav-link">FAQ</a>
      </nav>
      <div class="header-actions">
        <button class="btn btn-sm btn-brand" onclick="openDemoModal()">Book a demo</button>
      </div>
    </div>
  </header>
    """

def get_hero_html(C):
    eyebrow = get_c(C, '1. HERO', 'Eyebrow', 'Fleetsure by AIQoD')
    h1 = get_c(C, '1. HERO', 'H1', 'Know every vehicle is legal before it leaves the yard')
    subline = get_c(C, '1. HERO', 'Subline', '')
    primary_cta = get_c(C, '1. HERO', 'Primary CTA', 'Book a demo')
    secondary_cta = get_c(C, '1. HERO', 'Secondary CTA', 'Talk to our team')
    trust_line = get_c(C, '1. HERO', 'Trust line', 'Running with fleet operators today on the AIQoD platform.')

    return f"""
  <!-- =======================================================================
       1. HERO SECTION
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

      <!-- Hero Interactive Dashboard Console Card -->
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
              Fleetsure Live Fleet Compliance Console
            </div>
            <span class="example-data-tag">Example data</span>
          </div>

          <div class="hero-console-body">
            <!-- 4 Summary Metrics -->
            <div class="hero-metric-strip">
              <div class="hero-metric-box">
                <div class="label">Total Fleet</div>
                <div class="val">148</div>
              </div>
              <div class="hero-metric-box val-green">
                <div class="label">Valid &amp; Legal</div>
                <div class="val">136</div>
              </div>
              <div class="hero-metric-box val-amber">
                <div class="label">Expiring Soon</div>
                <div class="val">8</div>
              </div>
              <div class="hero-metric-box val-red">
                <div class="label">Challans Pending</div>
                <div class="val">₹38,500</div>
              </div>
            </div>

            <!-- Depot Filter Pills -->
            <div class="console-depot-filter">
              <button class="depot-filter-pill active" onclick="filterHeroTable('All')">All Depots (148)</button>
              <button class="depot-filter-pill" onclick="filterHeroTable('Pune')">Pune (42)</button>
              <button class="depot-filter-pill" onclick="filterHeroTable('Mumbai')">Mumbai (38)</button>
              <button class="depot-filter-pill" onclick="filterHeroTable('Delhi')">Delhi (36)</button>
              <button class="depot-filter-pill" onclick="filterHeroTable('Bengaluru')">Bengaluru (32)</button>
            </div>

            <!-- Vehicle List Table -->
            <table class="vehicle-table">
              <thead>
                <tr>
                  <th>Vehicle &amp; Depot</th>
                  <th>RC</th>
                  <th>Insurance</th>
                  <th>PUC</th>
                  <th>Tax</th>
                  <th>DL</th>
                  <th>Challan</th>
                </tr>
              </thead>
              <tbody id="hero-vehicle-rows">
                <tr onclick="inspectVehicle('MH-12-RN-4821', 'Pune North', '32ft Container', 'Valid', 'Expiring (7d)', 'Valid', 'Valid', 'Valid', '₹1,500 (1 pending)')">
                  <td>
                    <span class="veh-id">MH-12-RN-4821</span>
                    <span class="veh-sub">Pune North &middot; Owned</span>
                  </td>
                  <td><span class="status-pill valid">&bull; Valid</span></td>
                  <td><span class="status-pill expiring">&bull; 7 days</span></td>
                  <td><span class="status-pill valid">&bull; Valid</span></td>
                  <td><span class="status-pill valid">&bull; Valid</span></td>
                  <td><span class="status-pill valid">&bull; Valid</span></td>
                  <td><span class="status-pill expiring">₹1,500</span></td>
                </tr>
                <tr onclick="inspectVehicle('DL-01-AX-9942', 'NCR Hub', 'Tractor Trailer 40T', 'Valid', 'Valid', 'Expiring (12d)', 'Valid', 'Valid', 'Nil')">
                  <td>
                    <span class="veh-id">DL-01-AX-9942</span>
                    <span class="veh-sub">Delhi NCR &middot; Leased</span>
                  </td>
                  <td><span class="status-pill valid">&bull; Valid</span></td>
                  <td><span class="status-pill valid">&bull; Valid</span></td>
                  <td><span class="status-pill expiring">&bull; 12 days</span></td>
                  <td><span class="status-pill valid">&bull; Valid</span></td>
                  <td><span class="status-pill valid">&bull; Valid</span></td>
                  <td><span class="status-pill valid">Clear</span></td>
                </tr>
                <tr onclick="inspectVehicle('KA-05-MM-3310', 'Bengaluru South', '16T Multi-Axle', 'Valid', 'Valid', 'Valid', 'Valid', 'Expired (2d)', '₹3,000 (2 pending)')">
                  <td>
                    <span class="veh-id">KA-05-MM-3310</span>
                    <span class="veh-sub">Bengaluru &middot; Vendor</span>
                  </td>
                  <td><span class="status-pill valid">&bull; Valid</span></td>
                  <td><span class="status-pill valid">&bull; Valid</span></td>
                  <td><span class="status-pill valid">&bull; Valid</span></td>
                  <td><span class="status-pill valid">&bull; Valid</span></td>
                  <td><span class="status-pill expired">&bull; Expired</span></td>
                  <td><span class="status-pill expired">₹3,000</span></td>
                </tr>
                <tr onclick="inspectVehicle('MH-04-KF-1029', 'Navi Mumbai Port', '24ft Closed Body', 'Valid', 'Valid', 'Valid', 'Valid', 'Valid', 'Nil')">
                  <td>
                    <span class="veh-id">MH-04-KF-1029</span>
                    <span class="veh-sub">Mumbai Port &middot; Owned</span>
                  </td>
                  <td><span class="status-pill valid">&bull; Valid</span></td>
                  <td><span class="status-pill valid">&bull; Valid</span></td>
                  <td><span class="status-pill valid">&bull; Valid</span></td>
                  <td><span class="status-pill valid">&bull; Valid</span></td>
                  <td><span class="status-pill valid">&bull; Valid</span></td>
                  <td><span class="status-pill valid">Clear</span></td>
                </tr>
              </tbody>
            </table>

            <!-- Animated Alert Bar -->
            <div class="hero-slide-alert">
              <div class="alert-left">
                <svg width="16" height="16" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z"></path></svg>
                <span>Automated Alert: Insurance renewal due in 7 days (MH-12-RN-4821)</span>
              </div>
              <span class="example-data-tag">WhatsApp &amp; Email Sent</span>
            </div>

            <!-- Live State Challan Ticker -->
            <div class="hero-challan-strip">
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
