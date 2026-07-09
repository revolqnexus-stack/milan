# -*- coding: utf-8 -*-
"""Generate complete GNM CHN-I study app: chn.html"""
from pathlib import Path

OUT = Path(r"c:\Users\eathe\milan\chn.html")

CSS = r"""
  :root {
    --bg: #F0F4F8;
    --card: #FFFFFF;
    --primary: #1A73E8;
    --primary-dark: #1558B0;
    --red: #EA4335;
    --red-light: #FDECEA;
    --yellow: #F9A825;
    --yellow-light: #FFF8E1;
    --green: #34A853;
    --green-light: #E8F5E9;
    --text: #1C1C1E;
    --subtext: #5F6368;
    --border: #E8EAED;
    --nav-h: 64px;
  }
  [data-theme="dark"] {
    --bg: #0F1117;
    --card: #1C1F26;
    --text: #F1F3F4;
    --subtext: #9AA0A6;
    --border: #2D3035;
    --red-light: #2D1210;
    --yellow-light: #2D2200;
    --green-light: #0D2518;
    --primary: #4A90E2;
  }
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body {
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
    background: var(--bg);
    color: var(--text);
    font-size: 16px;
    line-height: 1.6;
    padding-bottom: calc(var(--nav-h) + 20px);
    transition: background 0.3s, color 0.3s;
  }
  .topbar {
    position: sticky; top: 0; z-index: 100;
    background: var(--card);
    border-bottom: 1px solid var(--border);
    padding: 12px 16px;
    display: flex; align-items: center; gap: 10px;
  }
  .topbar-title { font-size: 17px; font-weight: 700; color: var(--primary); flex: 1; }
  .topbar-sub { font-size: 12px; color: var(--subtext); }
  .theme-btn {
    background: var(--bg); border: 1px solid var(--border);
    border-radius: 20px; padding: 6px 12px; font-size: 14px;
    cursor: pointer; color: var(--text);
  }
  .search-wrap { padding: 12px 16px; }
  .search-input {
    width: 100%; padding: 12px 16px; border-radius: 24px;
    border: 1.5px solid var(--border); background: var(--card);
    font-size: 16px; color: var(--text); outline: none;
  }
  .search-input:focus { border-color: var(--primary); }
  .page { display: none; }
  .page.active { display: block; }
  .bottom-nav {
    position: fixed; bottom: 0; left: 0; right: 0; z-index: 200;
    background: var(--card);
    border-top: 1px solid var(--border);
    display: flex; height: var(--nav-h);
  }
  .nav-btn {
    flex: 1; display: flex; flex-direction: column;
    align-items: center; justify-content: center;
    gap: 3px; background: none; border: none;
    cursor: pointer; color: var(--subtext);
    font-size: 10px; font-weight: 500;
    padding: 8px 4px; transition: color 0.2s;
    -webkit-tap-highlight-color: transparent;
  }
  .nav-btn.active { color: var(--primary); }
  .nav-btn svg { width: 22px; height: 22px; }
  .section-head {
    padding: 18px 16px 8px;
    font-size: 13px; font-weight: 700;
    text-transform: uppercase; letter-spacing: 0.08em;
    color: var(--subtext);
  }
  .card {
    margin: 0 12px 10px;
    background: var(--card);
    border-radius: 16px;
    overflow: hidden;
    border: 1px solid var(--border);
  }
  .card-header {
    padding: 14px 16px;
    display: flex; align-items: center; gap: 10px;
    cursor: pointer; -webkit-tap-highlight-color: transparent;
    user-select: none;
  }
  .card-header:active { opacity: 0.7; }
  .badge {
    font-size: 11px; font-weight: 700; padding: 3px 8px;
    border-radius: 20px; white-space: nowrap; flex-shrink: 0;
  }
  .badge-red { background: var(--red-light); color: var(--red); }
  .badge-yellow { background: var(--yellow-light); color: #B06000; }
  .badge-green { background: var(--green-light); color: var(--green); }
  .card-title { font-size: 15px; font-weight: 600; flex: 1; }
  .card-sub { font-size: 12px; color: var(--subtext); }
  .chevron { margin-left: auto; font-size: 18px; color: var(--subtext); transition: transform 0.25s; flex-shrink: 0; }
  .card-body { display: none; padding: 0 16px 16px; }
  .card-body.open { display: block; }
  .card.expanded .chevron { transform: rotate(180deg); }
  .done-row { display: flex; align-items: center; gap: 8px; margin-bottom: 12px; }
  .done-checkbox {
    width: 22px; height: 22px; border-radius: 6px;
    border: 2px solid var(--border); background: var(--bg);
    cursor: pointer; display: flex; align-items: center; justify-content: center;
    flex-shrink: 0; transition: all 0.2s;
  }
  .done-checkbox.checked { background: var(--green); border-color: var(--green); color: #fff; font-size: 14px; }
  .done-label { font-size: 13px; color: var(--subtext); cursor: pointer; }
  .ans-block { font-size: 14px; line-height: 1.7; }
  .ans-block h4 { font-size: 13px; font-weight: 700; color: var(--primary); margin: 12px 0 4px; text-transform: uppercase; letter-spacing: 0.05em; }
  .ans-block p { margin-bottom: 8px; }
  .ans-block ul { padding-left: 18px; margin-bottom: 8px; }
  .ans-block ul li { margin-bottom: 4px; }
  .ans-block ol { padding-left: 18px; margin-bottom: 8px; }
  .ans-block ol li { margin-bottom: 4px; }
  .highlight { background: #FFF176; padding: 1px 4px; border-radius: 4px; color: #333; font-weight: 600; }
  .tip-box {
    background: var(--yellow-light); border-left: 3px solid var(--yellow);
    padding: 10px 12px; border-radius: 0 8px 8px 0; margin: 10px 0;
    font-size: 13px;
  }
  .trick-box {
    background: var(--red-light); border-left: 3px solid var(--red);
    padding: 10px 12px; border-radius: 0 8px 8px 0; margin: 10px 0;
    font-size: 13px;
  }
  .diagram-box {
    background: var(--bg); border: 1.5px dashed var(--border);
    border-radius: 12px; padding: 14px; margin: 10px 0;
    font-family: monospace; font-size: 13px; line-height: 1.8;
    white-space: pre; overflow-x: auto;
    color: var(--text);
  }
  .year-tags { display: flex; flex-wrap: wrap; gap: 4px; margin: 8px 0; }
  .year-tag { font-size: 10px; background: var(--border); padding: 2px 7px; border-radius: 10px; color: var(--subtext); }
  .meta-row { display: flex; gap: 8px; flex-wrap: wrap; margin-bottom: 10px; align-items: center; }
  .goal-banner {
    margin: 12px; border-radius: 20px;
    background: linear-gradient(135deg, #1A73E8 0%, #0D47A1 100%);
    color: #fff; padding: 20px; text-align: center;
  }
  .goal-banner h1 { font-size: 26px; font-weight: 800; }
  .goal-banner p { font-size: 14px; opacity: 0.9; margin-top: 4px; }
  .stats-row { display: flex; gap: 8px; margin: 0 12px 10px; }
  .stat-box {
    flex: 1; background: var(--card); border-radius: 14px;
    padding: 14px; text-align: center; border: 1px solid var(--border);
  }
  .stat-num { font-size: 24px; font-weight: 800; color: var(--primary); }
  .stat-label { font-size: 11px; color: var(--subtext); margin-top: 2px; }
  .exam-pattern { margin: 0 12px 12px; }
  .pattern-table { width: 100%; border-collapse: collapse; font-size: 13px; }
  .pattern-table th { background: var(--primary); color: #fff; padding: 8px 10px; text-align: left; }
  .pattern-table th:first-child { border-radius: 8px 0 0 0; }
  .pattern-table th:last-child { border-radius: 0 8px 0 0; }
  .pattern-table td { padding: 8px 10px; border-bottom: 1px solid var(--border); background: var(--card); }
  .pattern-table tr:last-child td { border-bottom: none; }
  .pattern-table tr:last-child td:first-child { border-radius: 0 0 0 8px; }
  .pattern-table tr:last-child td:last-child { border-radius: 0 0 8px 0; }
  .strategy-box {
    margin: 0 12px 12px; background: var(--green-light);
    border-radius: 14px; padding: 14px; border: 1px solid #A5D6A7;
  }
  .strategy-box h3 { font-size: 14px; font-weight: 700; color: var(--green); margin-bottom: 8px; }
  .strategy-box p { font-size: 13px; line-height: 1.7; }
  .filter-bar { display: flex; gap: 8px; padding: 4px 12px 12px; overflow-x: auto; }
  .filter-bar::-webkit-scrollbar { display: none; }
  .filter-btn {
    white-space: nowrap; padding: 7px 14px; border-radius: 20px;
    border: 1.5px solid var(--border); background: var(--card);
    font-size: 13px; font-weight: 600; cursor: pointer; color: var(--text);
    -webkit-tap-highlight-color: transparent;
  }
  .filter-btn.active-filter { background: var(--primary); border-color: var(--primary); color: #fff; }
  .mock-nav { display: flex; gap: 6px; padding: 0 12px 10px; overflow-x: auto; }
  .mock-nav::-webkit-scrollbar { display: none; }
  .mock-btn {
    flex-shrink: 0; padding: 8px 16px; border-radius: 20px;
    border: 1.5px solid var(--border); background: var(--card);
    font-size: 13px; font-weight: 600; cursor: pointer; color: var(--text);
  }
  .mock-btn.active-mock { background: var(--primary); border-color: var(--primary); color: #fff; }
  .mock-paper { display: none; }
  .mock-paper.active-paper { display: block; }
  .mock-toggle { display: flex; gap: 6px; margin: 0 12px 10px; }
  .mock-toggle-btn {
    flex: 1; padding: 10px; border-radius: 12px;
    border: 1.5px solid var(--border); background: var(--card);
    font-size: 14px; font-weight: 600; cursor: pointer; color: var(--text);
    -webkit-tap-highlight-color: transparent;
  }
  .mock-toggle-btn.active-toggle { background: var(--primary); border-color: var(--primary); color: #fff; }
  .q-view, .a-view { display: none; }
  .q-view.show, .a-view.show { display: block; }
  .q-item {
    margin: 0 12px 8px; background: var(--card);
    border-radius: 14px; padding: 14px; border: 1px solid var(--border);
  }
  .q-num { font-size: 11px; font-weight: 700; color: var(--primary); margin-bottom: 4px; }
  .q-text { font-size: 14px; font-weight: 600; }
  .q-marks { font-size: 12px; color: var(--subtext); margin-top: 4px; }
  .diff-easy { color: var(--green); }
  .diff-med { color: #B06000; }
  .diff-hard { color: var(--red); }
  .a-item {
    margin: 0 12px 10px; background: var(--card);
    border-radius: 14px; padding: 14px; border: 1px solid var(--border);
  }
  .a-qtext { font-size: 13px; font-weight: 700; color: var(--primary); margin-bottom: 8px; }
  .quick-tabs { display: flex; gap: 6px; padding: 4px 12px 10px; overflow-x: auto; }
  .quick-tabs::-webkit-scrollbar { display: none; }
  .quick-tab-btn {
    flex-shrink: 0; padding: 8px 14px; border-radius: 20px;
    border: 1.5px solid var(--border); background: var(--card);
    font-size: 12px; font-weight: 600; cursor: pointer; color: var(--text);
    -webkit-tap-highlight-color: transparent;
  }
  .quick-tab-btn.active-qtab { background: var(--primary); border-color: var(--primary); color: #fff; }
  .quick-section { display: none; }
  .quick-section.show { display: block; }
  .def-row { margin: 0 12px 8px; background: var(--card); border-radius: 12px; padding: 12px 14px; border: 1px solid var(--border); }
  .def-word { font-size: 13px; font-weight: 700; color: var(--primary); }
  .def-meaning { font-size: 13px; margin-top: 3px; }
  .val-table { margin: 0 12px; width: calc(100% - 24px); border-collapse: collapse; font-size: 13px; }
  .val-table th { background: var(--primary); color: #fff; padding: 8px; text-align: left; }
  .val-table td { padding: 8px; border-bottom: 1px solid var(--border); background: var(--card); vertical-align: top; }
  .val-table tr:last-child td { border-bottom: none; }
  .day-box { margin: 0 12px 10px; border-radius: 16px; padding: 14px; border: 1px solid var(--border); }
  .day-box.d1 { background: linear-gradient(135deg, #E3F2FD, #fff); border-color: #90CAF9; }
  .day-box.d2 { background: linear-gradient(135deg, #F3E5F5, #fff); border-color: #CE93D8; }
  .day-box.d3 { background: linear-gradient(135deg, #E8F5E9, #fff); border-color: #A5D6A7; }
  .day-box h3 { font-size: 15px; font-weight: 700; margin-bottom: 8px; }
  .day-box ul { padding-left: 18px; font-size: 13px; }
  .day-box ul li { margin-bottom: 5px; }
  .skip-box { background: var(--red-light); border-radius: 10px; padding: 8px 12px; margin-top: 8px; font-size: 12px; color: var(--red); }
  .template-tabs { display: flex; gap: 6px; padding: 4px 12px 10px; overflow-x: auto; }
  .template-tabs::-webkit-scrollbar { display: none; }
  .tmpl-tab-btn {
    flex-shrink: 0; padding: 8px 14px; border-radius: 20px;
    border: 1.5px solid var(--border); background: var(--card);
    font-size: 12px; font-weight: 600; cursor: pointer; color: var(--text);
  }
  .tmpl-tab-btn.active-tmpl { background: var(--primary); border-color: var(--primary); color: #fff; }
  .tmpl-section { display: none; }
  .tmpl-section.show { display: block; }
  .template-card { margin: 0 12px 10px; background: var(--card); border-radius: 14px; padding: 14px; border: 1px solid var(--border); }
  .step-row { display: flex; gap: 10px; align-items: flex-start; margin-bottom: 12px; }
  .step-num { width: 28px; height: 28px; border-radius: 50%; background: var(--primary); color: #fff; font-size: 13px; font-weight: 700; display: flex; align-items: center; justify-content: center; flex-shrink: 0; }
  .step-content { flex: 1; font-size: 14px; }
  .step-content strong { display: block; font-size: 13px; color: var(--primary); margin-bottom: 2px; }
  .marks-pill { display: inline-block; background: var(--green-light); color: var(--green); font-size: 11px; font-weight: 700; padding: 2px 8px; border-radius: 10px; margin-left: 6px; }
  .progress-bar-wrap { background: var(--border); border-radius: 20px; height: 8px; margin: 4px 0 12px; }
  .progress-bar { height: 8px; border-radius: 20px; background: var(--green); transition: width 0.5s; }
  .prob-badge { font-size: 11px; font-weight: 700; padding: 4px 10px; border-radius: 20px; display: inline-block; margin: 2px; }
  .prob-vhigh { background: var(--red-light); color: var(--red); }
  .prob-high { background: var(--yellow-light); color: #B06000; }
  .prob-medium { background: var(--green-light); color: var(--green); }
  .exam-scorecard { display: flex; flex-wrap: wrap; gap: 6px; margin-bottom: 12px; align-items: center; }
  .meta-pill { font-size: 11px; background: var(--bg); border: 1px solid var(--border); padding: 3px 8px; border-radius: 12px; color: var(--subtext); }
  .exam-grid { display: grid; gap: 8px; margin-bottom: 10px; }
  .exam-block { background: var(--bg); border-radius: 10px; padding: 10px 12px; font-size: 13px; border-left: 3px solid var(--primary); }
  .exam-block h5 { font-size: 12px; font-weight: 700; color: var(--primary); margin-bottom: 4px; text-transform: uppercase; letter-spacing: 0.04em; }
  .mistake-block { border-left-color: var(--red); background: var(--red-light); }
  .mini-table { width: 100%; border-collapse: collapse; font-size: 12px; margin-top: 4px; }
  .mini-table th, .mini-table td { padding: 4px 6px; border-bottom: 1px solid var(--border); text-align: left; }
  .rev-tabs { display: grid; grid-template-columns: 1fr 1fr; gap: 8px; margin: 10px 0; }
  .rev-box { border-radius: 10px; padding: 10px; font-size: 12px; }
  .fast-rev { background: #E3F2FD; border: 1px solid #90CAF9; }
  .last-rev { background: #FFEBEE; border: 1px solid #EF9A9A; }
  .rev-box h5 { font-size: 11px; font-weight: 700; margin-bottom: 4px; }
  .eli10-box { background: #F3E5F5; border-radius: 10px; padding: 10px 12px; font-size: 13px; margin: 8px 0; border: 1px solid #CE93D8; }
  .topic-divider { border: none; border-top: 1px dashed var(--border); margin: 14px 0; }
  .analysis-table { width: calc(100% - 24px); margin: 0 12px 12px; border-collapse: collapse; font-size: 12px; }
  .analysis-table th { background: var(--primary); color: #fff; padding: 8px; text-align: left; position: sticky; top: var(--nav-h); }
  .analysis-table td { padding: 7px 8px; border-bottom: 1px solid var(--border); background: var(--card); vertical-align: top; }
  .predict-card { margin: 0 12px 8px; background: var(--card); border-radius: 12px; padding: 12px 14px; border: 1px solid var(--border); display: flex; gap: 10px; align-items: flex-start; }
  .predict-rank { font-size: 18px; font-weight: 800; color: var(--primary); min-width: 28px; }
  .drill-item { margin: 0 12px 6px; background: var(--card); border-radius: 10px; padding: 10px 12px; border: 1px solid var(--border); font-size: 13px; cursor: pointer; }
  .drill-item .drill-ans { display: none; margin-top: 8px; padding-top: 8px; border-top: 1px dashed var(--border); color: var(--green); font-weight: 600; }
  .drill-item.revealed .drill-ans { display: block; }
  .model-answer { background: var(--green-light); border-radius: 10px; padding: 12px; margin: 10px 0; font-size: 13px; border: 1px solid #A5D6A7; }
  .model-answer h5 { color: var(--green); font-size: 12px; margin-bottom: 6px; }
  .score-hero { margin: 12px; border-radius: 16px; padding: 16px; background: linear-gradient(135deg, #B71C1C, #880E4F); color: #fff; }
  .survival-card { margin: 0 12px 10px; border-radius: 14px; padding: 14px; border: 2px solid; }
  .survival-card.s1 { border-color: #EF5350; background: #FFEBEE; }
  .survival-card.s2 { border-color: #7E57C2; background: #EDE7F6; }
  .survival-card.s3 { border-color: #FFA726; background: #FFF3E0; }
  .survival-card.s4 { border-color: #66BB6A; background: #E8F5E9; }
  .survival-card h3 { font-size: 15px; font-weight: 700; margin: 0 0 8px; }
  .survival-card ul { padding-left: 18px; font-size: 13px; margin: 0; }
  .survival-card ul li { margin-bottom: 4px; }
  [data-theme="dark"] .survival-card.s1 { background: #2D1210; }
  [data-theme="dark"] .survival-card.s2 { background: #1A1230; }
  [data-theme="dark"] .survival-card.s3 { background: #2D2200; }
  [data-theme="dark"] .survival-card.s4 { background: #0D2518; }
  @media (max-width: 400px) { .rev-tabs { grid-template-columns: 1fr; } }
  @media (min-width: 500px) {
    .topbar, .page, .bottom-nav { max-width: 480px; left: 50%; }
    .bottom-nav { transform: translateX(-50%); }
    body { display: flex; justify-content: center; }
    body > * { width: 100%; max-width: 480px; }
  }
"""

print("CSS ready", len(CSS))
