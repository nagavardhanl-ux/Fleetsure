# -*- coding: utf-8 -*-
"""
Fleetsure Sections 2-4 HTML (Streamlined & Intuitive)
"""

def get_problem_html(C):
    h2 = C['2. THE PROBLEM']['H2']['content']
    intro = C['2. THE PROBLEM']['Intro']['content']
    c1_h = C['2. THE PROBLEM']['Card 1 - Heading']['content']
    c1_c = C['2. THE PROBLEM']['Card 1 - Content']['content']
    c1_t = C['2. THE PROBLEM']['Card 1 - Tag']['content']
    
    c2_h = C['2. THE PROBLEM']['Card 2 - Heading']['content']
    c2_c = C['2. THE PROBLEM']['Card 2 - Content']['content']
    c2_t = C['2. THE PROBLEM']['Card 2 - Tag']['content']
    
    c3_h = C['2. THE PROBLEM']['Card 3 - Heading']['content']
    c3_c = C['2. THE PROBLEM']['Card 3 - Content']['content']
    c3_t = C['2. THE PROBLEM']['Card 3 - Tag']['content']

    return f"""
  <!-- =======================================================================
       2. THE PROBLEM SECTION
       ========================================================================= -->
  <section class="problem-section" id="problem">
    <div class="container">
      <div class="section-header">
        <h2>{h2}</h2>
        <p class="prose-760">{intro}</p>
      </div>

      <div class="problem-cards-grid">
        <!-- Card 1 -->
        <div class="problem-card">
          <div>
            <div class="card-icon-wrap">
              <svg width="24" height="24" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"></path></svg>
            </div>
            <h3>{c1_h}</h3>
            <p>{c1_c}</p>
          </div>
          <div class="cost-tag">
            <svg width="15" height="15" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z"></path></svg>
            {c1_t}
          </div>
        </div>

        <!-- Card 2 -->
        <div class="problem-card">
          <div>
            <div class="card-icon-wrap">
              <svg width="24" height="24" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z"></path><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 11a3 3 0 11-6 0 3 3 0 016 0z"></path></svg>
            </div>
            <h3>{c2_h}</h3>
            <p>{c2_c}</p>
          </div>
          <div class="cost-tag">
            <svg width="15" height="15" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13.875 18.825A10.05 10.05 0 0112 19c-4.478 0-8.268-2.943-9.543-7a9.97 9.97 0 011.563-3.029m5.858.908a3 3 0 114.243 4.243M9.878 9.878l4.242 4.242M9.88 9.88l-3.29-3.29m7.532 7.532l3.29 3.29M3 3l18 18"></path></svg>
            {c2_t}
          </div>
        </div>

        <!-- Card 3 -->
        <div class="problem-card">
          <div>
            <div class="card-icon-wrap">
              <svg width="24" height="24" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>
            </div>
            <h3>{c3_h}</h3>
            <p>{c3_c}</p>
          </div>
          <div class="cost-tag">
            <svg width="15" height="15" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 9V7a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2m2 4h10a2 2 0 002-2v-6a2 2 0 00-2-2H9a2 2 0 00-2 2v6a2 2 0 002 2zm7-5a2 2 0 11-4 0 2 2 0 014 0z"></path></svg>
            {c3_t}
          </div>
        </div>
      </div>
    </div>
  </section>
    """

def get_shift_html(C):
    h2 = C['3. THE SHIFT']['H2']['content']
    content = C['3. THE SHIFT']['Content']['content']
    
    rows_data = []
    for r in range(1, 6):
        raw = C['3. THE SHIFT'][f'Row {r}']['content']
        parts = [p.strip() for p in raw.split('|')]
        dim = parts[0]
        today = parts[1].replace('Today:', '').strip()
        fleetsure = parts[2].replace('Fleetsure:', '').strip()
        rows_data.append((dim, today, fleetsure))

    rows_html = ""
    for dim, today, fleetsure in rows_data:
        rows_html += f"""
          <div class="comp-row">
            <div class="comp-col-dim">{dim}</div>
            <div class="comp-col-today">
              <span class="cell-icon icon-cross"><svg width="16" height="16" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M6 18L18 6M6 6l12 12"></path></svg></span>
              <span>{today}</span>
            </div>
            <div class="comp-col-fleetsure">
              <span class="cell-icon icon-check"><svg width="16" height="16" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M5 13l4 4L19 7"></path></svg></span>
              <span>{fleetsure}</span>
            </div>
          </div>
        """

    return f"""
  <!-- =======================================================================
       3. THE SHIFT SECTION
       ========================================================================= -->
  <section class="bg-dark-band" id="the-shift">
    <div class="container shift-split">
      <div class="shift-left">
        <h2>{h2}</h2>
        <p>{content}</p>
      </div>

      <div class="shift-right">
        <div class="comparison-table-card">
          <div class="comp-header">
            <span>Dimension</span>
            <span>Today</span>
            <span>Fleetsure</span>
          </div>
          {rows_html}
        </div>
      </div>
    </div>
  </section>
    """

def get_how_it_works_html(C):
    h2 = C['4. HOW FLEETSURE WORKS']['H2']['content']
    static_line = C['4. HOW FLEETSURE WORKS']['Static line']['content']

    steps = [
        (
            1,
            C['4. HOW FLEETSURE WORKS']['Step 1 - Heading']['content'],
            C['4. HOW FLEETSURE WORKS']['Step 1 - Content']['content'],
            C['4. HOW FLEETSURE WORKS']['Step 1 - Panel']['content']
        ),
        (
            2,
            C['4. HOW FLEETSURE WORKS']['Step 2 - Heading']['content'],
            C['4. HOW FLEETSURE WORKS']['Step 2 - Content']['content'],
            C['4. HOW FLEETSURE WORKS']['Step 2 - Panel']['content']
        ),
        (
            3,
            C['4. HOW FLEETSURE WORKS']['Step 3 - Heading']['content'],
            C['4. HOW FLEETSURE WORKS']['Step 3 - Content']['content'],
            C['4. HOW FLEETSURE WORKS']['Step 3 - Panel']['content']
        ),
        (
            4,
            C['4. HOW FLEETSURE WORKS']['Step 4 - Heading']['content'],
            C['4. HOW FLEETSURE WORKS']['Step 4 - Content']['content'],
            C['4. HOW FLEETSURE WORKS']['Step 4 - Panel']['content']
        ),
        (
            5,
            C['4. HOW FLEETSURE WORKS']['Step 5 - Heading']['content'],
            C['4. HOW FLEETSURE WORKS']['Step 5 - Content']['content'],
            C['4. HOW FLEETSURE WORKS']['Step 5 - Panel']['content']
        )
    ]

    steps_btn_html = ""
    for num, heading, body, panel in steps:
        active_cls = "active" if num == 1 else ""
        steps_btn_html += f"""
          <div class="how-step {active_cls}" id="how-step-{num}" onclick="activateWorkflowStep({num})" role="button" tabindex="0">
            <div class="step-header-row">
              <span class="step-num-badge">{num}</span>
              <span class="step-title">{heading}</span>
            </div>
            <p class="step-body-desc">{body}</p>
          </div>
        """

    # Clean, intuitive visual preview panels
    screens_html = """
      <!-- Screen 1: Upload -->
      <div class="preview-screen-content active" id="how-screen-1">
        <div style="padding:24px 20px; background:var(--surface); border-radius:10px; border:1px dashed var(--line-hover); text-align:center; margin-bottom:20px;">
          <svg width="40" height="40" fill="none" stroke="var(--brand-light)" viewBox="0 0 24 24" style="margin:0 auto 12px;"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 16a4 4 0 01-.88-7.903A5 5 0 1115.9 6L16 6a5 5 0 011 9.9M15 13l-3-3m0 0l-3 3m3-3v12"></path></svg>
          <div style="font-weight:700; color:var(--heading); font-size:15px;">Upload Vehicle &amp; Driver Documents</div>
          <div style="font-size:12.5px; color:var(--muted); margin-top:4px;">Upload spreadsheets, scans, or PDFs once. Stored in encrypted cloud storage.</div>
        </div>
        <div style="font-size:13px; font-weight:700; color:var(--heading); margin-bottom:12px;">Tracked Document Records:</div>
        <div style="display:flex; flex-direction:column; gap:10px;">
          <div style="display:flex; justify-content:space-between; align-items:center; padding:11px 14px; background:var(--surface); border:1px solid var(--line); border-radius:6px; font-size:13px;">
            <span>📄 RC &middot; Vehicle Registration</span>
            <span class="status-pill valid">&bull; Stored &amp; Ready</span>
          </div>
          <div style="display:flex; justify-content:space-between; align-items:center; padding:11px 14px; background:var(--surface); border:1px solid var(--line); border-radius:6px; font-size:13px;">
            <span>📄 Commercial Insurance Policy</span>
            <span class="status-pill valid">&bull; Stored &amp; Ready</span>
          </div>
          <div style="display:flex; justify-content:space-between; align-items:center; padding:11px 14px; background:var(--surface); border:1px solid var(--line); border-radius:6px; font-size:13px;">
            <span>📄 Driver Licences &amp; PUC</span>
            <span class="status-pill valid">&bull; Stored &amp; Ready</span>
          </div>
        </div>
      </div>

      <!-- Screen 2: Alert Rules -->
      <div class="preview-screen-content" id="how-screen-2">
        <div style="font-weight:700; color:var(--heading); font-size:16px; margin-bottom:16px;">Standard Alert Cadence</div>
        <div style="display:grid; grid-template-columns:repeat(3, 1fr); gap:10px; margin-bottom:20px;">
          <div style="background:var(--surface); border:1px solid var(--line); padding:14px; border-radius:8px; text-align:center;">
            <div style="font-size:11px; color:var(--muted); text-transform:uppercase;">1st Reminder</div>
            <div style="font-size:20px; font-weight:800; color:#34D399; margin-top:4px;">30 Days</div>
          </div>
          <div style="background:var(--surface); border:1px solid var(--line); padding:14px; border-radius:8px; text-align:center;">
            <div style="font-size:11px; color:var(--muted); text-transform:uppercase;">2nd Reminder</div>
            <div style="font-size:20px; font-weight:800; color:#FBBF24; margin-top:4px;">15 Days</div>
          </div>
          <div style="background:var(--surface); border:1px solid var(--line); padding:14px; border-radius:8px; text-align:center;">
            <div style="font-size:11px; color:var(--muted); text-transform:uppercase;">Urgent Notice</div>
            <div style="font-size:20px; font-weight:800; color:#F87171; margin-top:4px;">7 Days</div>
          </div>
        </div>
        <div style="font-size:13px; font-weight:700; color:var(--heading); margin-bottom:10px;">Alert Delivery Channels:</div>
        <div style="display:flex; gap:10px; flex-wrap:wrap;">
          <span class="tool-pill" style="color:var(--heading);">✓ WhatsApp Reminders</span>
          <span class="tool-pill" style="color:var(--heading);">✓ Email Notifications</span>
          <span class="tool-pill" style="color:var(--heading);">✓ In-App Dashboard Alerts</span>
        </div>
      </div>

      <!-- Screen 3: Verification Tracking -->
      <div class="preview-screen-content" id="how-screen-3">
        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:16px;">
          <div style="font-weight:700; color:var(--heading); font-size:16px;">Government Record Checks</div>
          <span class="status-pill valid">&bull; Verified</span>
        </div>
        <div style="background:var(--surface); border:1px solid var(--line); border-radius:8px; padding:16px; margin-bottom:14px;">
          <div style="font-size:12px; color:var(--muted); margin-bottom:4px;">Official Registry Status:</div>
          <div style="font-size:16px; font-weight:700; color:var(--heading);">MH-12-RN-4821</div>
          <div style="font-size:12.5px; color:#34D399; margin-top:4px; font-weight:600;">✓ Authenticated against government records</div>
        </div>
        <div style="display:flex; flex-direction:column; gap:8px; font-size:12.5px;">
          <div style="display:flex; justify-content:space-between; padding:9px 12px; background:var(--surface); border-radius:6px;">
            <span>Registration (RC)</span>
            <span style="color:#34D399; font-weight:600;">Valid</span>
          </div>
          <div style="display:flex; justify-content:space-between; padding:9px 12px; background:var(--surface); border-radius:6px;">
            <span>Commercial Insurance</span>
            <span style="color:#FBBF24; font-weight:600;">Expires in 7 days</span>
          </div>
          <div style="display:flex; justify-content:space-between; padding:9px 12px; background:var(--surface); border-radius:6px;">
            <span>Driver Commercial DL</span>
            <span style="color:#34D399; font-weight:600;">Valid</span>
          </div>
        </div>
      </div>

      <!-- Screen 4: Expiry Alerts -->
      <div class="preview-screen-content" id="how-screen-4">
        <div style="font-weight:700; color:var(--heading); font-size:16px; margin-bottom:16px;">Automated Expiry Alert Dispatched</div>
        <div style="background:rgba(37,99,235,0.1); border:1px solid rgba(37,99,235,0.35); border-radius:8px; padding:18px; margin-bottom:16px;">
          <div style="display:flex; align-items:center; gap:8px; color:var(--brand-light); font-size:13.5px; font-weight:700; margin-bottom:8px;">
            <svg width="18" height="18" fill="currentColor" viewBox="0 0 24 24"><path d="M12.031 6.172c-3.181 0-5.767 2.586-5.768 5.766-.001 1.298.38 2.27 1.019 3.287l-.582 2.128 2.182-.573c.978.58 1.911.928 3.145.929 3.178 0 5.767-2.587 5.768-5.766.001-3.187-2.575-5.77-5.764-5.771zm3.392 8.244c-.144.405-.837.774-1.17.824-.312.045-.634.07-.996-.045-.506-.161-1.174-.473-2.023-1.218-.999-.877-1.636-1.954-1.802-2.222-.165-.268-.018-.413.118-.549.121-.121.268-.312.403-.468.135-.156.18-.268.27-.449.09-.18.045-.339-.023-.474-.067-.135-.6-1.444-.823-1.98-.217-.52-.438-.45-.6-.459-.156-.008-.337-.01-.518-.01-.18 0-.473.067-.72.339-.248.271-.945.926-.945 2.259 0 1.332.968 2.621 1.103 2.802.135.18 1.905 2.909 4.618 4.078.645.278 1.148.444 1.54.569.648.206 1.238.177 1.704.107.52-.078 1.6-1.654 1.825-1.294.225-.36.225-.668.158-.803-.067-.135-.248-.225-.518-.36z"></path></svg>
            WhatsApp Reminder &middot; Pune Depot Lead
          </div>
          <div style="font-size:13.5px; line-height:1.6; color:#F1F5F9;">
            "Reminder: Insurance for vehicle <strong>MH-12-RN-4821</strong> expires in 7 days (15-Nov-2026). Renewal quote is ready."
          </div>
        </div>
        <div style="font-size:13px; color:var(--muted); line-height:1.5;">
          Reminders go out automatically so renewals become a planned task instead of an emergency at the yard.
        </div>
      </div>

      <!-- Screen 5: Status & Challans -->
      <div class="preview-screen-content" id="how-screen-5">
        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:16px;">
          <div style="font-weight:700; color:var(--heading); font-size:16px;">Unified Compliance &amp; Challans</div>
          <span class="status-pill valid">&bull; 136 / 148 Legal</span>
        </div>
        <div style="display:grid; grid-template-columns:1fr 1fr; gap:12px; margin-bottom:16px;">
          <div style="background:var(--surface); border:1px solid var(--line); padding:14px; border-radius:8px;">
            <div style="font-size:11.5px; color:var(--muted); text-transform:uppercase;">Compliance Rate</div>
            <div style="font-size:22px; font-weight:800; color:#34D399; margin-top:2px;">97.3%</div>
          </div>
          <div style="background:var(--surface); border:1px solid var(--line); padding:14px; border-radius:8px;">
            <div style="font-size:11.5px; color:var(--muted); text-transform:uppercase;">Interstate Challans</div>
            <div style="font-size:22px; font-weight:800; color:#F87171; margin-top:2px;">₹38,500</div>
          </div>
        </div>
        <div style="font-size:12.5px; color:var(--muted);">
          Active and inactive vehicles are kept separate, so renewal effort goes exactly where it matters.
        </div>
      </div>
    """

    return f"""
  <!-- =======================================================================
       4. HOW FLEETSURE WORKS
       ========================================================================= -->
  <section class="bg-surface" id="how-it-works">
    <div class="container">
      <div class="how-intro prose-760">
        <h2>{h2}</h2>
        <p>{static_line}</p>
      </div>

      <div class="how-grid">
        <!-- Left Column: Phase Bar + Step List -->
        <div class="how-rail">
          <!-- Slim Grouping Bar for the 2 Workflow Stages -->
          <div class="how-phase-bar" id="how-phase-bar">
            <div class="how-phase-pill active" id="phase-pill-1" onclick="jumpToHowPhase(1)">
              <span>Set up once</span>
              <span class="phase-range">(Steps 1&ndash;2)</span>
            </div>
            <div class="how-phase-pill" id="phase-pill-2" onclick="jumpToHowPhase(2)">
              <span>Runs on its own</span>
              <span class="phase-range">(Steps 3&ndash;5)</span>
            </div>
          </div>

          <div class="how-step-list">
            {steps_btn_html}
          </div>
        </div>

        <!-- Right Column: Interactive UI Viewport -->
        <div class="how-preview-viewport">
          <div class="preview-topbar">
            <div class="window-controls">
              <span class="win-dot red"></span>
              <span class="win-dot yellow"></span>
              <span class="win-dot green"></span>
            </div>
            <div class="preview-screen-title" id="how-viewport-title">
              Step 1: Document upload and secure storage screen
            </div>
            <span class="example-data-tag">Example data</span>
          </div>
          {screens_html}
        </div>
      </div>
    </div>
  </section>
    """
