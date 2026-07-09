# -*- coding: utf-8 -*-
"""Full standalone mock model answers (no 'see Topics' stubs)."""

def _ai(q, body):
    return f'<div class="a-item"><div class="a-qtext">{q}</div><div class="ans-block">{body}</div></div>'

def build_m1a():
    return "\n".join([
        _ai("I — Meanings", """
        <ul>
          <li><strong>Epidemiology:</strong> Study of distribution and determinants of health-related events in populations, and application of this study to control health problems.</li>
          <li><strong>Cold chain:</strong> System of storing and transporting vaccines at recommended temperature from manufacturer to beneficiary so potency is maintained.</li>
          <li><strong>Family folder:</strong> A file containing health records of all members of one family.</li>
          <li><strong>Incubation period:</strong> Time from entry of infection to appearance of first symptoms.</li>
        </ul>"""),
        _ai("II — Fill blanks", "<ul><li>April 7</li><li>Well-baby</li><li>Plasmodium</li><li>Scurvy</li></ul>"),
        _ai("III — Short notes (model for each)", """
        <p><strong>1. Records and reports:</strong> Record = permanent written account; Report = summary communication. Types: family folder, cumulative, clinic registers. Uses: continuity, legal, planning, research. Principles: accurate, complete, legible, confidential, dated &amp; signed.</p>
        <p><strong>2. Modes of transmission:</strong> Direct — contact, droplet, vertical. Indirect — vehicle (water/food), vector, airborne, fomite. Control by breaking chain: isolation, sanitation, vector control, immunization, HE.</p>
        <p><strong>3. Under-five clinic:</strong> Also called well-baby clinic. Care of children &lt;5 yrs — growth monitoring, immunization, nutrition, treatment of minor illness, HE to mothers, referral.</p>
        <p><strong>4. Barriers of communication:</strong> Language, noise, cultural, psychological (fear/anger), physiological (deafness), organizational. Overcome by simple words, feedback, AV aids, listening.</p>
        <p><strong>5. Levels of health care:</strong> Primary (SC/PHC — first contact), Secondary (CHC/District), Tertiary (medical college/specialty). Referral links levels.</p>"""),
        _ai("IV — CHN Definition + Qualities/Functions (2+5=7)", """
        <p><strong>A. Definition (2):</strong> Community Health Nursing is a specialised field combining nursing and public health practice. It provides comprehensive care to individuals, families and communities in homes, clinics, schools and workplaces with emphasis on prevention of disease and promotion of health.</p>
        <p><strong>B. Qualities (write 5–6):</strong> Empathy, patience, honesty; good communication; leadership &amp; initiative; cultural sensitivity; professional knowledge &amp; skill; physical fitness; interest in people.</p>
        <p><strong>C. Functions:</strong> Care provider; educator; counsellor; manager/coordinator; epidemiologist/researcher; advocate linking people to services.</p>
        <p><strong>Conclusion:</strong> CHN focuses on prevention and community participation, unlike hospital nursing which focuses mainly on cure.</p>"""),
        _ai("V — Safe water + Purification (2+5=7)", """
        <p><strong>A. Safe water (2):</strong> Water free from pathogens and harmful chemicals; colourless, odourless, palatable, adequate in quantity.</p>
        <p><strong>B. Household purification:</strong> Boiling; chlorination/bleaching powder; filtration (candle/cloth); store covered.</p>
        <p><strong>C. Large scale:</strong> (1) Storage/sedimentation (2) Coagulation with alum (rapid sand) (3) Filtration — slow sand or rapid sand (4) Chlorination → clear water tank → supply. Horrock's apparatus estimates bleaching powder dose.</p>
        <p><strong>Water-borne diseases:</strong> Cholera, typhoid, hepatitis A/E, amoebiasis, giardiasis.</p>
        <p><strong>Nurse role:</strong> Teach boiling/chlorination, protect wells, report outbreaks.</p>"""),
        _ai("VI — T/F", "<ul><li>FALSE — Diabetes is non-communicable.</li><li>TRUE — Models are three-dimensional aids.</li><li>FALSE — Vitamin K helps clotting (not anticoagulant).</li><li>FALSE — Soya is a good/rich plant protein.</li></ul>"),
        _ai("VII — Short notes (model for each)", """
        <p><strong>1. Bag technique:</strong> Method of using community nursing bag during home visit without spreading infection. Place on clean paper; handwash; take articles; close bag; do procedure; clean &amp; replace; clean→dirty workflow.</p>
        <p><strong>2. NIS outline:</strong> Birth: BCG, OPV-0, HepB-0. 6/10/14 wk: OPV, Pentavalent, Rota, PCV, IPV as scheduled. 9–12 mo: MR-1 + Vit A. 16–24 mo: MR-2, DPT/OPV booster. 5–6 yr DPT booster; 10 &amp; 16 yr Td. Pregnant: Td.</p>
        <p><strong>3. Housing standards:</strong> Good site; adequate space; light &amp; ventilation; safe water; sanitary latrine; refuse disposal; no overcrowding; protection from damp/insects.</p>
        <p><strong>4. Counselling:</strong> Face-to-face helping process for informed decisions. Principles: confidentiality, acceptance, non-judgemental, client choice. Steps: rapport → explore → options → decide → follow-up.</p>
        <p><strong>5. Food adulteration:</strong> Adding cheap/harmful substances (water in milk, argemone in oil). Prevention: FSSAI packed foods, awareness, report. Law: Food Safety &amp; Standards Act / older PFA Act.</p>"""),
        _ai("VIII — Health Education (2+6=8)", """
        <p><strong>Definition:</strong> Process that informs, motivates and helps people adopt and maintain healthy practices.</p>
        <p><strong>Principles:</strong> Based on needs; community participation; known→unknown; simple language; reinforcement; use AV aids; evaluate results; culturally acceptable.</p>
        <p><strong>Methods/Approaches:</strong> Individual (counselling, home visit); Group (demo, discussion, role play); Mass (TV, radio, posters, campaigns).</p>
        <p><strong>Nurse role:</strong> Plan HE, choose method, use AV aids, involve leaders, evaluate change in practice.</p>"""),
        _ai("IX — Vitamins (2+7=9)", """
        <p><strong>A. Classification:</strong> Fat-soluble A,D,E,K; Water-soluble B-complex &amp; C.</p>
        <p><strong>B. Detail:</strong></p>
        <ul>
          <li><strong>Vit A:</strong> GLV, carrot, milk, liver — night blindness, xerophthalmia, Bitot's spots</li>
          <li><strong>Vit D:</strong> sunlight, fish liver oil — rickets / osteomalacia</li>
          <li><strong>Vit C:</strong> amla, citrus, guava — scurvy (bleeding gums)</li>
          <li><strong>Also:</strong> Vit K = clotting; Vit B1 = beriberi (NOT night blindness)</li>
        </ul>
        <p><strong>Nurse:</strong> Diet diversity, Vit A prophylaxis, early detection of deficiency.</p>"""),
    ])

def build_m2a():
    return "\n".join([
        _ai("I — Meanings", """
        <ul>
          <li><strong>Immunization:</strong> Artificial induction of immunity by vaccine or immunoglobulin.</li>
          <li><strong>Endemic:</strong> Constant presence of a disease in a given geographic area.</li>
          <li><strong>Weaning:</strong> Gradual introduction of complementary foods while continuing breastfeeding.</li>
          <li><strong>Ventilation:</strong> Supply of fresh air and removal of vitiated air from an enclosed space.</li>
        </ul>"""),
        _ai("II — Fill blanks", "<ul><li>Iodine</li><li>Fat</li><li>Hospital</li><li>FRU</li></ul>"),
        _ai("III — Short notes", """
        <p><strong>1. Epidemiological triad:</strong> Interaction of Agent + Host + Environment causing disease. Control by acting on any arm (kill agent, protect host, improve environment).</p>
        <p><strong>2. Referral system:</strong> Sending client to appropriate higher level of care with information; preferably two-way with feedback. Nurse prepares client, documents, follows up.</p>
        <p><strong>3. AV aids:</strong> Teaching aids using hearing/sight. Types: audio, visual, audio-visual; 2D/3D (models). Advantages: interest, clarity, retention, saves time.</p>
        <p><strong>4. Refuse disposal:</strong> Dumping, controlled tipping/landfill, composting, incineration, burial. Separate sewage (with excreta) vs sullage (without).</p>
        <p><strong>5. Minor ailments:</strong> Common self-limiting conditions (fever, diarrhoea, cold, scabies, worms). Manage with standing orders, ORS, hygiene; refer danger signs.</p>"""),
        _ai("IV — Home visit + Bag (2+5=7)", """
        <p><strong>A. Definition:</strong> Planned visit by community health nurse to the family home for assessment, nursing care, health education and follow-up.</p>
        <p><strong>B. Principles:</strong> Clear purpose; planned yet flexible; family-centred; use family resources; maintain privacy/dignity; educative; regular follow-up.</p>
        <p><strong>C. Bag technique:</strong> Place bag on clean paper; wash hands; remove needed articles and close bag; perform care; discard waste safely; clean articles; wash hands; replace; never contaminate bag interior. Clean → dirty workflow.</p>
        <p><strong>Conclusion:</strong> Home visit with correct bag technique brings safe nursing care to the family.</p>"""),
        _ai("V — PHC + Levels (2+5=7)", """
        <p><strong>A. PHC definition:</strong> Essential health care based on practical, scientifically sound methods, universally accessible to individuals and families with their full participation (Alma Ata 1978).</p>
        <p><strong>B. 8 elements:</strong> Education; nutrition; water &amp; sanitation; MCH/FP; immunization; prevention of endemic diseases; treatment of common diseases; essential drugs.</p>
        <p><strong>C. Levels:</strong> Primary (Sub-centre/PHC); Secondary (CHC/District hospital); Tertiary (Medical college/specialty centres).</p>"""),
        _ai("VI — T/F", "<ul><li>FALSE — Night blindness = Vit A; B1 = beriberi.</li><li>TRUE — Sewage contains excreta.</li><li>FALSE — Chikungunya by Aedes mosquito.</li><li>TRUE — BCG is live attenuated.</li></ul>"),
        _ai("VII — Short notes", """
        <p><strong>1. Dimensions of health:</strong> Physical, mental, social (WHO core); also emotional, spiritual, vocational as taught.</p>
        <p><strong>2. Cold chain:</strong> Keep vaccines +2 to +8°C using ILR, deep freezer, cold boxes, carriers; protect from heat/freezing; check VVM.</p>
        <p><strong>3. Balanced diet:</strong> All essential nutrients in correct proportion — energy, body-building, protective foods.</p>
        <p><strong>4. Mosquito control:</strong> Source reduction; larvicides/fish; adult spray/screens; personal protection (nets). Anopheles=malaria; Aedes=dengue/chikungunya.</p>
        <p><strong>5. Family welfare nurse role:</strong> Eligible couple register; counsel FP cafeteria approach; ANC/PNC; assist camps; follow-up side effects; HE.</p>"""),
        _ai("VIII — Communication (3+5=8)", """
        <p><strong>Definition:</strong> Process of sharing ideas, facts, feelings between persons for common understanding.</p>
        <p><strong>Process:</strong> Sender → Message → Channel → Receiver → Feedback.</p>
        <p><strong>Types:</strong> Verbal/non-verbal; one-way/two-way; individual/group/mass.</p>
        <p><strong>Barriers:</strong> Language, noise, culture, emotions, status, physiological defects.</p>
        <p><strong>Nurse:</strong> Simple language, listen, feedback, AV aids, respect culture.</p>"""),
        _ai("IX — Ventilation (2+7=9)", """
        <p><strong>A. Definition:</strong> Process of supplying fresh air and removing vitiated air to maintain healthy indoor atmosphere.</p>
        <p><strong>B. Standards:</strong> Adequate air change without draught; comfortable temperature/humidity; remove CO₂, odours, dust, pathogens.</p>
        <p><strong>C. Types:</strong> Natural — windows, doors, cross ventilation (opposite openings), stack effect. Mechanical — exhaust (extracts foul air), plenum (forces fresh air in), air-conditioning.</p>
        <p><strong>Nurse:</strong> Advise cross ventilation, avoid overcrowding; ensure ward ventilation.</p>"""),
    ])

def build_m3a():
    return "\n".join([
        _ai("I — Meanings", """
        <ul>
          <li><strong>Community:</strong> Group of people in a defined area sharing common interests/characteristics.</li>
          <li><strong>Carrier:</strong> Person harbouring infectious agent without symptoms but able to transmit.</li>
          <li><strong>Home visit:</strong> Planned nurse visit to family home for care and education.</li>
          <li><strong>Mortality:</strong> Death / death rate in a population.</li>
        </ul>"""),
        _ai("II — Fill blanks", "<ul><li>Proteins</li><li>Aedes aegypti</li><li>Decibels</li><li>Estimating bleaching powder dose for water</li></ul>"),
        _ai("III — Short notes", """
        <p><strong>1. Levels of prevention:</strong> Primary (health promotion + specific protection e.g. immunization); Secondary (early diagnosis &amp; treatment); Tertiary (disability limitation &amp; rehabilitation).</p>
        <p><strong>2. Immunization schedule key ages:</strong> Birth BCG/OPV0/HepB0; 6–14 wk primary series; 9 mo MR-1; 16–24 mo boosters; school-age/Td; pregnant Td.</p>
        <p><strong>3. Principles of recording:</strong> Accurate, complete, concise, legible, timely, confidential, dated &amp; signed, continuity in family folder.</p>
        <p><strong>4. Cooking methods:</strong> Boiling, steaming, pressure cooking, frying, roasting, baking. Prefer steam/pressure; wash before cutting; avoid overcooking (Vit C/B loss).</p>
        <p><strong>5. Well disinfection:</strong> Estimate volume; calculate bleaching powder (Horrock's); dissolve &amp; pour; contact time; advise alternate water temporarily; sanitary well features.</p>"""),
        _ai("IV — Health dimensions/determinants (2+5=7)", """
        <p><strong>A. Definition (WHO):</strong> Health is a state of complete physical, mental and social well-being and not merely the absence of disease or infirmity.</p>
        <p><strong>B. Dimensions:</strong> Physical, mental, social (+ emotional, spiritual, vocational).</p>
        <p><strong>C. Determinants:</strong> Biological; behavioural; environmental; socio-economic; health services; cultural factors.</p>"""),
        _ai("V — Counselling (2+5=7)", """
        <p><strong>A. Definition:</strong> Face-to-face helping process in which counsellor helps client understand problem and take informed decision.</p>
        <p><strong>B. Principles:</strong> Acceptance; confidentiality; non-judgemental attitude; client's right to decide; individuality; empathy.</p>
        <p><strong>C. Steps/Process:</strong> Establish rapport → explore problem → help see options → decision → action plan → follow-up.</p>
        <p><strong>Difference HE vs counselling:</strong> HE often group information; counselling usually one-to-one decision support.</p>"""),
        _ai("VI — T/F", "<ul><li>FALSE — OPV is live.</li><li>TRUE — Sullage has no excreta.</li><li>TRUE — Vasectomy = male sterilization.</li><li>TRUE — Under-five clinic = well-baby clinic.</li></ul>"),
        _ai("VII — Short notes", """
        <p><strong>1. PEM:</strong> Marasmus = severe wasting, no oedema; Kwashiorkor = oedema, moon face. Prevent by breastfeeding, complementary feeding, ICDS.</p>
        <p><strong>2. Functions of CHN:</strong> Care, education, counselling, coordination, epidemiology, advocacy.</p>
        <p><strong>3. Water-borne diseases:</strong> Cholera, typhoid, hep A/E, amoebiasis — prevent by safe water &amp; sanitation.</p>
        <p><strong>4. Community health team:</strong> MO, PHN/CHN, ANM/MPHW, ASHA, AWW, supervisors, pharmacist/lab — teamwork.</p>
        <p><strong>5. ORS &amp; diarrhoea:</strong> Assess dehydration; ORS sips; continue feeding/BF; zinc as protocol; refer severe dehydration/blood in stool.</p>"""),
        _ai("VIII — Nutrition/PEM (2+6=8)", """
        <p><strong>Balanced diet:</strong> Contains all essential nutrients in correct proportion.</p>
        <p><strong>Food classification:</strong> Energy-yielding (cereals/oils); body-building (pulses/milk/egg/soya); protective (fruits/vegetables).</p>
        <p><strong>PEM:</strong> Marasmus vs kwashiorkor as above; nurse identifies, educates, links to Anganwadi/ICDS.</p>
        <p><strong>Protein:</strong> Amino acids = building blocks; ~1 g/kg/day adult (as taught); 4 kcal/g.</p>"""),
        _ai("IX — CD + Transmission (3+6=9)", """
        <p><strong>A. Definition:</strong> Communicable disease is illness due to a specific infectious agent or its toxic products, transmissible from reservoir to susceptible host.</p>
        <p><strong>B. Modes:</strong> Direct (contact, droplet, vertical); Indirect (vehicle, vector, airborne, fomite).</p>
        <p><strong>C. Control:</strong> Early diagnosis &amp; treatment; isolation/quarantine as needed; immunization; sanitation &amp; safe water; vector control; health education; surveillance &amp; notification.</p>
        <p><strong>Nurse:</strong> Detect cases, educate, maintain cold chain/immunization, participate in control campaigns.</p>"""),
    ])

def build_m4a():
    return "\n".join([
        _ai("I — Meanings", "<ul><li><strong>Weaning:</strong> Gradual start of complementary foods with continued breastfeeding.</li><li><strong>Quarantine:</strong> Restricting movement of healthy contacts to prevent spread.</li><li><strong>Sanitary well:</strong> Protected well with parapet, platform, cover, drain.</li><li><strong>Demography:</strong> Scientific study of human population.</li></ul>"),
        _ai("II — Fill blanks", "<ul><li>Iodine</li><li>Aedes aegypti</li><li>April 7</li><li>Kesari dal</li></ul>"),
        _ai("III — Short notes", """
        <p><strong>Standing orders fever/diarrhoea:</strong> MO protocol; fever→assess/sponge/PCM; diarrhoea→ORS+feed; refer danger signs.</p>
        <p><strong>Family planning:</strong> Temp: condom/IUCD/OCP; Perm: vasectomy/tubectomy; counsel choice.</p>
        <p><strong>Air pollution:</strong> sources industry/vehicles/chulha; effects asthma; control clean fuel/laws/green cover.</p>
        <p><strong>Anthropometry:</strong> Ht/Wt/MUAC for nutrition/growth assessment.</p>
        <p><strong>Mid-Day Meal / ICDS:</strong> school meal + Anganwadi supplementary nutrition.</p>"""),
        _ai("IV — Safe water + Hardness (2+5)", """
        <p><strong>A:</strong> Safe water free from pathogens/harmful chemicals; clear, odourless.</p>
        <p><strong>B Hardness:</strong> Ca/Mg salts; wastes soap, scale in boilers; remove temporary by boiling/lime; permanent by lime-soda/ion exchange.</p>
        <p><strong>Purify:</strong> HH boil/chlorine; large Store→Filter→Chlorinate.</p>"""),
        _ai("V — ANC/PNC (2+5)", """
        <p><strong>A ANC:</strong> Care in pregnancy — register, TT, IFA, exam, danger signs, birth plan.</p>
        <p><strong>B PNC:</strong> Care after delivery (6 wks) for mother+newborn; BF; hygiene; watch bleeding/fever; FP counsel; newborn warmth/cord/immunize.</p>"""),
        _ai("VI — T/F", "<ul><li>FALSE — Night blindness = Vit A.</li><li>TRUE — Models are 3D aids.</li><li>FALSE — Tubectomy is female (not male).</li><li>TRUE — Home visit is backbone of PHN.</li></ul>"),
        _ai("VII — Short notes", """
        <p><strong>Rapid sand:</strong> Coagulate→Sediment→Filter→Chlorinate.</p>
        <p><strong>HE vs Counselling:</strong> group info vs 1:1 decision help.</p>
        <p><strong>Pulse Polio:</strong> mass OPV all under-5 on NID.</p>
        <p><strong>Housing standards:</strong> site, space, light, ventilation, water, latrine, no overcrowding.</p>
        <p><strong>School health nurse:</strong> screen, first aid, HE, records, refer.</p>"""),
        _ai("VIII — Vitamins ADEK/C (2+6)", "<p><strong>A:</strong> Fat ADEK; Water B &amp; C.</p><p><strong>B:</strong> A night blindness/Bitot; D rickets; C scurvy; K clotting; B1 beriberi.</p>"),
        _ai("IX — Home visit + Bag (2+7)", "<p><strong>A:</strong> Planned visit to family for assess/care/HE.</p><p><strong>B:</strong> Principles purposeful/planned/flexible/private. Bag: clean paper, handwash, articles out, close bag, procedure, clean→dirty.</p>"),
    ])

def build_m5a():
    return "\n".join([
        _ai("I — Meanings", "<ul><li><strong>Infection:</strong> Entry &amp; multiplication of pathogen causing disease.</li><li><strong>Carrier:</strong> Harbours agent without symptoms, can transmit.</li><li><strong>Calorie:</strong> Unit of heat/energy (kcal in nutrition).</li><li><strong>Disinfection:</strong> Kill/remove pathogens (spores may remain).</li></ul>"),
        _ai("II — Fill blanks", "<ul><li>4</li><li>9</li><li>28 days</li><li>Accredited Social Health Activist</li></ul>"),
        _ai("III — Short notes", """
        <p><strong>Disease cycle:</strong> incubation→prodromal→illness→decline→convalescence.</p>
        <p><strong>Food hygiene:</strong> clean hands, cover food, separate raw/cooked, safe water.</p>
        <p><strong>Socratic vs Didactic:</strong> questions/discussion vs one-way lecture.</p>
        <p><strong>Indicators of health:</strong> IMR, MMR, CBR, CDR, morbidity rates.</p>
        <p><strong>Global warming effects:</strong> heat, floods/drought, vector shift, food insecurity.</p>"""),
        _ai("IV — PHC + Levels (2+5)", "<p><strong>A:</strong> Essential accessible care, Alma Ata 1978.</p><p><strong>B:</strong> 8 elements; Primary SC/PHC, Secondary CHC/District, Tertiary medical college.</p>"),
        _ai("V — Nutrition pregnant + BF (2+5)", "<p><strong>A Pregnant diet:</strong> extra energy/protein, iron, calcium, greens, iodized salt.</p><p><strong>B BF advantages:</strong> complete nutrition, antibodies, bonding, cheap, sterile, helps involution.</p>"),
        _ai("VI — T/F", "<ul><li>FALSE — 1 g carb = 4 kcal not 9.</li><li>TRUE — Koplik = measles.</li><li>FALSE — Bitot = Vit A not measles.</li><li>TRUE — Oxidation pond treats sewage.</li></ul>"),
        _ai("VII — Short notes", """
        <p><strong>Active vs Passive immunity:</strong> body makes Abs vs ready Abs.</p>
        <p><strong>Concurrent vs Terminal disinfection:</strong> during illness vs after recovery/death.</p>
        <p><strong>Poached egg / barley water:</strong> write short prep steps.</p>
        <p><strong>ASHA in MCH:</strong> mobilize ANC/PNC, escort delivery, ORS/immunize link.</p>
        <p><strong>Diabetic diet:</strong> timed meals, fibre, avoid sugar, less fried fat.</p>"""),
        _ai("VIII — Epidemiology + Triad (2+6)", "<p><strong>A:</strong> Study of distribution &amp; determinants of health events.</p><p><strong>B:</strong> Agent–Host–Environment; aims describe/explain/control; draw triad.</p>"),
        _ai("IX — Waste + Mosquito (3+6)", "<p><strong>Refuse methods:</strong> dump, landfill, compost, incinerate.</p><p><strong>Sewage≠sullage.</strong> Mosquito: source reduction, larvicide, spray, nets; Anopheles/Aedes.</p>"),
    ])
