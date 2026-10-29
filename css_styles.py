# -*- coding: utf-8 -*-
"""
Fleetsure Design System CSS
Adapted from the Foresprint reference design with tailored Fleetsure royal blue, emerald green, amber & crimson tokens.
"""

def get_css():
    return """
    :root {
      --brand:            #2563EB;
      --brand-glow:       rgba(37, 99, 235, 0.35);
      --brand-subtle:     rgba(37, 99, 235, 0.12);
      --brand-light:      #60A5FA;
      --brand-dark:       #1D4ED8;
      --bg:               #080C16;
      --surface:          #0B1221;
      --surface-elevated: #111A30;
      --surface-card:     #0E1626;
      --surface-card-hover: #142038;
      --text:             #9AA1AC;
      --heading:          #FFFFFF;
      --muted:            rgba(154, 161, 172, 0.65);
      --line:             rgba(154, 161, 172, 0.14);
      --line-hover:       rgba(154, 161, 172, 0.32);
      
      --accent-cyan:      #06B6D4;
      --accent-green:     #10B981;
      --accent-green-bg:  rgba(16, 185, 129, 0.12);
      --accent-green-border: rgba(16, 185, 129, 0.3);
      --accent-amber:     #F59E0B;
      --accent-amber-bg:  rgba(245, 158, 11, 0.12);
      --accent-amber-border: rgba(245, 158, 11, 0.3);
      --accent-red:       #EF4444;
      --accent-red-bg:    rgba(239, 68, 68, 0.12);
      --accent-red-border: rgba(239, 68, 68, 0.3);
      --accent-purple:    #8B5CF6;
      --accent-blue:      #3B82F6;
    }

    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }

    html {
      scroll-behavior: smooth;
    }

    body {
      background-color: var(--bg);
      color: var(--text);
      font-family: system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
      font-size: 16px;
      line-height: 1.6;
      -webkit-font-smoothing: antialiased;
      overflow-x: hidden;
    }

    /* Container */
    .container {
      max-width: 1200px;
      margin: 0 auto;
      padding: 0 24px;
    }

    .prose-760 {
      max-width: 760px;
    }

    .prose-680 {
      max-width: 680px;
      margin: 0 auto;
    }

    .text-center {
      text-align: center;
    }

    /* Typography */
    h1, h2, h3, h4, h5, h6 {
      color: var(--heading);
      line-height: 1.25;
      font-weight: 700;
    }

    h1 {
      font-size: 44px;
      letter-spacing: -0.025em;
    }

    h2 {
      font-size: 34px;
      letter-spacing: -0.02em;
      margin-bottom: 16px;
    }

    h3 {
      font-size: 20px;
      letter-spacing: -0.01em;
      margin-bottom: 12px;
    }

    p {
      color: var(--text);
    }

    /* Common Buttons */
    .btn {
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 8px;
      padding: 12px 24px;
      border-radius: 8px;
      font-weight: 600;
      font-size: 14.5px;
      text-decoration: none;
      transition: all 0.2s ease;
      cursor: pointer;
      border: 1px solid transparent;
      white-space: nowrap;
    }

    .btn-brand {
      background: var(--brand);
      color: #FFFFFF;
      box-shadow: 0 0 24px var(--brand-glow);
    }

    .btn-brand:hover {
      background: var(--brand-light);
      box-shadow: 0 0 32px var(--brand-glow);
      transform: translateY(-1px);
      color: #FFFFFF;
    }

    .btn-outline {
      background: rgba(255, 255, 255, 0.03);
      border-color: var(--line-hover);
      color: var(--heading);
    }

    .btn-outline:hover {
      background: rgba(255, 255, 255, 0.08);
      border-color: var(--heading);
      transform: translateY(-1px);
    }

    .btn-sm {
      padding: 8px 18px;
      font-size: 13.5px;
      border-radius: 6px;
    }

    .btn-contrast-solid {
      background: #FFFFFF;
      color: #080C16;
      font-weight: 700;
    }

    .btn-contrast-solid:hover {
      background: #F1F5F9;
      transform: translateY(-1px);
    }

    .btn-contrast-outline {
      background: transparent;
      border: 1px solid rgba(255, 255, 255, 0.35);
      color: #FFFFFF;
    }

    .btn-contrast-outline:hover {
      background: rgba(255, 255, 255, 0.1);
      border-color: #FFFFFF;
    }

    /* Eyebrow & Badges */
    .eyebrow {
      display: inline-flex;
      align-items: center;
      gap: 8px;
      font-size: 12.5px;
      font-weight: 600;
      text-transform: uppercase;
      letter-spacing: 0.08em;
      color: var(--brand-light);
      margin-bottom: 16px;
    }

    .eyebrow-dot {
      width: 8px;
      height: 8px;
      border-radius: 50%;
      background: var(--accent-green);
      box-shadow: 0 0 10px var(--accent-green);
      animation: pulse 2s infinite;
    }

    @keyframes pulse {
      0% { transform: scale(0.95); box-shadow: 0 0 0 0 rgba(16, 185, 129, 0.7); }
      70% { transform: scale(1.05); box-shadow: 0 0 0 8px rgba(16, 185, 129, 0); }
      100% { transform: scale(0.95); box-shadow: 0 0 0 0 rgba(16, 185, 129, 0); }
    }

    .example-data-tag {
      display: inline-block;
      font-size: 11px;
      font-weight: 600;
      text-transform: uppercase;
      letter-spacing: 0.06em;
      padding: 3px 8px;
      background: rgba(154, 161, 172, 0.1);
      border: 1px solid var(--line);
      border-radius: 4px;
      color: var(--muted);
    }

    /* Header */
    .site-header {
      position: sticky;
      top: 0;
      z-index: 100;
      backdrop-filter: blur(16px);
      background: rgba(8, 12, 22, 0.88);
      border-bottom: 1px solid var(--line);
    }

    .header-container {
      display: flex;
      align-items: center;
      justify-content: space-between;
      height: 72px;
    }

    .header-brand {
      display: flex;
      align-items: center;
      gap: 12px;
      text-decoration: none;
    }

    .brand-logo-icon {
      width: 32px;
      height: 32px;
      border-radius: 8px;
      background: linear-gradient(135deg, var(--brand), #3B82F6);
      display: flex;
      align-items: center;
      justify-content: center;
      color: #FFF;
      box-shadow: 0 0 14px var(--brand-glow);
    }

    .brand-product {
      font-size: 21px;
      font-weight: 800;
      color: var(--heading);
      letter-spacing: -0.02em;
    }

    .brand-product span {
      color: var(--brand-light);
    }

    .brand-badge {
      font-size: 11.5px;
      padding: 3px 9px;
      border-radius: 999px;
      background: var(--brand-subtle);
      color: var(--brand-light);
      border: 1px solid rgba(37, 99, 235, 0.3);
      font-weight: 600;
    }

    .header-nav {
      display: flex;
      align-items: center;
      gap: 24px;
    }

    .nav-link {
      color: var(--text);
      text-decoration: none;
      font-size: 14px;
      font-weight: 500;
      transition: color 0.15s;
    }

    .nav-link:hover {
      color: var(--heading);
    }

    .header-actions {
      display: flex;
      align-items: center;
      gap: 16px;
    }

    /* Section Base */
    section {
      padding: 90px 0;
      position: relative;
    }

    .bg-surface {
      background-color: var(--surface);
    }

    .bg-dark-band {
      background-color: #060911;
      border-top: 1px solid var(--line);
      border-bottom: 1px solid var(--line);
    }

    .section-header {
      margin-bottom: 48px;
    }

    .section-header h2 {
      margin-bottom: 14px;
    }

    .section-header p {
      font-size: 17px;
      line-height: 1.6;
      color: var(--text);
    }

    /* 1. HERO */
    .hero-section {
      padding: 80px 0 100px;
      background: radial-gradient(circle at 75% 25%, rgba(37, 99, 235, 0.12) 0%, transparent 60%);
    }

    .hero-split {
      display: grid;
      grid-template-columns: 1fr 1.15fr;
      gap: 48px;
      align-items: center;
    }

    .hero-title {
      font-size: 44px;
      line-height: 1.15;
      font-weight: 800;
      color: var(--heading);
      margin-bottom: 20px;
      letter-spacing: -0.03em;
    }

    .hero-product-title {
      display: block;
      font-size: 15px;
      text-transform: uppercase;
      letter-spacing: 0.1em;
      color: var(--brand-light);
      margin-bottom: 8px;
      font-weight: 700;
    }

    .hero-tagline-title {
      display: block;
    }

    .hero-left p {
      font-size: 17px;
      line-height: 1.65;
      color: var(--text);
      margin-bottom: 28px;
    }

    .btn-group {
      display: flex;
      gap: 14px;
      align-items: center;
      margin-bottom: 24px;
      flex-wrap: wrap;
    }

    .hero-trust {
      font-size: 13.5px;
      color: var(--muted);
      display: flex;
      align-items: center;
      gap: 10px;
    }

    /* Product Preview Console Card */
    .product-preview-card {
      background: var(--surface-card);
      border: 1px solid var(--line);
      border-radius: 12px;
      overflow: hidden;
      box-shadow: 0 24px 60px rgba(0, 0, 0, 0.6), 0 0 30px var(--brand-glow);
      transition: border-color 0.2s ease;
    }

    .product-preview-card:hover {
      border-color: var(--line-hover);
    }

    .preview-topbar {
      background: var(--surface);
      padding: 12px 18px;
      border-bottom: 1px solid var(--line);
      display: flex;
      align-items: center;
      justify-content: space-between;
    }

    .window-controls {
      display: flex;
      gap: 7px;
    }

    .win-dot {
      width: 10px;
      height: 10px;
      border-radius: 50%;
    }

    .win-dot.red { background: #FF5F56; }
    .win-dot.yellow { background: #FFBD2E; }
    .win-dot.green { background: #27C93F; }

    .preview-screen-title {
      font-size: 12.5px;
      font-weight: 600;
      color: var(--heading);
      letter-spacing: -0.01em;
      display: flex;
      align-items: center;
      gap: 8px;
    }

    /* Hero Dashboard Console Inside */
    .hero-console-body {
      padding: 20px;
    }

    .hero-metric-strip {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 12px;
      margin-bottom: 18px;
    }

    .hero-metric-box {
      background: var(--surface);
      border: 1px solid var(--line);
      border-radius: 8px;
      padding: 12px 14px;
    }

    .hero-metric-box .label {
      font-size: 11px;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      color: var(--muted);
      margin-bottom: 4px;
    }

    .hero-metric-box .val {
      font-size: 19px;
      font-weight: 700;
      color: var(--heading);
    }

    .hero-metric-box.val-green .val { color: var(--accent-green); }
    .hero-metric-box.val-amber .val { color: var(--accent-amber); }
    .hero-metric-box.val-red .val { color: var(--accent-red); }

    .console-depot-filter {
      display: flex;
      gap: 6px;
      margin-bottom: 14px;
      overflow-x: auto;
      padding-bottom: 2px;
    }

    .depot-filter-pill {
      font-size: 12px;
      padding: 5px 12px;
      border-radius: 6px;
      background: var(--surface);
      border: 1px solid var(--line);
      color: var(--text);
      cursor: pointer;
      transition: all 0.15s;
      white-space: nowrap;
    }

    .depot-filter-pill.active, .depot-filter-pill:hover {
      background: var(--brand);
      color: #FFF;
      border-color: var(--brand-light);
    }

    .vehicle-table {
      width: 100%;
      border-collapse: collapse;
      font-size: 12.5px;
    }

    .vehicle-table th {
      text-align: left;
      padding: 8px 10px;
      color: var(--muted);
      border-bottom: 1px solid var(--line);
      font-weight: 600;
      text-transform: uppercase;
      font-size: 10.5px;
      letter-spacing: 0.04em;
    }

    .vehicle-table td {
      padding: 10px 10px;
      border-bottom: 1px solid rgba(154, 161, 172, 0.08);
      color: var(--text);
      vertical-align: middle;
    }

    .vehicle-table tr:hover td {
      background: rgba(37, 99, 235, 0.06);
      cursor: pointer;
    }

    .veh-id {
      font-weight: 700;
      color: var(--heading);
      letter-spacing: 0.02em;
    }

    .veh-sub {
      font-size: 11px;
      color: var(--muted);
      display: block;
    }

    /* Status Pills */
    .status-pill {
      display: inline-flex;
      align-items: center;
      gap: 5px;
      font-size: 11px;
      font-weight: 600;
      padding: 3px 8px;
      border-radius: 999px;
      white-space: nowrap;
    }

    .status-pill.valid {
      background: var(--accent-green-bg);
      color: #34D399;
      border: 1px solid var(--accent-green-border);
    }

    .status-pill.expiring {
      background: var(--accent-amber-bg);
      color: #FBBF24;
      border: 1px solid var(--accent-amber-border);
    }

    .status-pill.expired {
      background: var(--accent-red-bg);
      color: #F87171;
      border: 1px solid var(--accent-red-border);
    }

    /* Slide-in Alert in Hero */
    .hero-slide-alert {
      margin-top: 14px;
      background: rgba(245, 158, 11, 0.1);
      border: 1px solid rgba(245, 158, 11, 0.35);
      border-radius: 8px;
      padding: 10px 14px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      font-size: 12px;
      animation: alertSlide 4s infinite alternate ease-in-out;
    }

    @keyframes alertSlide {
      0% { transform: translateY(0); }
      100% { transform: translateY(-2px); box-shadow: 0 4px 14px rgba(245, 158, 11, 0.15); }
    }

    .alert-left {
      display: flex;
      align-items: center;
      gap: 8px;
      color: #FCD34D;
      font-weight: 500;
    }

    .hero-challan-strip {
      margin-top: 14px;
      padding: 9px 14px;
      background: var(--surface);
      border-radius: 8px;
      border: 1px solid var(--line);
      display: flex;
      align-items: center;
      justify-content: space-between;
      font-size: 11.5px;
    }

    .challan-states-row {
      display: flex;
      gap: 8px;
    }

    .state-chip {
      background: rgba(154, 161, 172, 0.1);
      border-radius: 4px;
      padding: 2px 7px;
      color: var(--heading);
      font-weight: 600;
    }

    /* 2. THE PROBLEM */
    .problem-cards-grid {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 24px;
    }

    .problem-card {
      background: var(--surface-card);
      border: 1px solid var(--line);
      border-radius: 12px;
      padding: 32px 28px;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      transition: all 0.2s ease;
    }

    .problem-card:hover {
      border-color: var(--line-hover);
      transform: translateY(-2px);
    }

    .card-icon-wrap {
      width: 48px;
      height: 48px;
      border-radius: 10px;
      background: rgba(239, 68, 68, 0.1);
      border: 1px solid rgba(239, 68, 68, 0.2);
      display: flex;
      align-items: center;
      justify-content: center;
      color: var(--accent-red);
      margin-bottom: 20px;
    }

    .problem-card h3 {
      font-size: 19px;
      margin-bottom: 12px;
    }

    .problem-card p {
      font-size: 14.5px;
      line-height: 1.6;
      color: var(--text);
      margin-bottom: 24px;
    }

    .cost-tag {
      display: inline-flex;
      align-items: center;
      gap: 8px;
      padding: 6px 12px;
      border-radius: 6px;
      background: rgba(239, 68, 68, 0.08);
      border: 1px solid rgba(239, 68, 68, 0.22);
      color: #F87171;
      font-size: 12px;
      font-weight: 600;
      width: fit-content;
    }

    /* 3. THE SHIFT */
    .shift-split {
      display: grid;
      grid-template-columns: 1fr 1.3fr;
      gap: 48px;
      align-items: center;
    }

    .shift-left h2 {
      margin-bottom: 18px;
    }

    .shift-left p {
      font-size: 16.5px;
      line-height: 1.65;
    }

    .comparison-table-card {
      background: var(--surface-card);
      border: 1px solid var(--line);
      border-radius: 12px;
      overflow: hidden;
      box-shadow: 0 16px 40px rgba(0, 0, 0, 0.4);
    }

    .comp-header {
      display: grid;
      grid-template-columns: 1.2fr 1.4fr 1.6fr;
      padding: 14px 20px;
      background: var(--surface);
      border-bottom: 1px solid var(--line);
      font-size: 12px;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      color: var(--muted);
    }

    .comp-row {
      display: grid;
      grid-template-columns: 1.2fr 1.4fr 1.6fr;
      padding: 16px 20px;
      border-bottom: 1px solid var(--line);
      font-size: 13.5px;
      align-items: center;
      gap: 12px;
    }

    .comp-row:last-child {
      border-bottom: none;
    }

    .comp-col-dim {
      font-weight: 600;
      color: var(--heading);
    }

    .comp-col-today {
      color: var(--muted);
      display: flex;
      align-items: flex-start;
      gap: 8px;
      line-height: 1.4;
    }

    .comp-col-fleetsure {
      color: #E2E8F0;
      display: flex;
      align-items: flex-start;
      gap: 8px;
      line-height: 1.4;
      font-weight: 500;
    }

    .cell-icon {
      flex-shrink: 0;
      margin-top: 2px;
    }

    .icon-cross { color: #EF4444; }
    .icon-check { color: #10B981; }

    /* 4. HOW FLEETSURE WORKS */
    .how-intro {
      margin-bottom: 40px;
    }

    .how-grid {
      display: grid;
      grid-template-columns: 1fr 1.15fr;
      gap: 40px;
      align-items: flex-start;
    }

    .how-phase-bar {
      display: flex;
      gap: 8px;
      margin-bottom: 24px;
      padding: 4px;
      background: var(--surface-card);
      border: 1px solid var(--line);
      border-radius: 8px;
    }

    .how-phase-pill {
      flex: 1;
      padding: 8px 14px;
      border-radius: 6px;
      font-size: 13px;
      font-weight: 600;
      color: var(--text);
      cursor: pointer;
      text-align: center;
      transition: all 0.2s;
    }

    .how-phase-pill.active {
      background: var(--brand);
      color: #FFFFFF;
      box-shadow: 0 0 16px var(--brand-glow);
    }

    .how-phase-pill .phase-range {
      font-size: 11px;
      opacity: 0.8;
      display: block;
      margin-top: 2px;
    }

    .how-step-list {
      display: flex;
      flex-direction: column;
      gap: 12px;
      position: relative;
    }

    .how-step {
      background: var(--surface-card);
      border: 1px solid var(--line);
      border-radius: 10px;
      padding: 20px 24px;
      cursor: pointer;
      text-align: left;
      transition: all 0.2s ease;
      width: 100%;
    }

    .how-step:hover {
      border-color: var(--line-hover);
      background: var(--surface-card-hover);
    }

    .how-step.active {
      border-color: var(--brand-light);
      background: var(--surface-elevated);
      box-shadow: 0 0 20px rgba(37, 99, 235, 0.15);
    }

    .step-header-row {
      display: flex;
      align-items: center;
      gap: 14px;
    }

    .step-num-badge {
      width: 30px;
      height: 30px;
      border-radius: 50%;
      background: rgba(154, 161, 172, 0.12);
      color: var(--heading);
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 13px;
      font-weight: 700;
      flex-shrink: 0;
    }

    .how-step.active .step-num-badge {
      background: var(--brand);
      color: #FFF;
      box-shadow: 0 0 12px var(--brand-glow);
    }

    .step-title {
      font-size: 16.5px;
      font-weight: 600;
      color: var(--heading);
    }

    .step-body-desc {
      font-size: 14px;
      color: var(--text);
      line-height: 1.55;
      margin-top: 10px;
      padding-left: 44px;
      display: none;
    }

    .how-step.active .step-body-desc {
      display: block;
    }

    /* Right Preview Screen Container */
    .how-preview-viewport {
      background: var(--surface-card);
      border: 1px solid var(--line);
      border-radius: 12px;
      overflow: hidden;
      min-height: 480px;
      position: sticky;
      top: 100px;
      box-shadow: 0 20px 50px rgba(0, 0, 0, 0.5);
    }

    .preview-screen-content {
      display: none;
      padding: 24px;
      animation: fadeIn 0.3s ease-in-out;
    }

    .preview-screen-content.active {
      display: block;
    }

    @keyframes fadeIn {
      from { opacity: 0; transform: translateY(6px); }
      to { opacity: 1; transform: translateY(0); }
    }

    /* 5. SEE THE WHOLE FLEET AT A GLANCE */
    .glance-split {
      display: grid;
      grid-template-columns: 1.15fr 1fr;
      gap: 48px;
      align-items: center;
    }

    .glance-bullets {
      list-style: none;
      display: flex;
      flex-direction: column;
      gap: 16px;
      margin: 28px 0;
    }

    .glance-bullet-item {
      display: flex;
      align-items: flex-start;
      gap: 12px;
      font-size: 15.5px;
      color: var(--heading);
    }

    .glance-bullet-icon {
      width: 24px;
      height: 24px;
      border-radius: 50%;
      background: rgba(16, 185, 129, 0.15);
      color: var(--accent-green);
      display: flex;
      align-items: center;
      justify-content: center;
      flex-shrink: 0;
      margin-top: 2px;
    }

    .comp-strip {
      margin-top: 48px;
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 20px;
      padding: 24px;
      background: var(--surface-card);
      border: 1px solid var(--line);
      border-radius: 12px;
    }

    .comp-strip-item {
      padding: 12px;
    }

    .strip-title {
      font-size: 13.5px;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      margin-bottom: 8px;
      display: flex;
      align-items: center;
      gap: 8px;
    }

    .strip-title.spreadsheet { color: #F87171; }
    .strip-title.fleetsure { color: #34D399; }

    /* 6. BUILT FOR THREE TEAMS */
    .teams-tab-nav {
      display: flex;
      gap: 12px;
      justify-content: center;
      margin-bottom: 36px;
    }

    .team-tab-btn {
      padding: 12px 24px;
      border-radius: 8px;
      background: var(--surface-card);
      border: 1px solid var(--line);
      color: var(--text);
      font-size: 14.5px;
      font-weight: 600;
      cursor: pointer;
      transition: all 0.2s ease;
    }

    .team-tab-btn:hover {
      border-color: var(--line-hover);
      color: var(--heading);
    }

    .team-tab-btn.active {
      background: var(--brand);
      border-color: var(--brand-light);
      color: #FFF;
      box-shadow: 0 0 20px var(--brand-glow);
    }

    .team-tab-pane {
      display: none;
      animation: fadeIn 0.3s ease;
    }

    .team-tab-pane.active {
      display: block;
    }

    .tab-content-grid {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 40px;
      align-items: center;
    }

    .tab-bullets {
      list-style: none;
      display: flex;
      flex-direction: column;
      gap: 14px;
      margin-top: 24px;
    }

    .tab-bullet {
      display: flex;
      align-items: flex-start;
      gap: 12px;
      font-size: 15px;
      color: var(--heading);
    }

    /* 7. ALERTS BEFORE EXPIRY (INTERACTIVE TIMELINE) */
    .timeline-widget {
      background: var(--surface-card);
      border: 1px solid var(--line);
      border-radius: 12px;
      padding: 36px;
      box-shadow: 0 20px 50px rgba(0, 0, 0, 0.4);
    }

    .timeline-split {
      display: grid;
      grid-template-columns: 1.25fr 1fr;
      gap: 48px;
      align-items: center;
    }

    .timeline-bar-wrap {
      position: relative;
      margin: 40px 0 20px;
      padding-top: 10px;
    }

    .timeline-track {
      height: 6px;
      background: rgba(154, 161, 172, 0.16);
      border-radius: 4px;
      position: relative;
    }

    .timeline-fill {
      height: 100%;
      background: linear-gradient(90deg, #10B981 0%, #F59E0B 70%, #EF4444 100%);
      border-radius: 4px;
      width: 85%;
    }

    .timeline-marker {
      position: absolute;
      top: -24px;
      transform: translateX(-50%);
      display: flex;
      flex-direction: column;
      align-items: center;
      cursor: pointer;
    }

    .marker-dot {
      width: 14px;
      height: 14px;
      border-radius: 50%;
      background: #FFF;
      border: 3px solid var(--brand);
      margin-bottom: 6px;
      transition: all 0.2s;
    }

    .timeline-marker:hover .marker-dot, .timeline-marker.active .marker-dot {
      transform: scale(1.3);
      box-shadow: 0 0 12px var(--brand-glow);
    }

    .marker-label {
      font-size: 11.5px;
      font-weight: 700;
      color: var(--heading);
      background: var(--surface);
      border: 1px solid var(--line);
      padding: 3px 8px;
      border-radius: 4px;
      white-space: nowrap;
    }

    .alert-channel-selector {
      display: flex;
      gap: 8px;
      margin: 20px 0;
    }

    .channel-tag {
      padding: 6px 14px;
      border-radius: 6px;
      background: var(--surface);
      border: 1px solid var(--line);
      font-size: 12.5px;
      font-weight: 600;
      color: var(--text);
      cursor: pointer;
      transition: all 0.15s;
    }

    .channel-tag.active {
      background: rgba(37, 99, 235, 0.15);
      border-color: var(--brand-light);
      color: #60A5FA;
    }

    .mock-alert-bubble {
      background: var(--surface);
      border: 1px solid var(--line);
      border-radius: 10px;
      padding: 16px 20px;
      margin-top: 16px;
    }

    /* 8. CHALLANS ON ONE SCREEN */
    .challans-split {
      display: grid;
      grid-template-columns: 1fr 1.25fr;
      gap: 48px;
      align-items: center;
    }

    .challan-console {
      background: var(--surface-card);
      border: 1px solid var(--line);
      border-radius: 12px;
      overflow: hidden;
      box-shadow: 0 20px 50px rgba(0, 0, 0, 0.4);
    }

    .challan-state-nav {
      display: flex;
      gap: 6px;
      padding: 12px 16px;
      background: var(--surface);
      border-bottom: 1px solid var(--line);
      overflow-x: auto;
    }

    .challan-state-btn {
      padding: 5px 12px;
      border-radius: 6px;
      background: rgba(154, 161, 172, 0.08);
      border: 1px solid var(--line);
      color: var(--text);
      font-size: 12px;
      font-weight: 600;
      cursor: pointer;
      transition: all 0.15s;
    }

    .challan-state-btn.active, .challan-state-btn:hover {
      background: var(--brand);
      color: #FFF;
      border-color: var(--brand-light);
    }

    .challan-table {
      width: 100%;
      border-collapse: collapse;
      font-size: 12px;
    }

    .challan-table th {
      padding: 10px 14px;
      color: var(--muted);
      border-bottom: 1px solid var(--line);
      text-align: left;
      font-weight: 600;
      text-transform: uppercase;
      font-size: 10.5px;
    }

    .challan-table td {
      padding: 11px 14px;
      border-bottom: 1px solid rgba(154, 161, 172, 0.07);
      color: var(--text);
    }

    .challan-total-footer {
      padding: 14px 18px;
      background: var(--surface);
      border-top: 1px solid var(--line);
      display: flex;
      align-items: center;
      justify-content: space-between;
      font-size: 13px;
    }

    .challan-total-sum {
      font-size: 18px;
      font-weight: 800;
      color: var(--accent-red);
    }

    /* 9. WORKS WITH YOUR SYSTEMS */
    .integration-diagram {
      max-width: 820px;
      margin: 40px auto 0;
      display: flex;
      flex-direction: column;
      align-items: center;
    }

    .diagram-top-block {
      width: 100%;
      background: linear-gradient(135deg, rgba(37, 99, 235, 0.18) 0%, rgba(37, 99, 235, 0.04) 100%);
      border: 1px solid rgba(37, 99, 235, 0.4);
      border-radius: 12px;
      padding: 24px;
      text-align: center;
      box-shadow: 0 0 30px rgba(37, 99, 235, 0.15);
    }

    .diagram-top-title {
      font-size: 18px;
      font-weight: 700;
      color: var(--heading);
      margin-bottom: 6px;
    }

    .diagram-connector {
      display: flex;
      flex-direction: column;
      align-items: center;
      padding: 14px 0;
      color: var(--brand-light);
    }

    .diagram-connector-line {
      width: 2px;
      height: 28px;
      background: linear-gradient(180deg, var(--brand-light), var(--line));
    }

    .diagram-bottom-block {
      width: 100%;
      background: var(--surface-card);
      border: 1px solid var(--line);
      border-radius: 12px;
      padding: 24px;
      text-align: center;
    }

    .tools-pill-grid {
      display: flex;
      gap: 10px;
      flex-wrap: wrap;
      justify-content: center;
      margin-top: 16px;
    }

    .tool-pill {
      font-size: 12.5px;
      padding: 6px 14px;
      border-radius: 6px;
      background: var(--surface);
      border: 1px solid var(--line);
      color: var(--heading);
      font-weight: 500;
    }

    .diagram-caption {
      margin-top: 16px;
      font-size: 13.5px;
      font-weight: 600;
      color: var(--accent-green);
      letter-spacing: 0.02em;
    }

    .integration-cards-grid {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 20px;
      margin-top: 48px;
    }

    .integration-card {
      background: var(--surface-card);
      border: 1px solid var(--line);
      border-radius: 10px;
      padding: 24px;
    }

    .integration-card h4 {
      font-size: 16px;
      margin-bottom: 8px;
    }

    .integration-card p {
      font-size: 13.5px;
      line-height: 1.55;
    }

    /* 10. WHAT YOU CAN SEE (2x2 GRID) */
    .dashboard-2x2-grid {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 24px;
      margin-top: 36px;
    }

    .dash-panel {
      background: var(--surface-card);
      border: 1px solid var(--line);
      border-radius: 12px;
      overflow: hidden;
      box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3);
    }

    .dash-panel-header {
      padding: 14px 18px;
      background: var(--surface);
      border-bottom: 1px solid var(--line);
      display: flex;
      align-items: center;
      justify-content: space-between;
      font-size: 13.5px;
      font-weight: 700;
      color: var(--heading);
    }

    .dash-panel-body {
      padding: 20px;
    }

    .dashboard-metrics-strip {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 16px;
      margin-top: 32px;
    }

    .metric-panel-card {
      background: var(--surface-card);
      border: 1px solid var(--line);
      border-radius: 10px;
      padding: 18px 20px;
    }

    .metric-panel-title {
      font-size: 12px;
      font-weight: 600;
      text-transform: uppercase;
      color: var(--muted);
      margin-bottom: 6px;
    }

    .metric-panel-val {
      font-size: 24px;
      font-weight: 800;
      color: var(--heading);
      margin-bottom: 4px;
    }

    .metric-panel-desc {
      font-size: 12px;
      color: var(--muted);
    }

    /* 11. BUILT FOR COMPLIANCE, NOT A GPS SUITE */
    .config-cards-grid {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 28px;
      margin-top: 36px;
    }

    .config-card {
      background: var(--surface-card);
      border: 1px solid var(--line);
      border-radius: 12px;
      padding: 36px 32px;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
    }

    .config-card-muted {
      opacity: 0.85;
      border-style: dashed;
    }

    .config-card-highlight {
      background: linear-gradient(180deg, var(--surface-card) 0%, rgba(37, 99, 235, 0.08) 100%);
      border: 1px solid rgba(37, 99, 235, 0.45);
      box-shadow: 0 0 35px rgba(37, 99, 235, 0.15);
      position: relative;
    }

    .highlight-badge {
      position: absolute;
      top: -12px;
      right: 24px;
      background: var(--brand);
      color: #FFF;
      font-size: 11px;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.06em;
      padding: 4px 12px;
      border-radius: 999px;
      box-shadow: 0 0 12px var(--brand-glow);
    }

    .time-to-value-strip {
      margin-top: 32px;
      padding: 16px 24px;
      background: rgba(16, 185, 129, 0.08);
      border: 1px solid rgba(16, 185, 129, 0.25);
      border-radius: 8px;
      color: #34D399;
      font-weight: 600;
      font-size: 14.5px;
      text-align: center;
    }

    /* 12. WHAT IS INCLUDED (8 TILES) */
    .included-grid {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 20px;
      margin-top: 36px;
    }

    .included-phase-header {
      grid-column: 1 / -1;
      display: flex;
      align-items: center;
      gap: 16px;
      margin-top: 16px;
      margin-bottom: 4px;
    }

    .included-phase-header:first-child {
      margin-top: 0;
    }

    .included-phase-title {
      font-size: 12.5px;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.08em;
      color: var(--brand-light);
    }

    .included-phase-line {
      flex: 1;
      height: 1px;
      background: var(--line);
    }

    .included-tile {
      background: var(--surface-card);
      border: 1px solid var(--line);
      border-radius: 10px;
      padding: 24px 20px;
      transition: all 0.2s ease;
    }

    .included-tile:hover {
      border-color: var(--line-hover);
      transform: translateY(-2px);
    }

    .included-icon-box {
      width: 40px;
      height: 40px;
      border-radius: 8px;
      background: var(--brand-subtle);
      border: 1px solid rgba(37, 99, 235, 0.25);
      display: flex;
      align-items: center;
      justify-content: center;
      color: var(--brand-light);
      margin-bottom: 16px;
    }

    .included-heading {
      font-size: 16px;
      font-weight: 700;
      color: var(--heading);
      margin-bottom: 8px;
    }

    .included-desc {
      font-size: 13.5px;
      line-height: 1.55;
      color: var(--text);
    }

    /* 13. FAQ ACCORDION */
    .faq-search-wrap {
      max-width: 540px;
      margin: 0 auto 36px;
      position: relative;
    }

    .faq-search-input {
      width: 100%;
      background: var(--surface-card);
      border: 1px solid var(--line);
      border-radius: 8px;
      padding: 12px 18px 12px 42px;
      color: var(--heading);
      font-size: 14.5px;
      outline: none;
      transition: border-color 0.2s;
    }

    .faq-search-input:focus {
      border-color: var(--brand-light);
      box-shadow: 0 0 16px var(--brand-glow);
    }

    .faq-search-icon {
      position: absolute;
      left: 14px;
      top: 50%;
      transform: translateY(-50%);
      color: var(--muted);
      pointer-events: none;
    }

    .faq-accordion {
      max-width: 820px;
      margin: 0 auto;
      display: flex;
      flex-direction: column;
      gap: 12px;
    }

    .faq-item {
      background: var(--surface-card);
      border: 1px solid var(--line);
      border-radius: 10px;
      overflow: hidden;
      transition: border-color 0.2s;
    }

    .faq-item:hover {
      border-color: var(--line-hover);
    }

    .faq-item[open] {
      border-color: rgba(37, 99, 235, 0.4);
      background: var(--surface-elevated);
    }

    .faq-question {
      padding: 18px 24px;
      font-size: 16px;
      font-weight: 600;
      color: var(--heading);
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: space-between;
      list-style: none;
    }

    .faq-question::-webkit-details-marker {
      display: none;
    }

    .faq-icon {
      font-size: 18px;
      color: var(--brand-light);
      transition: transform 0.2s;
    }

    .faq-item[open] .faq-icon {
      transform: rotate(45deg);
    }

    .faq-answer {
      padding: 0 24px 20px;
      font-size: 14.5px;
      line-height: 1.65;
      color: var(--text);
    }

    /* 14. FINAL CTA */
    .closing-band {
      background: linear-gradient(135deg, #1E40AF 0%, #1D4ED8 50%, #2563EB 100%);
      padding: 80px 0;
      text-align: center;
      color: #FFFFFF;
      position: relative;
      overflow: hidden;
    }

    .closing-band::before {
      content: "";
      position: absolute;
      top: -50%;
      left: -50%;
      width: 200%;
      height: 200%;
      background: radial-gradient(circle, rgba(255,255,255,0.1) 0%, transparent 60%);
      pointer-events: none;
    }

    .closing-band h2 {
      font-size: 36px;
      color: #FFFFFF;
      margin-bottom: 16px;
    }

    .closing-line {
      font-size: 17px;
      color: rgba(255, 255, 255, 0.88);
      max-width: 640px;
      margin: 0 auto 32px;
      line-height: 1.6;
    }

    .closing-buttons {
      display: flex;
      gap: 16px;
      justify-content: center;
      flex-wrap: wrap;
    }

    /* Site Footer */
    .site-footer {
      background: #050811;
      border-top: 1px solid var(--line);
      padding: 60px 0 36px;
      font-size: 14px;
    }

    .footer-grid {
      display: grid;
      grid-template-columns: 2fr 1fr 1fr 1fr;
      gap: 40px;
      margin-bottom: 48px;
    }

    .footer-desc {
      color: var(--muted);
      font-size: 13.5px;
      margin-top: 12px;
      max-width: 340px;
      line-height: 1.6;
    }

    .positioning-guard-pill {
      display: inline-block;
      margin-top: 16px;
      padding: 8px 14px;
      border-radius: 6px;
      background: rgba(154, 161, 172, 0.08);
      border: 1px solid var(--line);
      color: var(--muted);
      font-size: 12px;
      line-height: 1.5;
    }

    .footer-col h4 {
      font-size: 14px;
      font-weight: 600;
      color: var(--heading);
      margin-bottom: 16px;
      text-transform: uppercase;
      letter-spacing: 0.04em;
    }

    .footer-col ul {
      list-style: none;
      display: flex;
      flex-direction: column;
      gap: 10px;
    }

    .footer-col a {
      color: var(--muted);
      text-decoration: none;
      transition: color 0.15s ease;
    }

    .footer-col a:hover {
      color: var(--heading);
    }

    .footer-bottom {
      border-top: 1px solid var(--line);
      padding-top: 24px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      color: var(--muted);
      font-size: 13px;
    }

    /* Modals */
    .modal-backdrop {
      position: fixed;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      background: rgba(4, 7, 14, 0.85);
      backdrop-filter: blur(8px);
      z-index: 1000;
      display: none;
      align-items: center;
      justify-content: center;
      padding: 20px;
    }

    .modal-backdrop.active {
      display: flex;
    }

    .modal-card {
      background: var(--surface-card);
      border: 1px solid var(--line-hover);
      border-radius: 14px;
      width: 100%;
      max-width: 520px;
      box-shadow: 0 24px 60px rgba(0, 0, 0, 0.8);
      overflow: hidden;
      animation: modalPop 0.25s cubic-bezier(0.16, 1, 0.3, 1);
    }

    @keyframes modalPop {
      from { transform: scale(0.94); opacity: 0; }
      to { transform: scale(1); opacity: 1; }
    }

    .modal-header {
      padding: 20px 24px;
      background: var(--surface);
      border-bottom: 1px solid var(--line);
      display: flex;
      align-items: center;
      justify-content: space-between;
    }

    .modal-header h3 {
      font-size: 18px;
      margin: 0;
    }

    .modal-close-btn {
      background: none;
      border: none;
      color: var(--muted);
      font-size: 20px;
      cursor: pointer;
      line-height: 1;
    }

    .modal-close-btn:hover {
      color: var(--heading);
    }

    .modal-body {
      padding: 24px;
    }

    .form-group {
      margin-bottom: 16px;
    }

    .form-group label {
      display: block;
      font-size: 13px;
      font-weight: 600;
      color: var(--heading);
      margin-bottom: 6px;
    }

    .form-control {
      width: 100%;
      padding: 10px 14px;
      border-radius: 8px;
      background: var(--surface);
      border: 1px solid var(--line);
      color: var(--heading);
      font-size: 14px;
      outline: none;
      transition: border-color 0.15s;
    }

    .form-control:focus {
      border-color: var(--brand-light);
    }

    /* Responsive Breakpoints */
    @media (max-width: 1024px) {
      .hero-split, .glance-split, .shift-split, .how-grid, .tab-content-grid, .timeline-split, .challans-split {
        grid-template-columns: 1fr;
        gap: 40px;
      }
      .included-grid {
        grid-template-columns: repeat(2, 1fr);
      }
      .footer-grid {
        grid-template-columns: 1fr 1fr;
      }
      .how-preview-viewport {
        position: static;
        min-height: auto;
      }
    }

    @media (max-width: 768px) {
      h1 { font-size: 32px; }
      h2 { font-size: 26px; }
      .header-nav { display: none; }
      .problem-cards-grid, .dashboard-2x2-grid, .config-cards-grid, .integration-cards-grid, .comp-strip {
        grid-template-columns: 1fr;
      }
      .included-grid {
        grid-template-columns: 1fr;
      }
      .hero-metric-strip, .dashboard-metrics-strip {
        grid-template-columns: 1fr 1fr;
      }
      .comp-header, .comp-row {
        grid-template-columns: 1fr;
        gap: 6px;
      }
      .footer-grid {
        grid-template-columns: 1fr;
      }
      .footer-bottom {
        flex-direction: column;
        gap: 12px;
        text-align: center;
      }
    }
  """
