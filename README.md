# Fleetsure by AIQoD

> **Fleet Compliance and Challan Management Software**  
> *Know every vehicle is legal before it leaves the yard.*

Fleetsure tracks every vehicle and driver document, alerts the team before anything expires, shows live compliance status across every location, and brings challans from every state onto one dashboard. Built on the AIQoD platform and run by specialized AI agents, with people taking every renewal and payment action.

---

## Key Features

- **Centralized Document Vault**: Ingests and stores Registration (RC), Insurance, Pollution Under Control (PUC), Road Tax, and Driver Licences across owned, vendor, and leased fleets.
- **Government Record Verification**: Documents are verified against official government registries (VAHAN / Sarathi).
- **Proactive Expiry Cadence**: Automated reminders dispatched at **30, 15, and 7 days** before expiry via WhatsApp, Email, SMS, and in-app alerts.
- **Multi-State Challan Aggregation**: Live interstate e-challan tracking across state portals (MH, DL, KA, TN, GJ) with running total calculations and early payment workflows.
- **Multi-Location Status Boards**: Live, color-coded health tracking across depots, regions, and business units.
- **Zero Hardware Required**: 100% cloud-native SaaS and AI agent architecture with no OBD sensors or GPS trackers fitted to vehicles.

---

## Live Preview & Setup

1. Open `index.html` directly in any web browser.
2. Or serve locally:
   ```bash
   python -m http.server 3000
   ```
   and navigate to [http://localhost:3000](http://localhost:3000).

---

## Architecture & Rebuild Engine

- `index.html` &mdash; Production single-page landing site with self-contained styles, SVG iconography, and responsive interaction logic.
- `build_index.py` &mdash; Modular Python generator linking content schemas, custom design tokens, and interactive components.
- `Website Content - Fleetsure.xlsx` &mdash; Master product copy and layout specification.

---

&copy; 2026 AIQoD Inc. All rights reserved. Fleetsure is an AIQoD Enterprise Platform solution.
