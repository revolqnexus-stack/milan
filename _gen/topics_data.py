# -*- coding: utf-8 -*-
"""Topic definitions for CHN-I study app."""

def years_html(years):
    return "".join(f'<span class="year-tag">{y}</span>' for y in years)

def marks_table(rows):
    rows_html = "".join(f"<tr><td>{a}</td><td>{b}</td></tr>" for a, b in rows)
    return f'<table class="mini-table"><tr><th>Section</th><th>Marks</th></tr>{rows_html}</table>'

TOPICS = []

def T(**kw):
    TOPICS.append(kw)
    return kw

# ── FOUNDATIONS ──
T(
    id="t1", level="red", badge="badge-red", badge_txt="🔴 MUST",
    cat="Foundations", title="Community Health Nursing — Def, Qualities, Functions",
    topic="community health nursing definition qualities functions principles objectives hospital",
    prob="prob-vhigh", prob_txt="🔴 VERY HIGH · 96% likely",
    papers="12 papers · 2025, 2023, 2022, 2019, 2018, 2017, 2016, 2015, 2014, 2013, 2012, 2011",
    marks="7–9 marks",
    years=[2025,2023,2022,2019,2018,2017,2016,2015,2014,2013,2012,2011],
    why="Asked almost every year as definition, qualities, functions, principles, or difference from hospital nursing. 2025 & 2023 favoured long/short on CHN role.",
    must="Definition → objectives → principles → qualities of CHN → functions → difference hospital vs community → nurse role",
    mistakes="Writing only hospital nursing points. Forgetting principles (community participation, prevention). Mixing PHC with CHN definition.",
    mark_rows=[("A. Definition", "2"), ("B. Qualities / Functions / Principles", "5"), ("Difference hospital vs community", "1–2"), ("Nursing role / conclusion", "1")],
    fast="CHN = nursing care to individuals, families, community at home/clinic/school. Focus: prevention + health promotion. Qualities: empathy, communication, leadership.",
    last="DEF + OBJECTIVES + PRINCIPLES + QUALITIES + FUNCTIONS + HOSPITAL vs COMMUNITY",
    eli="Community nurse goes to people where they live — home, school, village — to keep them healthy, not only treat sick in hospital.",
    analogy="Hospital nurse = fire brigade after fire. CHN = smoke detector + fire drill + teaching safety.",
    viva="Define CHN? | 4 principles of CHN? | Difference hospital & community nursing?",
    draw="",
    trick='🧠 Memory: <strong>"POP-Q-F"</strong> — Principles, Objectives, Qualities, Functions (+ hospital difference)',
    answer="""
          <h4>📄 Full Exam Version — Write in Answer Sheet</h4>
          <h4>A. Definition <span class="marks-pill">2 marks</span></h4>
          <p><strong>Community Health Nursing</strong> is a specialised field of nursing that combines <strong>nursing</strong> and <strong>public health</strong> practice. It provides comprehensive care to <strong>individuals, families and communities</strong> in homes, clinics, schools and workplaces, with emphasis on <strong>prevention of disease</strong> and <strong>promotion of health</strong>.</p>
          <h4>B. Objectives</h4>
          <ul>
            <li>Promote and maintain <strong>health</strong> of community</li>
            <li><strong>Prevent</strong> disease, disability and premature death</li>
            <li>Provide <strong>comprehensive nursing care</strong> at home and clinic</li>
            <li>Encourage <strong>community participation</strong> in health programmes</li>
            <li>Identify health needs and utilise available resources</li>
          </ul>
          <h4>C. Principles of CHN</h4>
          <ul>
            <li>Based on identified <strong>needs</strong> of community</li>
            <li><strong>Community participation</strong> essential</li>
            <li>Focus on <strong>prevention</strong> and health promotion</li>
            <li>Care is <strong>family-centred</strong> and continuous</li>
            <li>Utilise available resources; work with health team</li>
            <li>Respect culture, beliefs and dignity of people</li>
          </ul>
          <h4>D. Qualities of a Community Health Nurse</h4>
          <ul>
            <li><strong>Empathy</strong>, patience, honesty and integrity</li>
            <li>Good <strong>communication</strong> and counselling skill</li>
            <li>Leadership, initiative and resourcefulness</li>
            <li>Interest in people; cultural sensitivity</li>
            <li>Physical fitness; professional knowledge and skill</li>
          </ul>
          <h4>E. Functions of CHN</h4>
          <ul>
            <li><strong>Care provider</strong> — nursing care at home/clinic</li>
            <li><strong>Educator</strong> — health education to family & community</li>
            <li><strong>Counsellor</strong> — guide on MCH, family welfare, nutrition</li>
            <li><strong>Manager / Coordinator</strong> — organise clinics, camps, records</li>
            <li><strong>Researcher / Epidemiologist</strong> — survey, report outbreaks</li>
            <li><strong>Advocate</strong> — link people to health services</li>
          </ul>
          <h4>F. Difference: Hospital Nursing vs Community Health Nursing</h4>
          <ul>
            <li><strong>Place:</strong> Hospital ward vs home/community</li>
            <li><strong>Focus:</strong> Cure of illness vs prevention + promotion</li>
            <li><strong>Client:</strong> Individual patient vs family & community</li>
            <li><strong>Control:</strong> Controlled environment vs variable home setting</li>
            <li><strong>Team:</strong> Doctors/nurses mainly vs multipurpose health team</li>
          </ul>
          <h4>🩺 Nursing Role</h4>
          <p>CHN plans home visits, maintains family folders, gives health education, immunizes, refers cases, and works with ASHA/ANM/MO for national health programmes.</p>
          <h4>✅ Conclusion</h4>
          <p>Community Health Nursing is the backbone of primary care. A skilled CHN improves community health through prevention, education and continuous family care.</p>
"""
)

T(
    id="t2", level="red", badge="badge-red", badge_txt="🔴 MUST",
    cat="Foundations", title="Health — Concept, Dimensions, Determinants",
    topic="health concept dimensions determinants who definition",
    prob="prob-vhigh", prob_txt="🔴 VERY HIGH · 94% likely",
    papers="9 papers · 2025, 2024, 2023, 2022, 2018, 2017, 2016, 2015, 2013",
    marks="4–7 marks",
    years=[2025,2024,2023,2022,2018,2017,2016,2015,2013],
    why="WHO definition + dimensions appear as meaning/short/long. 2024–2025 kept health concept hot.",
    must="WHO definition → positive concept → dimensions (physical, mental, social…) → determinants → nurse role",
    mistakes="Writing only 'absence of disease'. Forgetting social/spiritual dimensions. Mixing determinants with dimensions.",
    mark_rows=[("Definition (WHO)", "1–2"), ("Dimensions (list + explain)", "2–3"), ("Determinants", "2"), ("Nursing implication", "1")],
    fast="WHO: complete physical, mental, social well-being — not mere absence of disease. Dimensions + determinants (biology, behaviour, environment, health services, socio-economic).",
    last="WHO DEF + 6 DIMENSIONS + DETERMINANTS (BBESS)",
    eli="Health is not only 'not sick'. It means body, mind and friends/family life all feel good.",
    analogy="Health = a stool with many legs (dimensions). If one leg breaks, balance is lost.",
    viva="WHO definition of health? | Name dimensions of health? | What are determinants?",
    draw="",
    trick='🧠 Memory: Dimensions <strong>"PMS-ESS"</strong> — Physical, Mental, Social, Emotional, Spiritual, Vocational',
    answer="""
          <h4>📄 Full Exam Version — Write in Answer Sheet</h4>
          <h4>A. Definition <span class="marks-pill">2 marks</span></h4>
          <p>According to <strong>WHO</strong>, <strong>Health</strong> is a state of complete <strong>physical, mental and social well-being</strong> and not merely the <strong>absence of disease or infirmity</strong>.</p>
          <h4>B. Concept of Health</h4>
          <ul>
            <li><strong>Biomedical:</strong> absence of disease</li>
            <li><strong>Ecological:</strong> harmony with environment</li>
            <li><strong>Psychosocial:</strong> feeling well in mind & society</li>
            <li><strong>Holistic:</strong> whole person — body, mind, spirit, society</li>
          </ul>
          <h4>C. Dimensions of Health</h4>
          <ul>
            <li><strong>Physical</strong> — body fitness, no disease</li>
            <li><strong>Mental</strong> — clear thinking, emotional balance</li>
            <li><strong>Social</strong> — good relations, community participation</li>
            <li><strong>Emotional</strong> — ability to express feelings appropriately</li>
            <li><strong>Spiritual</strong> — sense of purpose / values</li>
            <li><strong>Vocational</strong> — satisfaction in work / role</li>
          </ul>
          <h4>D. Determinants of Health</h4>
          <ul>
            <li><strong>Biological</strong> — age, sex, genes</li>
            <li><strong>Behavioural</strong> — diet, exercise, smoking, alcohol</li>
            <li><strong>Environmental</strong> — water, air, housing, sanitation</li>
            <li><strong>Socio-economic</strong> — income, education, occupation</li>
            <li><strong>Health services</strong> — availability, accessibility, quality</li>
          </ul>
          <h4>🩺 Nursing Role</h4>
          <p>CHN assesses all dimensions, educates on healthy behaviour, improves environment (safe water, hygiene), and links families to health services.</p>
          <h4>✅ Conclusion</h4>
          <p>Health is multi-dimensional. Nurses must promote complete well-being, not only treat disease.</p>
"""
)

T(
    id="t3", level="red", badge="badge-red", badge_txt="🔴 MUST",
    cat="Foundations", title="Primary Health Care + Levels of Health Care",
    topic="primary health care phc levels of health care alma ata elements",
    prob="prob-vhigh", prob_txt="🔴 VERY HIGH · 90% likely",
    papers="8 papers · 2024, 2018, 2017, 2016, 2015, 2014, 2013, 2011",
    marks="4–7 marks",
    years=[2024,2018,2017,2016,2015,2014,2013,2011],
    why="PHC principles/elements and primary/secondary/tertiary levels are classic short notes; 2024 revived PHC.",
    must="Alma Ata 1978 → definition → 8 elements → principles → levels primary/secondary/tertiary with examples",
    mistakes="Confusing levels of prevention with levels of care. Forgetting Alma Ata. Listing only hospitals for primary care.",
    mark_rows=[("Definition + Alma Ata", "1–2"), ("Elements / Principles", "2–3"), ("Levels of care + examples", "2–3")],
    fast="PHC = essential health care, universally accessible. Elements: education, nutrition, water/sanitation, MCH/FP, immunization, endemic disease control, treatment, essential drugs. Levels: PHC→CHC/District→Medical college.",
    last="ALMA ATA 1978 + 8 ELEMENTS + PRIMARY/SECONDARY/TERTIARY",
    eli="Primary health care means basic health help near home — vaccines, clean water teaching, mother-baby care — before big hospital.",
    analogy="PHC = neighbourhood kirana shop for health; tertiary = big mall specialty store.",
    viva="Year of Alma Ata? | 8 elements of PHC? | Example of tertiary care?",
    draw="",
    trick='🧠 Memory: Elements <strong>"ENW-MIT-ED"</strong> — Education, Nutrition, Water/sanitation, MCH/FP, Immunization, Treatment of endemic, Essential drugs, Disease control',
    answer="""
          <h4>📄 Full Exam Version — Write in Answer Sheet</h4>
          <h4>A. Definition <span class="marks-pill">2 marks</span></h4>
          <p><strong>Primary Health Care (PHC)</strong> is essential health care based on practical, scientifically sound and socially acceptable methods, made <strong>universally accessible</strong> to individuals and families in the community at a cost they can afford. Declared at <strong>Alma Ata Conference, 1978</strong>.</p>
          <h4>B. Principles of PHC</h4>
          <ul>
            <li><strong>Equitable distribution</strong></li>
            <li><strong>Community participation</strong></li>
            <li><strong>Intersectoral coordination</strong></li>
            <li><strong>Appropriate technology</strong></li>
          </ul>
          <h4>C. Elements of PHC (8)</h4>
          <ul>
            <li>Health <strong>education</strong></li>
            <li>Adequate <strong>nutrition</strong> / food supply</li>
            <li>Safe <strong>water</strong> and basic <strong>sanitation</strong></li>
            <li><strong>MCH</strong> including family planning</li>
            <li><strong>Immunization</strong> against major infectious diseases</li>
            <li>Prevention & control of locally <strong>endemic</strong> diseases</li>
            <li>Appropriate <strong>treatment</strong> of common diseases & injuries</li>
            <li>Provision of <strong>essential drugs</strong></li>
          </ul>
          <h4>D. Levels of Health Care</h4>
          <ul>
            <li><strong>Primary:</strong> Sub-centre, PHC, village health — first contact (immunization, ANC, minor ailments)</li>
            <li><strong>Secondary:</strong> CHC, District hospital — specialist care, referral</li>
            <li><strong>Tertiary:</strong> Medical college, regional institutes — advanced specialty & research</li>
          </ul>
          <h4>🩺 Nursing Role</h4>
          <p>CHN delivers PHC elements at grass-root level, educates community, maintains records and refers appropriately up the levels.</p>
          <h4>✅ Conclusion</h4>
          <p>PHC is the foundation of health for all. Nurses are key workers in delivering primary care.</p>
"""
)

T(
    id="t4", level="yellow", badge="badge-yellow", badge_txt="🟡 HIGH",
    cat="Foundations", title="Levels of Prevention of Disease",
    topic="levels of prevention primary secondary tertiary primordial",
    prob="prob-high", prob_txt="🟡 HIGH · 78% likely",
    papers="4 papers · 2022, 2018, 2017, 2013",
    marks="4–7 marks",
    years=[2022,2018,2017,2013],
    why="Short note favourite: primary/secondary/tertiary prevention with examples. Often paired with epidemiology.",
    must="Primordial → Primary → Secondary → Tertiary with clear examples + nurse actions",
    mistakes="Mixing primary prevention with primary health care. Saying screening is primary (it is secondary).",
    mark_rows=[("Definition of prevention", "1"), ("Each level + examples", "3"), ("Nursing role", "1")],
    fast="Primordial=prevent risk factors. Primary=prevent disease (vaccine). Secondary=early detect (Pap smear). Tertiary=limit disability (rehab).",
    last="PRIMORDIAL→PRIMARY→SECONDARY→TERTIARY + EXAMPLES",
    eli="Stop bad habits before they start; stop germs with vaccine; catch disease early; help after illness so disability is less.",
    analogy="Primordial=don't buy junk food. Primary=lock door. Secondary=smoke alarm. Tertiary=rebuild after fire.",
    viva="Example of secondary prevention? | Is immunization primary or secondary?",
    draw="",
    trick='🧠 Memory: <strong>"PPST"</strong> — Primordial, Primary, Secondary, Tertiary',
    answer="""
          <h4>📄 Full Exam Version — Write in Answer Sheet</h4>
          <h4>Introduction</h4>
          <p><strong>Prevention</strong> means actions taken to stop occurrence, progress or complications of disease. Levels of prevention guide community nursing practice.</p>
          <h4>1. Primordial Prevention</h4>
          <ul>
            <li>Prevents emergence of <strong>risk factors</strong> in population</li>
            <li>Example: healthy lifestyle education in schools; discourage smoking from childhood</li>
          </ul>
          <h4>2. Primary Prevention</h4>
          <ul>
            <li>Prevents <strong>onset of disease</strong> in healthy people</li>
            <li>Health promotion + specific protection</li>
            <li>Examples: <strong>immunization</strong>, safe water, balanced diet, mosquito nets, health education</li>
          </ul>
          <h4>3. Secondary Prevention</h4>
          <ul>
            <li><strong>Early diagnosis</strong> and prompt treatment</li>
            <li>Examples: screening (BP, Pap smear, sputum AFB), under-five clinic growth monitoring</li>
          </ul>
          <h4>4. Tertiary Prevention</h4>
          <ul>
            <li>Limits <strong>disability</strong> and promotes rehabilitation</li>
            <li>Examples: physiotherapy after stroke, disability aids, counselling of chronic patients</li>
          </ul>
          <h4>🩺 Nursing Role</h4>
          <p>CHN applies all levels: vaccines (primary), clinic screening (secondary), home-based rehab teaching (tertiary).</p>
          <h4>✅ Conclusion</h4>
          <p>Knowing levels of prevention helps nurses plan the right intervention at the right time.</p>
"""
)

T(
    id="t5", level="red", badge="badge-red", badge_txt="🔴 MUST",
    cat="Epidemiology & Child/Family", title="Epidemiology + Epidemiological Triad",
    topic="epidemiology epidemiological triad agent host environment",
    prob="prob-vhigh", prob_txt="🔴 VERY HIGH · 91% likely",
    papers="7 papers · 2024, 2019, 2017, 2016, 2015, 2014, 2013",
    marks="4–7 marks",
    years=[2024,2019,2017,2016,2015,2014,2013],
    why="Definition + triad is a staple short/long. 2024 asked epidemiology concepts.",
    must="Definition → aims → triad (agent-host-environment) → diagram → uses for nurse",
    mistakes="Confusing endemic/epidemic/pandemic. Drawing triad without explaining interaction.",
    mark_rows=[("Definition + aims", "2"), ("Triad explain + diagram", "3–4"), ("Uses / nurse role", "1")],
    fast="Epidemiology = study of distribution & determinants of health events. Triad: Agent + Host + Environment → disease when imbalance.",
    last="DEF + AIMS + AGENT-HOST-ENVIRONMENT DIAGRAM",
    eli="Disease happens when a bad germ (agent), a weak person (host) and a dirty place (environment) meet.",
    analogy="Fire needs fuel + oxygen + spark — disease needs agent + host + environment.",
    viva="Define epidemiology? | Components of triad? | Difference endemic vs epidemic?",
    draw="""
          <div class="diagram-box">     AGENT
        (germ / cause)
            / \\
           /   \\
          /     \\
       HOST ---- ENVIRONMENT
     (person)    (surroundings)

Disease occurs when all three
interact unfavourably.</div>""",
    trick='🧠 Memory: <strong>"AHE"</strong> — Agent, Host, Environment',
    answer="""
          <h4>📄 Full Exam Version — Write in Answer Sheet</h4>
          <h4>A. Definition <span class="marks-pill">2 marks</span></h4>
          <p><strong>Epidemiology</strong> is the study of the <strong>distribution</strong> and <strong>determinants</strong> of health-related states or events in specified populations, and the application of this study to <strong>control health problems</strong>.</p>
          <h4>B. Aims of Epidemiology</h4>
          <ul>
            <li>Describe distribution of disease (who, where, when)</li>
            <li>Identify causes / risk factors</li>
            <li>Guide prevention and control</li>
            <li>Evaluate health services</li>
          </ul>
          <h4>C. Epidemiological Triad <span class="marks-pill">5 marks</span></h4>
          <ul>
            <li><strong>Agent:</strong> biological (bacteria, virus), nutritional, chemical, physical</li>
            <li><strong>Host:</strong> age, sex, immunity, nutrition, behaviour, genetics</li>
            <li><strong>Environment:</strong> physical (water, air), biological, social</li>
          </ul>
          <p>Disease results from interaction of all three. Breaking any link prevents disease (e.g., vaccine strengthens host; clean water improves environment).</p>
          <h4>🩺 Nursing Role</h4>
          <p>CHN surveys cases, reports outbreaks, educates on agent/host/environment control, and supports immunization and sanitation.</p>
          <h4>✅ Conclusion</h4>
          <p>Epidemiological triad is the basic model to understand and prevent community diseases.</p>
"""
)

T(
    id="t6", level="red", badge="badge-red", badge_txt="🔴 MUST",
    cat="Epidemiology & Child/Family", title="Communicable Disease + Modes of Transmission",
    topic="communicable disease modes of transmission contact droplet vector",
    prob="prob-vhigh", prob_txt="🔴 VERY HIGH · 92% likely",
    papers="5 papers · 2025, 2024, 2023, 2018, 2015",
    marks="4–9 marks",
    years=[2025,2024,2023,2018,2015],
    why="Modes of transmission repeatedly as short note; recent papers (2023–2025) keep CD hot.",
    must="Definition → classification → modes (direct/indirect) with examples → control measures → nurse role",
    mistakes="Saying diabetes is communicable. Mixing vector (Anopheles vs Aedes). Forgetting fomite/vehicle.",
    mark_rows=[("Definition", "1–2"), ("Modes + examples", "3–4"), ("Prevention/control", "2"), ("Nurse role", "1")],
    fast="CD spreads person to person. Direct: contact, droplet, vertical. Indirect: vehicle, vector, air-borne, fomite.",
    last="DEF + DIRECT/INDIRECT MODES + EXAMPLES + CONTROL",
    eli="Germs jump by touch, cough spray, dirty water, mosquitoes, or shared things.",
    analogy="Germs travel like messages — by hand delivery, post (water/food), or courier mosquito.",
    viva="Is diabetes communicable? | Vector of dengue? | What is fomite?",
    draw="",
    trick='🧠 Memory: Direct <strong>"CDV"</strong> Contact Droplet Vertical | Indirect <strong>"VAFF"</strong> Vehicle Airborne Fomite Vector',
    answer="""
          <h4>📄 Full Exam Version — Write in Answer Sheet</h4>
          <h4>A. Definition</h4>
          <p><strong>Communicable disease</strong> is an illness due to a specific infectious agent or its toxic products that can be transmitted from person/animal/reservoir to a susceptible host, directly or indirectly.</p>
          <h4>B. Modes of Transmission</h4>
          <p><strong>1. Direct transmission</strong></p>
          <ul>
            <li><strong>Direct contact</strong> — touch, sexual contact (scabies, syphilis)</li>
            <li><strong>Droplet</strong> — cough/sneeze within short distance (common cold, TB droplets)</li>
            <li><strong>Vertical / perinatal</strong> — mother to child (HIV, hepatitis B)</li>
          </ul>
          <p><strong>2. Indirect transmission</strong></p>
          <ul>
            <li><strong>Vehicle-borne</strong> — water, food, blood (cholera, hepatitis A)</li>
            <li><strong>Vector-borne</strong> — mosquito, fly (malaria–Anopheles, dengue–Aedes)</li>
            <li><strong>Air-borne</strong> — droplet nuclei (measles, TB)</li>
            <li><strong>Fomite-borne</strong> — contaminated objects (towels, instruments)</li>
          </ul>
          <h4>C. Control Measures</h4>
          <ul>
            <li>Early diagnosis & treatment; isolation if needed</li>
            <li>Immunization; chemoprophylaxis</li>
            <li>Safe water, sanitation, food hygiene</li>
            <li>Vector control; health education</li>
          </ul>
          <h4>🩺 Nursing Role</h4>
          <p>Identify cases, educate on hygiene & mosquito control, ensure immunization, maintain records and notify MO.</p>
          <h4>✅ Conclusion</h4>
          <p>Understanding transmission modes helps break the chain of infection in the community.</p>
"""
)

T(
    id="t7", level="red", badge="badge-red", badge_txt="🔴 MUST",
    cat="Epidemiology & Child/Family", title="Immunization + NIS + Cold Chain",
    topic="immunization national immunization schedule cold chain vaccine",
    prob="prob-vhigh", prob_txt="🔴 VERY HIGH · 93% likely",
    papers="8 papers · 2024, 2023, 2018, 2017, 2016, 2015, 2014, 2011",
    marks="4–7 marks",
    years=[2024,2023,2018,2017,2016,2015,2014,2011],
    why="NIS table + cold chain repeatedly asked as short note; 2023–2024 kept immunization high.",
    must="Definition → types (active/passive) → NIS key vaccines/ages → cold chain equipment → nurse role",
    mistakes="Saying BCG/polio are killed vaccines (they are live). Mixing Vit K with vaccines. Wrong cold chain temperatures.",
    mark_rows=[("Definition + types", "1–2"), ("NIS key points", "2–3"), ("Cold chain", "2"), ("Nurse role", "1")],
    fast="Immunization = artificial immunity. Cold chain 2–8°C. Birth: BCG+OPV0+HepB0. 6/10/14 wk primary series. 9 mo MR-1. 16–24 mo boosters. Td at 10 & 16 yrs / pregnancy.",
    last="DEF + ACTIVE/PASSIVE + NIS AGES + COLD CHAIN 2–8°C",
    eli="Vaccines teach the body to fight germs before real germs come. Keep vaccines in fridge like ice cream — not too hot, not frozen wrong.",
    analogy="Vaccine = fire drill practice. Cold chain = refrigerated truck keeping ice cream solid.",
    viva="Temperature of ILR? | BCG route? | Is OPV live or killed?",
    draw="""
          <div class="diagram-box">COLD CHAIN (keep vaccines potent)
Manufacturer → State store → District → PHC/ILR → Sub-centre → Session
Temperature: usually +2°C to +8°C (ILR)
Ice-lined refrigerator (ILR) + Deep freezer + Cold boxes + Vaccine carriers
Shake test for freeze-sensitive vaccines (DPT/TT/HepB)</div>""",
    trick='🧠 Memory: <strong>"Birth BCG+OPV+HepB"</strong> then follow NIS card; Cold chain <strong>"2 to 8"</strong>',
    answer="""
          <h4>📄 Full Exam Version — Write in Answer Sheet</h4>
          <h4>A. Definition</h4>
          <p><strong>Immunization</strong> is the process of inducing immunity artificially by administering vaccine or immunoglobulin to protect against specific infectious diseases.</p>
          <h4>B. Types</h4>
          <ul>
            <li><strong>Active:</strong> body makes antibodies (vaccines — BCG, OPV, measles)</li>
            <li><strong>Passive:</strong> ready-made antibodies given (ATS, Hep B immunoglobulin)</li>
          </ul>
          <h4>C. National Immunization Schedule (write this table)</h4>
          <table class="mini-table">
            <tr><th>Age</th><th>Vaccines</th></tr>
            <tr><td><strong>At birth</strong></td><td>BCG, OPV-0, Hepatitis B-0</td></tr>
            <tr><td><strong>6 weeks</strong></td><td>OPV-1, IPV-1, Pentavalent-1, Rotavirus-1, PCV-1</td></tr>
            <tr><td><strong>10 weeks</strong></td><td>OPV-2, Pentavalent-2, Rotavirus-2, PCV-2</td></tr>
            <tr><td><strong>14 weeks</strong></td><td>OPV-3, IPV-2, Pentavalent-3, Rotavirus-3, PCV-3</td></tr>
            <tr><td><strong>9–12 months</strong></td><td>MR-1, JE-1 (endemic areas), Vitamin A (1st dose)</td></tr>
            <tr><td><strong>16–24 months</strong></td><td>MR-2, JE-2 (if applicable), DPT-booster-1, OPV-booster, Vit A</td></tr>
            <tr><td><strong>5–6 years</strong></td><td>DPT-booster-2</td></tr>
            <tr><td><strong>10 years &amp; 16 years</strong></td><td>Td</td></tr>
            <tr><td><strong>Pregnant women</strong></td><td>Td-1, Td-2 (or Td-booster if previously immunized)</td></tr>
          </table>
          <p><strong>Routes (high-yield):</strong> BCG — intradermal left upper arm; OPV — oral; Hep B / Pentavalent / PCV / IPV — intramuscular (as per site protocol); MR — subcutaneous.</p>
          <p><em>Note: State may add JE/fIPV fractional dose variants — if your class card differs slightly, keep ages/vaccines above as the core exam answer.</em></p>
          <h4>D. Cold Chain</h4>
          <ul>
            <li>System to keep vaccines at recommended temperature from manufacturer to beneficiary</li>
            <li>Equipment: Walk-in cooler, ILR, deep freezer, cold box, vaccine carrier, ice packs</li>
            <li>Most vaccines: <span class="highlight">+2°C to +8°C</span></li>
            <li>Protect from heat and freezing (DPT/TT/HepB freeze-sensitive)</li>
          </ul>
          <h4>🩺 Nursing Role</h4>
          <p>Check vaccine vial monitor, maintain cold chain, give correct dose/route, counsel mother, record in MCP card & register, manage AEFI reporting.</p>
          <h4>✅ Conclusion</h4>
          <p>Immunization with intact cold chain is the most cost-effective way to prevent childhood killer diseases.</p>
"""
)

T(
    id="t8", level="red", badge="badge-red", badge_txt="🔴 MUST",
    cat="Epidemiology & Child/Family", title="Under Five Clinic",
    topic="under five clinic well baby clinic growth monitoring",
    prob="prob-vhigh", prob_txt="🔴 VERY HIGH · 89% likely",
    papers="8 papers · 2024, 2023, 2022, 2016, 2015, 2014, 2013, 2011",
    marks="4–7 marks",
    years=[2024,2023,2022,2016,2015,2014,2013,2011],
    why="Classic short note; often equated with well-baby clinic. 2022–2024 appearances.",
    must="Definition (=well baby clinic) → objectives → activities (GOBI-FFF style) → nurse role",
    mistakes="Saying under-five clinic is only for sick children. Forgetting growth chart / immunization.",
    mark_rows=[("Definition", "1"), ("Objectives", "1–2"), ("Functions/activities", "2–3"), ("Nurse role", "1")],
    fast="Under-five = Well baby clinic. Growth monitoring, ORS, breastfeeding, immunization, family planning, female education, food.",
    last="WELL BABY = U5 | GROWTH + IMMUNIZATION + NUTRITION + HE",
    eli="A special clinic for children below 5 years to check growth, give vaccines and teach mothers — even when baby looks healthy.",
    analogy="Under-five clinic = regular service check for a young car — prevent breakdown.",
    viva="Under five clinic is also called? | Age group? | Main activities?",
    draw="",
    trick='🧠 Memory: <strong>"GOBI-FFF"</strong> Growth, ORS, Breastfeeding, Immunization + Female education, Family planning, Food',
    answer="""
          <h4>📄 Full Exam Version — Write in Answer Sheet</h4>
          <h4>A. Definition</h4>
          <p><strong>Under-five clinic</strong> (also called <span class="highlight">Well-baby clinic</span>) is a clinic that provides comprehensive preventive, promotive and curative care to children below <strong>5 years</strong> of age.</p>
          <h4>B. Objectives</h4>
          <ul>
            <li>Monitor growth and development</li>
            <li>Prevent malnutrition and infections</li>
            <li>Complete immunization</li>
            <li>Early detection & treatment of illness</li>
            <li>Health education to mothers</li>
          </ul>
          <h4>C. Activities / Functions</h4>
          <ul>
            <li><strong>Growth monitoring</strong> — weight, height, growth chart</li>
            <li><strong>Immunization</strong> as per NIS</li>
            <li>Nutrition advice; Vitamin A; deworming</li>
            <li>ORS & diarrhoea management teaching</li>
            <li>Treatment of minor ailments; referral of sick child</li>
            <li>Family planning & mother education</li>
          </ul>
          <h4>🩺 Nursing Role</h4>
          <p>Weigh child, plot growth chart, give vaccines, counsel on breastfeeding/complementary feeding, identify at-risk children and refer.</p>
          <h4>✅ Conclusion</h4>
          <p>Under-five clinic reduces child morbidity and mortality through continuous preventive care.</p>
"""
)

T(
    id="t9", level="yellow", badge="badge-yellow", badge_txt="🟡 HIGH",
    cat="Epidemiology & Child/Family", title="Minor Ailments",
    topic="minor ailments fever diarrhoea cough scabies home management",
    prob="prob-high", prob_txt="🟡 HIGH · 82% likely",
    papers="4 papers · 2025, 2019, 2016, 2011",
    marks="7 marks",
    years=[2025,2019,2016,2011],
    why="Often long answer listing common minor ailments + home/community management; asked in 2025.",
    must="Definition → list common ailments → assessment → home care + when to refer → nurse role",
    mistakes="Giving only drug names without nursing care. Not writing referral danger signs.",
    mark_rows=[("Definition + list", "2"), ("Management of 3–4 ailments", "4"), ("Referral + nurse role", "1")],
    fast="Fever, cold, diarrhoea, worm, scabies, conjunctivitis, boils. Home care + ORS + hygiene + refer danger signs.",
    last="LIST + HOME CARE + DANGER SIGNS → REFER",
    eli="Small common sicknesses treated at home/clinic — fever, loose motion, cough, skin itch — but know when to rush to hospital.",
    analogy="Minor ailments = small potholes you can fill yourself; big cracks need engineer (referral).",
    viva="ORS use? | Danger signs in diarrhoea? | Scabies teaching?",
    draw="",
    trick='🧠 Memory: <strong>"FCD-WSC"</strong> Fever, Cold/cough, Diarrhoea, Worms, Scabies, Conjunctivitis',
    answer="""
          <h4>📄 Full Exam Version — Write in Answer Sheet</h4>
          <h4>A. Definition <span class="marks-pill">2 marks</span></h4>
          <p><strong>Minor ailments</strong> are common, usually self-limiting illnesses that can be managed at home or primary care level with simple nursing measures, health education and basic treatment.</p>
          <h4>B. Common Minor Ailments</h4>
          <ul>
            <li>Fever, common cold, cough</li>
            <li>Diarrhoea, vomiting, constipation</li>
            <li>Worm infestation, scabies, boils, conjunctivitis</li>
            <li>Minor injuries, toothache, earache</li>
          </ul>
          <h4>C. Management (examples) <span class="marks-pill">5 marks</span></h4>
          <ul>
            <li><strong>Fever:</strong> tepid sponging, fluids, light clothing, antipyretic as advised, observe for danger signs</li>
            <li><strong>Diarrhoea:</strong> ORS, continue feeding/breastfeeding, hand hygiene; refer if blood, severe dehydration, persistent vomiting</li>
            <li><strong>Scabies:</strong> whole family treatment, wash clothes/bedding in hot water, personal hygiene teaching</li>
            <li><strong>Cough/cold:</strong> steam inhalation, warm fluids, avoid dust/smoke; refer if fast breathing / chest in-drawing</li>
          </ul>
          <h4>🩺 Nursing Role</h4>
          <p>Assess, give first-line care, educate family, maintain records, and <strong>refer promptly</strong> when danger signs present.</p>
          <h4>✅ Conclusion</h4>
          <p>Skilled management of minor ailments reduces hospital load and prevents complications.</p>
"""
)

T(
    id="t10", level="red", badge="badge-red", badge_txt="🔴 MUST",
    cat="Epidemiology & Child/Family", title="Home Visit + Bag Technique",
    topic="home visit bag technique community nursing bag principles",
    prob="prob-vhigh", prob_txt="🔴 VERY HIGH · 95% likely",
    papers="10 papers · 2024, 2023, 2019, 2018, 2017, 2016, 2015, 2014, 2013, 2011",
    marks="4–9 marks",
    years=[2024,2023,2019,2018,2017,2016,2015,2014,2013,2011],
    why="One of the most repeated CHN practical topics — principles of home visit + bag technique steps.",
    must="Definition → purposes → principles → steps of home visit → bag technique principles/steps → nurse role",
    mistakes="Opening bag on dirty floor. Touching sterile articles with unclean hands. No family participation.",
    mark_rows=[("Home visit def + principles", "2–3"), ("Steps of visit", "2"), ("Bag technique", "3–4")],
    fast="Home visit = planned family care at home. Bag = portable clinic. Clean to dirty workflow; protect bag from contamination.",
    last="PURPOSE + PRINCIPLES + STEPS + BAG RULES (CLEAN→DIRTY)",
    eli="Nurse visits family at home with a special bag of clean instruments — like a mini clinic in a suitcase.",
    analogy="Nursing bag = toolbox of a field engineer; home visit = on-site service.",
    viva="Principles of bag technique? | Purposes of home visit?",
    draw="",
    trick='🧠 Memory: Visit <strong>"APPRAISE"</strong> Approach, Purpose, Plan, Respect, Assess, Intervene, Support, Evaluate | Bag: Clean hand → clean article → dirty last',
    answer="""
          <h4>📄 Full Exam Version — Write in Answer Sheet</h4>
          <h4>A. Home Visit — Definition <span class="marks-pill">2 marks</span></h4>
          <p><strong>Home visit</strong> is a planned visit by the community health nurse to the family in their home to assess health needs, give nursing care, health education and follow-up.</p>
          <h4>B. Purposes</h4>
          <ul>
            <li>Establish nurse–family relationship</li>
            <li>Assess home environment and health needs</li>
            <li>Provide nursing care and health education</li>
            <li>Follow-up of ANC, PNC, under-five, chronic cases</li>
            <li>Motivate for immunization & family welfare</li>
          </ul>
          <h4>C. Principles of Home Visit</h4>
          <ul>
            <li>Must have a <strong>clear purpose</strong> and be planned</li>
            <li>Flexible; based on family needs</li>
            <li>Use available family resources</li>
            <li>Maintain privacy, dignity and confidentiality</li>
            <li>Educative and family-centred</li>
          </ul>
          <h4>D. Bag Technique <span class="marks-pill">5 marks</span></h4>
          <p><strong>Bag technique</strong> is a tool by which the nurse performs nursing procedures during home visit using articles from the community nursing bag, while preventing spread of infection.</p>
          <ul>
            <li>Place bag on clean paper/newspaper; never on dirty floor</li>
            <li>Wash hands before touching clean articles</li>
            <li>Take out needed articles; close bag</li>
            <li>Do procedure; discard waste safely</li>
            <li>Clean used articles; wash hands; replace; close bag</li>
            <li>Separate clean and dirty; protect bag from contamination</li>
          </ul>
          <h4>🩺 Nursing Role</h4>
          <p>Plan visit, use bag correctly, give care, record in family folder, and schedule follow-up.</p>
          <h4>✅ Conclusion</h4>
          <p>Home visit with correct bag technique brings quality nursing care to the family doorstep.</p>
"""
)

T(
    id="t11", level="yellow", badge="badge-yellow", badge_txt="🟡 HIGH",
    cat="Epidemiology & Child/Family", title="Referral System",
    topic="referral system two way referral first referral unit",
    prob="prob-high", prob_txt="🟡 HIGH · 84% likely",
    papers="6 papers · 2025, 2023, 2022, 2018, 2017, 2016",
    marks="4–7 marks",
    years=[2025,2023,2022,2018,2017,2016],
    why="Short note on two-way referral; 2025 appearance. Linked to levels of care.",
    must="Definition → need → types (internal/external, one-way/two-way) → steps → nurse role + FRU",
    mistakes="Describing only sending patient up — forgetting feedback (two-way). No referral slip details.",
    mark_rows=[("Definition + need", "1–2"), ("Types / process", "2–3"), ("Nurse responsibilities", "1–2")],
    fast="Referral = sending client to higher/appropriate facility. Two-way = refer + get feedback. Use referral slip.",
    last="DEF + TWO-WAY + SLIP + ESCORT + FOLLOW-UP",
    eli="If village clinic cannot treat, nurse sends patient to bigger hospital with a note — and later checks what happened.",
    analogy="Referral = escalating a ticket in customer support and getting resolution update back.",
    viva="What is two-way referral? | What is FRU?",
    draw="",
    trick='🧠 Memory: <strong>"SENSE"</strong> Select case, Explain, Note (slip), Send/escort, Evaluate feedback',
    answer="""
          <h4>📄 Full Exam Version — Write in Answer Sheet</h4>
          <h4>A. Definition</h4>
          <p><strong>Referral system</strong> is a process by which a health worker sends a client to a higher or more appropriate level of care for further diagnosis and treatment, and receives <strong>feedback</strong> for continuity of care (<strong>two-way referral</strong>).</p>
          <h4>B. Need / Importance</h4>
          <ul>
            <li>Ensures right care at right place</li>
            <li>Avoids delay in emergencies (obstructed labour, severe dehydration)</li>
            <li>Uses resources efficiently</li>
            <li>Maintains continuity of care</li>
          </ul>
          <h4>C. Process</h4>
          <ul>
            <li>Identify need for referral</li>
            <li>Explain to patient/family; get consent</li>
            <li>Fill <strong>referral slip</strong> (identity, findings, treatment given, reason)</li>
            <li>Arrange transport; escort if needed</li>
            <li>Inform receiving facility when possible</li>
            <li>Obtain feedback; follow up at home</li>
          </ul>
          <h4>D. First Referral Unit (FRU)</h4>
          <p>Facility (often CHC level) equipped for emergency obstetric and newborn care — caesarean, blood transfusion, etc.</p>
          <h4>🩺 Nursing Role</h4>
          <p>Decide timely referral, stabilize patient, complete records, counsel family, and continue care after return.</p>
          <h4>✅ Conclusion</h4>
          <p>An effective referral system saves lives by linking primary care to specialist services.</p>
"""
)

T(
    id="t12", level="red", badge="badge-red", badge_txt="🔴 MUST",
    cat="Epidemiology & Child/Family", title="Records & Reports — Types, Uses, Family Folder",
    topic="records reports cumulative record family folder principles",
    prob="prob-vhigh", prob_txt="🔴 VERY HIGH · 94% likely",
    papers="12 papers · 2025, 2024, 2022, 2019, 2018, 2017, 2016, 2015, 2014, 2013, 2012, 2011",
    marks="4–8 marks",
    years=[2025,2024,2022,2019,2018,2017,2016,2015,2014,2013,2012,2011],
    why="Almost every paper — types, uses, principles, cumulative records, family folder.",
    must="Definition → types → uses → principles → family folder / cumulative → nurse role",
    mistakes="Saying records are only for legal use. Incomplete/illegible writing. Mixing report vs record.",
    mark_rows=[("Definition + types", "2"), ("Uses + principles", "2–3"), ("Family folder / cumulative", "2")],
    fast="Record=permanent written evidence. Report=summary communication. Family folder holds all family health data. Principles: accurate, brief, complete, confidential.",
    last="TYPES + USES + PRINCIPLES + FAMILY FOLDER",
    eli="Nurse writes what she did and what family health is like — so next nurse knows the story.",
    analogy="Records = school diary of health; family folder = one file for whole family.",
    viva="What is family folder? | Principles of recording? | Difference record vs report?",
    draw="",
    trick='🧠 Memory: Principles <strong>"ABC-CLEAR"</strong> Accurate, Brief, Complete, Confidential, Legible, Early, Authentic, Relevant',
    answer="""
          <h4>📄 Full Exam Version — Write in Answer Sheet</h4>
          <h4>A. Definitions</h4>
          <ul>
            <li><strong>Record:</strong> permanent written account of information about client/family/community health activities</li>
            <li><strong>Report:</strong> summary account of activities/events communicated to higher authority (oral/written)</li>
          </ul>
          <h4>B. Types of Records</h4>
          <ul>
            <li>Family folder / family health record</li>
            <li>Cumulative record (continuous record of one person over time)</li>
            <li>Clinic registers (ANC, immunization, OP)</li>
            <li>Daily diary, reports, survey forms</li>
          </ul>
          <h4>C. Uses</h4>
          <ul>
            <li>Communication between health team</li>
            <li>Planning & evaluating care</li>
            <li>Legal document; research & statistics</li>
            <li>Continuity of care; education tool</li>
          </ul>
          <h4>D. Principles / Essential Requirements of Record Maintenance</h4>
          <ul>
            <li><strong>Accurate &amp; truthful</strong> — never invent data</li>
            <li><strong>Complete</strong> — who, what, when, where, findings, action</li>
            <li><strong>Concise &amp; clear</strong> — standard terms; no vague words</li>
            <li><strong>Legible</strong> — readable handwriting / neat entries</li>
            <li><strong>Timely</strong> — write immediately after care / visit</li>
            <li><strong>Dated &amp; signed</strong> with designation</li>
            <li><strong>Confidential</strong> — keep secure; share only with health team as needed</li>
            <li><strong>Continuity</strong> — update family folder / cumulative record each contact</li>
            <li>Keep in orderly files; avoid overwriting; correct errors properly (single line + initial)</li>
          </ul>
          <h4>E. Family Folder &amp; Cumulative Record</h4>
          <ul>
            <li><strong>Family folder:</strong> file with health information of <strong>all members of one family</strong> — ID, environment, history, services, follow-up</li>
            <li><strong>Cumulative record:</strong> continuous longitudinal record of one person over years (school/clinic)</li>
          </ul>
          <h4>🩺 Nursing Role</h4>
          <p>Maintain family folders, update after each visit, prepare monthly reports, and use data for prioritising families.</p>
          <h4>✅ Conclusion</h4>
          <p>Good records and reports are essential for quality community health nursing.</p>
"""
)

T(
    id="t13", level="yellow", badge="badge-yellow", badge_txt="🟡 HIGH",
    cat="Epidemiology & Child/Family", title="Family Health / MCH / Family Welfare — Nurse Role",
    topic="family health mch family welfare nurse role antenatal",
    prob="prob-high", prob_txt="🟡 HIGH · 85% likely",
    papers="5 papers · 2025, 2017, 2016, 2014, 2013",
    marks="7–9 marks",
    years=[2025,2017,2016,2014,2013],
    why="Long answers on nurse role in MCH/family welfare; 2025 kept family health relevant.",
    must="Family health concept → MCH components → family welfare methods → detailed nurse role",
    mistakes="Listing only contraceptives without nursing responsibilities. Forgetting ANC/PNC/newborn.",
    mark_rows=[("Family health / MCH intro", "2"), ("Family welfare methods", "2"), ("Nurse role detailed", "3–5")],
    fast="MCH: ANC, natal, PNC, newborn, under-five. FW: spacing + terminal (IUCD, pills, condom, vasectomy, tubectomy). Nurse educates, counsels, refers.",
    last="MCH PACKAGE + FW METHODS + NURSE ROLE LIST",
    eli="Nurse helps mothers stay healthy in pregnancy, safe delivery follow-up, baby care, and guides couple on planning family size.",
    analogy="Family health nurse = coach for the whole family team — mother, father, children.",
    viva="Vasectomy vs tubectomy? | Antenatal visits minimum? | Spacing methods?",
    draw="",
    trick='🧠 Memory: MCH <strong>"ANP-NU"</strong> Antenatal, Natal, Postnatal, Newborn, Under-five | Terminal: Vase=Male, Tube=Female',
    answer="""
          <h4>📄 Full Exam Version — Write in Answer Sheet</h4>
          <h4>A. Family Health / MCH</h4>
          <p><strong>Family health nursing</strong> focuses on the family as a unit. <strong>MCH</strong> includes care of mother and child from antenatal period through under-five care.</p>
          <ul>
            <li><strong>Antenatal:</strong> registration, TT, IFA, weight, BP, danger signs education</li>
            <li><strong>Intranatal:</strong> promote institutional delivery; birth preparedness</li>
            <li><strong>Postnatal:</strong> mother & newborn check, breastfeeding, hygiene</li>
            <li><strong>Child care:</strong> immunization, growth, nutrition</li>
          </ul>
          <h4>B. Family Welfare</h4>
          <ul>
            <li><strong>Spacing:</strong> condom, OC pills, IUCD, injectable (as available)</li>
            <li><strong>Terminal:</strong> <span class="highlight">Vasectomy (male)</span>, <span class="highlight">Tubectomy (female)</span></li>
          </ul>
          <h4>C. Role of Nurse <span class="marks-pill">5–7 marks</span></h4>
          <ul>
            <li>Identify eligible couples & antenatal mothers</li>
            <li>Provide ANC/PNC care and counselling</li>
            <li>Motivate for immunization & nutrition</li>
            <li>Counsel on family planning; dispel myths</li>
            <li>Assist in camps; maintain eligible couple register</li>
            <li>Refer high-risk mothers; follow up acceptors</li>
            <li>Health education on birth spacing & small family norm</li>
          </ul>
          <h4>✅ Conclusion</h4>
          <p>CHN is central to MCH and family welfare success in the community.</p>
"""
)

T(
    id="t14", level="red", badge="badge-red", badge_txt="🔴 MUST",
    cat="Environment & Nutrition & Communication", title="Communication — Types, Process, Barriers",
    topic="communication types process barriers elements",
    prob="prob-vhigh", prob_txt="🔴 VERY HIGH · 93% likely",
    papers="10 papers · 2025, 2023, 2018, 2017, 2016, 2015, 2014, 2013, 2012, 2011",
    marks="4–9 marks",
    years=[2025,2023,2018,2017,2016,2015,2014,2013,2012,2011],
    why="Process + barriers appear constantly as short/long; 2025 included communication themes.",
    must="Definition → elements/process → types → barriers → how nurse overcomes",
    mistakes="Listing only verbal. Forgetting feedback in process. Vague barriers without examples.",
    mark_rows=[("Definition + process", "2"), ("Types", "2"), ("Barriers + overcome", "3")],
    fast="SMCR + feedback. Verbal/non-verbal; one-way/two-way. Barriers: language, noise, culture, emotions, daydreaming.",
    last="PROCESS (SENDER-MSG-CHANNEL-RECEIVER-FEEDBACK) + TYPES + BARRIERS",
    eli="Communication is sharing meaning. If mother doesn't understand vaccine talk, message failed.",
    analogy="Communication = phone call: speaker, message, network, listener, reply.",
    viva="Elements of communication? | Example of psychological barrier?",
    draw="",
    trick='🧠 Memory: Process <strong>"SMCR-F"</strong> Sender Message Channel Receiver Feedback',
    answer="""
          <h4>📄 Full Exam Version — Write in Answer Sheet</h4>
          <h4>A. Definition</h4>
          <p><strong>Communication</strong> is the process of exchanging information, ideas and feelings between two or more persons to create common understanding.</p>
          <h4>B. Process / Elements</h4>
          <ul>
            <li><strong>Sender</strong> → encodes message</li>
            <li><strong>Message</strong> — content</li>
            <li><strong>Channel</strong> — spoken, written, AV</li>
            <li><strong>Receiver</strong> → decodes</li>
            <li><strong>Feedback</strong> — confirms understanding</li>
          </ul>
          <h4>C. Types</h4>
          <ul>
            <li><strong>Verbal</strong> / <strong>Non-verbal</strong> (gestures, touch, expression)</li>
            <li>One-way / two-way</li>
            <li>Formal / informal</li>
            <li>Intrapersonal / interpersonal / group / mass</li>
          </ul>
          <h4>D. Barriers</h4>
          <ul>
            <li><strong>Physiological:</strong> deafness, illness</li>
            <li><strong>Psychological:</strong> fear, anger, low interest</li>
            <li><strong>Environmental:</strong> noise, overcrowding</li>
            <li><strong>Semantic/language:</strong> difficult medical words</li>
            <li><strong>Cultural / social</strong> differences</li>
          </ul>
          <h4>🩺 Nursing Role</h4>
          <p>Use simple language, listen actively, check feedback, choose quiet place, respect culture, use AV aids.</p>
          <h4>✅ Conclusion</h4>
          <p>Effective communication is the foundation of health education and counselling.</p>
"""
)

T(
    id="t15", level="yellow", badge="badge-yellow", badge_txt="🟡 HIGH",
    cat="Environment & Nutrition & Communication", title="Audio-Visual Aids",
    topic="audio visual aids classification puppets charts models",
    prob="prob-high", prob_txt="🟡 HIGH · 86% likely",
    papers="9 papers · 2023, 2022, 2018, 2017, 2016, 2015, 2014, 2013, 2011",
    marks="4–7 marks",
    years=[2023,2022,2018,2017,2016,2015,2014,2013,2011],
    why="Classification of AV aids is a frequent short note; models = 3D aids (TRUE in T/F).",
    must="Definition → classification (audio/visual/AV) with examples → advantages → nurse use",
    mistakes="Saying models are not AV aids. Listing without classification. No advantages.",
    mark_rows=[("Definition", "1"), ("Classification + examples", "2–3"), ("Advantages / principles", "1–2")],
    fast="Audio: radio, mike. Visual: charts, posters, flashcards, models, specimens. AV: TV, films, video. Models are three-dimensional aids.",
    last="AUDIO / VISUAL / AUDIO-VISUAL + EXAMPLES + ADVANTAGES",
    eli="Teaching tools you hear, see, or both — charts, puppets, videos — make health talk stick.",
    analogy="AV aids = subtitles + pictures in a movie — easier to understand.",
    viva="Example of 3D aid? | Advantage of AV aids?",
    draw="",
    trick='🧠 Memory: <strong>"A-V-AV"</strong> Audio | Visual (2D+3D) | Audio-Visual',
    answer="""
          <h4>📄 Full Exam Version — Write in Answer Sheet</h4>
          <h4>A. Definition</h4>
          <p><strong>Audio-visual aids</strong> are instructional devices that help the teacher communicate messages more effectively through hearing and/or seeing.</p>
          <h4>B. Classification</h4>
          <ul>
            <li><strong>Audio aids:</strong> radio, tape recorder, public address system</li>
            <li><strong>Visual aids:</strong> chalk board, charts, posters, flash cards, flannel graph, specimens, <strong>models (3D)</strong>, puppets</li>
            <li><strong>Audio-visual:</strong> TV, films, video, LCD projection</li>
          </ul>
          <h4>C. Advantages</h4>
          <ul>
            <li>Create interest; improve understanding & retention</li>
            <li>Save time; useful for illiterate groups</li>
            <li>Standardize message; stimulate discussion</li>
          </ul>
          <h4>🩺 Nursing Role</h4>
          <p>Select aid suitable to audience, prepare locally, use with talk (not alone), evaluate understanding.</p>
          <h4>✅ Conclusion</h4>
          <p>AV aids make health education lively and effective in the community.</p>
"""
)

T(
    id="t16", level="red", badge="badge-red", badge_txt="🔴 MUST",
    cat="Environment & Nutrition & Communication", title="Health Education — Principles, Methods, Nurse Role",
    topic="health education principles methods nurse role",
    prob="prob-vhigh", prob_txt="🔴 VERY HIGH · 95% likely",
    papers="12 papers · 2024, 2023, 2022, 2019, 2018, 2017, 2016, 2015, 2014, 2013, 2012, 2011",
    marks="4–8 marks",
    years=[2024,2023,2022,2019,2018,2017,2016,2015,2014,2013,2012,2011],
    why="Top repeated long/short across decade — principles, methods, nurse role.",
    must="Definition → aims → principles → methods (individual/group/mass) → nurse role",
    mistakes="Writing only lecture method. Principles without examples. No evaluation of HE.",
    mark_rows=[("Definition + aims", "1–2"), ("Principles", "2–3"), ("Methods", "2"), ("Nurse role", "1–2")],
    fast="HE = learning experiences for healthy behaviour. Principles: need-based, participation, known to unknown. Methods: individual, group, mass.",
    last="DEF + PRINCIPLES + METHODS + NURSE ROLE",
    eli="Health education teaches people how to stay healthy in words they understand — not scolding.",
    analogy="HE = coaching a team so they play better, not only treating injured players.",
    viva="Principles of HE? | Mass method example?",
    draw="",
    trick='🧠 Memory: Methods <strong>"IGM"</strong> Individual, Group, Mass',
    answer="""
          <h4>📄 Full Exam Version — Write in Answer Sheet</h4>
          <h4>A. Definition</h4>
          <p><strong>Health education</strong> is a process that informs, motivates and helps people to adopt and maintain healthy practices and lifestyles.</p>
          <h4>B. Aims</h4>
          <ul>
            <li>Inform about health matters</li>
            <li>Motivate healthy behaviour change</li>
            <li>Help people take decisions about health</li>
          </ul>
          <h4>C. Principles</h4>
          <ul>
            <li>Based on felt <strong>needs</strong> of people</li>
            <li><strong>Interest</strong> and active <strong>participation</strong></li>
            <li>Known to unknown; simple language</li>
            <li>Reinforcement; use of AV aids</li>
            <li>Leaders & community involvement</li>
            <li>Evaluation of results</li>
          </ul>
          <h4>D. Methods</h4>
          <ul>
            <li><strong>Individual:</strong> interview, counselling, home visit</li>
            <li><strong>Group:</strong> lecture, demonstration, group discussion, role play</li>
            <li><strong>Mass:</strong> TV, radio, newspaper, exhibitions, campaigns</li>
          </ul>
          <h4>🩺 Role of Nurse</h4>
          <ul>
            <li>Assess learning needs; plan HE session</li>
            <li>Use suitable method & AV aids</li>
            <li>Demonstrate skills (ORS, handwashing)</li>
            <li>Evaluate change; follow up</li>
          </ul>
          <h4>✅ Conclusion</h4>
          <p>Health education is a core function of the community health nurse.</p>
"""
)

T(
    id="t17", level="red", badge="badge-red", badge_txt="🔴 MUST",
    cat="Environment & Nutrition & Communication", title="Counselling",
    topic="counselling principles steps qualities counsellor",
    prob="prob-vhigh", prob_txt="🔴 VERY HIGH · 88% likely",
    papers="7 papers · 2025, 2024, 2022, 2019, 2018, 2017, 2016",
    marks="4–7 marks",
    years=[2025,2024,2022,2019,2018,2017,2016],
    why="Short note on counselling principles/steps; strong 2024–2025 presence.",
    must="Definition → principles → steps (GATHER/ROPE style) → qualities → nurse role",
    mistakes="Confusing counselling with giving orders. No confidentiality. Mixing with health education lecture.",
    mark_rows=[("Definition", "1"), ("Principles", "2"), ("Steps / qualities", "2–3"), ("Nurse role", "1")],
    fast="Counselling = face-to-face helping to take own decision. Confidential, non-judgemental, client-centred.",
    last="DEF + PRINCIPLES + STEPS + QUALITIES",
    eli="Counselling is private helpful talk so the person chooses what is best — nurse guides, not forces.",
    analogy="Counsellor = GPS suggesting routes; client still drives the car.",
    viva="Principles of counselling? | Difference HE vs counselling?",
    draw="",
    trick='🧠 Memory: Steps <strong>"GREAT"</strong> Greet, Rapport, Explore, Advise options, Together decide / follow-up',
    answer="""
          <h4>📄 Full Exam Version — Write in Answer Sheet</h4>
          <h4>A. Definition</h4>
          <p><strong>Counselling</strong> is a person-to-person helping process in which the counsellor assists the client to understand problems and make informed decisions.</p>
          <h4>B. Principles</h4>
          <ul>
            <li>Acceptance and respect</li>
            <li><strong>Confidentiality</strong></li>
            <li>Non-judgemental attitude</li>
            <li>Client's right to decide</li>
            <li>Empathy; individualization</li>
          </ul>
          <h4>C. Steps</h4>
          <ul>
            <li>Establish rapport; greet privately</li>
            <li>Listen & explore problem</li>
            <li>Give accurate information / options</li>
            <li>Help client decide</li>
            <li>Follow up</li>
          </ul>
          <h4>D. Qualities of Counsellor</h4>
          <ul>
            <li>Good listener; patience; honesty</li>
            <li>Knowledgeable; emotionally stable</li>
            <li>Maintains privacy</li>
          </ul>
          <h4>🩺 Nursing Role</h4>
          <p>Counsel on FP, HIV, breastfeeding, nutrition, adolescent issues; refer when specialized help needed.</p>
          <h4>✅ Conclusion</h4>
          <p>Counselling empowers clients to take healthy decisions with dignity.</p>
"""
)

T(
    id="t18", level="red", badge="badge-red", badge_txt="🔴 MUST",
    cat="Environment & Nutrition & Communication", title="Nutrition — Balanced Diet, Food, PEM, Adulteration",
    topic="nutrition balanced diet food classification cooking pem adulteration",
    prob="prob-vhigh", prob_txt="🔴 VERY HIGH · 97% likely",
    papers="13 papers · 2025, 2024, 2023, 2022, 2019, 2018, 2017, 2016, 2015, 2014, 2013, 2012, 2011",
    marks="4–9 marks",
    years=[2025,2024,2023,2022,2019,2018,2017,2016,2015,2014,2013,2012,2011],
    why="Highest frequency cluster — balanced diet, classification, cooking methods, PEM, adulteration.",
    must="Balanced diet def → food groups → cooking effects → PEM (marasmus/kwashiorkor) → adulteration examples → nurse role",
    mistakes="Saying soya is poor protein (FALSE). Amino acids = building blocks of proteins. Mixing marasmus/kwashiorkor.",
    mark_rows=[("Balanced diet + groups", "2–3"), ("Cooking / adulteration / PEM", "3–4"), ("Nurse role", "1")],
    fast="Balanced diet = all nutrients in right proportion. Energy+body building+protective foods. PEM: marasmus (wasting), kwashiorkor (oedema). Adulteration: water in milk, argemone in oil.",
    last="BALANCED DIET + 3 FOOD GROUPS + PEM + ADULTERATION",
    eli="Eat different foods so body gets energy, building blocks and vitamins — not only rice every day.",
    analogy="Balanced diet = full cricket team — batsmen (energy), bowlers (protein), fielders (vitamins).",
    viva="Building blocks of protein? | Difference marasmus vs kwashiorkor? | Soya protein quality?",
    draw="",
    trick='🧠 Memory: Foods <strong>"EBP"</strong> Energy, Body-building, Protective | PEM: Marasmus=Muscle waste; Kwashiorkor=oedema/Kwashi',
    answer="""
          <h4>📄 Full Exam Version — Write in Answer Sheet</h4>
          <h4>A. Balanced Diet</h4>
          <p>A <strong>balanced diet</strong> contains all essential nutrients (<strong>carbohydrates, proteins, fats, vitamins, minerals, water, fibre</strong>) in correct proportion to meet body needs.</p>
          <h4>B. Classification of Foods</h4>
          <ul>
            <li><strong>Energy-yielding:</strong> cereals, oils, sugar</li>
            <li><strong>Body-building:</strong> pulses, milk, egg, meat, fish, soya (good protein)</li>
            <li><strong>Protective:</strong> fruits, vegetables (vitamins & minerals)</li>
          </ul>
          <p><strong>Amino acids</strong> are building blocks of proteins.</p>
          <h4>C. Nutrients — Classification &amp; Protein (9-mark style)</h4>
          <ul>
            <li><strong>Macronutrients:</strong> carbohydrates, proteins, fats</li>
            <li><strong>Micronutrients:</strong> vitamins, minerals; also water &amp; fibre</li>
            <li><strong>By function:</strong> energy-yielding, body-building, protective</li>
            <li><strong>Protein:</strong> body-building; amino acids are building blocks; about <strong>1 g/kg/day</strong> adult requirement (write as taught); deficiency → PEM, poor healing, oedema (kwashiorkor)</li>
            <li>1 g carbohydrate = 4 kcal; 1 g protein = 4 kcal; 1 g fat = 9 kcal</li>
          </ul>
          <h4>D. PEM (Protein Energy Malnutrition)</h4>
          <ul>
            <li><strong>Marasmus:</strong> severe wasting, old man face, no oedema</li>
            <li><strong>Kwashiorkor:</strong> oedema, moon face, apathy, flaky paint skin</li>
          </ul>
          <h4>E. Food Adulteration + Food Adulteration Act (exam points)</h4>
          <ul>
            <li><strong>Meaning:</strong> intentional addition of inferior/harmful substances OR removal of valuable ingredients to cheat / cheapen food</li>
            <li><strong>Examples:</strong> water in milk; argemone in mustard oil; brick powder in chilli; chicory in coffee; metanil yellow in sweets</li>
            <li><strong>Prevention:</strong> buy sealed FSSAI/ISI packed foods; read labels; public awareness; report to food inspector</li>
            <li><strong>Law (write):</strong> Food safety regulated under <strong>FSSAI / Food Safety and Standards Act</strong> (older papers may say Prevention of Food Adulteration Act — PFA). Aims: ensure safe food, punish adulterators, set standards.</li>
          </ul>
          <p><em>For cooking methods &amp; food hygiene → open Topics card t26.</em></p>
          <h4>🩺 Nursing Role</h4>
          <p>Assess nutrition, educate on balanced diet &amp; weaning, identify PEM, counsel mothers, promote ICDS/Anganwadi services.</p>
          <h4>✅ Conclusion</h4>
          <p>Good nutrition prevents disease; nurses are key nutrition educators in the community.</p>
"""
)

T(
    id="t19", level="red", badge="badge-red", badge_txt="🔴 MUST",
    cat="Environment & Nutrition & Communication", title="Vitamins — Classification, A, D, C, Sources, Deficiency",
    topic="vitamins classification vitamin a d c k deficiency sources",
    prob="prob-vhigh", prob_txt="🔴 VERY HIGH · 92% likely",
    papers="8 papers · 2024, 2023, 2019, 2018, 2017, 2016, 2015, 2013",
    marks="7–8 marks",
    years=[2024,2023,2019,2018,2017,2016,2015,2013],
    why="Long answer favourite — classification + Vit A/D/C sources & deficiency.",
    must="Fat vs water soluble → Vit A, D, C, K (and B1 trap) sources + deficiency + nurse role",
    mistakes="Vit B1 → night blindness (WRONG — Vit A). Vit K anticoagulant (WRONG — helps clotting). Vit C fat soluble (WRONG).",
    mark_rows=[("Classification", "1–2"), ("Vit A, D, C detail", "4–5"), ("Others / nurse role", "1–2")],
    fast="Fat: A D E K. Water: B complex, C. A=night blindness; D=rickets; C=scurvy; B1=beriberi; K=clotting.",
    last="FAT ADEK / WATER BC | A-night blind | D-rickets | C-scurvy | K-clot",
    eli="Vitamins are tiny helpers in food. No Vit A → hard to see at night; no Vit C → gums bleed.",
    analogy="Vitamins = spice box — small amount, big effect if missing.",
    viva="Deficiency of Vit A? | Fat soluble vitamins? | Vit K function?",
    draw="",
    trick='🧠 Memory: <strong>"ADEK fat"</strong> | <strong>"A-Night, D-Bone, C-Gum, B1-Beriberi, K-Klott"</strong>',
    answer="""
          <h4>📄 Full Exam Version — Write in Answer Sheet</h4>
          <h4>A. Classification <span class="marks-pill">2–3 marks</span></h4>
          <ul>
            <li><strong>Fat-soluble:</strong> A, D, E, K — stored in body; excess can be toxic; need dietary fat for absorption</li>
            <li><strong>Water-soluble:</strong> B-complex, C — not stored much; excess excreted in urine; need regular intake</li>
          </ul>
          <h4>B. Fat-Soluble Vitamins — Full Block (ADEK)</h4>
          <ul>
            <li><strong>Vitamin A (Retinol):</strong> GLV, carrot, milk, liver, red palm oil → night blindness, xerophthalmia, Bitot's spots</li>
            <li><strong>Vitamin D (Calciferol):</strong> sunlight, fish liver oil, egg → rickets / osteomalacia</li>
            <li><strong>Vitamin E (Tocopherol):</strong> vegetable oils, nuts, green veg → antioxidant; deficiency rare (haemolytic anaemia in some contexts)</li>
            <li><strong>Vitamin K:</strong> green leafy veg + gut synthesis → <span class="highlight">blood clotting</span> (NOT anticoagulant)</li>
          </ul>
          <h4>C. Water-Soluble Highlights <span class="marks-pill">often 5 marks with A/D/C</span></h4>
          <ul>
            <li><strong>Vitamin C:</strong> amla, citrus, guava, tomato → <span class="highlight">scurvy</span> (bleeding gums)</li>
            <li><strong>Vitamin B1 (Thiamine):</strong> cereals, yeast → <span class="highlight">beriberi</span> (NOT night blindness)</li>
            <li>B2 riboflavin; B3 niacin (pellagra); B6; B12 / folate (megaloblastic anaemia) — name if asked</li>
          </ul>
          <h4>🩺 Nursing Role</h4>
          <p>Educate on diet diversity, give Vitamin A prophylaxis as scheduled, identify deficiency signs early, refer.</p>
          <h4>✅ Conclusion</h4>
          <p>Knowledge of vitamins helps prevent common deficiency diseases in the community.</p>
"""
)

T(
    id="t20", level="red", badge="badge-red", badge_txt="🔴 MUST",
    cat="Environment & Nutrition & Communication", title="Water — Safe Water, Purification, Water-borne Diseases",
    topic="water safe water purification filtration chlorination water borne",
    prob="prob-vhigh", prob_txt="🔴 VERY HIGH · 96% likely",
    papers="11 papers · 2025, 2024, 2022, 2019, 2018, 2017, 2015, 2014, 2013, 2012, 2011",
    marks="7–9 marks",
    years=[2025,2024,2022,2019,2018,2017,2015,2014,2013,2012,2011],
    why="Top long-answer topic — safe water criteria, purification methods, water-borne diseases.",
    must="Uses → safe water characteristics → purification (HH & large scale) → water-borne diseases → Horrock's → nurse role",
    mistakes="Confusing sewage/sullage. Skipping steps of slow sand filter. Forgetting boiling time.",
    mark_rows=[("Safe water + uses", "2"), ("Purification methods", "3–4"), ("Water-borne diseases", "2"), ("Nurse role", "1")],
    fast="Safe water: clear, odourless, free from pathogens/chemicals. HH: boiling, chlorine, filter. Large: storage, filtration, chlorination. Horrock's = bleaching powder dose.",
    last="SAFE WATER CRITERIA + HH PURIFY + LARGE SCALE + DISEASES",
    eli="Clean drinking water stops cholera and diarrhoea. Boil or add chlorine if unsure.",
    analogy="Water purification = washing dirty clothes in steps — settle dirt, filter, disinfect.",
    viva="Horrock's apparatus? | Water-borne diseases? | Household purification methods?",
    draw="""
          <div class="diagram-box">LARGE SCALE PURIFICATION
1. Storage / sedimentation
2. Filtration (slow sand / rapid sand)
3. Chlorination (disinfection)
        ↓
   Safe drinking water

HOUSEHOLD: Boiling | Chlorine tabs | Candle filter | SODIS</div>""",
    trick='🧠 Memory: Large scale <strong>"SFC"</strong> Storage, Filtration, Chlorination',
    answer="""
          <h4>📄 Full Exam Version — Write in Answer Sheet</h4>
          <h4>A. Uses of Water</h4>
          <ul>
            <li>Drinking, cooking, personal hygiene</li>
            <li>Cleaning, agriculture, industry</li>
          </ul>
          <h4>B. Safe / Potable Water <span class="marks-pill">2 marks</span></h4>
          <ul>
            <li>Free from pathogens and harmful chemicals</li>
            <li>Colourless, odourless, pleasant taste</li>
            <li>Adequate quantity; acceptable turbidity</li>
          </ul>
          <h4>C. Household Purification</h4>
          <ul>
            <li><strong>Boiling:</strong> rolling boil (commonly taught 5–10 min / as per class) then cool covered</li>
            <li><strong>Chemical:</strong> bleaching powder / chlorine tablets — correct dose &amp; contact time</li>
            <li><strong>Filtration:</strong> candle / ceramic / cloth filter (pre-filter turbid water)</li>
            <li>SODIS (solar) where taught; store in clean covered vessels</li>
          </ul>
          <h4>D. Large-Scale Purification (full 4–7 mark answer)</h4>
          <ol>
            <li><strong>Storage / plain sedimentation:</strong> hold raw water; heavier particles settle; some bacteria die</li>
            <li><strong>Coagulation–flocculation</strong> (rapid sand plants): alum added to form floc</li>
            <li><strong>Sedimentation:</strong> floc settles in settling tanks</li>
            <li><strong>Filtration:</strong>
              <ul>
                <li><strong>Slow sand filter:</strong> biological film (schmutzdecke) purifies; slow rate; classic exam method</li>
                <li><strong>Rapid sand filter:</strong> faster; needs coagulation first; frequent backwashing</li>
              </ul>
            </li>
            <li><strong>Disinfection / Chlorination:</strong> kill remaining pathogens; maintain residual chlorine; store in clear-water reservoir; distribute</li>
          </ol>
          <p><strong>Horrock's apparatus:</strong> estimates bleaching powder needed to disinfect a known volume of water (wells/tanks).</p>
          <h4>E. Water-borne Diseases</h4>
          <ul>
            <li>Cholera, typhoid, viral hepatitis A/E, amoebiasis, giardiasis, poliomyelitis (faecal-oral)</li>
          </ul>
          <h4>🩺 Nursing Role</h4>
          <p>Educate on safe water &amp; boiling, demonstrate chlorination, protect wells, report outbreaks, promote sanitation.</p>
          <h4>✅ Conclusion</h4>
          <p>Safe water is fundamental to community health; purification prevents major epidemics.</p>
"""
)

T(
    id="t21", level="yellow", badge="badge-yellow", badge_txt="🟡 HIGH",
    cat="Environment & Nutrition & Communication", title="Ventilation",
    topic="ventilation types natural mechanical standards",
    prob="prob-high", prob_txt="🟡 HIGH · 80% likely",
    papers="3 papers · 2025, 2019, 2018",
    marks="7–9 marks",
    years=[2025,2019,2018],
    why="Long answer in recent papers (2018, 2019, 2025) on types/standards of ventilation.",
    must="Definition → standards → types natural/mechanical/artificial → advantages → nurse role",
    mistakes="Saying any open window is enough without standards. Confusing exhaust vs plenum.",
    mark_rows=[("Definition + standards", "2"), ("Types explained", "4–5"), ("Importance / nurse", "1–2")],
    fast="Ventilation = supply fresh air & remove vitiated air. Natural: windows, doors, cross ventilation. Mechanical: exhaust, plenum, AC.",
    last="DEF + STANDARDS + NATURAL vs MECHANICAL TYPES",
    eli="Ventilation means fresh air in, stale air out — so rooms don't feel stuffy and germs don't stay.",
    analogy="Ventilation = changing water in a fish tank so fish stay healthy.",
    viva="Types of ventilation? | What is cross ventilation?",
    draw="""
          <div class="diagram-box">NATURAL VENTILATION
  Wind → [Window IN] Room [Window OUT] → stale air
         Cross ventilation = openings on opposite walls

MECHANICAL
  Exhaust: sucks air out
  Plenum: pushes fresh air in
  AC: filters + cools + circulates</div>""",
    trick='🧠 Memory: Mechanical <strong>"EPA"</strong> Exhaust, Plenum, Air-conditioning',
    answer="""
          <h4>📄 Full Exam Version — Write in Answer Sheet</h4>
          <h4>A. Definition <span class="marks-pill">2 marks</span></h4>
          <p><strong>Ventilation</strong> is the process of supplying fresh air and removing vitiated (used) air from an enclosed space to maintain a healthy atmosphere.</p>
          <h4>B. Standards / Requirements</h4>
          <ul>
            <li>Adequate air change without draught</li>
            <li>Comfortable temperature & humidity</li>
            <li>Removal of odours, CO2, dust, pathogens</li>
          </ul>
          <h4>C. Types <span class="marks-pill">5 marks</span></h4>
          <p><strong>1. Natural ventilation</strong></p>
          <ul>
            <li>Perflation / wind action through windows & doors</li>
            <li><strong>Cross ventilation</strong> — openings on opposite sides</li>
            <li>Diffusion; temperature difference (stack effect)</li>
          </ul>
          <p><strong>2. Mechanical / Artificial</strong></p>
          <ul>
            <li><strong>Exhaust system</strong> — extracts foul air</li>
            <li><strong>Plenum system</strong> — forces fresh air in</li>
            <li><strong>Air conditioning</strong> — controls temp, humidity, purity</li>
          </ul>
          <h4>🩺 Nursing Role</h4>
          <p>Advise families on windows, cross ventilation, avoid overcrowding; ensure ward ventilation in institutions.</p>
          <h4>✅ Conclusion</h4>
          <p>Good ventilation prevents respiratory infections and improves comfort and health.</p>
"""
)

T(
    id="t22", level="yellow", badge="badge-yellow", badge_txt="🟡 HIGH",
    cat="Environment & Nutrition & Communication", title="Housing Standards + Environmental Health Factors",
    topic="housing standards environmental health factors site",
    prob="prob-high", prob_txt="🟡 HIGH · 79% likely",
    papers="5 papers · 2025, 2018, 2017, 2016, 2013",
    marks="4 marks",
    years=[2025,2018,2017,2016,2013],
    why="Short note on standards of housing / environmental factors; appeared 2025.",
    must="Criteria of healthy housing → site, space, light, ventilation, water, waste → health effects",
    mistakes="Only listing 'clean house' without measurable standards. Ignoring overcrowding & lighting.",
    mark_rows=[("Definition / importance", "1"), ("Standards list", "2–3"), ("Health effects / nurse", "1")],
    fast="Healthy house: good site, adequate rooms, light, ventilation, safe water, latrine, waste disposal, no overcrowding.",
    last="SITE + SPACE + LIGHT + VENTILATION + WATER + LATRINE + WASTE",
    eli="A healthy house has space, light, air, clean water and toilet — not just four walls.",
    analogy="House standards = safety checklist before buying a vehicle.",
    viva="Criteria of good housing? | Effect of overcrowding?",
    draw="",
    trick='🧠 Memory: <strong>"SLVW-LO"</strong> Site, Light, Ventilation, Water, Latrine, Overcrowding avoided',
    answer="""
          <h4>📄 Full Exam Version — Write in Answer Sheet</h4>
          <h4>A. Introduction</h4>
          <p><strong>Housing</strong> is a basic environmental determinant of health. Poor housing causes respiratory infections, accidents, stress and vector breeding.</p>
          <h4>B. Standards of Healthy Housing</h4>
          <ul>
            <li><strong>Site:</strong> elevated, dry, away from pollution/floods</li>
            <li><strong>Space:</strong> adequate floor space; avoid overcrowding</li>
            <li><strong>Rooms:</strong> separate living/kitchen as far as possible</li>
            <li><strong>Light & ventilation:</strong> enough windows; sunlight</li>
            <li><strong>Water supply:</strong> safe and adequate</li>
            <li><strong>Sanitation:</strong> sanitary latrine; waste water drainage</li>
            <li><strong>Refuse disposal</strong> arrangement</li>
            <li>Protection from dampness, insects, animals</li>
          </ul>
          <h4>C. Environmental Health Factors</h4>
          <ul>
            <li>Air, water, soil, housing, vectors, noise, radiation</li>
          </ul>
          <h4>🩺 Nursing Role</h4>
          <p>Assess home during visit, educate on overcrowding/ventilation/latrine use, link to sanitation programmes.</p>
          <h4>✅ Conclusion</h4>
          <p>Healthy housing is preventive medicine for the whole family.</p>
"""
)

T(
    id="t23", level="red", badge="badge-red", badge_txt="🔴 MUST",
    cat="Environment & Nutrition & Communication", title="Waste Disposal + Well Disinfection + Mosquito Control",
    topic="waste refuse disposal well disinfection mosquito control sewage sullage",
    prob="prob-vhigh", prob_txt="🔴 VERY HIGH · 90% likely",
    papers="10 papers · 2024, 2022, 2018, 2017, 2016, 2015, 2014, 2013, 2012, 2011",
    marks="4–7 marks",
    years=[2024,2022,2018,2017,2016,2015,2014,2013,2012,2011],
    why="Refuse disposal methods + mosquito control + well disinfection frequently as short notes.",
    must="Refuse types → disposal methods → sewage vs sullage → well disinfection steps → mosquito control → nurse role",
    mistakes="Sewage = without excreta (WRONG — sewage HAS excreta; sullage does NOT). Chikungunya from chicken (WRONG — Aedes).",
    mark_rows=[("Refuse disposal", "2"), ("Well disinfection", "2"), ("Mosquito control", "2"), ("Sewage/sullage note", "1")],
    fast="Refuse: dumping, composting, incineration, burial. Sullage=wastewater without excreta. Well: bleaching powder. Mosquito: source reduction, larvicide, nets, spray.",
    last="REFUSE METHODS + SULLAGE≠SEWAGE + WELL BLEACH + MOSQUITO 4 METHODS",
    eli="Throw garbage properly, clean wells with bleach powder, and stop mosquitoes by removing stored water.",
    analogy="Mosquito control = remove the mosquito's 'hotel' (stagnant water).",
    viva="Sewage vs sullage? | Vector of dengue? | Methods of refuse disposal?",
    draw="",
    trick='🧠 Memory: <strong>Sullage = NO stool</strong>; <strong>Sewage = WITH stool</strong> | Dengue/Chikungunya = Aedes | Malaria = Anopheles',
    answer="""
          <h4>📄 Full Exam Version — Write in Answer Sheet</h4>
          <h4>A. Refuse / Waste Disposal</h4>
          <ul>
            <li><strong>Refuse:</strong> solid waste from houses (ash, rubbish, garbage)</li>
            <li>Methods: dumping, controlled tipping/sanitary landfill, composting, incineration, burial, manure pits</li>
          </ul>
          <h4>B. Sewage vs Sullage</h4>
          <ul>
            <li><strong>Sewage:</strong> wastewater <span class="highlight">WITH human excreta</span></li>
            <li><strong>Sullage:</strong> wastewater from kitchen/bath <span class="highlight">WITHOUT excreta</span></li>
          </ul>
          <h4>C. Well Disinfection</h4>
          <ul>
            <li>Find volume of water; calculate bleaching powder dose (Horrock's / formula taught)</li>
            <li>Mix bleaching powder into paste; dissolve; pour around well</li>
            <li>Allow contact time; advise temporary alternate water if needed</li>
          </ul>
          <h4>D. Mosquito Control</h4>
          <ul>
            <li><strong>Anti-larval:</strong> source reduction (empty pots), larvicides, fish</li>
            <li><strong>Anti-adult:</strong> insecticide spray, screens</li>
            <li><strong>Personal protection:</strong> nets, repellents, full sleeves</li>
            <li>Vectors: <strong>Anopheles</strong> (malaria), <strong>Aedes aegypti</strong> (dengue, chikungunya)</li>
          </ul>
          <h4>🩺 Nursing Role</h4>
          <p>Educate on dry day, waste segregation, latrine use; assist disinfection; participate in fogging campaigns.</p>
          <h4>✅ Conclusion</h4>
          <p>Environmental sanitation and vector control prevent major community diseases.</p>
"""
)

T(
    id="t24", level="green", badge="badge-green", badge_txt="🟢 MED",
    cat="Foundations", title="Community Health Team + Nursing Process",
    topic="community health team nursing process assessment planning",
    prob="prob-medium", prob_txt="🟢 MEDIUM · 68% likely",
    papers="5 papers · 2024, 2015, 2014, 2013, 2012",
    marks="4 marks",
    years=[2024,2015,2014,2013,2012],
    why="Medium probability short note — health team members + nursing process steps in community.",
    must="Team members (MO, PHN, ANM, ASHA, AWW…) → nursing process ADPIE in community context",
    mistakes="Forgetting ASHA/AWW. Writing hospital nursing process without community examples.",
    mark_rows=[("Health team members", "2"), ("Nursing process steps + example", "2")],
    fast="Team: MO, health supervisor, PHN/CHN, ANM/MPHW, ASHA, AWW, village leaders. Process: Assess→Diagnose→Plan→Implement→Evaluate.",
    last="TEAM LIST + ADPIE WITH COMMUNITY EXAMPLE",
    eli="Many workers share community health work. Nurse follows steps: check → find problem → plan → do → check again.",
    analogy="Health team = cricket team with different roles; nursing process = match plan.",
    viva="Members of health team? | Steps of nursing process?",
    draw="",
    trick='🧠 Memory: Process <strong>"ADPIE"</strong> Assess, Diagnose, Plan, Implement, Evaluate',
    answer="""
          <h4>📄 Full Exam Version — Write in Answer Sheet</h4>
          <h4>A. Community Health Team</h4>
          <ul>
            <li><strong>Medical Officer</strong> — clinical & administrative head at PHC</li>
            <li><strong>PHN / Community Health Nurse</strong> — nursing care, supervision, HE</li>
            <li><strong>Health Supervisor / LHV</strong></li>
            <li><strong>ANM / MPHW</strong> — sub-centre services, MCH, immunization</li>
            <li><strong>ASHA</strong> — link worker, mobilization, home visits</li>
            <li><strong>Anganwadi worker</strong> — nutrition, ICDS</li>
            <li>Pharmacist, lab tech, village leaders as partners</li>
          </ul>
          <h4>B. Community Health Nursing Process — Importance</h4>
          <ul>
            <li>Provides <strong>systematic, scientific</strong> care (not trial-and-error)</li>
            <li>Identifies actual &amp; potential family/community problems early</li>
            <li>Improves continuity, quality and documentation of care</li>
            <li>Helps involve family in goal-setting; measures outcomes</li>
            <li>Guides priority setting when caseload is large</li>
          </ul>
          <h4>C. Steps of Community Health Nursing Process (full)</h4>
          <ol>
            <li><strong>Assessment:</strong> collect data — family survey, history, observation of home, environment, records, community resources</li>
            <li><strong>Nursing diagnosis:</strong> state health problems / needs (e.g., knowledge deficit regarding ORS; risk of dehydration)</li>
            <li><strong>Planning:</strong> set short- &amp; long-term goals with family; select interventions; arrange resources/referral</li>
            <li><strong>Implementation:</strong> give care, health education, procedures, immunization motivation, referral — using bag technique as needed</li>
            <li><strong>Evaluation:</strong> compare results with goals; reassess; modify plan; document in family folder</li>
          </ol>
          <h4>🩺 Nursing Role</h4>
          <p>Coordinate team, apply nursing process to families, document and follow up.</p>
          <h4>✅ Conclusion</h4>
          <p>Teamwork plus systematic nursing process improves community health outcomes.</p>
"""
)

# Extra past-paper gap cards (t25–t36)
import sys
from pathlib import Path as _Path
sys.path.insert(0, str(_Path(__file__).resolve().parent))
from extra_topics import register as _register_extra
_register_extra(T)

# Replace long prose with short mark-wise answers
from markwise_answers import apply_markwise
apply_markwise(TOPICS)

# Extra diagrams on high-yield cards
_EXTRA_DRAW = {
    "t3": '<div class="diagram-box">LEVELS OF CARE / REFERRAL\nHome/Community → Sub-centre → PHC → CHC/District → Tertiary\n(two-way arrows = referral + feedback)</div>',
    "t4": '<div class="diagram-box">LEVELS OF PREVENTION\nPRIMARY (promote+protect) → SECONDARY (early Dx/Rx) → TERTIARY (rehab)</div>',
    "t10": '<div class="diagram-box">BAG TECHNIQUE FLOW\nClean paper → Handwash → Articles OUT → Close bag → Procedure\n→ Waste discard → Clean → Handwash → Replace → Close</div>',
    "t14": '<div class="diagram-box">COMMUNICATION PROCESS\nSENDER → MESSAGE → CHANNEL → RECEIVER → FEEDBACK\n(Barriers/Noise around the path)</div>',
    "t21": '<div class="diagram-box">CROSS VENTILATION\nWind → [Window IN] ROOM [Window OUT] → stale air\nOpposite wall openings</div>',
    "t28": '<div class="diagram-box">RAPID SAND FILTRATION\nCoagulation (alum) → Sedimentation → Rapid sand filter → Chlorination</div>',
    "t33": '<div class="diagram-box">DISEASE CYCLE\nIncubation → Prodromal → Illness → Decline → Convalescence</div>',
    "t11": '<div class="diagram-box">REFERRAL LADDER\nSC → PHC → FRU/CHC → District → Tertiary\n↑ feedback ↓</div>',
}
for _t in TOPICS:
    if _t["id"] in _EXTRA_DRAW and not (_t.get("draw") or "").strip():
        _t["draw"] = _EXTRA_DRAW[_t["id"]]

assert len(TOPICS) == 36, len(TOPICS)
print("TOTAL TOPICS", len(TOPICS))
