# -*- coding: utf-8 -*-
"""
Fleetsure Sections 5-9 HTML
"""

def get_glance_html(C):
    h2 = C['5. SEE THE WHOLE FLEET AT A GLANCE']['H2']['content']
    content = C['5. SEE THE WHOLE FLEET AT A GLANCE']['Content']['content']
    p1 = C['5. SEE THE WHOLE FLEET AT A GLANCE']['Point 1']['content']
    p2 = C['5. SEE THE WHOLE FLEET AT A GLANCE']['Point 2']['content']
    p3 = C['5. SEE THE WHOLE FLEET AT A GLANCE']['Point 3']['content']
    comp_sheet = C['5. SEE THE WHOLE FLEET AT A GLANCE']['Comparison - Tracked on a spreadsheet']['content']
    comp_fleetsure = C['5. SEE THE WHOLE FLEET AT A GLANCE']['Comparison - Tracked on Fleetsure']['content']
    img_alt = C['5. SEE THE WHOLE FLEET AT A GLANCE']['Image alt text']['content']

    return f"""
  <!-- =======================================================================
       5. SEE THE WHOLE FLEET AT A GLANCE
       ========================================================================= -->
  <section id="fleet-at-a-glance" aria-label="{img_alt}">
    <div class="container">
      <div class="glance-split">
        <!-- Left: Compliance Dashboard Screenshot Simulation -->
        <div class="product-preview-card" role="region" aria-label="{img_alt}">
          <div class="preview-topbar">
            <div class="window-controls">
              <span class="win-dot red"></span>
              <span class="win-dot yellow"></span>
              <span class="win-dot green"></span>
            </div>
            <div class="preview-screen-title">
              National Fleet Compliance Overview
            </div>
            <span class="example-data-tag">Example data</span>
          </div>

          <div style="padding:20px;">
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:16px;">
              <div>
                <div style="font-size:18px; font-weight:800; color:var(--heading);">148 Total Vehicles Tracked</div>
                <div style="font-size:12px; color:var(--muted); margin-top:2px;">5 Hubs &middot; Maharashtra, Delhi NCR, Karnataka, Tamil Nadu</div>
              </div>
              <span class="status-pill valid" style="font-size:12px; padding:4px 10px;">&bull; 97.3% Legal Fleet</span>
            </div>

            <!-- Hub status pills -->
            <div style="display:grid; grid-template-columns:repeat(5, 1fr); gap:8px; margin-bottom:16px; font-size:11.5px;">
              <div style="background:var(--surface); padding:8px; border-radius:6px; border:1px solid var(--line); text-align:center;">
                <div style="color:var(--muted); font-size:10px;">PUNE</div>
                <div style="font-weight:700; color:#34D399; margin-top:2px;">100% OK</div>
              </div>
              <div style="background:var(--surface); padding:8px; border-radius:6px; border:1px solid var(--line); text-align:center;">
                <div style="color:var(--muted); font-size:10px;">MUMBAI</div>
                <div style="font-weight:700; color:#FBBF24; margin-top:2px;">97.4%</div>
              </div>
              <div style="background:var(--surface); padding:8px; border-radius:6px; border:1px solid var(--line); text-align:center;">
                <div style="color:var(--muted); font-size:10px;">DELHI</div>
                <div style="font-weight:700; color:#34D399; margin-top:2px;">100% OK</div>
              </div>
              <div style="background:var(--surface); padding:8px; border-radius:6px; border:1px solid var(--line); text-align:center;">
                <div style="color:var(--muted); font-size:10px;">BLR</div>
                <div style="font-weight:700; color:#F87171; margin-top:2px;">93.8%</div>
              </div>
              <div style="background:var(--surface); padding:8px; border-radius:6px; border:1px solid var(--line); text-align:center;">
                <div style="color:var(--muted); font-size:10px;">CHENNAI</div>
                <div style="font-weight:700; color:#34D399; margin-top:2px;">100% OK</div>
              </div>
            </div>

            <div style="background:var(--surface); border:1px solid var(--line); border-radius:8px; padding:14px; font-size:12.5px;">
              <div style="display:flex; justify-content:space-between; margin-bottom:8px;">
                <span style="color:var(--muted);">All-India Challan Pool:</span>
                <span style="color:#F87171; font-weight:700;">₹38,500 Outstanding</span>
              </div>
              <div style="display:flex; justify-content:space-between;">
                <span style="color:var(--muted);">Upcoming Expiries (&lt;15 Days):</span>
                <span style="color:#FBBF24; font-weight:700;">4 Documents</span>
              </div>
            </div>
          </div>
        </div>

        <!-- Right: Text & Points -->
        <div class="glance-right">
          <h2>{h2}</h2>
          <p>{content}</p>

          <ul class="glance-bullets">
            <li class="glance-bullet-item">
              <div class="glance-bullet-icon">
                <svg width="14" height="14" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="3" d="M5 13l4 4L19 7"></path></svg>
              </div>
              <span>{p1}</span>
            </li>
            <li class="glance-bullet-item">
              <div class="glance-bullet-icon">
                <svg width="14" height="14" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="3" d="M5 13l4 4L19 7"></path></svg>
              </div>
              <span>{p2}</span>
            </li>
            <li class="glance-bullet-item">
              <div class="glance-bullet-icon">
                <svg width="14" height="14" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="3" d="M5 13l4 4L19 7"></path></svg>
              </div>
              <span>{p3}</span>
            </li>
          </ul>
        </div>
      </div>

      <!-- Comparison Strip Below -->
      <div class="comp-strip">
        <div class="comp-strip-item">
          <div class="strip-title spreadsheet">
            <svg width="16" height="16" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path></svg>
            Tracked on a spreadsheet
          </div>
          <p style="font-size:13.5px; line-height:1.55; color:var(--text);">{comp_sheet}</p>
        </div>
        <div class="comp-strip-item">
          <div class="strip-title fleetsure">
            <svg width="16" height="16" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path></svg>
            Tracked on Fleetsure
          </div>
          <p style="font-size:13.5px; line-height:1.55; color:#E2E8F0;">{comp_fleetsure}</p>
        </div>
      </div>
    </div>
  </section>
    """

def get_teams_html(C):
    h2 = C['6. BUILT FOR THREE TEAMS']['H2']['content']
    
    t1_l = C['6. BUILT FOR THREE TEAMS']['Tab 1 - Label']['content']
    t1_h = C['6. BUILT FOR THREE TEAMS']['Tab 1 - H3']['content']
    t1_c = C['6. BUILT FOR THREE TEAMS']['Tab 1 - Content']['content']
    t1_b = [C['6. BUILT FOR THREE TEAMS'][f'Tab 1 - Bullet {i}']['content'] for i in range(1, 5)]

    t2_l = C['6. BUILT FOR THREE TEAMS']['Tab 2 - Label']['content']
    t2_h = C['6. BUILT FOR THREE TEAMS']['Tab 2 - H3']['content']
    t2_c = C['6. BUILT FOR THREE TEAMS']['Tab 2 - Content']['content']
    t2_b = [C['6. BUILT FOR THREE TEAMS'][f'Tab 2 - Bullet {i}']['content'] for i in range(1, 5)]

    t3_l = C['6. BUILT FOR THREE TEAMS']['Tab 3 - Label']['content']
    t3_h = C['6. BUILT FOR THREE TEAMS']['Tab 3 - H3']['content']
    t3_c = C['6. BUILT FOR THREE TEAMS']['Tab 3 - Content']['content']
    t3_b = [C['6. BUILT FOR THREE TEAMS'][f'Tab 3 - Bullet {i}']['content'] for i in range(1, 5)]

    def render_bullets(bullets):
        out = ""
        for b in bullets:
            out += f"""
              <li class="tab-bullet">
                <span class="cell-icon icon-check"><svg width="16" height="16" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M5 13l4 4L19 7"></path></svg></span>
                <span>{b}</span>
              </li>
            """
        return out

    return f"""
  <!-- =======================================================================
       6. BUILT FOR THREE TEAMS
       ========================================================================= -->
  <section class="bg-surface" id="three-teams">
    <div class="container">
      <div class="section-header text-center prose-760" style="margin:0 auto 36px;">
        <h2>{h2}</h2>
      </div>

      <!-- Tab Buttons -->
      <div class="teams-tab-nav">
        <button class="team-tab-btn active" id="team-tab-btn-1" onclick="switchTeamTab(1)">{t1_l}</button>
        <button class="team-tab-btn" id="team-tab-btn-2" onclick="switchTeamTab(2)">{t2_l}</button>
        <button class="team-tab-btn" id="team-tab-btn-3" onclick="switchTeamTab(3)">{t3_l}</button>
      </div>

      <!-- Tab 1: Fleet managers -->
      <div class="team-tab-pane active" id="team-pane-1">
        <div class="tab-content-grid">
          <div>
            <h3>{t1_h}</h3>
            <p>{t1_c}</p>
            <ul class="tab-bullets">
              {render_bullets(t1_b)}
            </ul>
          </div>
          <div class="product-preview-card">
            <div class="preview-topbar">
              <span class="preview-screen-title">Fleet Dispatch Readiness Console</span>
              <span class="example-data-tag">Manager View</span>
            </div>
            <div style="padding:20px;">
              <div style="display:flex; justify-content:space-between; margin-bottom:12px; font-size:12px;">
                <span>Active Assets Ready: <strong>142 / 148</strong></span>
                <span style="color:#FBBF24; font-weight:600;">6 Inactive / Under Renewal</span>
              </div>
              <div style="background:var(--surface); border:1px solid var(--line); border-radius:8px; padding:12px; font-size:12px; margin-bottom:10px;">
                <div style="display:flex; justify-content:space-between; margin-bottom:4px;">
                  <span style="font-weight:700; color:var(--heading);">MH-12-RN-4821</span>
                  <span class="status-pill expiring">&bull; Insurance 7d</span>
                </div>
                <div style="color:var(--muted);">Driver: Ramesh Shinde &middot; Depot: Pune North</div>
              </div>
              <div style="background:var(--surface); border:1px solid var(--line); border-radius:8px; padding:12px; font-size:12px;">
                <div style="display:flex; justify-content:space-between; margin-bottom:4px;">
                  <span style="font-weight:700; color:var(--heading);">KA-05-MM-3310 (Vendor Leased)</span>
                  <span class="status-pill expired">&bull; Driver DL Lapsed</span>
                </div>
                <div style="color:var(--muted);">Carrier: Express Logistics &middot; Bengaluru</div>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- Tab 2: Operations and compliance teams -->
      <div class="team-tab-pane" id="team-pane-2">
        <div class="tab-content-grid">
          <div>
            <h3>{t2_h}</h3>
            <p>{t2_c}</p>
            <ul class="tab-bullets">
              {render_bullets(t2_b)}
            </ul>
          </div>
          <div class="product-preview-card">
            <div class="preview-topbar">
              <span class="preview-screen-title">Central Compliance &amp; Audit Vault</span>
              <span class="example-data-tag">Operations View</span>
            </div>
            <div style="padding:20px;">
              <div style="font-size:13px; font-weight:700; color:var(--heading); margin-bottom:12px;">Depot-Level Audit Readiness:</div>
              <div style="display:flex; flex-direction:column; gap:8px; font-size:12px;">
                <div style="display:flex; justify-content:space-between; padding:8px 12px; background:var(--surface); border-radius:6px;">
                  <span>Pune Depot (42 Vehicles)</span>
                  <span style="color:#34D399; font-weight:700;">100% Audit Ready</span>
                </div>
                <div style="display:flex; justify-content:space-between; padding:8px 12px; background:var(--surface); border-radius:6px;">
                  <span>Mumbai Trans-Port (38 Vehicles)</span>
                  <span style="color:#34D399; font-weight:700;">100% Audit Ready</span>
                </div>
                <div style="display:flex; justify-content:space-between; padding:8px 12px; background:var(--surface); border-radius:6px;">
                  <span>Delhi NCR Hub (36 Vehicles)</span>
                  <span style="color:#34D399; font-weight:700;">100% Audit Ready</span>
                </div>
                <div style="display:flex; justify-content:space-between; padding:8px 12px; background:var(--surface); border-radius:6px;">
                  <span>Bengaluru Logistics (32 Vehicles)</span>
                  <span style="color:#FBBF24; font-weight:700;">96.8% Audit Ready</span>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- Tab 3: Finance and leadership -->
      <div class="team-tab-pane" id="team-pane-3">
        <div class="tab-content-grid">
          <div>
            <h3>{t3_h}</h3>
            <p>{t3_c}</p>
            <ul class="tab-bullets">
              {render_bullets(t3_b)}
            </ul>
          </div>
          <div class="product-preview-card">
            <div class="preview-topbar">
              <span class="preview-screen-title">Executive Challan &amp; Penalty Analytics</span>
              <span class="example-data-tag">Finance View</span>
            </div>
            <div style="padding:20px;">
              <div style="display:grid; grid-template-columns:1fr 1fr; gap:10px; margin-bottom:14px;">
                <div style="background:var(--surface); padding:10px; border-radius:6px; border:1px solid var(--line);">
                  <div style="font-size:11px; color:var(--muted); text-transform:uppercase;">Monthly Challan Spend</div>
                  <div style="font-size:17px; font-weight:800; color:var(--heading); margin-top:4px;">₹54,200</div>
                </div>
                <div style="background:var(--surface); padding:10px; border-radius:6px; border:1px solid var(--line);">
                  <div style="font-size:11px; color:var(--muted); text-transform:uppercase;">Early Settlement Savings</div>
                  <div style="font-size:17px; font-weight:800; color:#34D399; margin-top:4px;">100% Court Penalties Avoided</div>
                </div>
              </div>
              <div style="font-size:12px; color:var(--muted); margin-bottom:6px;">Interstate Spend Breakdown:</div>
              <div style="display:flex; flex-direction:column; gap:6px; font-size:12px;">
                <div style="display:flex; justify-content:space-between; padding:6px 10px; background:var(--surface); border-radius:4px;">
                  <span>Maharashtra Highways (Speed Cameras)</span>
                  <span style="color:#F87171; font-weight:700;">₹18,500</span>
                </div>
                <div style="display:flex; justify-content:space-between; padding:6px 10px; background:var(--surface); border-radius:4px;">
                  <span>Delhi Border (Pollution / Non-Destined)</span>
                  <span style="color:#F87171; font-weight:700;">₹12,000</span>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
    """

def get_alerts_html(C):
    h2 = C['7. ALERTS BEFORE EXPIRY']['H2']['content']
    content = C['7. ALERTS BEFORE EXPIRY']['Content']['content']
    label = C['7. ALERTS BEFORE EXPIRY']['Interactive label']['content']

    return f"""
  <!-- =======================================================================
       7. ALERTS BEFORE EXPIRY (INTERACTIVE TIMELINE)
       ========================================================================= -->
  <section class="bg-dark-band" id="expiry-alerts">
    <div class="container">
      <div class="timeline-widget">
        <div class="timeline-split">
          <!-- Interactive Timeline Left -->
          <div>
            <div style="display:flex; justify-content:space-between; align-items:center;">
              <span style="font-size:13px; font-weight:700; color:var(--heading); text-transform:uppercase; letter-spacing:0.05em;">{label}</span>
              <span class="example-data-tag">Interactive Simulation</span>
            </div>

            <label for="expiry-doc-type" style="font-size:12px; color:var(--muted); display:block; margin-top:16px;">Select Document Type to Track:</label>
            <select id="expiry-doc-type" class="form-control" style="margin-top:6px;" onchange="updateAlertSimulation()">
              <option value="Commercial Vehicle Insurance (ICICI Lombard)">Commercial Vehicle Insurance</option>
              <option value="Pollution Under Control (PUC)">Pollution Under Control (PUC)</option>
              <option value="National Goods Permit">National Goods Permit</option>
              <option value="Heavy Transport Road Tax">Heavy Transport Road Tax</option>
              <option value="Driver Commercial Heavy Licence">Driver Commercial Licence</option>
            </select>

            <!-- Channel selector tags -->
            <div class="alert-channel-selector">
              <span class="channel-tag active" id="chan-all" onclick="selectAlertChannel('All')">All Channels</span>
              <span class="channel-tag" id="chan-whatsapp" onclick="selectAlertChannel('WhatsApp')">WhatsApp</span>
              <span class="channel-tag" id="chan-email" onclick="selectAlertChannel('Email')">Email</span>
              <span class="channel-tag" id="chan-inapp" onclick="selectAlertChannel('In-App')">In-App Alert</span>
            </div>

            <!-- Timeline Visual -->
            <div class="timeline-bar-wrap">
              <div class="timeline-track">
                <div class="timeline-fill" id="alert-timeline-fill"></div>
                <!-- Marker 30d -->
                <div class="timeline-marker" style="left: 33%;" onclick="selectMarker(30)">
                  <span class="marker-dot"></span>
                  <span class="marker-label">30 Days</span>
                </div>
                <!-- Marker 15d -->
                <div class="timeline-marker" style="left: 66%;" onclick="selectMarker(15)">
                  <span class="marker-dot"></span>
                  <span class="marker-label">15 Days</span>
                </div>
                <!-- Marker 7d -->
                <div class="timeline-marker active" style="left: 88%;" onclick="selectMarker(7)">
                  <span class="marker-dot" style="background:#EF4444; border-color:#FFF;"></span>
                  <span class="marker-label" style="color:#F87171; border-color:#EF4444;">7 Days</span>
                </div>
              </div>
            </div>

            <!-- Simulated Dispatched Message Preview -->
            <div class="mock-alert-bubble" id="mock-alert-box">
              <div style="font-size:11px; text-transform:uppercase; color:var(--brand-light); font-weight:700; margin-bottom:6px;" id="mock-alert-channel-title">
                WhatsApp Dispatch &middot; 7-Day Pre-Expiry Reminder
              </div>
              <div style="font-size:13px; color:#F1F5F9; line-height:1.5;" id="mock-alert-text">
                "Fleetsure Alert: Vehicle <strong>MH-12-RN-4821</strong> Insurance policy expires on <strong>15-Nov-2026</strong> (7 days remaining). Renewal quotation prepared. Tap to approve."
              </div>
            </div>
          </div>

          <!-- Right Column Copy -->
          <div>
            <h2>{h2}</h2>
            <p>{content}</p>
          </div>
        </div>
      </div>
    </div>
  </section>
    """

def get_challans_html(C):
    h2 = C['8. CHALLANS ON ONE SCREEN']['H2']['content']
    content = C['8. CHALLANS ON ONE SCREEN']['Content']['content']
    content2 = C['8. CHALLANS ON ONE SCREEN']['Content 2']['content']

    return f"""
  <!-- =======================================================================
       8. CHALLANS ON ONE SCREEN
       ========================================================================= -->
  <section id="challans">
    <div class="container challans-split">
      <div class="challans-left">
        <h2>{h2}</h2>
        <p style="margin-bottom:16px;">{content}</p>
        <p>{content2}</p>
      </div>

      <div class="challans-right">
        <div class="challan-console">
          <div class="preview-topbar">
            <div class="preview-screen-title">
              <svg width="15" height="15" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2"></path></svg>
              Multi-State e-Challan Central Pool
            </div>
            <span class="example-data-tag">Example data</span>
          </div>

          <!-- State Filter Buttons -->
          <div class="challan-state-nav">
            <button class="challan-state-btn active" onclick="filterChallanState('All')">All States (14)</button>
            <button class="challan-state-btn" onclick="filterChallanState('MH')">MH (6)</button>
            <button class="challan-state-btn" onclick="filterChallanState('DL')">DL (4)</button>
            <button class="challan-state-btn" onclick="filterChallanState('KA')">KA (3)</button>
            <button class="challan-state-btn" onclick="filterChallanState('TN')">TN (1)</button>
          </div>

          <!-- Challans Table -->
          <div style="max-height:280px; overflow-y:auto;">
            <table class="challan-table">
              <thead>
                <tr>
                  <th>Vehicle</th>
                  <th>State &amp; Offense</th>
                  <th>Date</th>
                  <th>Amount</th>
                  <th>Status</th>
                </tr>
              </thead>
              <tbody id="challan-rows-body">
                <tr data-state="MH">
                  <td><strong>MH-12-RN-4821</strong><br><span style="color:var(--muted); font-size:10.5px;">Owned &middot; Pune</span></td>
                  <td>Maharashtra Highway<br><span style="color:var(--muted); font-size:10.5px;">Over-speeding (NH-48)</span></td>
                  <td>24 Oct 2026</td>
                  <td style="color:#F87171; font-weight:700;">₹1,500</td>
                  <td><span class="status-pill expiring">Pending</span></td>
                </tr>
                <tr data-state="MH">
                  <td><strong>MH-04-KF-1029</strong><br><span style="color:var(--muted); font-size:10.5px;">Owned &middot; Mumbai</span></td>
                  <td>Mumbai Eastern Freeway<br><span style="color:var(--muted); font-size:10.5px;">Lane Discipline</span></td>
                  <td>22 Oct 2026</td>
                  <td style="color:#F87171; font-weight:700;">₹1,000</td>
                  <td><span class="status-pill expiring">Pending</span></td>
                </tr>
                <tr data-state="DL">
                  <td><strong>DL-01-AX-9942</strong><br><span style="color:var(--muted); font-size:10.5px;">Leased &middot; Delhi</span></td>
                  <td>Delhi Outer Ring Road<br><span style="color:var(--muted); font-size:10.5px;">Red Light Camera</span></td>
                  <td>19 Oct 2026</td>
                  <td style="color:#F87171; font-weight:700;">₹2,000</td>
                  <td><span class="status-pill expiring">Pending</span></td>
                </tr>
                <tr data-state="KA">
                  <td><strong>KA-05-MM-3310</strong><br><span style="color:var(--muted); font-size:10.5px;">Vendor &middot; Bengaluru</span></td>
                  <td>Hosur Road Toll Hub<br><span style="color:var(--muted); font-size:10.5px;">Non-display of Permit</span></td>
                  <td>16 Oct 2026</td>
                  <td style="color:#F87171; font-weight:700;">₹2,000</td>
                  <td><span class="status-pill expiring">Pending</span></td>
                </tr>
                <tr data-state="TN">
                  <td><strong>TN-09-CQ-7712</strong><br><span style="color:var(--muted); font-size:10.5px;">Owned &middot; Chennai</span></td>
                  <td>Chennai Bypass Road<br><span style="color:var(--muted); font-size:10.5px;">Excess Axle Load</span></td>
                  <td>12 Oct 2026</td>
                  <td style="color:#F87171; font-weight:700;">₹3,000</td>
                  <td><span class="status-pill expiring">Pending</span></td>
                </tr>
              </tbody>
            </table>
          </div>

          <!-- Challan Running Total Footer -->
          <div class="challan-total-footer">
            <div>
              <span style="color:var(--muted);">Fleet Running Total:</span>
              <span class="challan-total-sum" id="challan-total-display">₹38,500</span>
            </div>
            <button class="btn btn-sm btn-outline" onclick="simulateSettleChallans()">Settle &amp; Clear Selected</button>
          </div>
        </div>
      </div>
    </div>
  </section>
    """

def get_systems_html(C):
    h2 = C['9. WORKS WITH YOUR SYSTEMS AND YOUR TEAM']['H2']['content']
    content = C['9. WORKS WITH YOUR SYSTEMS AND YOUR TEAM']['Content']['content']
    top_block = C['9. WORKS WITH YOUR SYSTEMS AND YOUR TEAM']['Diagram - Top block']['content']
    bot_block = C['9. WORKS WITH YOUR SYSTEMS AND YOUR TEAM']['Diagram - Bottom block']['content']
    caption = C['9. WORKS WITH YOUR SYSTEMS AND YOUR TEAM']['Caption']['content']

    return f"""
  <!-- =======================================================================
       9. WORKS WITH YOUR SYSTEMS AND YOUR TEAM
       ========================================================================= -->
  <section class="bg-surface" id="integrations">
    <div class="container">
      <div class="section-header text-center prose-760" style="margin:0 auto 40px;">
        <h2>{h2}</h2>
        <p>{content}</p>
      </div>

      <!-- Layered Diagram -->
      <div class="integration-diagram">
        <!-- Top: Fleetsure -->
        <div class="diagram-top-block">
          <div class="eyebrow" style="margin-bottom:6px;">AIQoD Agent Engine</div>
          <div class="diagram-top-title">{top_block}</div>
          <p style="font-size:13.5px; color:var(--text); max-width:580px; margin:0 auto;">
            Reads document records &amp; government portals without disrupting ongoing daily depot operations.
          </p>
        </div>

        <!-- Connector -->
        <div class="diagram-connector">
          <div class="diagram-connector-line"></div>
          <svg width="18" height="18" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 14l-7 7m0 0l-7-7m7 7V3"></path></svg>
        </div>

        <!-- Bottom: Current systems -->
        <div class="diagram-bottom-block">
          <div style="font-size:16px; font-weight:700; color:var(--heading);">{bot_block}</div>
          <div class="tools-pill-grid">
            <span class="tool-pill">GPS &amp; Telematics Suites</span>
            <span class="tool-pill">ERP &amp; SAP Systems</span>
            <span class="tool-pill">Cloud Document Stores</span>
            <span class="tool-pill">WhatsApp &amp; SMS Gateways</span>
            <span class="tool-pill">Spreadsheets &amp; Folders</span>
          </div>
        </div>

        <div class="diagram-caption">
          <svg width="16" height="16" fill="none" stroke="currentColor" viewBox="0 0 24 24" style="display:inline; vertical-align:middle; margin-right:4px;"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M5 13l4 4L19 7"></path></svg>
          {caption}
        </div>
        <div style="margin-top:16px;">
          <a href="/platform" class="text-link" style="color:var(--brand-light); text-decoration:none; font-weight:600; font-size:14px;">See how Fleetsure fits your systems &rarr;</a>
        </div>
      </div>

      <!-- 3 Integration Cards -->
      <div class="integration-cards-grid">
        <div class="integration-card">
          <h4>Telematics &amp; Fleet Systems</h4>
          <p>Sits alongside GPS tools (Fleetx, FleetOnGo, Teletrac) without needing hardware changes or sensor reinstallation.</p>
        </div>
        <div class="integration-card">
          <h4>Spreadsheets &amp; Document Vaults</h4>
          <p>Ingests existing Excel sheets, scanned PDFs, Google Drive and SharePoint folders in minutes.</p>
        </div>
        <div class="integration-card">
          <h4>Enterprise ERP &amp; Messaging</h4>
          <p>Dispatches compliance alerts straight into WhatsApp, SMS and email, with audit exports for finance.</p>
        </div>
      </div>
    </div>
  </section>
    """
