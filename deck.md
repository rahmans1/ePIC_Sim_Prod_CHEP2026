---
marp: true
theme: default
paginate: true
size: 16:9
title: Scaling ePIC Simulation Production
description: MARP source generated from the current PowerPoint deck.
---

<style>
section {
  font-family: Arial, Helvetica, sans-serif;
  color: #1f2933;
  background: #ffffff;
  justify-content: flex-start;
  padding: 18px 56px 28px;
}
h1 {
  color: #123f6d;
  font-size: 42px;
  margin-top: 0;
  margin-bottom: 0.35em;
}
h2 {
  color: #123f6d;
  font-size: 32px;
  margin-top: 0;
  margin-bottom: 0.25em;
}
h3 {
  color: #2f6f8f;
  font-size: 22px;
  margin-top: 0.45em;
  margin-bottom: 0.2em;
}
strong {
  color: #123f6d;
}
section.title {
  background: #f7fafc;
  padding: 30px 46px 28px;
  overflow: hidden;
}
section.title h1 {
  font-size: 38px;
  line-height: 1.1;
}
.title-layout {
  display: grid;
  grid-template-columns: 0.82fr 1.18fr;
  gap: 26px;
  align-items: center;
  min-height: 420px;
}
.title-copy {
  display: flex;
  flex-direction: column;
  gap: 12px;
}
.title-copy p {
  margin: 0;
}
.nowrap {
  white-space: nowrap;
}
.detector-hero {
  text-align: center;
  align-self: stretch;
  display: flex;
  align-items: center;
  justify-content: center;
}
.detector-hero img {
  width: 112%;
  max-height: 455px;
  object-fit: contain;
  opacity: 0.86;
  mix-blend-mode: multiply;
  filter: saturate(0.96) contrast(1.04);
  -webkit-mask-image: radial-gradient(ellipse at center, #000 55%, rgba(0, 0, 0, 0.72) 72%, transparent 100%);
  mask-image: radial-gradient(ellipse at center, #000 55%, rgba(0, 0, 0, 0.72) 72%, transparent 100%);
}
.title-top {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 26px;
  align-items: center;
  margin-bottom: 14px;
  min-height: 96px;
}
.title-top img {
  max-width: 100%;
  max-height: 86px;
  object-fit: contain;
  justify-self: center;
}
.title-top img:first-child {
  justify-self: start;
}
section.compact {
  font-size: 23px;
}
section.small {
  font-size: 20px;
}
.subtitle {
  font-size: 24px;
  color: #4a5568;
}
.muted {
  color: #5f6b7a;
}
.grid-2 {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 28px;
  align-items: start;
}
.grid-3 {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 18px;
}
.stat {
  border-top: 5px solid #2f6f8f;
  padding-top: 10px;
}
.stat .value {
  font-size: 42px;
  font-weight: 700;
  color: #123f6d;
}
.figure {
  text-align: center;
}
.figure img {
  max-width: 100%;
  max-height: 410px;
  object-fit: contain;
}
</style>

<!-- _class: title -->

<p style="position:absolute;bottom:14px;left:46px;font-size:13px;color:#a0aab4;margin:0;">Slide template generated with Claude Sonnet 4.6</p>

<div class="title-top">
  <img src="assets/epic_logo.png" alt="ePIC logo">
  <img src="assets/bnl_logo.png" alt="Brookhaven National Laboratory logo">
  <img src="assets/jefferson_lab_logo.png" alt="Jefferson Lab logo">
  <img src="assets/office_of_science_logo.png" alt="Office of Science logo">
</div>

<div class="title-layout">
<div class="title-copy">

# Scaling ePIC Simulation Production:<br><span class="nowrap" style="font-size:30px;">Distributed Workflow and Data Management</span>

<p style="color:#2f6f8f;font-size:28px;">Sakib Rahman<br>
<span class="nowrap" style="font-size:20px;">on behalf of the ePIC Collaboration</span><br>
<span class="nowrap" style="font-size:20px;">Brookhaven National Laboratory</span></p>

<p style="color:#5f6b7a;font-size:28px;"><span class="nowrap">Computing in High Energy and Nuclear Physics (CHEP)</span><br>
<span class="nowrap">Chulalongkorn University, Bangkok, Thailand</span><br>
<span class="nowrap">26 May 2026</span></p>

</div>

<div class="detector-hero">
  <img src="assets/detector.jpg" alt="ePIC detector rendering">
</div>
</div>

---

## The ePIC Experiment at the Electron-Ion Collider

<div class="grid-3">
  <div class="stat"><div class="value">1157</div><div>Collaborators</div></div>
  <div class="stat"><div class="value">183</div><div>Institutions</div></div>
  <div class="stat"><div class="value">26</div><div>Countries</div></div>
</div>

<div class="grid-2" style="align-items:stretch;">
<div style="display:flex;flex-direction:column;gap:7px;">
<div style="background:#eef4fb;border-left:5px solid #1E5BA8;border-radius:4px;padding:8px 12px;font-size:18px;">
ePIC will be the first detector at the future Electron-Ion Collider. Data taking planned for the <strong>early 2030s</strong>.
</div>
<div style="background:#f0f5f9;border-left:5px solid #2f6f8f;border-radius:4px;padding:8px 12px;font-size:18px;">
Being realized through a partnership between host labs: <strong>Brookhaven National Laboratory (BNL)</strong> and <strong>Jefferson Lab (JLab)</strong>
</div>
<div style="flex-grow:1;display:flex;flex-direction:column;justify-content:flex-end;text-align:center;margin-top:7px;">
  <img src="assets/image4.jpg" alt="EIC beam specifications" style="width:100%;object-fit:contain;flex-grow:1;">
  <p class="muted" style="font-size:24px;margin-top:4px;font-weight:bold;">EIC Beam Specifications</p>
</div>
</div>
<div style="display:flex;flex-direction:column;gap:7px;">
<div style="background:#eaf4ea;border-left:5px solid #1E8449;border-radius:4px;padding:8px 12px;font-size:18px;min-height:82px;display:flex;align-items:center;">
Will enable precision studies of nucleons and nuclei at the scale of sea quarks and gluons
</div>
<div style="flex-grow:1;display:flex;flex-direction:column;justify-content:flex-end;text-align:center;margin-top:7px;">
  <img src="assets/image5.png" alt="ePIC collaboration map" style="width:100%;object-fit:contain;flex-grow:1;">
  <p class="muted" style="font-size:24px;margin-top:4px;font-weight:bold;">ePIC: A Global Collaboration</p>
</div>
</div>
</div>

---

## The ePIC Production Working Group

<style>
.orgchart { width:100%; border-collapse:collapse; font-size:14px; }
.orgchart th { background:#2f6f8f; color:#fff; padding:6px 4px; text-align:center; font-size:13px; border:1px solid #2f6f8f; }
.orgchart .spox { background:#123f6d; color:#fff; text-align:center; font-weight:bold; padding:6px; font-size:14px; border:1px solid #123f6d; }
.orgchart td { border:1px solid #c0cdd8; padding:5px 4px; text-align:center; color:#1f2933; vertical-align:middle; }
.orgchart tr:nth-child(even) td { background:#f0f5f9; }
.orgchart tr:nth-child(odd) td { background:#ffffff; }
.orgchart .highlight { background:#e8f4e8 !important; color:#1a5c1a; font-weight:bold; border:2px solid #2a8a2a !important; font-size:15px; }
.resp-boxes { display:grid; grid-template-columns:repeat(3,1fr); gap:14px; margin-top:14px; }
.resp-box { background:#f0f5f9; border-left:4px solid #2f6f8f; border-radius:4px; padding:10px 12px; font-size:22px; }
.resp-box > strong:first-child { display:block; color:#123f6d; margin-bottom:4px; font-size:24px; }
</style>

<div class="grid-2" style="margin-bottom:6px;">
<div style="font-size:22px;">
<ul style="margin:0;padding-left:22px;">
<li>Sits within the <strong>Software &amp; Computing</strong> branch of the ePIC collaboration</li>
<li>Runs large-scale monthly simulation campaigns on HTC and HPC resources — opportunistic sites via the Open Science Grid (OSG) and allocated domestic &amp; international sites</li>
<li>Enables detector and physics studies for the Technical Design Report</li>
</ul>
</div>
<div>
<table class="orgchart">
  <tr><td colspan="3" class="spox" style="background:#123f6d;color:#ffffff;text-align:center;font-weight:bold;padding:6px;font-size:14px;"><a href="https://www.epic-eic.org/collaboration/overview.html" style="color:#ffffff;text-decoration:underline;">SPOKESPERSON'S OFFICE</a></td></tr>
  <tr>
    <th>TECHNICAL<br>COORDINATION</th>
    <th>SOFTWARE &amp;<br>COMPUTING</th>
    <th>ANALYSIS<br>COORDINATORS</th>
  </tr>
  <tr><td>Tracking</td><td>Physics &amp; Detector Simulations</td><td>BSM &amp; Precision EW</td></tr>
  <tr><td>Electronics, Readout &amp; DAQ</td><td>Reconstruction</td><td>Exclusive, Diffraction &amp; Tagging</td></tr>
  <tr><td>AC-LGAD</td><td>Streaming Computing</td><td>Jets &amp; Heavy Flavor</td></tr>
  <tr><td>Calorimetry</td><td>User Learning</td><td>Inclusive Physics</td></tr>
  <tr><td>PID</td><td class="highlight">⭐ PRODUCTION</td><td>Semi-Inclusive Physics</td></tr>
  <tr><td></td><td>Validation</td><td></td></tr>
</table>
</div>
</div>

<div class="resp-boxes">
  <div class="resp-box"><strong>Campaigns</strong>Running continuously since <strong>May 2023</strong>, growing to <strong>&gt;1M core hours</strong> and <strong>~150 TB</strong> per month</div>
  <div class="resp-box"><strong>Infrastructure</strong>Develop and maintain workflow and data management systems that leverage heterogeneous resources efficiently <span class="muted" style="font-size:0.85em;">(<a href="https://indico.cern.ch/event/1471803/contributions/6967984/" style="color:#5f6b7a;text-decoration:underline;">See my other talk on acceleration pathways</a>)</span></div>
  <div class="resp-box"><strong>Operations</strong>Deliver production-scale simulated data to Physics Working Groups (PWG) and Detector Subsystem Collaborations (DSC)</div>
</div>

---

## Simulation Production: Compute

<div class="figure">
  <img src="assets/computing_usage.png" alt="Simulation production core hours by resource" style="width:100%;max-height:400px;object-fit:contain;">
  <p class="muted" style="font-size:24px;margin-top:4px;font-weight:bold;">ePIC Computing Usage by Site (2024–2026)</p>
</div>

<div style="background:#f0f5f9;border-left:4px solid #2f6f8f;border-radius:4px;padding:10px 16px;font-size:20px;margin-top:8px;">
<ul style="margin:0;padding-left:20px;">
<li>Continue to rely heavily on opportunistic resources from OSG</li>
<li>Added more allocated resources in 2026, anticipating growing compute demand for new physics studies and background mixed simulations</li>
</ul>
</div>

---

## Simulation Production: Storage

<div style="display:grid;grid-template-columns:30% 70%;gap:20px;align-items:start;">
<div style="display:flex;flex-direction:column;gap:14px;">
<div style="font-size:21px;background:#f0f5f9;border-left:4px solid #2f6f8f;padding:10px 16px;border-radius:4px;"><ul style="margin:0;padding-left:20px;">
<li><strong>750 TB</strong> disk added at BNL (March 2026) to meet growing collaboration demand</li>
<li><strong>500 TB</strong> disk + scalable tape at JLab</li>
<li>Additional resources being discussed with international partners</li>
</ul></div>
<div style="font-size:21px;background:#eaf4ea;border-left:4px solid #1E8449;padding:10px 16px;border-radius:4px;"><ul style="margin:0;padding-left:20px;">
<li><strong>Storage backends:</strong> BNL uses ZFS, JLab uses Lustre</li>
<li>Access via <strong>XRootD</strong>, dual instance to simultaneously allow authenticated write and unauthenticated public read access</li>
</ul></div>
</div>
<div style="display:flex;flex-direction:column;align-items:center;">
  <img src="assets/StorageResourceGrowth.png" alt="Storage resource growth" style="width:100%;object-fit:contain;">
  <p class="muted" style="font-size:22px;margin-top:6px;font-weight:bold;">ePIC Storage Usage (2025–2026)</p>
</div>
</div>

---

## Simulation Production: Infrastructure Evolution

<div class="grid-2">
<div>

### Workflow & Data Management Stack

<div style="display:flex;flex-direction:column;gap:8px;margin-top:4px;">
<div style="background:#eef4fb;border-left:5px solid #1E5BA8;border-radius:4px;padding:9px 14px;font-size:21px;">
<strong style="color:#1E5BA8;font-size:22px;">PanDA WMS / iDDS</strong><br>
Automated production workflow and adaptive job brokerage
</div>
<div style="background:#f3eef8;border-left:5px solid #7B3FA0;border-radius:4px;padding:9px 14px;font-size:21px;">
<strong style="color:#7B3FA0;font-size:22px;">Rucio</strong><br>
Distributed data management and replication across storage elements
</div>
<div style="background:#f3eef8;border-left:5px solid #6B2FA0;border-radius:4px;padding:9px 14px;font-size:21px;">
<strong style="color:#6B2FA0;font-size:22px;">AI-Powered Monitoring and Self-Documentation</strong><br>
MCP server stack powering an AI agent for monitoring across systems
</div>
<div style="background:#fdf6e3;border-left:5px solid #b07d00;border-radius:4px;padding:9px 14px;font-size:21px;">
<strong style="color:#b07d00;font-size:22px;">Physics Configuration System (PCS)</strong> <span style="font-size:17px;color:#b07d00;font-weight:bold;">⚠ beta</span><br>
Simulation task provenance and configuration record
</div>
</div>

</div>
<div>

### Integrating International Resources

<div style="display:flex;flex-direction:column;gap:8px;margin-top:4px;">
<div style="background:#eef4fb;border-left:5px solid #1E5BA8;border-radius:4px;padding:9px 14px;font-size:21px;">
<strong style="color:#1E5BA8;font-size:22px;">OSG Umbrella</strong><br>
INFN-T1, DRAC, and UManitoba HPCC onboarded as allocated resources under the OSG umbrella
</div>
<div style="background:#eaf4ea;border-left:5px solid #1E8449;border-radius:4px;padding:9px 14px;font-size:21px;">
<strong style="color:#1E8449;font-size:22px;">Next Steps</strong><br>
Direct PanDA submission and Rucio replication between storage elements are being validated at UManitoba HPCC to develop a model for future sites.
</div>
<div style="background:#eef4fb;border-left:5px solid #1E5BA8;border-radius:4px;padding:9px 14px;font-size:21px;margin-top:8px;">
<strong style="color:#1E5BA8;font-size:22px;">ePIC Computing Model</strong><br>
Infrastructure planning guided by the collaboration's computing model <span class="muted" style="font-size:0.85em;">(<a href="https://indico.cern.ch/event/1471803/contributions/6967120/" style="color:#5f6b7a;text-decoration:underline;">See Holly Szumila-Vance's talk</a>)</span>
</div>
</div>

</div>
</div>

<p class="muted" style="font-size:16px;margin-top:8px;text-align:right;">Each component elaborated in follow-up slides →</p>

---

## PanDA WMS + iDDS: Improved Workflow Management

<style>
.flow-box { border-radius:6px; padding:8px 12px; text-align:center; font-size:15px; font-weight:bold; }
.flow-arrow { text-align:center; font-size:18px; color:#888; margin:2px 0; }
.phase-bar { border-radius:6px; padding:10px 14px; font-size:17px; }
.phase-bar strong { display:block; font-size:19px; margin-bottom:2px; }
</style>

<div class="grid-2" style="margin-bottom:0;align-items:stretch;">

<div style="font-size:18px;display:flex;flex-direction:column;">

Started with lightweight shell scripts and job submission templates <a href="https://www.epj-conferences.org/articles/epjconf/abs/2025/22/epjconf_chep2025_01263/epjconf_chep2025_01263.html" style="font-size:15px;color:#2f6f8f;">(CHEP 2024)</a> — but have now reached a scale of complexity that necessitates a dedicated **Workflow Management System (WMS)**.

**PanDA/iDDS meet our urgent needs:**
- **PanDA WMS** — task brokerage, scalability, adaptive scheduling
- **iDDS** — data transformations and task dependency chains

Production orchestration will be consolidated around **BNL PanDA/iDDS** and **JLab Rucio** by **2026**. WMS options for streaming orchestration will be re-evaluated in **FY2028**.

<img src="assets/PanDAMonitoringExample.jpg" alt="PanDA monitoring example" style="width:100%;max-height:200px;object-fit:contain;border-radius:4px;border:1px solid #c0cdd8;margin-top:8px;display:block;">
<p class="muted" style="font-size:15px;margin-top:4px;text-align:center;font-weight:bold;">Example of PanDA Monitoring</p>

</div>

<div style="display:flex;flex-direction:column;align-items:center;width:100%;justify-content:space-between;flex-grow:1;">
    <img src="assets/pandalogo.jpg" alt="PanDA logo" style="max-height:32px;object-fit:contain;margin-bottom:4px;">
    <div style="background:#eef4fb;border:2px solid #1E5BA8;border-radius:8px;padding:8px 14px;text-align:center;width:95%;font-size:18px;font-weight:bold;color:#1E5BA8;">
      Local Orchestration
      <div style="font-size:15px;font-weight:normal;color:#333;margin-top:2px;">CSV chunks · environment tarball</div>
    </div>
    <div style="width:2px;height:10px;background:#888;"></div>
    <div style="font-size:14px;color:#666;margin:-2px 0;">Submit Task</div>
    <div style="width:2px;height:6px;background:#888;"></div>
    <div style="display:flex;gap:8px;width:95%;">
      <div style="background:#eaf4ea;border:2px solid #1E8449;border-radius:8px;padding:7px 8px;text-align:left;flex:1;font-size:17px;font-weight:bold;color:#1E8449;">
        PanDA JEDI
        <ul style="font-size:13px;font-weight:normal;color:#333;margin:3px 0 0 0;padding-left:14px;">
          <li>Generates jobs from tasks</li>
          <li>Brokers to optimal compute &amp; storage</li>
        </ul>
      </div>
      <div style="background:#eaf4ea;border:2px solid #1E8449;border-radius:8px;padding:7px 8px;text-align:left;flex:1;font-size:17px;font-weight:bold;color:#1E8449;">
        Harvester
        <ul style="font-size:13px;font-weight:normal;color:#333;margin:3px 0 0 0;padding-left:14px;">
          <li>Provisions pilots onto compute resources</li>
          <li>Relays status to PanDA server</li>
        </ul>
      </div>
      <div style="background:#eaf4ea;border:2px solid #1E8449;border-radius:8px;padding:7px 8px;text-align:left;flex:1;font-size:17px;font-weight:bold;color:#1E8449;">
        PanDA Cache
        <ul style="font-size:13px;font-weight:normal;color:#333;margin:3px 0 0 0;padding-left:14px;">
          <li>Stores job payload tarballs</li>
          <li>Fetched by pilots at runtime</li>
        </ul>
      </div>
    </div>
    <div style="width:2px;height:10px;background:#888;"></div>
    <div style="font-size:14px;color:#666;margin:-2px 0;">Assign Job</div>
    <div style="width:2px;height:6px;background:#888;"></div>
    <div style="background:#f3eef8;border:2px solid #7B3FA0;border-radius:8px;padding:8px 14px;text-align:center;width:95%;font-size:17px;font-weight:bold;color:#7B3FA0;">
      Worker Node
      <div style="font-size:14px;font-weight:normal;color:#333;margin-top:2px;">CVMFS Singularity · BG merge (opt.) · Sim + Reco</div>
      <div style="font-size:14px;font-weight:normal;color:#7B3FA0;margin-top:3px;font-style:italic;">Pilot job paradigm — blank pilots submitted to sites fetch jobs when CPUs are available (<a href="https://panda-wms.readthedocs.io/en/latest/architecture/pilot.html" style="color:#7B3FA0;text-decoration:underline;font-weight:bold;">pull</a>), or PanDA dispatches jobs directly to the batch system (<a href="https://panda-wms.readthedocs.io/en/latest/architecture/pilot.html" style="color:#7B3FA0;text-decoration:underline;font-weight:bold;">push</a>)</div>
    </div>
    <div style="width:2px;height:10px;background:#888;"></div>
    <div style="font-size:14px;color:#666;margin:-2px 0;">Register Output</div>
    <div style="width:2px;height:6px;background:#888;"></div>
    <div style="display:flex;gap:8px;width:95%;">
      <div style="background:#fdf6e3;border:2px solid #b07d00;border-radius:8px;padding:8px 8px;text-align:center;flex:1;font-size:16px;font-weight:bold;color:#b07d00;">
        JLab Rucio
        <div style="font-size:13px;font-weight:normal;color:#333;margin-top:2px;">Production output → storage elements</div>
      </div>
      <div style="background:#fdf6e3;border:2px solid #b07d00;border-radius:8px;padding:8px 8px;text-align:center;flex:1;font-size:16px;font-weight:bold;color:#b07d00;">
        BNL Rucio
        <div style="font-size:13px;font-weight:normal;color:#333;margin-top:2px;">PanDA pilot logs</div>
      </div>
    </div>
    <p class="muted" style="font-size:14px;margin-top:4px;font-weight:bold;text-align:center;">Current State of PanDA Integration for ePIC</p>
</div>

</div>

---

## Rucio for Data Management

<img src="assets/rucio.png" alt="Rucio logo" style="position:absolute;top:18px;right:56px;height:64px;object-fit:contain;">

<div class="grid-2" style="gap:20px;margin-bottom:10px;align-items:stretch;">
<div style="display:flex;flex-direction:column;gap:10px;">

<div style="background:#eef4fb;border-left:5px solid #1E5BA8;border-radius:4px;padding:12px 14px;font-size:19px;">
<strong style="color:#1E5BA8;font-size:21px;">Current State</strong><br>
<ul style="margin:6px 0 0 0;padding-left:18px;">
<li>Server at JLab in production since Jan 2025</li>
<li>File &amp; dataset-level DIDs</li>
<li>FTS transfers via subscription rules</li>
<li>X.509 auth for uploads; token-based auth with <strong>CILogon</strong> being developed</li>
</ul>
</div>

<div style="background:#eaf4ea;border-left:5px solid #1E8449;border-radius:4px;padding:12px 14px;font-size:19px;flex-grow:1;">
<strong style="color:#1E8449;font-size:21px;">Rucio Concepts</strong>
<table style="width:100%;border-collapse:collapse;margin-top:6px;font-size:18px;">
<tr style="background:#c8e6c9;"><th style="padding:6px 8px;text-align:left;">Term</th><th style="padding:6px 8px;text-align:left;">Meaning</th></tr>
<tr><td style="padding:5px 8px;"><strong>DID</strong></td><td style="padding:5px 8px;">Data Identifier — <code>scope:name</code> for any object</td></tr>
<tr style="background:#f0faf0;"><td style="padding:5px 8px;"><strong>Scope</strong></td><td style="padding:5px 8px;">Namespace prefix, e.g. <code>epic</code></td></tr>
<tr><td style="padding:5px 8px;"><strong>File</strong></td><td style="padding:5px 8px;">Atomic unit with checksum &amp; size</td></tr>
<tr style="background:#f0faf0;"><td style="padding:5px 8px;"><strong>Dataset</strong></td><td style="padding:5px 8px;">Ordered collection of files</td></tr>
<tr><td style="padding:5px 8px;"><strong>Container</strong></td><td style="padding:5px 8px;">Collection of datasets or containers</td></tr>
</table>
</div>

</div>
<div style="display:flex;flex-direction:column;gap:10px;">

<div style="background:#fdf6e3;border-left:5px solid #b07d00;border-radius:4px;padding:12px 14px;font-size:19px;">
<strong style="color:#b07d00;font-size:21px;">Naming Convention</strong><br>
<code style="font-size:15px;">epic:/dataLevel/path/to/dataset/file</code><br>
<code style="font-size:15px;">protocol://host:port/prefix/dataLevel/...</code>
<div style="margin-top:8px;font-size:16px;"><strong>Strategy:</strong> full filesystem path reflected in DID for human readability</div>
<div style="margin-top:4px;font-size:16px;color:#b07d00;"><strong>Limitations:</strong>
<ul style="margin:4px 0 0 0;padding-left:18px;">
<li>Rucio character limits constrain deeply nested paths</li>
<li>PanDA interprets <code>/</code> as container boundary separator</li>
</ul>
</div>
</div>

<div style="background:#eaf4ea;border-left:5px solid #1E8449;border-radius:4px;padding:12px 14px;font-size:19px;flex-grow:1;">
<strong style="color:#1E8449;font-size:21px;">Rucio Metadata Rollout</strong><br>
<ul style="margin:6px 0 0 0;padding-left:18px;">
<li>Data made <strong>Findable</strong> and <strong>Accessible</strong> under <strong>FAIR data principles</strong>
  <ul style="margin:4px 0 0 0;padding-left:18px;">
  <li>Metadata tags (energy, EvGen, PWG, detector geometry, …) for precise discovery and filtering</li>
  <li>Rucio CLI available inside the <a href="https://github.com/eic/containers" style="color:#1E8449;text-decoration:underline;">eic-shell</a> container</li>
  </ul>
</li>
<li>Rucio tools introduced to collaboration via user learning &amp; training efforts <span class="muted" style="font-size:0.85em;">(<a href="https://indico.cern.ch/event/1471803/contributions/6968308/" style="color:#5f6b7a;text-decoration:underline;">See Alexandr Prozorov's talk</a>)</span></li>
</ul>
</div>

</div>
</div>

<div style="display:flex;justify-content:space-between;margin-top:4px;">
<p class="muted" style="font-size:15px;margin:0;">Further reading: <a href="https://indico.cern.ch/event/1545309/contributions/6733613/attachments/3168793/5632824/Rucio_workshop_v5.pdf" style="color:#2f6f8f;text-decoration:underline;">Rucio for ePIC — Rucio Workshop 2025</a></p>
<p class="muted" style="font-size:15px;margin:0;">Tutorial: <a href="https://eic.github.io/tutorial-file-access/" style="color:#2f6f8f;text-decoration:underline;">EIC File Access</a></p>
</div>

---

## AI-Powered Monitoring and Self-Documentation

<div class="grid-2" style="gap:20px;">
<div style="display:flex;flex-direction:column;gap:6px;font-size:18px;height:100%;">

<div style="font-size:20px;font-weight:bold;color:#123f6d;margin-bottom:2px;">MCP Server Stack</div>

<div style="background:#eef4fb;border-left:4px solid #1E5BA8;border-radius:4px;padding:6px 10px;flex:1;">
<strong style="color:#1E5BA8;font-size:19px;">Production Systems</strong><br>
<a href="https://github.com/BNLnpps/SWF-monitor" style="color:#2f6f8f;text-decoration:underline;"><code>SWF-monitor</code></a> — PanDA jobs/tasks/queues, PCS tags, error summaries<br>
<a href="https://github.com/eic/rucio-eic-mcp-server" style="color:#2f6f8f;text-decoration:underline;"><code>rucio-eic-mcp-server</code></a> — DIDs, replicas, replication rules
</div>

<div style="background:#f3eef8;border-left:4px solid #7B3FA0;border-radius:4px;padding:6px 10px;flex:1;">
<strong style="color:#7B3FA0;font-size:19px;">Storage & Data</strong><br>
<a href="https://github.com/eic/xrootd-mcp-server" style="color:#2f6f8f;text-decoration:underline;"><code>xrootd-mcp-server</code></a> — browse &amp; read files on EIC storage<br>
<a href="https://github.com/eic/uproot-mcp-server" style="color:#2f6f8f;text-decoration:underline;"><code>uproot-mcp-server</code></a> — inspect ROOT file structure, histogram branches
</div>

<div style="background:#eaf4ea;border-left:4px solid #1E8449;border-radius:4px;padding:6px 10px;flex:1;">
<strong style="color:#1E8449;font-size:19px;">Code & Documentation</strong><br>
<a href="https://github.com/BNLNPPS/lxr-mcp-server" style="color:#2f6f8f;text-decoration:underline;"><code>lxr-mcp-server</code></a> — cross-reference EIC source code<br>
<a href="https://github.com/github/github-mcp-server" style="color:#2f6f8f;text-decoration:underline;"><code>github-mcp-server</code></a> — issues, PRs, discussions<br>
<a href="https://github.com/eic/zenodo-mcp-server" style="color:#2f6f8f;text-decoration:underline;"><code>zenodo-mcp-server</code></a> — search &amp; download records<br>
<a href="https://github.com/eic/corun-mcp-server" style="color:#2f6f8f;text-decoration:underline;"><code>corun-mcp-server</code></a> — generate ePIC documentation pages
</div>

</div>
<div style="display:flex;flex-direction:column;gap:6px;font-size:17px;">

<div style="font-size:20px;font-weight:bold;color:#123f6d;margin-bottom:2px;">Examples: AI Chatbot on Mattermost</div>

<div style="background:#f0f5f9;border-left:4px solid #2f6f8f;border-radius:6px;padding:7px 14px;font-size:17px;font-style:italic;color:#1f2933;">
  "Summarize failed jobs on Perlmutter in the month of April and specify the most dominant error"
</div>
<div class="figure">
  <img src="assets/example-agent-response.jpg" alt="AI chatbot response on Mattermost" style="max-height:195px;width:100%;object-fit:contain;border-radius:6px;border:1px solid #c0cdd8;image-rendering:crisp-edges;">
</div>

<div style="background:#f0f5f9;border-left:4px solid #7B3FA0;border-radius:6px;padding:7px 14px;font-size:17px;font-style:italic;color:#1f2933;">
  "List what's available under the /volatile/eic/EPIC/EVGEN directory on JLab XRootD"
</div>
<div class="figure">
  <img src="assets/example-xrootd-response.jpg" alt="AI chatbot XRootD response on Mattermost" style="max-height:195px;width:100%;object-fit:contain;border-radius:6px;border:1px solid #c0cdd8;image-rendering:crisp-edges;">
</div>

</div>
</div>

---

<!-- _class: compact -->

## Physics Configuration System <span style="font-size:22px;color:#b07d00;font-weight:bold;">⚠ beta</span>

PCS follows a **user-centered design** — mapping collaboration requests to job settings, automating request tracking, and bridging the gap between physics groups and production infrastructure. Authoritative provenance and configuration record for simulation tasks, with direct PanDA job injection as the long-term goal.

<div style="display:grid;grid-template-columns:0.6fr 1.4fr;gap:24px;align-items:start;">
<div>

### Stores Per Task

<div style="display:grid;grid-template-columns:1fr 1fr;gap:6px;">
<div style="background:#eef4fb;border:1px solid #b0c8e8;border-radius:4px;padding:5px 8px;font-size:18px;">Physics &amp; EvGen tags</div>
<div style="background:#eef4fb;border:1px solid #b0c8e8;border-radius:4px;padding:5px 8px;font-size:18px;">Simulation &amp; reco tags</div>
<div style="background:#eef4fb;border:1px solid #b0c8e8;border-radius:4px;padding:5px 8px;font-size:18px;">Input/output datasets</div>
<div style="background:#eef4fb;border:1px solid #b0c8e8;border-radius:4px;padding:5px 8px;font-size:18px;">Workflow mode &amp; stages</div>
<div style="background:#eef4fb;border:1px solid #b0c8e8;border-radius:4px;padding:5px 8px;font-size:18px;">Validation status</div>
<div style="background:#eef4fb;border:1px solid #b0c8e8;border-radius:4px;padding:5px 8px;font-size:18px;">Public catalogue entry</div>
<div style="background:#eef4fb;border:1px solid #b0c8e8;border-radius:4px;padding:5px 8px;font-size:18px;">Downstream task IDs</div>
<div style="background:#eef4fb;border:1px solid #b0c8e8;border-radius:4px;padding:5px 8px;font-size:18px;">Request state</div>
</div>

</div>
<div>

<div class="figure">
  <img src="assets/image11_sharp.jpg" alt="PCS screenshot" style="max-height:420px;width:100%;object-fit:contain;border-radius:4px;border:1px solid #c0cdd8;image-rendering:crisp-edges;">
</div>

</div>
</div>

<div style="background:#f0f5f9;border-left:5px solid #2f6f8f;border-radius:4px;padding:10px 16px;font-size:19px;margin-top:10px;">
<strong style="color:#123f6d;">Preliminary IAM Model — </strong>ePIC Phonebook defines groups/roles → <strong>COmanage</strong> translates to registry groups → <strong>CILogon</strong> issues tokens (JWTs) → PCS enforces local community permissions.
</div>


---

<!-- _class: compact -->

## PCS in Action: Example PanDA Task

<p style="font-size:18px;background:#fdf6e3;border-left:4px solid #b07d00;padding:8px 14px;border-radius:4px;margin-bottom:10px;">PCS is inspired by the <strong><a href="https://cds.cern.ch/record/2649430" style="color:#b07d00;text-decoration:underline;">ATLAS Metadata Interface (AMI)</a></strong> — Odier et al., EPJ Web Conf. 214 (2019) 05046</p>

<div style="display:grid;grid-template-columns:0.75fr 1.25fr;gap:20px;align-items:start;">
<div style="font-size:19px;">

### Dataset Naming Convention

<div style="background:#f0f5f9;border-left:4px solid #2f6f8f;border-radius:4px;padding:8px 12px;font-size:16px;font-family:monospace;word-break:break-all;margin-bottom:10px;">
group.EIC.<strong>26.02.0</strong>.<strong>epic_craterlake</strong>.<strong>p4017</strong>.<strong>e7</strong>.<strong>s1</strong>.<strong>r1</strong>
</div>

<div style="display:grid;grid-template-columns:auto 1fr;gap:4px 10px;font-size:18px;">
<div style="color:#2f6f8f;font-weight:bold;">26.02.0</div><div>Campaign version</div>
<div style="color:#2f6f8f;font-weight:bold;">epic_craterlake</div><div>Detector geometry</div>
<div style="color:#2f6f8f;font-weight:bold;">p4017</div><div>Physics tag</div>
<div style="color:#2f6f8f;font-weight:bold;">e7</div><div>EvGen tag</div>
<div style="color:#2f6f8f;font-weight:bold;">s1</div><div>Simulation tag</div>
<div style="color:#2f6f8f;font-weight:bold;">r1</div><div>Reconstruction tag</div>
</div>

### PanDA Jargon

<div style="display:grid;grid-template-columns:auto 1fr;gap:4px 10px;font-size:18px;margin-top:6px;">
<div style="color:#7B3FA0;font-weight:bold;">Task</div><div>Unit of work submitted to PanDA; maps to one PCS dataset</div>
<div style="color:#7B3FA0;font-weight:bold;">Job</div><div>Individual pilot execution within a task</div>
<div style="color:#7B3FA0;font-weight:bold;">Queue</div><div>Site-level resource endpoint for job brokerage</div>
<div style="color:#7B3FA0;font-weight:bold;">JUG_XL</div><div>ePIC software container image tag</div>
</div>

</div>
<div>

<div class="figure">
  <img src="assets/example-panda-task-on-pcs-sharp.jpg" alt="Example PanDA task on PCS" style="width:100%;object-fit:contain;border-radius:4px;border:1px solid #c0cdd8;image-rendering:crisp-edges;">
</div>

</div>
</div>

---

## Simulation Payload Optimizations: Background Merging

<div class="grid-2" style="gap:24px;align-items:start;">
<div style="font-size:21px;">

Every reconstructed event is an overlay of signal and multiple background sources. The slowest detector subsystem has a **2 µs readout window**:

<div style="font-size:16px;color:#5f6b7a;margin-bottom:4px;">Background inputs at 10×275 GeV</div>
<div style="display:grid;grid-template-columns:1.35fr auto auto;gap:4px 12px;font-size:16px;background:#f0f5f9;border-radius:6px;padding:10px 14px;margin-bottom:8px;">
<div style="font-weight:bold;color:#123f6d;">Process</div><div style="font-weight:bold;color:#123f6d;text-align:right;">Frequency</div><div style="font-weight:bold;color:#123f6d;text-align:right;">Status</div>
<div><strong>Synchrotron radiation (synrad)</strong></div><div style="color:#C0392B;font-weight:bold;text-align:right;">13.277 GHz</div><div style="text-align:right;">2000</div>
<div>Electron beam gas</div><div style="color:#7B3FA0;text-align:right;">3.177 MHz</div><div style="text-align:right;">3000</div>
<div>Electron Coulomb</div><div style="color:#7B3FA0;text-align:right;">29.56 kHz</div><div style="text-align:right;">4000</div>
<div>Electron Touschek</div><div style="color:#7B3FA0;text-align:right;">233.5 kHz</div><div style="text-align:right;">5000</div>
<div>Proton beam gas</div><div style="color:#7B3FA0;text-align:right;">32.6 kHz</div><div style="text-align:right;">6000</div>
<div style="color:#2f6f8f;font-weight:bold;">Signal (e.g. DIS)</div><div style="color:#2f6f8f;font-weight:bold;text-align:right;">500 kHz</div><div style="text-align:right;">-</div>
</div>

Synrad alone arrives **~26,554× per frame** relative to a 500 kHz signal in a 2 µs window. Re-simulating background signals per physics sample is prohibitively expensive.

<div style="background:#eaf4ea;border-left:4px solid #1E8449;border-radius:4px;padding:8px 12px;font-size:19px;margin-top:6px;">
<strong>Solution:</strong> simulate background pools once and merge statistically at the 2 µs frame level — one synrad campaign reused across <strong>all physics analyses</strong>. Processes tagged via <code>MCParticles.generatorStatus</code> for post-hoc separation.
</div>


</div>
<div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:16px;font-size:17px;">

<div style="background:#fffde7;border:2px solid #f0c040;border-radius:8px;padding:12px 10px;">
<div style="font-weight:bold;font-size:18px;color:#7a5c00;text-align:center;margin-bottom:10px;">HepMC3 Merger Workflow</div>
<div style="display:flex;flex-direction:column;align-items:center;gap:4px;">
  <div style="background:#123f6d;color:#fff;border-radius:5px;padding:6px 14px;text-align:center;width:80%;">MC Generators<br><span style="font-size:14px;opacity:0.85;">Signal + Background</span></div>
  <div style="color:#1E8449;font-weight:bold;font-size:20px;">↓↓↓</div>
  <div style="background:#1E8449;color:#fff;border-radius:5px;padding:6px 14px;text-align:center;width:80%;font-weight:bold;">HEPMC Merger</div>
  <div style="color:#555;font-size:18px;">↓</div>
  <div style="background:#C0392B;color:#fff;border-radius:5px;padding:6px 14px;text-align:center;width:80%;">Simulation</div>
  <div style="color:#555;font-size:18px;">↓</div>
  <div style="background:#626567;color:#fff;border-radius:5px;padding:6px 14px;text-align:center;width:80%;">Digitization</div>
  <div style="color:#555;font-size:18px;">↓</div>
  <div style="background:#1E5BA8;color:#fff;border-radius:5px;padding:6px 14px;text-align:center;width:80%;">Reconstruction</div>
  <div style="color:#555;font-size:18px;">↓</div>
  <div style="background:#7B3FA0;color:#fff;border-radius:5px;padding:6px 14px;text-align:center;width:80%;">Analysis</div>
</div>
</div>

<div style="background:#e8f4fb;border:2px solid #2f6f8f;border-radius:8px;padding:12px 10px;">
<div style="font-weight:bold;font-size:18px;color:#123f6d;text-align:center;margin-bottom:10px;">EDM4hep Merger Workflow</div>
<div style="display:flex;flex-direction:column;align-items:center;gap:4px;">
  <div style="background:#123f6d;color:#fff;border-radius:5px;padding:6px 14px;text-align:center;width:80%;">MC Generators<br><span style="font-size:14px;opacity:0.85;">Signal + Background</span></div>
  <div style="color:#555;font-size:18px;">↓</div>
  <div style="background:#C0392B;color:#fff;border-radius:5px;padding:6px 14px;text-align:center;width:80%;">Simulation</div>
  <div style="color:#1E8449;font-weight:bold;font-size:20px;">↓↓↓</div>
  <div style="background:#1E8449;color:#fff;border-radius:5px;padding:6px 14px;text-align:center;width:80%;font-weight:bold;">EDM4hep Merger</div>
  <div style="color:#555;font-size:18px;">↓</div>
  <div style="background:#626567;color:#fff;border-radius:5px;padding:6px 14px;text-align:center;width:80%;">Digitization</div>
  <div style="color:#555;font-size:18px;">↓</div>
  <div style="background:#1E5BA8;color:#fff;border-radius:5px;padding:6px 14px;text-align:center;width:80%;">Reconstruction</div>
  <div style="color:#555;font-size:18px;">↓</div>
  <div style="background:#7B3FA0;color:#fff;border-radius:5px;padding:6px 14px;text-align:center;width:80%;">Analysis</div>
</div>
</div>

</div>
<p class="muted" style="font-size:17px;margin-top:6px;font-weight:bold;text-align:center;">Merge before simulation (HepMC3) vs. after simulation (EDM4hep)</p>
<div style="background:#f0f5f9;border-left:4px solid #2f6f8f;border-radius:4px;padding:10px 14px;font-size:18px;margin-top:8px;">
Simulated background data with distinguishability through <code>generatorStatus</code> code offsets is relevant to streaming reconstruction algorithm development <span class="muted">(<a href="https://indico.cern.ch/event/1471803/contributions/6967323/" style="color:#5f6b7a;text-decoration:underline;">See Takuya Kumaoka's talk</a>)</span>
</div>

</div>
</div>

---

<!-- _class: small -->

## Summary: Scaling ePIC Simulation Production

### Experiment and Collaboration

- Primary detector at the EIC, realized by the ePIC Collaboration in partnership with the EIC Project, BNL and JLab
- Worldwide footprint: more than 1100 collaborators across 181 institutions in 25 countries

### Infrastructure and Resource Evolution

- Monthly simulation campaigns run on HTC and HPC resources — opportunistic sites via OSG and allocated domestic &amp; international sites — in preparation for the TDR
- International resources from Canada, Italy, NERSC, JLab, BNL, and university HPC sites are being integrated into production
- Storage at BNL and JLab is scaling with compute demand

### Workload and Data Management

- PanDA WMS / iDDS enables automated production workflows and job brokerage
- Rucio enables distributed data management, replication, and user data access
- PCS records production configuration and provenance across campaigns

### Payload Optimizations

- Optimization of expensive background mixed simulations

<div style="background:#eef4fb;border-left:5px solid #1E5BA8;border-radius:4px;padding:7px 12px;font-size:17px;margin-top:8px;">
ePIC builds on Grid computing experience and lessons learnt from the LHC experiments — and contributes back to the community through our development efforts.
</div>

---

<!-- _class: compact -->

## Related ePIC Talks at CHEP 2026

<div class="title-top" style="margin-bottom:8px;">
  <img src="assets/epic_logo.png" alt="ePIC logo">
  <img src="assets/bnl_logo.png" alt="Brookhaven National Laboratory logo">
  <img src="assets/jefferson_lab_logo.png" alt="Jefferson Lab logo">
  <img src="assets/office_of_science_logo.png" alt="Office of Science logo">
</div>

<div style="display:flex;flex-direction:column;gap:12px;margin-top:8px;font-size:20px;">

<div style="background:#eef4fb;border-left:5px solid #1E5BA8;border-radius:4px;padding:10px 16px;">
<strong style="color:#1E5BA8;"><a href="https://indico.cern.ch/event/1471803/contributions/6967120/" style="color:#1E5BA8;text-decoration:underline;">The ePIC Streaming Computing Model</a></strong><br>
<span class="muted">Holly Szumila-Vance</span>
</div>

<div style="background:#eaf4ea;border-left:5px solid #1E8449;border-radius:4px;padding:10px 16px;">
<strong style="color:#1E8449;"><a href="https://indico.cern.ch/event/1471803/contributions/6967984/" style="color:#1E8449;text-decoration:underline;">Exploring Potential Pathways to Accelerate ePIC Detector Simulation</a></strong><br>
<span class="muted">Sakib Rahman</span>
</div>

<div style="background:#f3eef8;border-left:5px solid #7B3FA0;border-radius:4px;padding:10px 16px;">
<strong style="color:#7B3FA0;"><a href="https://indico.cern.ch/event/1471803/contributions/6967323/" style="color:#7B3FA0;text-decoration:underline;">Development of Streaming Data Reconstruction for ePIC Experiment at EIC</a></strong><br>
<span class="muted">Takuya Kumaoka</span>
</div>

<div style="background:#fdf6e3;border-left:5px solid #b07d00;border-radius:4px;padding:10px 16px;">
<strong style="color:#b07d00;"><a href="https://indico.cern.ch/event/1471803/contributions/6968308/" style="color:#b07d00;text-decoration:underline;">ePIC User Learning Training and Documentation Strategies</a></strong><br>
<span class="muted">Alexandr Prozorov</span>
</div>

</div>
