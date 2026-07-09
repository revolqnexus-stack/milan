# -*- coding: utf-8 -*-
"""CHN templates — same visual pattern as nurse.html (header → structure → green MODEL → WHY FULL MARKS)."""

TEMPLATES = r'''
  <div class="section-head">📋 Answer Templates</div>
  <div class="template-tabs">
    <button class="tmpl-tab-btn active-tmpl" onclick="showTmpl('seven',this)">7-Mark</button>
    <button class="tmpl-tab-btn" onclick="showTmpl('long',this)">8–9 Mark</button>
    <button class="tmpl-tab-btn" onclick="showTmpl('short',this)">4-Mark</button>
    <button class="tmpl-tab-btn" onclick="showTmpl('one',this)">1-Mark</button>
    <button class="tmpl-tab-btn" onclick="showTmpl('framework',this)">Framework</button>
    <button class="tmpl-tab-btn" onclick="showTmpl('diagrams',this)">Diagrams</button>
  </div>

  <!-- ═══════ 7-MARK (default — same layout as nurse) ═══════ -->
  <div class="tmpl-section show" id="tmpl-seven">
    <div class="template-card">
      <div style="background:#1565C0;color:#fff;padding:12px;border-radius:10px;margin-bottom:14px;text-align:center;">
        <strong>7-MARK TEMPLATE</strong> — Definition + Explain (2+5)
      </div>
      <p style="font-size:13px;margin-bottom:10px;">Structure: (1) Definition/Intro (2) Diagram if useful (3) Main points / types (4) Steps or principles (5) Examples (6) Nursing role (7) Conclusion</p>
      <div class="model-answer">
        <h5>MODEL — Q: Define Community Health Nursing. Explain qualities and functions (2+5=7)</h5>
        <p><strong>A. Definition (2 marks):</strong> Community Health Nursing is a specialised field combining nursing and public health practice. It provides comprehensive care to individuals, families and communities in homes, clinics, schools and workplaces, with emphasis on <strong>prevention of disease</strong> and <strong>promotion of health</strong>.</p>
        <p><strong>B. Qualities:</strong> Empathy, patience, honesty; good communication; leadership; cultural sensitivity; professional knowledge and skill.</p>
        <p><strong>Functions:</strong> Care provider; educator; counsellor; manager/coordinator; epidemiologist/researcher; advocate linking people to services.</p>
        <p><strong>Hospital vs CHN:</strong> Ward/cure/individual vs home/prevention/family-community.</p>
        <p><strong>Nursing:</strong> Home visits, family folders, immunization, health education, referral.</p>
        <p><strong>Conclusion:</strong> CHN is the backbone of primary care through prevention, education and continuous family care.</p>
      </div>
      <div class="tip-box"><strong>WHY FULL MARKS:</strong> Clear A/B split (2+5). Definition has keywords. Qualities + Functions as separate bullets. Difference line + nurse conclusion = full examiner checklist.</div>

      <div class="model-answer">
        <h5>MODEL — Q: Define safe water. Explain methods of purification (2+5=7)</h5>
        <p><strong>A. Definition (2):</strong> Safe water is free from pathogens and harmful chemicals; colourless, odourless, palatable, adequate in quantity.</p>
        <p><strong>B. Household:</strong> Boiling; chlorination/bleaching powder; filtration (candle/cloth); store covered.</p>
        <p><strong>B. Large scale:</strong> (1) Storage/sedimentation (2) Coagulation with alum (3) Filtration — slow sand / rapid sand (4) Chlorination → supply.</p>
        <p><strong>[DRAW: Storage → Filtration → Chlorination — label all steps]</strong></p>
        <p><strong>Horrock's apparatus:</strong> estimates bleaching powder dose. <strong>Diseases:</strong> cholera, typhoid, hep A/E.</p>
        <p><strong>Nursing:</strong> Teach boiling/chlorination, protect wells, report outbreaks.</p>
        <p><strong>Conclusion:</strong> Safe water prevents major community epidemics.</p>
      </div>
      <div class="tip-box"><strong>WHY FULL MARKS:</strong> Household + large-scale both listed. Diagram placeholder + Horrock's + diseases + nurse line.</div>

      <div class="model-answer">
        <h5>MODEL — Q: Define home visit. Explain principles and bag technique (2+5=7)</h5>
        <p><strong>A. Definition (2):</strong> Home visit is a planned visit by the community health nurse to the family home for assessment, nursing care, health education and follow-up.</p>
        <p><strong>B. Principles:</strong> Clear purpose; planned yet flexible; family-centred; use family resources; privacy &amp; dignity; educative; regular follow-up.</p>
        <p><strong>Bag technique:</strong></p>
        <ol>
          <li>Place bag on clean paper — never dirty floor</li>
          <li>Handwash → take articles → close bag</li>
          <li>Do procedure; discard waste safely</li>
          <li>Clean articles; handwash; replace; close bag</li>
          <li>Clean → dirty workflow; protect bag interior</li>
        </ol>
        <p><strong>[DRAW bag flow if time]</strong></p>
        <p><strong>Conclusion:</strong> Correct bag technique brings safe nursing care to the family.</p>
      </div>
      <div class="tip-box"><strong>WHY FULL MARKS:</strong> Definition + principles list + numbered bag steps. Process answers love numbered steps.</div>
    </div>
  </div>

  <!-- ═══════ 8–9 MARK ═══════ -->
  <div class="tmpl-section" id="tmpl-long">
    <div class="template-card">
      <div style="background: var(--primary); color: #fff; padding: 12px; border-radius: 10px; margin-bottom: 14px; text-align: center;">
        <strong>🥇 GOLDEN TEMPLATE — 8 / 9 Mark Answer</strong><br>
        <span style="font-size:13px;">Vitamins · Water · HE · Communication · Ventilation · Nutrition</span>
      </div>
      <div class="tip-box">💡 STRATEGY: Write <strong>definition / classification FIRST</strong> — banks 2 marks. Draw diagram early if topic allows!</div>

      <div class="step-row">
        <div class="step-num">1</div>
        <div class="step-content">
          <strong>DEFINITION / CLASSIFICATION <span class="marks-pill">2 marks</span></strong>
          [Topic] is defined as ___________.<br>
          Classification (if asked): ___________
        </div>
      </div>
      <div class="step-row">
        <div class="step-num">2</div>
        <div class="step-content">
          <strong>⭐ DIAGRAM <span class="marks-pill">1–2 marks</span></strong>
          Triad · Cold chain · Water SFC · Cross ventilation · Communication process<br>
          Rough + 4–5 labels = marks.
        </div>
      </div>
      <div class="step-row">
        <div class="step-num">3</div>
        <div class="step-content">
          <strong>MAIN CONTENT <span class="marks-pill">4–5 marks</span></strong>
          Headings + 5–7 bullets · types/steps/sources+deficiency · numbers (2–8°C, April 7, 1978)
        </div>
      </div>
      <div class="step-row">
        <div class="step-num">4</div>
        <div class="step-content">
          <strong>NURSING ROLE <span class="marks-pill">1</span></strong>
          Educate / home visit / record / refer / immunize + one example
        </div>
      </div>
      <div class="step-row">
        <div class="step-num">5</div>
        <div class="step-content">
          <strong>CONCLUSION <span class="marks-pill">0.5–1</span></strong>
          Thus, [topic] is essential for prevention and promotion of community health.
        </div>
      </div>

      <div class="tip-box">
        <strong>💡 GOLDEN RULES:</strong><br>
        ✅ BULLET POINTS — more bullets = more marks<br>
        ✅ Label <strong>A / B</strong> for split questions<br>
        ✅ Underline keywords · Never leave blank
      </div>

      <div class="model-answer">
        <h5>MODEL — Classify vitamins. Sources &amp; deficiency of A, D, C (2+7=9)</h5>
        <p><strong>A. Classification (2):</strong> Fat-soluble A, D, E, K · Water-soluble B-complex, C.</p>
        <p><strong>B. Detail (7):</strong></p>
        <ul>
          <li><strong>Vitamin A:</strong> GLV, carrot, milk, liver → night blindness, xerophthalmia, Bitot's spots</li>
          <li><strong>Vitamin D:</strong> sunlight, fish liver oil → rickets / osteomalacia</li>
          <li><strong>Vitamin C:</strong> amla, citrus, guava → scurvy (bleeding gums)</li>
          <li><strong>Traps:</strong> Vit K = clotting (NOT anticoagulant); Vit B1 = beriberi (NOT night blindness)</li>
        </ul>
        <p><strong>Nursing:</strong> Diet diversity, Vit A prophylaxis, early detection of deficiency.</p>
        <p><strong>Conclusion:</strong> Vitamin knowledge prevents common deficiency diseases in the community.</p>
      </div>
      <div class="tip-box"><strong>WHY FULL MARKS:</strong> Classification first. Each vitamin = source + deficiency. Trap corrections show paper awareness.</div>

      <div class="model-answer">
        <h5>MODEL — Define health education. Principles and methods (2+6=8)</h5>
        <p><strong>Definition:</strong> Process that informs, motivates and helps people adopt healthy practices.</p>
        <p><strong>Principles:</strong> need-based; participation; known→unknown; simple language; reinforcement; evaluate; culturally acceptable.</p>
        <p><strong>Methods:</strong> Individual (counselling, home visit) · Group (demo, discussion) · Mass (TV, radio, posters, campaigns).</p>
        <p><strong>Nursing:</strong> Plan HE, choose method by audience, use AV aids, evaluate practice change.</p>
        <p><strong>Conclusion:</strong> HE is the cheapest tool for disease prevention in the community.</p>
      </div>
      <div class="tip-box"><strong>WHY FULL MARKS:</strong> Definition + principles list + IGM methods + nurse line.</div>
    </div>
  </div>

  <!-- ═══════ 4-MARK ═══════ -->
  <div class="tmpl-section" id="tmpl-short">
    <div class="template-card">
      <div style="background:#7B1FA2;color:#fff;padding:12px;border-radius:10px;margin-bottom:14px;text-align:center;">
        <strong>4-Mark Short Note Template</strong><br>
        <span style="font-size:13px;">Target: 4/4 — any FOUR short notes</span>
      </div>
      <p style="font-size:13px;margin-bottom:10px;">Structure: (1) Definition (2) 4–6 key bullets (3) Tiny diagram optional (4) Nurse role / conclusion</p>

      <div class="step-row">
        <div class="step-num">1</div>
        <div class="step-content">
          <strong>DEFINITION <span class="marks-pill">1 mark</span></strong>
          [Topic] is defined as ___________
        </div>
      </div>
      <div class="step-row">
        <div class="step-num">2</div>
        <div class="step-content">
          <strong>KEY POINTS — 4 to 6 bullets <span class="marks-pill">2–3 marks</span></strong>
          • Point 1<br>• Point 2<br>• Point 3<br>• Point 4
        </div>
      </div>
      <div class="step-row">
        <div class="step-num">3</div>
        <div class="step-content">
          <strong>NURSE / CONCLUSION <span class="marks-pill">0.5–1</span></strong>
          It is important in nursing because ___________
        </div>
      </div>

      <div class="model-answer">
        <h5>MODEL 4-MARK — Bag Technique</h5>
        <p><strong>Definition:</strong> Method of using the community nursing bag during home visit without spreading infection.</p>
        <ul>
          <li>Place bag on clean paper; never on dirty floor</li>
          <li>Handwash before touching clean articles</li>
          <li>Take articles; close bag before procedure</li>
          <li>Discard waste; clean articles; replace; close bag</li>
          <li>Clean → dirty workflow</li>
        </ul>
        <p><strong>Nursing:</strong> Follow bag technique every home visit to prevent cross-infection.</p>
      </div>
      <div class="tip-box"><strong>WHY FULL MARKS:</strong> One-line definition + 5 action bullets + nurse line = exact 4-mark rubric. No paragraphs.</div>

      <div class="model-answer">
        <h5>MODEL 4-MARK — Under-five / Well-baby clinic</h5>
        <p><strong>Definition:</strong> Under-five clinic (well-baby clinic) provides comprehensive care to children below 5 years.</p>
        <ul>
          <li>Growth monitoring (weight, growth chart)</li>
          <li>Immunization as per NIS</li>
          <li>Nutrition &amp; breastfeeding counselling</li>
          <li>Minor illness care; ORS teaching</li>
          <li>HE to mothers; referral of sick children</li>
        </ul>
        <p><strong>Conclusion:</strong> Prevents malnutrition and vaccine-preventable deaths.</p>
      </div>

      <div class="model-answer">
        <h5>MODEL 4-MARK — Records and reports</h5>
        <p><strong>Record</strong> = permanent written account. <strong>Report</strong> = summary to higher authority.</p>
        <ul>
          <li>Types: family folder, cumulative record, clinic registers</li>
          <li>Uses: continuity, legal, planning, research</li>
          <li>Principles: accurate, complete, legible, timely, confidential, dated &amp; signed</li>
          <li>Family folder = all members of one family</li>
        </ul>
        <p><strong>Nurse:</strong> Update after every visit; prepare monthly reports.</p>
      </div>
      <div class="tip-box">💡 Time: <strong>6–8 minutes</strong> per short note. Pick 4 you know 100%!</div>
    </div>
  </div>

  <!-- ═══════ 1-MARK ═══════ -->
  <div class="tmpl-section" id="tmpl-one">
    <div class="template-card">
      <div style="background:var(--green);color:#fff;padding:12px;border-radius:10px;margin-bottom:14px;text-align:center;">
        <strong>1-MARK DEFINITION FORMULA</strong>
      </div>
      <p style="font-size:15px;font-weight:600;text-align:center;margin:12px 0;">"<strong>________</strong> is defined as __________."</p>
      <div class="model-answer">
        <h5>Examples from actual papers:</h5>
        <ul>
          <li><strong>Cold chain</strong> is defined as a system of storing and transporting vaccines at recommended temperature from manufacturer to beneficiary.</li>
          <li><strong>Endemic</strong> means the constant presence of a disease in a given geographic area.</li>
          <li><strong>Family folder</strong> is a file containing health records of all members of one family.</li>
          <li><strong>Incubation period</strong> is the time interval between infection and appearance of first symptoms.</li>
          <li><strong>Epidemiology</strong> is the study of distribution and determinants of health-related events in populations, applied to control health problems.</li>
          <li><strong>Weaning</strong> is the gradual introduction of complementary foods while continuing breastfeeding.</li>
          <li><strong>Home visit</strong> is a planned visit by the community health nurse to the family home for assessment, care and education.</li>
          <li><strong>Ventilation</strong> is the process of supplying fresh air and removing vitiated air from an enclosed space.</li>
        </ul>
      </div>
      <div class="ans-block">
        <h4>Top 25 Ready CHN Definitions</h4>
        <ul>
          <li><strong>Health (WHO)</strong> — complete physical, mental and social well-being, not merely absence of disease</li>
          <li><strong>Primary Health Care</strong> — essential health care universally accessible (Alma Ata 1978)</li>
          <li><strong>Immunization</strong> — artificial induction of immunity by vaccine or immunoglobulin</li>
          <li><strong>Communicable disease</strong> — illness due to infectious agent transmissible from reservoir to host</li>
          <li><strong>Carrier</strong> — harbours agent without symptoms but can transmit</li>
          <li><strong>Pandemic</strong> — epidemic spanning many countries / worldwide</li>
          <li><strong>Mortality</strong> — death / death rate in a population</li>
          <li><strong>Morbidity</strong> — sickness rate in a population</li>
          <li><strong>Quarantine</strong> — restriction of healthy contacts to prevent spread</li>
          <li><strong>Disinfection</strong> — kill/remove pathogens (spores may remain)</li>
          <li><strong>Sullage</strong> — wastewater WITHOUT excreta</li>
          <li><strong>Sewage</strong> — wastewater WITH excreta</li>
          <li><strong>Eligible couple</strong> — married couple, wife ~15–49 years</li>
          <li><strong>ASHA</strong> — Accredited Social Health Activist</li>
          <li><strong>Demography</strong> — scientific study of human population</li>
          <li><strong>Anthropometry</strong> — body measurements (Ht, Wt, MUAC)</li>
          <li><strong>Calorie</strong> — unit of heat/energy (kcal)</li>
          <li><strong>Counselling</strong> — face-to-face help for informed decisions</li>
          <li><strong>Health education</strong> — informs and motivates healthy practices</li>
          <li><strong>Referral</strong> — send to higher care (two-way + feedback)</li>
          <li><strong>Standing order</strong> — MO written protocol for nurse treatment</li>
          <li><strong>Sanitary well</strong> — parapet, platform, cover, drain</li>
          <li><strong>Neonatal period</strong> — first 28 days of life</li>
          <li><strong>Infant</strong> — birth to 1 completed year</li>
          <li><strong>Balanced diet</strong> — all essential nutrients in correct proportion</li>
        </ul>
      </div>
    </div>
  </div>

  <!-- ═══════ FRAMEWORK ═══════ -->
  <div class="tmpl-section" id="tmpl-framework">
    <div class="template-card">
      <div style="background:#37474F;color:#fff;padding:12px;border-radius:10px;margin-bottom:14px;text-align:center;">
        <strong>LONG ANSWER MASTER FRAMEWORK</strong> — Use even if you forget 40%
      </div>
      <div class="diagram-box" style="text-align:center;">DEFINITION ↓ OBJECTIVES ↓ DIAGRAM ↓ MAIN POINTS (bullets) ↓ STEPS/TYPES ↓ NURSING ROLE ↓ CONCLUSION</div>
      <div class="tip-box"><strong>Partial recall:</strong> Write headings anyway + draw triad/cold chain/water + 3 nurse points (home visit, HE, records, referral, immunization) + one number (2–8°C / April 7 / 1978).</div>

      <div class="model-answer">
        <h5>8-MARK MODEL — Communication</h5>
        <p><strong>Definition:</strong> Sharing ideas, facts and feelings for common understanding.</p>
        <p><strong>[DIAGRAM: Sender → Message → Channel → Receiver → Feedback]</strong></p>
        <p><strong>Types:</strong> Verbal/non-verbal; individual/group/mass.</p>
        <p><strong>Barriers:</strong> language, noise, culture, emotion, status, deafness.</p>
        <p><strong>Nursing:</strong> Simple words, listen, feedback, AV aids, respect culture.</p>
        <p><strong>Conclusion:</strong> Good communication is the base of HE and counselling.</p>
      </div>

      <div class="model-answer">
        <h5>RESCUE LINES — when blank</h5>
        <ul>
          <li>Community participation is essential</li>
          <li>Focus on prevention and health promotion</li>
          <li>Maintain records / family folder</li>
          <li>Health educate in simple language</li>
          <li>Refer with feedback (two-way)</li>
          <li>Work with ASHA / ANM / MO as a team</li>
        </ul>
      </div>
    </div>
  </div>

  <!-- ═══════ DIAGRAMS ═══════ -->
  <div class="tmpl-section" id="tmpl-diagrams">
    <div class="template-card">
      <div style="background:#C62828;color:#fff;padding:12px;border-radius:10px;margin-bottom:14px;text-align:center;">
        <strong>📐 10 Must-Draw CHN Diagrams</strong><br>
        <span style="font-size:13px;">Easy marks in Water / Epi / Imm / Ventilation answers</span>
      </div>

      <div class="ans-block">
        <h4>1. EPIDEMIOLOGICAL TRIAD</h4>
        <p>⏱ Time: 1 min | Labels: 3</p>
        <div class="diagram-box">        AGENT
       /      \
    HOST ---- ENVIRONMENT

MUST LABEL: Agent, Host, Environment
❌ MISTAKE: Only two components
✅ Add one control example per arm</div>

        <h4>2. COLD CHAIN</h4>
        <p>⏱ Time: 2 min | Labels: 5+</p>
        <div class="diagram-box">Manufacturer → State → District → PHC (ILR) → Sub-centre → Session
Temp: +2°C to +8°C
Equipment: ILR, Deep freezer, Cold box, Vaccine carrier

MUST LABEL: ILR, +2 to +8°C, Cold box
❌ MISTAKE: Freezing DPT/TT/HepB (freeze-sensitive)
✅ Mention Shake test if space</div>

        <h4>3. LARGE-SCALE WATER PURIFICATION</h4>
        <p>⏱ Time: 2 min</p>
        <div class="diagram-box">Raw water → Storage/Sedimentation → Coagulation (alum)
→ Filtration (slow/rapid sand) → Chlorination → Supply

MUST LABEL: Storage, Filtration, Chlorination
❌ MISTAKE: Skipping chlorination
✅ Horrock's = bleach dose</div>

        <h4>4. RAPID SAND STEPS</h4>
        <div class="diagram-box">Coagulation → Sedimentation → Rapid sand filter → Chlorination
Slow sand = schmutzdecke biological film, slower</div>

        <h4>5. LEVELS OF CARE / REFERRAL</h4>
        <div class="diagram-box">Home → Sub-centre → PHC → CHC/FRU/District → Tertiary
Arrows BOTH ways = two-way referral + feedback
MUST LABEL: Primary, Secondary, Tertiary</div>

        <h4>6. COMMUNICATION PROCESS</h4>
        <div class="diagram-box">SENDER → MESSAGE → CHANNEL → RECEIVER → FEEDBACK
(+ Noise / Barriers)
❌ MISTAKE: Forgetting feedback</div>

        <h4>7. LEVELS OF PREVENTION</h4>
        <div class="diagram-box">PRIMARY (promote + protect: immunization, safe water)
→ SECONDARY (early Dx/Rx: screening)
→ TERTIARY (rehab)
❌ MISTAKE: Calling screening primary</div>

        <h4>8. CROSS VENTILATION</h4>
        <div class="diagram-box">Wind → [Window IN] ROOM [Window OUT] → stale air
Opposite wall openings
Mechanical: Exhaust | Plenum | AC
❌ MISTAKE: Single window ≠ cross ventilation</div>

        <h4>9. BAG TECHNIQUE FLOW</h4>
        <div class="diagram-box">Clean paper → Handwash → Articles OUT → Close bag
→ Procedure → Waste → Clean → Handwash → Replace → Close
Rule: CLEAN → DIRTY
❌ MISTAKE: Bag open during procedure</div>

        <h4>10. DISEASE CYCLE</h4>
        <div class="diagram-box">Incubation → Prodromal → Illness → Decline → Convalescence
MUST LABEL: all 5 in order</div>
      </div>
      <div class="tip-box">
        <strong>💡 DIAGRAM RULES:</strong><br>
        ✅ Draw FIRST for Water / Epi / Cold chain / Ventilation<br>
        ✅ Minimum 4 labels — rough OK · Write "Fig: …"<br>
        ✅ 30–60 seconds — don't over-art
      </div>
    </div>
  </div>
'''
