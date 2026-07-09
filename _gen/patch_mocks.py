# -*- coding: utf-8 -*-
from pathlib import Path

p = Path(r"c:\Users\eathe\milan\_gen\assemble_chn.py")
t = p.read_text(encoding="utf-8")

old_start = t.find("# Mock papers helper")
if old_start < 0:
    old_start = t.find("# Mock 1")
old_end = t.find("def mock_block")
if old_start < 0 or old_end < 0:
    raise SystemExit(f"markers not found {old_start} {old_end}")

new_block = r'''
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

m1a = "\n".join([
  _ai("Meanings", "<ul><li><strong>Epidemiology:</strong> Study of distribution &amp; determinants of health events in populations, applied to control health problems.</li><li><strong>Cold chain:</strong> System to keep vaccines potent at recommended temperature from manufacturer to beneficiary.</li><li><strong>Family folder:</strong> Record file containing health information of all members of one family.</li><li><strong>Incubation period:</strong> Time interval between infection and appearance of first symptoms.</li></ul>"),
  _ai("Fill blanks", "<ul><li>April 7</li><li>Well-baby</li><li>Plasmodium</li><li>Scurvy</li></ul>"),
  _ai("T/F", "<ul><li>FALSE — Diabetes is non-communicable.</li><li>TRUE — Models are three-dimensional aids.</li><li>FALSE — Vitamin K helps clotting.</li><li>FALSE — Soya is good/rich protein.</li></ul>"),
  _ai("IV — CHN Definition + Qualities/Functions (model)", "<p><strong>A. Definition (2):</strong> CHN combines nursing and public health to care for individuals, families and communities with focus on prevention and health promotion.</p><p><strong>B. Qualities:</strong> empathy, communication, leadership, cultural sensitivity, professional skill, honesty.</p><p><strong>C. Functions:</strong> care provider, educator, counsellor, manager, epidemiologist/researcher, advocate.</p><p class=\"tip-box\">Full expanded answer → Topics → t1</p>"),
  _ai("V — Safe water + Purification (model)", "<p><strong>A. Safe water (2):</strong> Free from pathogens &amp; harmful chemicals; colourless, odourless, palatable.</p><p><strong>B. Household:</strong> boiling, chlorination, filtration.</p><p><strong>C. Large scale:</strong> Storage → Filtration → Chlorination. Horrock's for bleaching powder dose.</p><p><strong>Diseases:</strong> cholera, typhoid, hepatitis A/E.</p><p class=\"tip-box\">Full answer → Topics → t20</p>"),
  _ai("VIII — Health Education (model)", "<p><strong>Definition:</strong> Process that informs, motivates and helps people adopt healthy practices.</p><p><strong>Principles:</strong> need-based, participation, known→unknown, simple language, reinforcement, evaluation.</p><p><strong>Methods:</strong> Individual (counselling, home visit), Group (demo, discussion), Mass (TV, radio, campaigns).</p><p class=\"tip-box\">Full answer → Topics → t16</p>"),
  _ai("IX — Vitamins (model)", "<p><strong>Classification:</strong> Fat soluble ADEK; Water soluble B &amp; C.</p><ul><li><strong>A:</strong> GLV, carrot, milk — night blindness, xerophthalmia</li><li><strong>D:</strong> sunlight, fish liver oil — rickets</li><li><strong>C:</strong> amla, citrus — scurvy</li></ul><p class=\"tip-box\">Full answer → Topics → t19</p>"),
  '<div class="tip-box" style="margin:12px;">Short notes: open matching Topics cards (Records t12, Transmission t6, U5 t8, Barriers t14, Levels t3, Bag t10, NIS t7, Housing t22, Counselling t17, Adulteration t18).</div>',
])

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

m2a = "\n".join([
  _ai("Meanings", "<ul><li><strong>Immunization:</strong> Artificial induction of immunity using vaccine/immunoglobulin.</li><li><strong>Endemic:</strong> Constant presence of a disease in a given geographic area.</li><li><strong>Weaning:</strong> Gradual introduction of complementary foods while continuing breastfeeding.</li><li><strong>Ventilation:</strong> Process of supplying fresh air and removing vitiated air.</li></ul>"),
  _ai("Fill blanks", "<ul><li>Iodine</li><li>Fat</li><li>Hospital</li><li>FRU</li></ul>"),
  _ai("T/F", "<ul><li>FALSE — Night blindness = Vit A; B1 = beriberi.</li><li>TRUE — Sewage has excreta.</li><li>FALSE — Aedes mosquito transmits chikungunya.</li><li>TRUE — BCG is live attenuated.</li></ul>"),
  _ai("IV — Home visit + Bag (model)", "<p><strong>Home visit:</strong> Planned CHN visit to family for assessment, care, HE, follow-up.</p><p><strong>Principles:</strong> purposeful, planned, flexible, family-centred, privacy, use resources.</p><p><strong>Bag technique:</strong> clean surface, handwash, clean→dirty workflow, protect bag from contamination.</p><p class=\"tip-box\">Full → Topics t10</p>"),
  _ai("V — PHC + Levels (model)", "<p><strong>PHC:</strong> Essential, universally accessible care (Alma Ata 1978).</p><p><strong>8 elements:</strong> education, nutrition, water/sanitation, MCH/FP, immunization, endemic control, treatment, essential drugs.</p><p><strong>Levels:</strong> Primary (SC/PHC), Secondary (CHC/District), Tertiary (Medical college).</p><p class=\"tip-box\">Full → Topics t3</p>"),
  _ai("VIII — Communication (model)", "<p>Process: Sender–Message–Channel–Receiver–Feedback. Types: verbal/nonverbal; individual/group/mass. Barriers: language, noise, culture, psychological. Nurse uses simple words + feedback.</p><p class=\"tip-box\">Full → Topics t14</p>"),
  _ai("IX — Ventilation (model)", "<p>Natural (windows, cross ventilation) vs Mechanical (exhaust, plenum, AC). Improves air quality, reduces infection. Nurse advises housing ventilation.</p><p class=\"tip-box\">Full → Topics t21</p>"),
])

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

m3a = "\n".join([
  _ai("Meanings", "<ul><li><strong>Community:</strong> Group of people in a defined area with common interests/characteristics.</li><li><strong>Carrier:</strong> Person harbouring infectious agent without symptoms but able to transmit.</li><li><strong>Home visit:</strong> Planned visit by nurse to family home for care and education.</li><li><strong>Mortality:</strong> Death occurrence / death rate in a population.</li></ul>"),
  _ai("Fill blanks", "<ul><li>Proteins</li><li>Aedes aegypti</li><li>Decibels</li><li>Estimating bleaching powder dose for water</li></ul>"),
  _ai("T/F", "<ul><li>FALSE — OPV is live.</li><li>TRUE — Sullage has no excreta.</li><li>TRUE — Vasectomy = male.</li><li>TRUE — Under five = well baby clinic.</li></ul>"),
  _ai("IV — Health dimensions/determinants (model)", "<p>WHO definition. Dimensions: physical, mental, social, emotional, spiritual, vocational. Determinants: biological, behavioural, environmental, socio-economic, health services.</p><p class=\"tip-box\">Full → Topics t2</p>"),
  _ai("V — Counselling (model)", "<p>Helping process for informed decisions. Principles: confidentiality, acceptance, non-judgemental, client choice. Steps: rapport → explore → options → decide → follow-up.</p><p class=\"tip-box\">Full → Topics t17</p>"),
  _ai("VIII — Nutrition/PEM (model)", "<p>Balanced diet = all nutrients in right proportion. Foods: energy, body-building, protective. PEM: marasmus (wasting) vs kwashiorkor (oedema).</p><p class=\"tip-box\">Full → Topics t18</p>"),
  _ai("IX — CD + Transmission (model)", "<p>Direct: contact, droplet, vertical. Indirect: vehicle, vector, airborne, fomite. Control: early Rx, immunization, sanitation, vector control, HE.</p><p class=\"tip-box\">Full → Topics t6</p>"),
])

'''

t2 = t[:old_start] + new_block + "\n" + t[old_end:]
p.write_text(t2, encoding="utf-8")
print("Patched OK")
