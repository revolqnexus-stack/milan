# -*- coding: utf-8 -*-
"""Assemble complete chn.html"""
from pathlib import Path
import importlib.util

# Load topics
spec = importlib.util.spec_from_file_location("topics_data", r"c:\Users\eathe\milan\_gen\topics_data.py")
td = importlib.util.module_from_spec(spec)
spec.loader.exec_module(td)
TOPICS = td.TOPICS
years_html = td.years_html
marks_table = td.marks_table

OUT = Path(r"c:\Users\eathe\milan\chn.html")
GEN = Path(r"c:\Users\eathe\milan\_gen")

import re
build_src = (GEN / "build_chn.py").read_text(encoding="utf-8")
m = re.search(r'CSS = r"""(.*?)"""', build_src, re.S)
CSS = m.group(1)

def card_html(t):
    draw = t.get("draw") or ""
    draw_section = f"<p><strong>Draw / Diagram:</strong></p>{draw}" if draw else ""
    return f'''
    <div class="card topic-card" data-level="{t['level']}" data-topic="{t['topic']}" data-id="{t['id']}">
      <div class="card-header" onclick="toggleCard(this)">
        <span class="badge {t['badge']}">{t['badge_txt']}</span>
        <div><div class="card-title">{t['title']}</div><div class="card-sub">{t['cat']}</div></div>
        <span class="chevron">⌄</span>
      </div>
      <div class="card-body">
        <div class="done-row">
          <div class="done-checkbox" id="cb-{t['id']}" onclick="toggleDone('{t['id']}')"></div>
          <span class="done-label" onclick="toggleDone('{t['id']}')">Mark as Done ✅</span>
        </div>
        <div class="exam-scorecard">
          <span class="prob-badge {t['prob']}">{t['prob_txt']}</span>
          <span class="meta-pill">📊 {t['papers']}</span>
          <span class="meta-pill">📝 {t['marks']}</span>
        </div>
        <div class="exam-grid">
          <div class="exam-block">
            <h5>❓ Why Examiners Ask This</h5>
            <p>{t['why']}</p>
          </div>
          <div class="exam-block">
            <h5>✍️ What You MUST Write</h5>
            <p>{t['must']}</p>
          </div>
          <div class="exam-block mistake-block">
            <h5>🚫 Common Mistakes (Mark Killers)</h5>
            <p>{t['mistakes']}</p>
          </div>
          <div class="exam-block">
            <h5>📊 Mark Distribution</h5>
            {marks_table(t['mark_rows'])}
          </div>
        </div>
        <div class="rev-tabs">
          <div class="rev-box fast-rev"><h5>⚡ Fast Revision (2 min)</h5><p>{t['fast']}</p></div>
          <div class="rev-box last-rev"><h5>🚨 Last-Minute Memory</h5><p>{t['last']}</p></div>
        </div>
        <div class="eli10-box"><strong>🧒 Explain Like I'm 10:</strong> {t['eli']}<br><strong>🔮 Analogy:</strong> {t['analogy']}</div>
        <div class="tip-box"><strong>🎤 Viva:</strong> {t['viva']}</div>
        {draw_section}
        <hr class="topic-divider">
        <div class="year-tags">{years_html(t['years'])}</div>
        <div class="trick-box">{t['trick']}</div>
        <div class="ans-block">{t['answer']}
        </div>
      </div>
    </div>
'''

# Group topics
foundations = [t for t in TOPICS if t['id'] in ('t1','t2','t3','t4','t24')]
# User said FOUNDATIONS (8), EPI (8), ENV (8)
# t1-t4 foundations-ish, but list says:
# FOUNDATIONS (8): t1-t4 + maybe more from first group
# Looking at user list:
# FOUNDATIONS (8), EPIDEMIOLOGY & CHILD/FAMILY (8), ENVIRONMENT & NUTRITION & COMMUNICATION (8)
# t1-t4 foundations core, t5-t13 epi/child? That's 9...
# Better mapping by user categories in topic list:
# FOUNDATIONS: t1 CHN, t2 Health, t3 PHC, t4 Prevention, and they said 8...
# Looking again at user:
# Categories: FOUNDATIONS (8), EPIDEMIOLOGY & CHILD/FAMILY (8), ENVIRONMENT & NUTRITION & COMMUNICATION (8)
# Topics t1-t24 in order - likely:
# Foundations: t1-t4, t11?, t12?, t24? 
# Actually sequential:
# t1-t8 first 8? But t5 is epidemiology...
# Logical:
# FOUNDATIONS: t1 CHN, t2 Health, t3 PHC, t4 Prevention, t11 Referral, t12 Records, t13 Family?, t24 Team
# EPI & CHILD: t5 Epi, t6 CD, t7 Imm, t8 U5, t9 Minor, t10 Home visit, t13 MCH, ? 
# ENV: t14-t23

# User said exactly 8+8+8. Best split by topic numbers as listed:
# Group 1 Foundations: t1,t2,t3,t4,t11,t12,t13,t24 (nurse foundations + systems)
# Group 2 Epi & Child/Family: t5,t6,t7,t8,t9,t10 + wait need 8: t5-t10,t? 
# t5,t6,t7,t8,t9,t10 = 6, plus need 2 more from family...

# Simplest: use categories already on topics and redistribute:
# Foundations: t1,t2,t3,t4,t11,t12,t24 + one more
# Looking at my cat field:
# Foundations: t1,t2,t3,t4,t24
# Epidemiology & Child/Family: t5-t13
# Environment...: t14-t23

# Pedagogical groups (natural sizes — not forced 8/8/8):
# Foundations: CHN, Health, PHC, Prevention, Referral, Records, MCH, Team
# Epi & Child/Family: Epi, CD, Imm, U5, Minor, Home visit
# Env / Nutrition / Communication: Comm, AV, HE, Counselling, Nutrition, Vitamins, Water, Vent, Housing, Waste
found_ids = ['t1', 't2', 't3', 't4', 't11', 't12', 't13', 't24', 't33', 't36']
epi_ids = ['t5', 't6', 't7', 't8', 't9', 't10', 't25', 't29', 't30', 't31', 't34']
env_ids = ['t14', 't15', 't16', 't17', 't18', 't19', 't20', 't21', 't22', 't23', 't26', 't27', 't28', 't32', 't35']

by_id = {t['id']: t for t in TOPICS}

def section_cards(ids):
    return "\n".join(card_html(by_id[i]) for i in ids)

# Probability table rows
def prob_row(t):
    level_map = {'red':'VERY HIGH','yellow':'HIGH','green':'MEDIUM'}
    icon = {'red':'🔴','yellow':'🟡','green':'🟢'}[t['level']]
    pct = t['prob_txt'].split('·')[1].strip().replace(' likely','')
    return f"<tr><td>{icon} {t['title'].split('—')[0].strip()}</td><td>{level_map[t['level']]}</td><td>{pct}</td><td>{t['marks']}</td></tr>"

prob_rows = "\n".join(prob_row(t) for t in TOPICS)

# Score page top 25 - use 24 topics + 1 combined tip
score_order = sorted(TOPICS, key=lambda x: {'red':0,'yellow':1,'green':2}[x['level']])
# Manual priority order from user scores
priority_order = [
    't18','t1','t20','t10','t16','t12','t7','t26','t30','t28','t14','t19','t25','t6',
    't31','t2','t36','t8','t23','t17','t5','t3','t35','t32','t27','t13','t11','t9',
    't21','t22','t29','t34','t33','t15','t4','t24'
]

def predict_cards():
    cards = []
    for i, tid in enumerate(priority_order, 1):
        t = by_id[tid]
        cards.append(f'''<div class="predict-card"><div class="predict-rank">{i}</div><div><strong>{t['title'].split('—')[0].strip()}</strong><br><span style="font-size:12px;color:var(--subtext)">{t['prob_txt']} · {t['marks']}</span></div></div>''')
    return "\n".join(cards)

# Drill items
def drill_item(q, a):
    return f'''<div class="drill-item" onclick="this.classList.toggle('revealed')"><strong>{q}</strong><div class="drill-ans">{a}</div></div>'''

DEFS = [
("Community Health Nursing","Nursing + public health care to individuals, families & communities focusing on prevention and health promotion."),
("Health (WHO)","Complete physical, mental and social well-being — not merely absence of disease."),
("Primary Health Care","Essential health care universally accessible; Alma Ata 1978."),
("Epidemiology","Study of distribution & determinants of health events in populations, applied to control problems."),
("Epidemiological triad","Agent + Host + Environment interaction causing disease."),
("Communicable disease","Illness due to infectious agent transmissible from reservoir to host."),
("Immunization","Artificial induction of immunity by vaccine or immunoglobulin."),
("Cold chain","System keeping vaccines at recommended temperature from maker to beneficiary."),
("Under-five clinic","Well-baby clinic providing comprehensive care to children below 5 years."),
("Home visit","Planned visit by CHN to family home for assessment, care and education."),
("Bag technique","Method of using community nursing bag during home visit without spreading infection."),
("Referral system","Sending client to appropriate higher care with feedback (two-way)."),
("Family folder","File with health records of all members of one family."),
("Health education","Process that informs & motivates people to adopt healthy practices."),
("Counselling","Face-to-face helping process for informed client decisions."),
("Balanced diet","Diet with all essential nutrients in correct proportion."),
("PEM","Protein Energy Malnutrition — marasmus / kwashiorkor."),
("Safe water","Water free from pathogens & harmful chemicals; clear, odourless."),
("Ventilation","Supply of fresh air and removal of vitiated air from enclosed space."),
("Sullage","Wastewater from kitchen/bath WITHOUT excreta."),
("Sewage","Wastewater WITH human excreta."),
("Endemic","Constant presence of disease in a geographic area."),
("Epidemic","Unusual increase of disease cases in a community/time."),
("Pandemic","Epidemic spanning many countries / worldwide."),
("Carrier","Person harbouring agent without symptoms, can transmit."),
("Incubation period","Time from infection to appearance of first symptoms."),
("Mortality","Death rate in a population."),
("Weaning","Gradual introduction of complementary foods with continued breastfeeding."),
("Community","Group of people living in a defined area sharing common interests."),
("Nosocomial infection","Hospital-acquired infection."),
("Horrock's apparatus","Device to estimate bleaching powder dose for water disinfection."),
("First Referral Unit","Facility equipped for emergency obstetric & newborn care."),
("Vasectomy","Permanent male sterilization."),
("Tubectomy","Permanent female sterilization."),
("Cross ventilation","Openings on opposite walls allowing air to pass through."),
("Fomite","Inanimate object that can transmit infection."),
("Active immunity","Immunity from body's own antibody response (vaccines/disease)."),
("Passive immunity","Ready-made antibodies given (immunoglobulin)."),
("Night blindness","Early sign of Vitamin A deficiency."),
("Scurvy","Vitamin C deficiency — bleeding gums."),
("Rickets","Vitamin D deficiency in children — soft bones."),
("Beriberi","Vitamin B1 (thiamine) deficiency."),
("Aedes aegypti","Mosquito vector of dengue and chikungunya."),
("Anopheles","Mosquito vector of malaria."),
("Plasmodium","Parasite causing malaria."),
("Infant","Child from birth to 1 completed year of age."),
("Infection","Entry and multiplication of pathogen in body tissues causing disease."),
("Sporadic","Scattered / occasional occurrence of a disease (few cases, irregular)."),
("Morbidity rate","Rate of illness / sickness in a population in a given time."),
("Antenatal woman","Pregnant woman receiving care before delivery."),
("ASHA","Accredited Social Health Activist — community link health worker."),
("Joint family","Family of multiple generations living together sharing kitchen/resources."),
("Family","Basic social unit of parents and children (and relatives) living together."),
("Record","Permanent written account of health information / nursing activities."),
("Community Nursing Process","Systematic ADPIE steps applied to family/community care."),
("Demography","Scientific study of human population — size, structure, change."),
("Antenatal care","Care of pregnant woman from conception to onset of labour."),
("Postnatal care","Care of mother and newborn after delivery (classically 6 weeks)."),
("Contraceptive","Method/device/drug used to prevent pregnancy."),
("Disinfection","Killing / removing pathogenic organisms from articles/environment (spores may remain)."),
("Neonatal period","First 28 days of life after birth."),
("Quarantine","Restriction of movement of healthy contacts to prevent spread of infection."),
("Infant mortality rate","Deaths of infants under 1 year per 1000 live births in a year."),
("Disease","Maladjustment / departure from health — structural or functional abnormality."),
("Maternal and Child Health (MCH)","Health services for mothers, infants and children to reduce mortality/morbidity."),
("Anthropometry","Body measurements (height, weight, MUAC, etc.) to assess nutrition/growth."),
("Calorie","Unit of heat/energy; nutrition uses kilocalorie (kcal)."),
("Sanitary well","Protected well with parapet, platform, cover and drain — safe water source."),
("Disease cycle","Stages of disease in a person: incubation → prodromal → illness → decline → convalescence."),
("Eligible couple","Currently married couple with wife in reproductive age (about 15–49 yrs)."),
("Community diagnosis","Identification of health problems/needs of a community using data."),
("Cumulative record","Continuous longitudinal health record of one person over time."),
]

FILLS = [
("World Health Day is observed on ____.","April 7"),
("Under-five clinic is also called ____ clinic.","Well-baby"),
("Goitre is due to deficiency of ____.","Iodine"),
("Vitamin K is a ____ soluble vitamin.","Fat"),
("Malaria is caused by ____.","Plasmodium"),
("Vitamin C deficiency causes ____.","Scurvy"),
("Amino acids are building blocks of ____.","Proteins"),
("Hospital-acquired infection is called ____.","Nosocomial infection"),
("FRU means ____.","First Referral Unit"),
("Cold chain temperature for most vaccines is ____ °C.","+2 to +8"),
("BCG is given by ____ route.","Intradermal"),
("Night blindness is due to deficiency of Vitamin ____.","A"),
("Vector of dengue is ____.","Aedes aegypti"),
("Vector of malaria is ____.","Anopheles"),
("Sullage does ____ contain excreta.","NOT"),
("Sewage ____ contain excreta.","DOES"),
("Noise is measured in ____.","Decibels"),
("Alma Ata conference year ____.","1978"),
("Vitamin D deficiency in children causes ____.","Rickets"),
("Vitamin B1 deficiency causes ____.","Beriberi"),
("Permanent male sterilization is ____.","Vasectomy"),
("Permanent female sterilization is ____.","Tubectomy"),
("Horrock's apparatus is used for ____.","Bleaching powder dose for water"),
("OPV is a ____ vaccine (live/killed).","Live"),
("Models are ____ dimensional AV aids.","Three (3D)"),
("Kwashiorkor shows ____ (oedema/no oedema).","Oedema"),
("Marasmus shows severe ____.","Wasting"),
("Primary prevention example: ____.","Immunization"),
("Secondary prevention example: ____.","Screening / early diagnosis"),
("Tertiary prevention example: ____.","Rehabilitation"),
("PHC has ____ essential elements.","Eight (8)"),
("Most heat-sensitive vaccine commonly tested in papers is ____.","OPV (oral polio)"),
("Bleaching powder used to disinfect ____.","Water / well"),
("Complementary feeding starts around ____ months.","6 months"),
("TT is given to antenatal mothers for preventing ____.","Neonatal tetanus"),
("ORS is used in ____.","Diarrhoea / dehydration"),
("Growth monitoring uses ____ chart.","Growth chart"),
("Family folder contains records of ____.","All family members"),
("Two-way referral includes ____.","Feedback from higher facility"),
("Chikungunya is transmitted by ____.","Aedes mosquito (NOT chicken)"),
("Vitamin K helps in blood ____.","Clotting"),
("Diabetes is a ____ disease (communicable/non).","Non-communicable"),
("Soya is a ____ source of protein.","Good / rich"),
("Bitot's spots seen in Vitamin ____ deficiency.","A"),
("Slow sand filter is used in ____ purification.","Large-scale water"),
("Ice-lined refrigerator short form ____.","ILR"),
("Eligible couple register is used in ____ programme.","Family welfare"),
("ASHA is a ____ worker.","Link / community health"),
("Anganwadi is under ____ scheme.","ICDS"),
("Decibels measure ____.","Noise intensity"),
("Anthropometry means measurement of ____.","Human body (Ht/Wt/MUAC etc.)"),
("1 gram fat yields ____ kcal.","9"),
("1 gram protein yields ____ kcal.","4"),
("Demography is study of ____.","Human population"),
("Oxidation pond is used for ____.","Sewage treatment"),
("Lathyrism is caused by ____.","Kesari dal (Lathyrus sativus)"),
("Koplik's spots are seen in ____.","Measles"),
("Bitot's spots are due to deficiency of ____.","Vitamin A"),
("Didactic method is ____-way teaching.","One"),
("Socratic method uses ____ and discussion.","Questions"),
("Pulse Polio gives ____ vaccine to under-fives.","OPV"),
("Mid-Day Meal is given in ____.","Schools"),
("ASHA full form starts with Accredited Social ____.","Health Activist"),
("Neonatal period is first ____ days.","28"),
("IMR is infant deaths per ____ live births.","1000"),
("Temporary hardness removed by ____.","Boiling / lime"),
("Rapid sand filtration needs ____ before filter.","Coagulation (alum)"),
("Standing orders are written by ____.","Medical Officer"),
("Exclusive breastfeeding recommended for ____ months.","6"),
]

TF = [
("Diabetes mellitus is a communicable disease.","FALSE — Non-communicable / lifestyle disease."),
("Soya is a poor source of protein.","FALSE — Soya is a rich/good plant protein."),
("Vitamin B1 deficiency causes night blindness.","FALSE — Night blindness is Vitamin A; B1 causes beriberi."),
("Sullage contains human excreta.","FALSE — Sullage has NO excreta; sewage does."),
("Chikungunya is transmitted from chicken.","FALSE — Transmitted by Aedes mosquito."),
("Models are three-dimensional AV aids.","TRUE"),
("Vitamin K is an anticoagulant.","FALSE — Vitamin K helps clotting."),
("BCG is a killed vaccine.","FALSE — BCG is live attenuated."),
("OPV is a live vaccine.","TRUE"),
("Under-five clinic is only for sick children.","FALSE — Also well-baby / preventive care."),
("Primary prevention includes screening tests.","FALSE — Screening is secondary prevention."),
("Alma Ata declaration was in 1978.","TRUE"),
("Aedes transmits malaria.","FALSE — Anopheles transmits malaria; Aedes dengue/chikungunya."),
("Vasectomy is female sterilization.","FALSE — Vasectomy is male; tubectomy female."),
("Cold chain vaccines are stored at 2–8°C.","TRUE"),
("Family folder is for one individual only.","FALSE — For entire family."),
("Health is merely absence of disease.","FALSE — WHO: complete physical, mental, social well-being."),
("Kwashiorkor presents with oedema.","TRUE"),
("Marasmus presents with oedema.","FALSE — Marasmus = wasting without oedema."),
("Horrock's apparatus measures BP.","FALSE — Estimates bleaching powder for water."),
("World Health Day is May 1.","FALSE — April 7."),
("Noise is measured in millimetres.","FALSE — Decibels."),
("Referral should be one-way only.","FALSE — Two-way with feedback preferred."),
("Cross ventilation needs opposite openings.","TRUE"),
("Vitamin C is fat soluble.","FALSE — Water soluble; ADEK are fat soluble."),
("Immunization is primary prevention.","TRUE"),
("Sewage is wastewater without excreta.","FALSE — Sewage WITH excreta."),
("Dengue vector is Anopheles.","FALSE — Aedes aegypti."),
("Amino acids build proteins.","TRUE"),
("PHC has 8 elements.","TRUE"),
("Incubation period is time from treatment to cure.","FALSE — Infection to first symptoms."),
("Carrier can transmit disease without symptoms.","TRUE"),
("Boiling is a household water purification method.","TRUE"),
("Overcrowding is a housing health hazard.","TRUE"),
("Counselling means forcing client decision.","FALSE — Helps client make own informed decision."),
("AV aids reduce interest in teaching.","FALSE — They increase interest & retention."),
("Composting is a refuse disposal method.","TRUE"),
("Vitamin D deficiency causes scurvy.","FALSE — Scurvy is Vit C; Vit D causes rickets."),
("First Referral Unit manages EmOC.","TRUE"),
("Passive immunity uses vaccines.","FALSE — Vaccines = active; Ig = passive."),
("Endemic means worldwide spread.","FALSE — Endemic = constant local presence; pandemic = worldwide."),
("Growth chart is used in under-five clinic.","TRUE"),
("Bag technique prevents infection spread.","TRUE"),
("Plenum ventilation extracts air only.","FALSE — Plenum pushes fresh air in; exhaust extracts."),
("IFA tablets are given in antenatal care.","TRUE"),
("Argemone oil adulteration of mustard oil is harmful.","TRUE"),
("Tertiary prevention includes rehabilitation.","TRUE"),
("Community participation is a PHC principle.","TRUE"),
("Measles vaccine is given at birth.","FALSE — MR usually at 9 completed months (as per NIS)."),
("Confidentiality is a counselling principle.","TRUE"),
("Anthropometry is useful for nutritional assessment.","TRUE"),
("1 g carbohydrate yields 9 calories.","FALSE — Carbohydrate yields 4 kcal/g; fat yields 9."),
("Blackboard is an auditory aid.","FALSE — Visual aid."),
("Symposium is always a two-way group method.","FALSE — Often largely one-way expert talks."),
("Pressure cooking destroys all valuable nutrients.","FALSE — It often retains nutrients better than long boiling."),
("Home visit is the backbone of public health nursing.","TRUE"),
("Nursing process is used for families and communities.","TRUE"),
("Koplik's spots indicate Vitamin A deficiency.","FALSE — Koplik = measles; Bitot = Vit A."),
("Didactic method is teaching by questions.","FALSE — That is Socratic; didactic is lecture/one-way."),
("Oxidation pond treats sewage.","TRUE"),
("Lathyrism is caused by kesari dal.","TRUE"),
("Hardness of water is mainly due to NaCl.","FALSE — Mainly calcium and magnesium salts."),
("Sanitary well should have a parapet and platform.","TRUE"),
("Pulse Polio is only for children who never received OPV.","FALSE — All under-5s on NID days, regardless of prior doses."),
]

FACTS = [
("World Health Day","April 7"),
("Alma Ata year","1978"),
("Cold chain range","+2°C to +8°C"),
("Vit A deficiency","Night blindness / xerophthalmia"),
("Vit B1 deficiency","Beriberi"),
("Vit C deficiency","Scurvy"),
("Vit D deficiency","Rickets / osteomalacia"),
("Vit K function","Blood clotting (fat soluble)"),
("Malaria parasite","Plasmodium"),
("Malaria vector","Anopheles"),
("Dengue/Chikungunya vector","Aedes aegypti"),
("Sullage","Wastewater WITHOUT excreta"),
("Sewage","Wastewater WITH excreta"),
("Under-five clinic aka","Well-baby clinic"),
("Goitre","Iodine deficiency"),
("Amino acids","Building blocks of protein"),
("Nosocomial","Hospital-acquired infection"),
("Noise unit","Decibel"),
("Horrock's","Bleaching powder dose for water"),
("Vasectomy","Male permanent FP"),
("Tubectomy","Female permanent FP"),
("FRU","First Referral Unit"),
("PHC elements","8"),
("Fat soluble vitamins","A, D, E, K"),
("Water soluble","B-complex, C"),
("Marasmus","Severe wasting, no oedema"),
("Kwashiorkor","Oedema, moon face"),
("BCG type","Live vaccine"),
("OPV type","Live vaccine"),
("Primary prevention eg","Immunization, safe water"),
("Secondary prevention eg","Screening"),
("Tertiary prevention eg","Rehab"),
("Epidemiological triad","Agent–Host–Environment"),
("Home visit tool","Bag technique"),
("Family record","Family folder"),
("HE methods","Individual, Group, Mass"),
("Large-scale water steps","Storage → Filtration → Chlorination"),
("Mechanical ventilation","Exhaust, Plenum, AC"),
("Refuse methods","Dumping, composting, incineration, landfill"),
("Eligible couple","Couple needing FP services"),
("ASHA role","Link worker / mobilize / counsel"),
("ORS use","Diarrhoea dehydration"),
("Weaning start","~6 months complementary feeds"),
("TT in pregnancy","Prevent neonatal tetanus"),
("Cross ventilation","Opposite wall openings"),
("Carrier","Infected, asymptomatic transmitter"),
("Incubation period","Infection → first symptoms"),
("Endemic","Constant presence in area"),
("Epidemic","Unusual rise in cases"),
("Anthropometry","Ht, Wt, MUAC, head circumference"),
("Calorie yields","Carb 4 / Protein 4 / Fat 9 kcal per g"),
("Demography","Study of human population"),
("Sanitary well features","Parapet, platform, cover, drain"),
("Rapid sand steps","Coagulate → Sediment → Filter → Chlorinate"),
("Hardness salts","Calcium & magnesium"),
("Koplik's spots","Measles (buccal mucosa)"),
("Bitot's spots","Vitamin A deficiency (conjunctiva)"),
("Didactic method","One-way lecture teaching"),
("Socratic method","Teaching by questions/discussion"),
("Pulse Polio","Mass OPV to all under-5 on NID"),
("Mid-Day Meal","School supplementary nutrition programme"),
("Standing order","MO written protocol for nurse treatment"),
("Oxidation pond","Sewage treatment method"),
("Lathyrism cause","Kesari dal"),
("Neonatal period","First 28 days"),
("IMR","Infant deaths / 1000 live births"),
("ASHA full form","Accredited Social Health Activist"),
("Concurrent disinfection","During illness while source present"),
("Terminal disinfection","After recovery/death/transfer"),
("Active immunity","Body makes antibodies (vaccines)"),
("Passive immunity","Ready-made antibodies (Ig)"),

("Pandemic","Global/multi-country spread"),
]

drill_defs = "\n".join(drill_item(q,a) for q,a in DEFS)
drill_fill = "\n".join(drill_item(q,a) for q,a in FILLS)
drill_tf = "\n".join(drill_item(q,a) for q,a in TF)
drill_facts = "\n".join(drill_item(q,a) for q,a in FACTS)

# Quick defs
quick_defs = "\n".join(f'<div class="def-row"><div class="def-word">{q}</div><div class="def-meaning">{a}</div></div>' for q,a in DEFS)
quick_fill_rows = "\n".join(f"<tr><td>{q}</td><td><strong>{a}</strong></td></tr>" for q,a in FILLS)
quick_tf = "\n".join(f'<div class="def-row"><div class="def-word">{q}</div><div class="def-meaning">{a}</div></div>' for q,a in TF)
quick_facts_rows = "\n".join(f"<tr><td>{q}</td><td><strong>{a}</strong></td></tr>" for q,a in FACTS)


# Mock papers - questions and answers as plain HTML (no nested triple quotes)

def _qi(num, text, marks, diff="diff-med"):
    return f'<div class="q-item"><div class="q-num">{num}</div><div class="q-text">{text}</div><div class="q-marks {diff}">{marks}</div></div>'

def _ai(q, body):
    return f'<div class="a-item"><div class="a-qtext">{q}</div><div class="ans-block">{body}</div></div>'

m1q = "\n".join([
  '<div class="section-head" style="padding-top:8px;">SECTION I — Meanings (1×4=4)</div>',
  _qi("I-1","Epidemiology","1 mark","diff-easy"),
  _qi("I-2","Cold chain","1 mark","diff-easy"),
  _qi("I-3","Family folder","1 mark","diff-easy"),
  _qi("I-4","Incubation period","1 mark","diff-easy"),
  '<div class="section-head">SECTION II — Fill in the blanks (1×4=4)</div>',
  _qi("II-1","World Health Day is celebrated on ____.","1","diff-easy"),
  _qi("II-2","Under five clinic is also known as ____ clinic.","1","diff-easy"),
  _qi("II-3","Malaria is caused by ____.","1","diff-easy"),
  _qi("II-4","Vitamin C deficiency causes ____.","1","diff-easy"),
  '<div class="section-head">SECTION III — Short notes (any 4) (4×4=16)</div>',
  _qi("III-1","Records and reports","4"),
  _qi("III-2","Modes of transmission","4"),
  _qi("III-3","Under five clinic","4"),
  _qi("III-4","Barriers of communication","4"),
  _qi("III-5","Levels of health care","4"),
  '<div class="section-head">SECTION IV — Long (2+5=7)</div>',
  _qi("IV","Define Community Health Nursing. Explain qualities and functions of a community health nurse.","2+5=7","diff-hard"),
  '<div class="section-head">SECTION V — Long (2+5=7)</div>',
  _qi("V","Define safe water. Explain methods of purification of water.","2+5=7","diff-hard"),
  '<div class="section-head">SECTION VI — True/False (1×4=4)</div>',
  _qi("VI-1","Diabetes is a communicable disease.","1","diff-easy"),
  _qi("VI-2","Models are 3D AV aids.","1","diff-easy"),
  _qi("VI-3","Vitamin K is anticoagulant.","1","diff-easy"),
  _qi("VI-4","Soya is poor protein.","1","diff-easy"),
  '<div class="section-head">SECTION VII — Short notes (any 4) (4×4=16)</div>',
  _qi("VII-1","Bag technique","4"),
  _qi("VII-2","National Immunization Schedule (outline)","4"),
  _qi("VII-3","Housing standards","4"),
  _qi("VII-4","Counselling","4"),
  _qi("VII-5","Food adulteration","4"),
  '<div class="section-head">SECTION VIII — Long (~8)</div>',
  _qi("VIII","Define health education. Explain principles and methods of health education.","2+6=8","diff-hard"),
  '<div class="section-head">SECTION IX — Long (~9)</div>',
  _qi("IX","Classify vitamins. Explain sources and deficiency of Vitamin A, D and C.","2+7=9","diff-hard"),
])

from mock_answers import build_m1a, build_m2a, build_m3a, build_m4a, build_m5a
m1a = build_m1a()

m2q = "\n".join([
  '<div class="section-head" style="padding-top:8px;">SECTION I — Meanings (4)</div>',
  _qi("I-1","Immunization","1","diff-easy"),
  _qi("I-2","Endemic","1","diff-easy"),
  _qi("I-3","Weaning","1","diff-easy"),
  _qi("I-4","Ventilation","1","diff-easy"),
  '<div class="section-head">SECTION II — Fill blanks (4)</div>',
  _qi("II-1","Goitre is caused by deficiency of ____.","1","diff-easy"),
  _qi("II-2","Vitamin K is ____ soluble.","1","diff-easy"),
  _qi("II-3","Nosocomial infection means ____ acquired infection.","1","diff-easy"),
  _qi("II-4","First referral unit short form is ____.","1","diff-easy"),
  '<div class="section-head">SECTION III — Short any 4 (16)</div>',
  _qi("III-1","Epidemiological triad","4"),
  _qi("III-2","Referral system","4"),
  _qi("III-3","Audio-visual aids","4"),
  _qi("III-4","Waste / refuse disposal","4"),
  _qi("III-5","Minor ailments (list & care outline)","4"),
  '<div class="section-head">SECTION IV — Long 2+5=7</div>',
  _qi("IV","Define home visit. Explain principles of home visit and bag technique.","2+5=7","diff-hard"),
  '<div class="section-head">SECTION V — Long 2+5=7</div>',
  _qi("V","Define Primary Health Care. List elements and explain levels of health care.","2+5=7","diff-hard"),
  '<div class="section-head">SECTION VI — T/F (4)</div>',
  _qi("VI-1","Vitamin B1 deficiency causes night blindness.","1","diff-easy"),
  _qi("VI-2","Sewage contains excreta.","1","diff-easy"),
  _qi("VI-3","Chikungunya comes from chicken.","1","diff-easy"),
  _qi("VI-4","BCG is a live vaccine.","1","diff-easy"),
  '<div class="section-head">SECTION VII — Short any 4 (16)</div>',
  _qi("VII-1","Dimensions of health","4"),
  _qi("VII-2","Cold chain","4"),
  _qi("VII-3","Balanced diet","4"),
  _qi("VII-4","Mosquito control measures","4"),
  _qi("VII-5","Family welfare nurse role (outline)","4"),
  '<div class="section-head">SECTION VIII — Long ~8</div>',
  _qi("VIII","Define communication. Explain process, types and barriers of communication.","3+5=8","diff-hard"),
  '<div class="section-head">SECTION IX — Long ~9</div>',
  _qi("IX","Define ventilation. Explain types of ventilation with nursing importance.","2+7=9","diff-hard"),
])

m2a = build_m2a()

m3q = "\n".join([
  '<div class="section-head" style="padding-top:8px;">SECTION I — Meanings (4)</div>',
  _qi("I-1","Community","1","diff-easy"),
  _qi("I-2","Carrier","1","diff-easy"),
  _qi("I-3","Home visit","1","diff-easy"),
  _qi("I-4","Mortality","1","diff-easy"),
  '<div class="section-head">SECTION II — Fill blanks (4)</div>',
  _qi("II-1","Amino acids are building blocks of ____.","1","diff-easy"),
  _qi("II-2","Vector of dengue is ____.","1","diff-easy"),
  _qi("II-3","Noise is measured in ____.","1","diff-easy"),
  _qi("II-4","Horrock's apparatus is used for ____.","1","diff-easy"),
  '<div class="section-head">SECTION III — Short any 4 (16)</div>',
  _qi("III-1","Levels of prevention","4"),
  _qi("III-2","Immunization schedule (key ages)","4"),
  _qi("III-3","Principles of recording","4"),
  _qi("III-4","Cooking methods & nutrient loss","4"),
  _qi("III-5","Well disinfection","4"),
  '<div class="section-head">SECTION IV — Long 2+5=7</div>',
  _qi("IV","Define health. Explain dimensions and determinants of health.","2+5=7","diff-hard"),
  '<div class="section-head">SECTION V — Long 2+5=7</div>',
  _qi("V","Define counselling. Explain principles and steps of counselling.","2+5=7","diff-hard"),
  '<div class="section-head">SECTION VI — T/F (4)</div>',
  _qi("VI-1","OPV is a killed vaccine.","1","diff-easy"),
  _qi("VI-2","Sullage contains no excreta.","1","diff-easy"),
  _qi("VI-3","Vasectomy is male sterilization.","1","diff-easy"),
  _qi("VI-4","Under five clinic = well baby clinic.","1","diff-easy"),
  '<div class="section-head">SECTION VII — Short any 4 (16)</div>',
  _qi("VII-1","PEM — marasmus & kwashiorkor","4"),
  _qi("VII-2","Functions of CHN","4"),
  _qi("VII-3","Water-borne diseases","4"),
  _qi("VII-4","Community health team","4"),
  _qi("VII-5","ORS & home management of diarrhoea","4"),
  '<div class="section-head">SECTION VIII — Long ~8</div>',
  _qi("VIII","Define balanced diet. Explain food classification and protein energy malnutrition.","2+6=8","diff-hard"),
  '<div class="section-head">SECTION IX — Long ~9</div>',
  _qi("IX","Define communicable disease. Explain modes of transmission and control measures.","3+6=9","diff-hard"),
])

m3a = build_m3a()

m4q = "\n".join([
  '<div class="section-head" style="padding-top:8px;">SECTION I — Meanings (4)</div>',
  _qi("I-1","Weaning","1","diff-easy"),
  _qi("I-2","Quarantine","1","diff-easy"),
  _qi("I-3","Sanitary well","1","diff-easy"),
  _qi("I-4","Demography","1","diff-easy"),
  '<div class="section-head">SECTION II — Fill blanks (4)</div>',
  _qi("II-1","Goitre is due to deficiency of ____.","1","diff-easy"),
  _qi("II-2","Dengue vector is ____.","1","diff-easy"),
  _qi("II-3","World Health Day is on ____.","1","diff-easy"),
  _qi("II-4","Lathyrism is caused by ____.","1","diff-easy"),
  '<div class="section-head">SECTION III — Short any 4 (16)</div>',
  _qi("III-1","Standing orders for fever and diarrhoea","4"),
  _qi("III-2","Family planning methods","4"),
  _qi("III-3","Air pollution — sources and control","4"),
  _qi("III-4","Anthropometry","4"),
  _qi("III-5","Mid-Day Meal / ICDS (outline)","4"),
  '<div class="section-head">SECTION IV — Long 2+5=7</div>',
  _qi("IV","Define safe water. Explain hardness of water and its removal.","2+5=7","diff-hard"),
  '<div class="section-head">SECTION V — Long 2+5=7</div>',
  _qi("V","Define antenatal care. Explain postnatal care and advice to mother.","2+5=7","diff-hard"),
  '<div class="section-head">SECTION VI — T/F (4)</div>',
  _qi("VI-1","Vitamin B1 deficiency causes night blindness.","1","diff-easy"),
  _qi("VI-2","Models are three dimensional aids.","1","diff-easy"),
  _qi("VI-3","Tubectomy is permanent method for males.","1","diff-easy"),
  _qi("VI-4","Home visit is backbone of public health nursing.","1","diff-easy"),
  '<div class="section-head">SECTION VII — Short any 4 (16)</div>',
  _qi("VII-1","Rapid sand filtration","4"),
  _qi("VII-2","Difference: Health education and counselling","4"),
  _qi("VII-3","Pulse Polio programme","4"),
  _qi("VII-4","Housing standards","4"),
  _qi("VII-5","Role of school health nurse","4"),
  '<div class="section-head">SECTION VIII — Long ~8</div>',
  _qi("VIII","Classify vitamins. Explain sources and deficiency of A, D, C.","2+6=8","diff-hard"),
  '<div class="section-head">SECTION IX — Long ~9</div>',
  _qi("IX","Define home visit. Explain principles and bag technique.","2+7=9","diff-hard"),
])
m4a = build_m4a()

m5q = "\n".join([
  '<div class="section-head" style="padding-top:8px;">SECTION I — Meanings (4)</div>',
  _qi("I-1","Infection","1","diff-easy"),
  _qi("I-2","Carrier","1","diff-easy"),
  _qi("I-3","Calorie","1","diff-easy"),
  _qi("I-4","Disinfection","1","diff-easy"),
  '<div class="section-head">SECTION II — Fill blanks (4)</div>',
  _qi("II-1","1 g carbohydrate yields ____ kcal.","1","diff-easy"),
  _qi("II-2","1 g fat yields ____ kcal.","1","diff-easy"),
  _qi("II-3","Neonatal period is first ____ days.","1","diff-easy"),
  _qi("II-4","ASHA full form: Accredited Social ____ Activist.","1","diff-easy"),
  '<div class="section-head">SECTION III — Short any 4 (16)</div>',
  _qi("III-1","Disease cycle","4"),
  _qi("III-2","Food sanitation / food hygiene","4"),
  _qi("III-3","Socratic method vs Didactic method","4"),
  _qi("III-4","Indicators of health","4"),
  _qi("III-5","Global warming and its effects","4"),
  '<div class="section-head">SECTION IV — Long 2+5=7</div>',
  _qi("IV","Define Primary Health Care. Explain levels of health care.","2+5=7","diff-hard"),
  '<div class="section-head">SECTION V — Long 2+5=7</div>',
  _qi("V","Write nutrition for pregnant woman. Explain advantages of breastfeeding.","2+5=7","diff-hard"),
  '<div class="section-head">SECTION VI — T/F (4)</div>',
  _qi("VI-1","One gram carbohydrate yields 9 calories.","1","diff-easy"),
  _qi("VI-2","Koplik spots are seen in measles.","1","diff-easy"),
  _qi("VI-3","Bitot spots indicate measles.","1","diff-easy"),
  _qi("VI-4","Oxidation pond is used for sewage treatment.","1","diff-easy"),
  '<div class="section-head">SECTION VII — Short any 4 (16)</div>',
  _qi("VII-1","Active vs Passive immunity","4"),
  _qi("VII-2","Concurrent vs Terminal disinfection","4"),
  _qi("VII-3","Preparation of poached egg / barley water","4"),
  _qi("VII-4","Role of ASHA in MCH","4"),
  _qi("VII-5","Diet for diabetic patient","4"),
  '<div class="section-head">SECTION VIII — Long ~8</div>',
  _qi("VIII","Define epidemiology. Explain epidemiological triad with diagram.","2+6=8","diff-hard"),
  '<div class="section-head">SECTION IX — Long ~9</div>',
  _qi("IX","Explain refuse disposal methods and mosquito control measures.","3+6=9","diff-hard"),
])
m5a = build_m5a()


def mock_block(num, qhtml, ahtml, active=False):
    act = " active-paper" if active else ""
    qshow = " show" if True else ""
    return f'''
  <div class="mock-paper{act}" id="mock-{num}">
    <div class="mock-toggle">
      <button class="mock-toggle-btn active-toggle" onclick="showView({num},'q',this)">📄 Questions</button>
      <button class="mock-toggle-btn" onclick="showView({num},'a',this)">✅ Answers</button>
    </div>
    <div class="q-view{qshow}" id="mock-{num}-q">{qhtml}</div>
    <div class="a-view" id="mock-{num}-a">{ahtml}</div>
  </div>'''

from templates_chn import TEMPLATES

JS = r'''
/* Neon-backed licence: /api/auth/login binds device_id in Postgres.
   Seller creates IDs at /admin. Reset device from admin if buyer changes phone. */
const AUTH_KEY = 'chnLicenceV1';

function showLoginError(msg) {
  const el = document.getElementById('login-error');
  if (!el) return;
  el.textContent = msg;
  el.classList.toggle('show', !!msg);
}

function getOrCreateDeviceId() {
  let id = localStorage.getItem('chnDeviceId');
  if (!id) {
    id = 'dev_' + Math.random().toString(36).slice(2) + Date.now().toString(36);
    localStorage.setItem('chnDeviceId', id);
  }
  return id;
}

function unlockApp() {
  document.body.classList.add('app-unlocked');
  showLoginError('');
  const tip = document.getElementById('licence-device-tip');
  if (tip) {
    const sess = JSON.parse(localStorage.getItem(AUTH_KEY) || '{}');
    tip.textContent = 'Licence OK · ' + (sess.id || '') + ' · Device locked on Neon';
  }
}

function lockApp() {
  document.body.classList.remove('app-unlocked');
}

async function verifySession() {
  try {
    const raw = localStorage.getItem(AUTH_KEY);
    if (!raw) return false;
    const sess = JSON.parse(raw);
    const device = getOrCreateDeviceId();
    if (!sess.id || sess.deviceId !== device) return false;
    const res = await fetch('/api/auth/session', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ loginId: sess.id, deviceId: device })
    });
    const data = await res.json();
    if (!data.ok) {
      localStorage.removeItem(AUTH_KEY);
      return false;
    }
    return true;
  } catch (e) {
    // Offline: allow cached unlock on same device only
    try {
      const sess = JSON.parse(localStorage.getItem(AUTH_KEY) || '{}');
      return !!(sess.id && sess.deviceId === getOrCreateDeviceId());
    } catch (e2) {
      return false;
    }
  }
}

async function tryLogin() {
  const idEl = document.getElementById('login-id');
  const passEl = document.getElementById('login-pass');
  const btn = document.getElementById('login-btn');
  const id = (idEl.value || '').trim();
  const pass = passEl.value || '';
  showLoginError('');
  if (!id || !pass) {
    showLoginError('Enter Login ID and password.');
    return;
  }
  const device = getOrCreateDeviceId();
  btn.disabled = true;
  btn.textContent = 'Checking…';
  try {
    const res = await fetch('/api/auth/login', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ loginId: id, password: pass, deviceId: device })
    });
    const data = await res.json();
    if (!data.ok) {
      showLoginError(data.error || 'Login failed.');
      btn.disabled = false;
      btn.textContent = 'Unlock App';
      return;
    }
    localStorage.setItem(AUTH_KEY, JSON.stringify({
      id: data.loginId,
      deviceId: data.deviceId,
      unlockedAt: Date.now()
    }));
    btn.textContent = 'Unlocked ✓';
    unlockApp();
  } catch (e) {
    showLoginError('Network error — need internet for first unlock.');
    btn.disabled = false;
    btn.textContent = 'Unlock App';
  }
}

(async function bootAuth() {
  lockApp();
  if (await verifySession()) unlockApp();
  const passEl = document.getElementById('login-pass');
  if (passEl) {
    passEl.addEventListener('keydown', function (e) {
      if (e.key === 'Enter') tryLogin();
    });
  }
  const idEl = document.getElementById('login-id');
  if (idEl) {
    idEl.addEventListener('keydown', function (e) {
      if (e.key === 'Enter') {
        e.preventDefault();
        document.getElementById('login-pass').focus();
      }
    });
  }
})();

let dark = localStorage.getItem('theme') === 'dark';
if (dark) document.documentElement.setAttribute('data-theme','dark');
function toggleTheme() {
  dark = !dark;
  document.documentElement.setAttribute('data-theme', dark ? 'dark' : '');
  localStorage.setItem('theme', dark ? 'dark' : 'light');
  document.querySelector('.theme-btn').textContent = dark ? '☀️' : '🌙';
}
if (dark) document.querySelector('.theme-btn').textContent = '☀️';

function showPage(id) {
  document.querySelectorAll('.page').forEach(p => p.classList.remove('active'));
  document.getElementById('page-' + id).classList.add('active');
  document.querySelectorAll('.nav-btn').forEach(b => b.classList.remove('active'));
  document.getElementById('nav-' + id).classList.add('active');
  window.scrollTo(0,0);
}

function toggleCard(header) {
  const card = header.parentElement;
  const body = card.querySelector('.card-body');
  body.classList.toggle('open');
  card.classList.toggle('expanded');
}

const doneState = JSON.parse(localStorage.getItem('chnDoneTopics') || '{}');
const TOTAL = 36;

function updateStats() {
  const count = Object.values(doneState).filter(Boolean).length;
  document.getElementById('done-count').textContent = count;
  document.getElementById('left-count').textContent = TOTAL - count;
  document.getElementById('done-pct').textContent = Math.round(count/TOTAL*100) + '%';
  document.getElementById('progress-bar').style.width = (count/TOTAL*100) + '%';
}

function toggleDone(id) {
  doneState[id] = !doneState[id];
  localStorage.setItem('chnDoneTopics', JSON.stringify(doneState));
  const cb = document.getElementById('cb-' + id);
  if (cb) {
    cb.classList.toggle('checked', doneState[id]);
    cb.textContent = doneState[id] ? '✓' : '';
  }
  updateStats();
}

function initCheckboxes() {
  Object.keys(doneState).forEach(id => {
    if (doneState[id]) {
      const cb = document.getElementById('cb-' + id);
      if (cb) { cb.classList.add('checked'); cb.textContent = '✓'; }
    }
  });
  updateStats();
}
initCheckboxes();

let currentFilter = 'all';
function setFilter(f, btn) {
  currentFilter = f;
  document.querySelectorAll('.filter-btn').forEach(b => b.classList.remove('active-filter'));
  btn.classList.add('active-filter');
  applyFilters();
}

function filterTopics() { applyFilters(); }

function applyFilters() {
  const search = document.getElementById('topic-search').value.toLowerCase();
  document.querySelectorAll('.topic-card').forEach(card => {
    const level = card.getAttribute('data-level');
    const topic = card.getAttribute('data-topic') || '';
    const id = card.getAttribute('data-id');
    const matchFilter = currentFilter === 'all' ||
      (currentFilter === 'red' && level === 'red') ||
      (currentFilter === 'yellow' && level === 'yellow') ||
      (currentFilter === 'green' && level === 'green') ||
      (currentFilter === 'undone' && !doneState[id]);
    const matchSearch = !search || topic.includes(search) ||
      card.querySelector('.card-title').textContent.toLowerCase().includes(search);
    card.style.display = (matchFilter && matchSearch) ? '' : 'none';
  });
}

function showMock(num, btn) {
  document.querySelectorAll('.mock-paper').forEach(p => p.classList.remove('active-paper'));
  document.getElementById('mock-' + num).classList.add('active-paper');
  document.querySelectorAll('.mock-btn').forEach(b => b.classList.remove('active-mock'));
  btn.classList.add('active-mock');
}

function showView(num, view, btn) {
  const paper = document.getElementById('mock-' + num);
  paper.querySelectorAll('.q-view, .a-view').forEach(v => v.classList.remove('show'));
  paper.querySelector('.' + view + '-view').classList.add('show');
  paper.querySelectorAll('.mock-toggle-btn').forEach(b => b.classList.remove('active-toggle'));
  btn.classList.add('active-toggle');
}

function showQuick(id, btn) {
  document.querySelectorAll('.quick-section').forEach(s => s.classList.remove('show'));
  document.getElementById('quick-' + id).classList.add('show');
  document.querySelectorAll('.quick-tab-btn').forEach(b => b.classList.remove('active-qtab'));
  btn.classList.add('active-qtab');
}

function showDrill(id, btn) {
  document.querySelectorAll('#page-drill .quick-section').forEach(s => s.classList.remove('show'));
  document.getElementById('drill-' + id).classList.add('show');
  document.querySelectorAll('#page-drill .quick-tab-btn').forEach(b => b.classList.remove('active-qtab'));
  btn.classList.add('active-qtab');
}

function showTmpl(id, btn) {
  document.querySelectorAll('.tmpl-section').forEach(s => s.classList.remove('show'));
  document.getElementById('tmpl-' + id).classList.add('show');
  document.querySelectorAll('.tmpl-tab-btn').forEach(b => b.classList.remove('active-tmpl'));
  btn.classList.add('active-tmpl');
}
'''

NAV = '''
<nav class="bottom-nav">
  <button class="nav-btn active" id="nav-home" onclick="showPage('home')">
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/><polyline points="9 22 9 12 15 12 15 22"/></svg>
    Home
  </button>
  <button class="nav-btn" id="nav-topics" onclick="showPage('topics')">
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/></svg>
    Topics
  </button>
  <button class="nav-btn" id="nav-score" onclick="showPage('score')">
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><circle cx="12" cy="12" r="6"/><circle cx="12" cy="12" r="2"/></svg>
    Score
  </button>
  <button class="nav-btn" id="nav-drill" onclick="showPage('drill')">
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"/><polyline points="22 4 12 14.01 9 11.01"/></svg>
    Drill
  </button>
  <button class="nav-btn" id="nav-mock" onclick="showPage('mock')">
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/></svg>
    Mock
  </button>
  <button class="nav-btn" id="nav-templates" onclick="showPage('templates')">
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="7" height="7"/><rect x="14" y="3" width="7" height="7"/><rect x="14" y="14" width="7" height="7"/><rect x="3" y="14" width="7" height="7"/></svg>
    Templates
  </button>
  <button class="nav-btn" id="nav-quick" onclick="showPage('quick')">
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"/></svg>
    Quick
  </button>
</nav>
'''

html = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0">
<title>GNM Community Health Nursing–I — Score 60-75</title>
<style>
{CSS}
</style>
</head>
<body>

<!-- LOGIN GATE — app stays hidden until unlock -->
<div id="login-gate" role="dialog" aria-label="Login">
  <div class="login-card">
    <div class="login-brand">🏘️ CHN Study Pack</div>
    <div class="login-sub">GNM Community Health Nursing–I<br>Q.P. 9114 · Karnataka</div>
    <div style="text-align:center"><span class="login-price">₹200 · 1 device licence</span></div>
    <label class="login-label" for="login-id">Login ID</label>
    <input class="login-input" id="login-id" type="text" autocomplete="username" placeholder="Enter your Login ID" enterkeyhint="next">
    <label class="login-label" for="login-pass">Password</label>
    <input class="login-input" id="login-pass" type="password" autocomplete="current-password" placeholder="Enter password" enterkeyhint="go">
    <button class="login-btn" id="login-btn" type="button" onclick="tryLogin()">Unlock App</button>
    <div class="login-error" id="login-error"></div>
    <p class="login-note">₹200 · unlocks on <strong>this phone only</strong> (saved in Neon DB). New phone? Ask seller to reset device.</p>
  </div>
</div>

<div class="topbar">
  <div>
    <div class="topbar-title">🏘️ GNM Community Health Nursing–I</div>
    <div class="topbar-sub">Score 60–75 · Q.P. 9114 · Karnataka</div>
  </div>
  <button class="theme-btn" onclick="toggleTheme()">🌙</button>
</div>

<!-- PAGE HOME -->
<div class="page active" id="page-home">
  <div class="tip-box" id="licence-device-tip" style="margin:12px 12px 0;font-size:11px;">Licence OK</div>
  <div class="goal-banner">
    <h1>🎯 Target: 60-75/75</h1>
    <p>Mark-Scoring System · Q.P. 9114 · Karnataka GNM</p>
  </div>
  <div class="stats-row">
    <div class="stat-box"><div class="stat-num" id="done-count">0</div><div class="stat-label">Topics Done</div></div>
    <div class="stat-box"><div class="stat-num" id="left-count">36</div><div class="stat-label">Remaining</div></div>
    <div class="stat-box"><div class="stat-num" id="done-pct">0%</div><div class="stat-label">Complete</div></div>
  </div>
  <div style="margin: 0 12px 12px;"><div class="progress-bar-wrap"><div class="progress-bar" id="progress-bar" style="width:0%"></div></div></div>

  <div class="section-head">📊 Phase 1 — Paper Analysis (2011–2025)</div>
  <div class="card" style="margin:0 12px 12px;padding:14px;font-size:13px;">
    <p><strong>Evidence base:</strong> Karnataka GNM CHN-I papers 2011–2025 (supplied set). <strong>2024 & 2025 weighted 3×</strong>; 2023/2022/2019 = 2×; older = 1×.</p>
    <p style="margin-top:8px;"><strong>Most repeated long answers:</strong> Water purification/safe water · Vitamins · Health Education · Home visit/Bag technique · CHN qualities/functions · Communication · Nutrition/balanced diet · Minor ailments · Ventilation · MCH/family health · Epidemiology · PHC · Counselling · Hardness of water</p>
    <p style="margin-top:6px;"><strong>Most repeated short notes:</strong> Records · Under five · NIS · Transmission · Housing · Counselling · AV aids · Levels of care · Cooking/preservation · Food adulteration · Waste/mosquito · Standing orders fever/diarrhoea · Family planning · Air pollution · School health · Nutritional programmes · Pulse Polio · Disease cycle · Referral · Bag technique</p>
    <p style="margin-top:6px;"><strong>Most repeated meanings:</strong> Endemic, Epidemiology, Immunization, Cold chain, Family folder, Incubation, Mortality, Weaning, Community, Health, Carrier, Pandemic, Ventilation, Home visit, Infant, Infection, Sporadic, Demography, Quarantine, ASHA, Disinfection, MCH</p>
    <p style="margin-top:6px;"><strong>Fill-blank favourites:</strong> World Health Day April 7 · Goitre–iodine · Under five=Well baby · Vit K fat soluble · Malaria–Plasmodium · Vit C–scurvy · Amino acids · Nosocomial · FRU · Anthropometry · Calorie 4-4-9 · Koplik/Bitot · Oxidation pond · Lathyrism–kesari dal</p>
    <p style="margin-top:6px;"><strong>Difference favourites:</strong> HE vs Counselling · Concurrent vs Terminal disinfection · Active vs Passive immunity · Hospital vs Community nursing · Socratic vs Didactic · Sewage vs Sullage · Koplik vs Bitot</p>
    <p style="margin-top:6px;"><strong>T/F traps:</strong> Diabetes communicable (F) · Soya poor protein (F) · Vit B1 night blindness (F–Vit A) · Sewage vs sullage · Chikungunya from chicken (F–Aedes) · Models 3D (T) · Vit K anticoagulant (F) · BCG/OPV killed (F–live)</p>
  </div>

  <div class="section-head">🎯 Topic Probability (All 36 Topics)</div>
  <table class="analysis-table">
    <thead><tr><th>Topic</th><th>Level</th><th>Score %</th><th>Expected Marks</th></tr></thead>
    <tbody>
{prob_rows}
    </tbody>
  </table>

  <div class="strategy-box" style="margin-top:0;">
    <h3>🏆 60-75 Mark Strategy</h3>
    <p>Lock <strong>16 marks</strong> (meanings+blanks+T/F) in 20 min → <strong>32 marks</strong> short notes (pick easiest 8) → <strong>27–31 marks</strong> long answers (Water / Vitamins / HE / Home visit / CHN / Nutrition). Always write <strong>nursing role</strong>.</p>
  </div>

  <div class="section-head">📋 Exam Pattern (Current 9114 · 2022–2025 style)</div>
  <div class="exam-pattern card" style="margin: 0 12px 12px; padding: 0; overflow: hidden;">
    <table class="pattern-table">
      <thead><tr><th>Section</th><th>Type</th><th>Marks</th></tr></thead>
      <tbody>
        <tr><td>Meanings</td><td>4 meanings</td><td>4</td></tr>
        <tr><td>Fill blanks</td><td>4 blanks</td><td>4</td></tr>
        <tr><td>Short notes</td><td>Any 4</td><td>4×4 = 16</td></tr>
        <tr><td>Long</td><td>2+5</td><td>7</td></tr>
        <tr><td>Long</td><td>2+5</td><td>7</td></tr>
        <tr><td>True/False</td><td>4 statements</td><td>4</td></tr>
        <tr><td>Short notes</td><td>Any 4</td><td>4×4 = 16</td></tr>
        <tr><td>Long</td><td>~2+6 / 3+5</td><td>8</td></tr>
        <tr><td>Long</td><td>~2+7 / 3+6</td><td>9</td></tr>
        <tr style="font-weight:700;"><td colspan="2">TOTAL</td><td>75</td></tr>
      </tbody>
    </table>
  </div>
  <div class="card" style="margin:0 12px 12px;padding:12px;font-size:12px;color:var(--subtext);">Older papers varied (MCQ, 5×3 short notes). Strategy focuses on <strong>current 9114 pattern</strong>.</div>

  <div class="strategy-box">
    <h3>⚡ EXAM STRATEGY — Do This Order!</h3>
    <p>
      <strong>1st (20 min):</strong> Meanings + Fill blanks + T/F — easy 16 marks<br>
      <strong>2nd (50 min):</strong> Short notes × 8 — 32 marks<br>
      <strong>3rd (70 min):</strong> Long answers — Water/Vitamins/HE/Home visit/CHN<br>
      <strong>Last 10 min:</strong> Check nursing role lines & headings for 2+5 splits<br>
      💡 Write <strong>definition first</strong> in every long answer — bank 2 marks early
    </p>
  </div>

  <div class="section-head">📅 3-Day CHN Plan</div>
  <div class="day-box d1">
    <h3>📘 Day 1 — Foundations + Systems</h3>
    <ul>
      <li><strong>Morning:</strong> CHN, Health, PHC, Levels of prevention</li>
      <li><strong>Afternoon:</strong> Records & reports, Referral, Health team + nursing process</li>
      <li><strong>Evening:</strong> 1-mark meanings drill (20 items)</li>
    </ul>
    <div class="skip-box">⏭ Skip today: Deep nutrition tables, mosquito species beyond Anopheles/Aedes</div>
  </div>
  <div class="day-box d2">
    <h3>📗 Day 2 — Epi + Child + Family</h3>
    <ul>
      <li><strong>Morning:</strong> Epidemiology triad, Communicable disease, Immunization + cold chain</li>
      <li><strong>Afternoon:</strong> Under-five, Minor ailments, Home visit + bag, MCH/FW</li>
      <li><strong>Evening:</strong> Fill-blanks + T/F traps</li>
    </ul>
    <div class="skip-box">⏭ Skip today: Rare tropical diseases not in past papers</div>
  </div>
  <div class="day-box d3">
    <h3>📙 Day 3 — Environment + Nutrition + Communication</h3>
    <ul>
      <li><strong>Morning:</strong> Water, Ventilation, Housing, Waste + mosquito + well</li>
      <li><strong>Afternoon:</strong> Nutrition, Vitamins, Communication, HE, Counselling, AV aids</li>
      <li><strong>Evening:</strong> 1 mock paper + Quick sheet</li>
    </ul>
    <div class="skip-box">⏭ Skip: Advanced lab water analysis formulas</div>
  </div>
</div>

<!-- PAGE TOPICS -->
<div class="page" id="page-topics">
  <div class="search-wrap">
    <input class="search-input" id="topic-search" placeholder="🔍  Search any topic..." oninput="filterTopics()" />
  </div>
  <div class="filter-bar">
    <button class="filter-btn active-filter" onclick="setFilter('all',this)">All</button>
    <button class="filter-btn" onclick="setFilter('red',this)">🔴 Very High</button>
    <button class="filter-btn" onclick="setFilter('yellow',this)">🟡 High</button>
    <button class="filter-btn" onclick="setFilter('green',this)">🟢 Medium</button>
    <button class="filter-btn" onclick="setFilter('undone',this)">⬜ Not Done</button>
  </div>
  <div id="topics-container">
    <div class="section-head">🏛️ FOUNDATIONS ({len(found_ids)} Topics)</div>
{section_cards(found_ids)}
    <div class="section-head">🦠 EPIDEMIOLOGY & CHILD/FAMILY ({len(epi_ids)} Topics)</div>
{section_cards(epi_ids)}
    <div class="section-head">🌿 ENVIRONMENT · NUTRITION · COMMUNICATION ({len(env_ids)} Topics)</div>
{section_cards(env_ids)}
  </div>
</div>

<!-- PAGE SCORE -->
<div class="page" id="page-score">
  <div class="score-hero">
    <h2 style="margin:0 0 6px;font-size:20px;">🎯 Score Maximizer</h2>
    <p style="margin:0;opacity:0.95;font-size:13px;">Study in this order · Weighted for 2024–2025 papers</p>
  </div>
  <div class="section-head">TOP 36 — Study In This Order</div>
{predict_cards()}
  <div class="section-head">✅ How Examiners Award Marks</div>
  <div class="template-card" style="margin:0 12px 12px;">
    <div class="ans-block">
      <h4>What Examiners LOVE (CHN)</h4>
      <ul>
        <li><strong>Exact definition first</strong> — banks 1–2 marks immediately</li>
        <li><strong>Label A / B for 2+5</strong> — they tick parts separately</li>
        <li><strong>Headings + bullets</strong> — not paragraphs</li>
        <li><strong>Underlined keywords</strong> — ORS, cold chain 2–8°C, Alma Ata 1978, Aedes</li>
        <li><strong>Nursing role line</strong> almost always rewarded</li>
        <li><strong>Tiny diagram</strong> — triad / cold chain / water SFC / cross ventilation</li>
        <li><strong>Examples</strong> — vaccine ages, vectors, vitamin deficiencies</li>
      </ul>
      <h4>Marking Psychology</h4>
      <ul>
        <li>1-mark meaning = one precise sentence</li>
        <li>4-mark short = def + 4–6 bullets + nurse line</li>
        <li>2+5 long = definition (2) then explain (5) with clear split</li>
        <li>Wrong trap facts kill marks fast (Vit B1≠night blindness; sewage≠sullage)</li>
        <li>Never leave blank — partial relevant bullets still score</li>
      </ul>
      <h4>Page-Filling Without Nonsense</h4>
      <ul>
        <li>Add classification (ADEK / levels of care / FP methods)</li>
        <li>Add numbers (2–8°C, April 7, 1978, 4-4-9 kcal)</li>
        <li>Add nurse role + one-line conclusion</li>
        <li>Draw labelled process diagram when stuck on theory</li>
      </ul>
    </div>
  </div>
  <div class="section-head">🚨 Student Survival Mode</div>
  <div class="survival-card s1">
    <h3>1 Day Before Exam</h3>
    <ul>
      <li>Finish all 🔴 MUST topics (mark Done)</li>
      <li>Write once: Water, Vitamins, HE, Home visit/Bag, CHN, Records</li>
      <li>Drill: T/F + Fill blanks 45 min</li>
      <li>Draw from memory: triad, cold chain, water SFC, cross ventilation</li>
      <li>Read Score Top 12 twice</li>
    </ul>
  </div>
  <div class="survival-card s2">
    <h3>Night Before Exam</h3>
    <ul>
      <li>ONLY Fast Revision + Last-Minute boxes — no new topics</li>
      <li>Memorize: April 7 · 2–8°C · sewage≠sullage · Aedes/Anopheles · ADEK</li>
      <li>Meanings pack: endemic, cold chain, family folder, incubation, weaning</li>
      <li>Sleep 7 hours</li>
    </ul>
  </div>
  <div class="survival-card s3">
    <h3>Morning of Exam</h3>
    <ul>
      <li>Quick → Definitions + T/F traps only</li>
      <li>Redraw cold chain + water steps once</li>
      <li>Light breakfast; admit card + pen</li>
    </ul>
  </div>
  <div class="survival-card s4">
    <h3>In the Hall (3 hours)</h3>
    <ul>
      <li><strong>0–20 min:</strong> Meanings + Blanks + T/F (lock ~16)</li>
      <li><strong>Next 50 min:</strong> Short notes — pick 8 you know 100%</li>
      <li><strong>Next 70 min:</strong> Long answers — label A/B; def first; nurse role last</li>
      <li><strong>Last 10 min:</strong> headings check + underline keywords</li>
    </ul>
  </div>
</div>

<!-- PAGE DRILL -->
<div class="page" id="page-drill">
  <div class="section-head">⚡ High-Yield Drill — Tap to Reveal</div>
  <div class="quick-tabs">
    <button class="quick-tab-btn active-qtab" onclick="showDrill('defs',this)">1-Mark ({len(DEFS)})</button>
    <button class="quick-tab-btn" onclick="showDrill('fill',this)">Fill Blanks ({len(FILLS)})</button>
    <button class="quick-tab-btn" onclick="showDrill('tf',this)">T/F ({len(TF)})</button>
    <button class="quick-tab-btn" onclick="showDrill('facts',this)">Rapid Facts ({len(FACTS)})</button>
  </div>
  <div class="quick-section show" id="drill-defs">{drill_defs}</div>
  <div class="quick-section" id="drill-fill">{drill_fill}</div>
  <div class="quick-section" id="drill-tf">{drill_tf}</div>
  <div class="quick-section" id="drill-facts">{drill_facts}</div>
</div>

<!-- PAGE MOCK -->
<div class="page" id="page-mock">
  <div class="section-head">📝 MOCK PAPERS — 5 Papers (75 marks each)</div>
  <div class="mock-nav">
    <button class="mock-btn active-mock" onclick="showMock(1,this)">Paper 1</button>
    <button class="mock-btn" onclick="showMock(2,this)">Paper 2</button>
    <button class="mock-btn" onclick="showMock(3,this)">Paper 3</button>
    <button class="mock-btn" onclick="showMock(4,this)">Paper 4</button>
    <button class="mock-btn" onclick="showMock(5,this)">Paper 5</button>
  </div>
{mock_block(1, m1q, m1a, True)}
{mock_block(2, m2q, m2a, False)}
{mock_block(3, m3q, m3a, False)}
{mock_block(4, m4q, m4a, False)}
{mock_block(5, m5q, m5a, False)}
</div>

<!-- PAGE TEMPLATES -->
<div class="page" id="page-templates">
{TEMPLATES}
</div>

<!-- PAGE QUICK -->
<div class="page" id="page-quick">
  <div class="section-head">⚡ Quick Reference</div>
  <div class="quick-tabs">
    <button class="quick-tab-btn active-qtab" onclick="showQuick('defs',this)">Definitions</button>
    <button class="quick-tab-btn" onclick="showQuick('fill',this)">Fill-Blanks</button>
    <button class="quick-tab-btn" onclick="showQuick('tf',this)">T/F Traps</button>
    <button class="quick-tab-btn" onclick="showQuick('facts',this)">Numbers/Facts</button>
    <button class="quick-tab-btn" onclick="showQuick('exam',this)">Exam Day</button>
  </div>
  <div class="quick-section show" id="quick-defs">{quick_defs}</div>
  <div class="quick-section" id="quick-fill">
    <table class="val-table"><thead><tr><th>Blank</th><th>Answer</th></tr></thead><tbody>
{quick_fill_rows}
    </tbody></table>
  </div>
  <div class="quick-section" id="quick-tf">{quick_tf}</div>
  <div class="quick-section" id="quick-facts">
    <table class="val-table"><thead><tr><th>Fact</th><th>Value</th></tr></thead><tbody>
{quick_facts_rows}
    </tbody></table>
  </div>
  <div class="quick-section" id="quick-exam">
    <div class="day-box d1">
      <h3>🌅 Morning of Exam</h3>
      <ul>
        <li>Revise Quick → Definitions + T/F traps only</li>
        <li>Water SFC · Vitamins ADEK · HE IGM · Bag clean→dirty</li>
        <li>Eat light; carry pen + admit card</li>
      </ul>
    </div>
    <div class="day-box d2">
      <h3>📝 In the Hall</h3>
      <ul>
        <li>20 min: meanings + blanks + T/F</li>
        <li>Pick short notes you know 100%</li>
        <li>Long answers: write A/B headings for 2+5</li>
        <li>Always end with nursing role</li>
      </ul>
    </div>
    <div class="day-box d3">
      <h3>🚫 Last-Minute Don'ts</h3>
      <ul>
        <li>Don't write Vit B1 = night blindness</li>
        <li>Don't mix sewage / sullage</li>
        <li>Don't say BCG/OPV are killed</li>
        <li>Don't skip definition in long answers</li>
      </ul>
    </div>
  </div>
</div>

{NAV}

<script>
{JS}
</script>
</body>
</html>
'''

OUT.write_text(html, encoding="utf-8")
text = OUT.read_text(encoding="utf-8")
lines = text.count("\n") + 1
cards = text.count('data-id="t')
print(f"Wrote {OUT}")
print(f"Lines: {lines}")
print(f"data-id topic markers: {cards}")
print(f"Starts DOCTYPE: {text.startswith('<!DOCTYPE html>')}")
print(f"Ends html: {text.rstrip().endswith('</html>')}")
print(f"TOTAL=36 present: {'const TOTAL = 36' in text}")
print(f"chnDoneTopics: {'chnDoneTopics' in text}")
print(f"Topics defined: {len(TOPICS)}")
