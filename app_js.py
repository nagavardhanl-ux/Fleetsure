# -*- coding: utf-8 -*-
"""
Fleetsure Interactive JavaScript
"""

def get_js():
    return """
    // 1. Workflow Clickable Steps (Section 4)
    var currentStep = 1;
    var stepTitles = [
      "Step 1: Document upload and secure storage screen",
      "Step 2: Alert rule configuration screen",
      "Step 3: Compliance tracking view with validity status",
      "Step 4: Expiry alert on email, SMS and dashboard",
      "Step 5: Fleet compliance and challan dashboard"
    ];

    function activateWorkflowStep(stepNum) {
      currentStep = stepNum;
      for (var i = 1; i <= 5; i++) {
        var btn = document.getElementById('how-step-' + i);
        var screen = document.getElementById('how-screen-' + i);
        if (btn) {
          if (i === stepNum) {
            btn.classList.add('active');
          } else {
            btn.classList.remove('active');
          }
        }
        if (screen) {
          if (i === stepNum) {
            screen.classList.add('active');
          } else {
            screen.classList.remove('active');
          }
        }
      }

      var titleEl = document.getElementById('how-viewport-title');
      if (titleEl && stepTitles[stepNum - 1]) {
        titleEl.textContent = stepTitles[stepNum - 1];
      }

      // Sync Phase Pill
      var p1 = document.getElementById('phase-pill-1');
      var p2 = document.getElementById('phase-pill-2');
      if (p1 && p2) {
        if (stepNum <= 2) {
          p1.classList.add('active');
          p2.classList.remove('active');
        } else {
          p1.classList.remove('active');
          p2.classList.add('active');
        }
      }
    }

    function jumpToHowPhase(phase) {
      if (phase === 1) activateWorkflowStep(1);
      else activateWorkflowStep(3);
    }

    // 2. Built for Three Teams Tab Switcher (Section 6)
    function switchTeamTab(tabIndex) {
      for (var i = 1; i <= 3; i++) {
        var btn = document.getElementById('team-tab-btn-' + i);
        var pane = document.getElementById('team-pane-' + i);
        if (btn) {
          if (i === tabIndex) {
            btn.classList.add('active');
          } else {
            btn.classList.remove('active');
          }
        }
        if (pane) {
          if (i === tabIndex) {
            pane.classList.add('active');
          } else {
            pane.classList.remove('active');
          }
        }
      }
    }

    // 3. Interactive Expiry Timeline Widget (Section 7)
    var currentMarkerDays = 7;
    var currentAlertChannel = 'All';

    function selectMarker(days) {
      currentMarkerDays = days;
      var markers = document.querySelectorAll('.timeline-marker');
      markers.forEach(function(m) { m.classList.remove('active'); });

      var fill = document.getElementById('alert-timeline-fill');
      if (days === 30) {
        if (fill) fill.style.width = '35%';
        markers[0].classList.add('active');
      } else if (days === 15) {
        if (fill) fill.style.width = '68%';
        markers[1].classList.add('active');
      } else {
        if (fill) fill.style.width = '90%';
        markers[2].classList.add('active');
      }

      updateAlertSimulation();
    }

    function selectAlertChannel(channel) {
      currentAlertChannel = channel;
      document.querySelectorAll('.channel-tag').forEach(function(tag) {
        tag.classList.remove('active');
      });
      if (channel === 'All') document.getElementById('chan-all').classList.add('active');
      else if (channel === 'WhatsApp') document.getElementById('chan-whatsapp').classList.add('active');
      else if (channel === 'Email') document.getElementById('chan-email').classList.add('active');
      else if (channel === 'In-App') document.getElementById('chan-inapp').classList.add('active');

      updateAlertSimulation();
    }

    function updateAlertSimulation() {
      var docSelect = document.getElementById('expiry-doc-type');
      var docName = docSelect ? docSelect.value : 'Commercial Vehicle Insurance';
      var titleEl = document.getElementById('mock-alert-channel-title');
      var textEl = document.getElementById('mock-alert-text');

      var channelStr = currentAlertChannel === 'All' ? 'WhatsApp & Email & Dashboard' : currentAlertChannel;
      if (titleEl) {
        titleEl.textContent = channelStr + ' Dispatch &middot; ' + currentMarkerDays + '-Day Pre-Expiry Reminder';
      }

      var urgency = currentMarkerDays <= 7 ? 'URGENT: ' : 'Reminder: ';
      if (textEl) {
        textEl.innerHTML = '"' + urgency + 'Vehicle <strong>MH-12-RN-4821</strong> ' + docName + ' renewal deadline in <strong>' + currentMarkerDays + ' days</strong> (15-Nov-2026). Renewal quotation ready &middot; Dispatched to Pune Depot Lead &amp; Driver."';
      }
    }

    // 4. Hero Depot Filter
    function filterHeroTable(depot) {
      var pills = document.querySelectorAll('.depot-filter-pill');
      pills.forEach(function(p) { p.classList.remove('active'); });
      event.target.classList.add('active');

      var rows = document.querySelectorAll('#hero-vehicle-rows tr');
      rows.forEach(function(row) {
        if (depot === 'All') {
          row.style.display = '';
        } else {
          var text = row.textContent || '';
          if (text.indexOf(depot) !== -1) {
            row.style.display = '';
          } else {
            row.style.display = 'none';
          }
        }
      });
    }

    // 5. Vehicle Inspection Modal
    function inspectVehicle(id, depot, type, rc, ins, puc, tax, dl, challan) {
      document.getElementById('veh-modal-id').textContent = id;
      document.getElementById('veh-modal-sub').textContent = depot + ' &middot; ' + type;
      
      var setPill = function(elId, val) {
        var el = document.getElementById(elId);
        if (!el) return;
        el.textContent = '• ' + val;
        el.className = 'status-pill';
        if (val.indexOf('Valid') !== -1) el.classList.add('valid');
        else if (val.indexOf('Expiring') !== -1) el.classList.add('expiring');
        else el.classList.add('expired');
      };

      setPill('veh-rc-val', rc);
      setPill('veh-ins-val', ins);
      setPill('veh-puc-val', puc);
      setPill('veh-tax-val', tax);
      setPill('veh-dl-val', dl);

      var challanEl = document.getElementById('veh-challan-val');
      if (challanEl) challanEl.textContent = challan;

      document.getElementById('vehicle-modal').classList.add('active');
    }

    function closeVehicleModal() {
      document.getElementById('vehicle-modal').classList.remove('active');
    }

    // 6. Challans Filter by State & Running Total (Section 8)
    function filterChallanState(state) {
      document.querySelectorAll('.challan-state-btn').forEach(function(btn) {
        btn.classList.remove('active');
      });
      event.target.classList.add('active');

      var rows = document.querySelectorAll('#challan-rows-body tr');
      var total = 0;
      rows.forEach(function(r) {
        var rState = r.getAttribute('data-state');
        if (state === 'All' || rState === state) {
          r.style.display = '';
          var amtText = r.children[3].textContent.replace('₹', '').replace(',', '');
          total += parseInt(amtText) || 0;
        } else {
          r.style.display = 'none';
        }
      });

      var totalEl = document.getElementById('challan-total-display');
      if (totalEl) {
        totalEl.textContent = '₹' + total.toLocaleString('en-IN');
      }
    }

    function simulateSettleChallans() {
      alert('Simulation: All visible pending challans verified against Parivahan portals and scheduled for batch bulk payment.');
      var totalEl = document.getElementById('challan-total-display');
      if (totalEl) totalEl.textContent = '₹0 (All Settled)';
      document.querySelectorAll('#challan-rows-body tr').forEach(function(r) {
        if (r.style.display !== 'none') {
          var statusCell = r.children[4];
          statusCell.innerHTML = '<span class="status-pill valid">Settled</span>';
        }
      });
    }

    // 7. FAQ Filter & Search (Section 13)
    function filterFAQs() {
      var query = document.getElementById('faq-search-input').value.toLowerCase();
      var items = document.querySelectorAll('.faq-item');
      items.forEach(function(item) {
        var text = item.textContent.toLowerCase();
        if (text.indexOf(query) !== -1) {
          item.style.display = '';
        } else {
          item.style.display = 'none';
        }
      });
    }

    // 8. Demo Booking Modal
    function openDemoModal() {
      document.getElementById('demo-modal').classList.add('active');
    }

    function closeDemoModal() {
      document.getElementById('demo-modal').classList.remove('active');
    }

    function closeModalOnBackdrop(e, modalId) {
      if (e.target.id === modalId) {
        document.getElementById(modalId).classList.remove('active');
      }
    }

    function handleDemoSubmit(e) {
      e.preventDefault();
      var name = document.getElementById('demo-name').value;
      var company = document.getElementById('demo-company').value;
      alert('Thank you, ' + name + '! We have scheduled your 20-minute Fleetsure demo for ' + company + '. A calendar invitation has been sent to your work email.');
      closeDemoModal();
      e.target.reset();
    }
  """

print("app_js.py ready.")
