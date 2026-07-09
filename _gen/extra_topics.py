# -*- coding: utf-8 -*-
"""Additional CHN-I topic cards for past-paper gaps (t25–t36)."""

def register(T):
    """Append new topics using the T() helper from topics_data."""

    T(
        id="t25", level="red", badge="badge-red", badge_txt="🔴 MUST",
        cat="Epidemiology & Child/Family", title="Standing Orders — Fever, Diarrhoea, Digestive",
        topic="standing orders fever diarrhoea digestive minor ailments home management",
        prob="prob-vhigh", prob_txt="🔴 VERY HIGH · 88% likely",
        papers="7 papers · 2019, 2018, 2017, 2016, 2013, 2012, 2011",
        marks="4 marks",
        years=[2019,2018,2017,2016,2013,2012,2011],
        why="Standing orders for fever/diarrhoea/digestive conditions are classic short notes across many papers.",
        must="Meaning of standing order → fever steps → diarrhoea/ORS → digestive conditions → when to refer",
        mistakes="Giving antibiotics without indication. Skipping ORS. Not listing danger signs for referral.",
        mark_rows=[("Meaning of standing order", "1"), ("Fever / diarrhoea / digestive points", "2–3"), ("Referral / nurse role", "1")],
        fast="Standing order = written order by MO for nurse to treat common conditions. Fever: assess, sponge, paracetamol as ordered, fluids. Diarrhoea: ORS, continue feeding, zinc. Refer if danger signs.",
        last="STANDING ORDER DEF + FEVER + ORS DIARRHOEA + DIGESTIVE + REFER DANGER SIGNS",
        eli="Doctor writes a ready plan so the nurse can start simple treatment for fever or loose stools without waiting every time.",
        analogy="Standing order = recipe card the cook can follow when the chef is busy.",
        viva="What is standing order? | ORS use in diarrhoea? | When to refer fever case?",
        draw="",
        trick='🧠 Memory: <strong>"FAR"</strong> Fever care · Assess/ORS for diarrhoea · Refer danger signs',
        answer="""
          <h4>📄 Full Exam Version — Write in Answer Sheet</h4>
          <h4>A. Meaning of Standing Order</h4>
          <p>A <strong>standing order</strong> is a written order by the medical officer authorizing the community health nurse to give specified treatment for common minor conditions according to a fixed protocol.</p>
          <h4>B. Standing Orders — Fever</h4>
          <ul>
            <li>Assess temperature, history, danger signs (convulsion, stiff neck, rash, severe dehydration, unconsciousness)</li>
            <li>Remove excess clothing; tepid sponging if high fever</li>
            <li>Give <strong>paracetamol</strong> as per standing order / age-dose</li>
            <li>Encourage fluids; advise rest; record temperature</li>
            <li><strong>Refer immediately</strong> if danger signs or fever not responding / suspected malaria, measles complications</li>
          </ul>
          <h4>C. Standing Orders — Diarrhoea</h4>
          <ul>
            <li>Assess dehydration (sunken eyes, skin pinch, thirst, urine)</li>
            <li>Start <strong>ORS</strong> — frequent small sips; continue breastfeeding / feeding</li>
            <li>Give <strong>zinc</strong> as per protocol (where standing order allows)</li>
            <li>Advise handwashing, clean water, safe food</li>
            <li><strong>Refer</strong> if severe dehydration, blood in stool, persistent vomiting, infant &lt;2 months with danger signs</li>
          </ul>
          <h4>D. Standing Orders — Digestive System Conditions</h4>
          <ul>
            <li><strong>Constipation:</strong> fluids, fibre diet, exercise; avoid harsh purgatives in children without order</li>
            <li><strong>Indigestion / mild gastritis:</strong> light diet, avoid spicy/oily food; antacid only if ordered</li>
            <li><strong>Worm infestation (suspected):</strong> hygiene advice; anthelmintic as per standing order / camp protocol</li>
            <li>Always assess for acute abdomen / severe pain → <strong>urgent referral</strong></li>
          </ul>
          <h4>🩺 Nursing Role</h4>
          <p>Follow written standing orders exactly, document treatment, educate family, and refer beyond protocol limits.</p>
          <h4>✅ Conclusion</h4>
          <p>Standing orders help nurses give timely, safe first-line care for common community illnesses.</p>
"""
    )

    T(
        id="t26", level="red", badge="badge-red", badge_txt="🔴 MUST",
        cat="Environment & Nutrition & Communication", title="Cooking Methods + Preservation + Food Hygiene",
        topic="cooking methods principles preservation storage food sanitation hygiene",
        prob="prob-vhigh", prob_txt="🔴 VERY HIGH · 91% likely",
        papers="10 papers · 2025, 2019, 2018, 2017, 2016, 2014, 2013, 2012, 2011",
        marks="4 marks",
        years=[2025,2019,2018,2017,2016,2014,2013,2012,2011],
        why="Methods/principles of cooking, preservation/storage, and food hygiene/sanitation appear repeatedly as short notes.",
        must="Principles of cooking → methods → nutrient loss tips → preservation/storage → food hygiene rules → nurse role",
        mistakes="Saying pressure cooking always destroys all nutrients (papers test this trap). Mixing preservation with adulteration.",
        mark_rows=[("Principles", "1"), ("Methods", "1–2"), ("Preservation / hygiene", "1–2")],
        fast="Cook to kill germs + improve digestibility. Methods: boiling, steaming, frying, roasting, baking, pressure cooking. Preserve: drying, salting, refrigeration, canning. Hygiene: clean hands, covered food, separate raw/cooked.",
        last="PRINCIPLES + METHODS + PRESERVE + FOOD HYGIENE 5 RULES",
        eli="Cook food the right way so it is safe and still has vitamins. Keep leftovers covered and cold.",
        analogy="Food hygiene = traffic rules for the kitchen — follow them or accidents (food poisoning) happen.",
        viva="Name 4 cooking methods? | Advantage of steaming? | What is food sanitation?",
        draw="",
        trick='🧠 Memory: Cook <strong>"BSFRBP"</strong> Boil Steam Fry Roast Bake Pressure | Hygiene <strong>"CHOPS"</strong> Clean hands, Hot/cold store, Open covered, Prevent flies, Separate raw/cooked',
        answer="""
          <h4>📄 Full Exam Version — Write in Answer Sheet</h4>
          <h4>A. Principles of Cooking</h4>
          <ul>
            <li>Make food <strong>digestible, palatable and safe</strong> (destroy pathogens)</li>
            <li>Preserve maximum nutrients — wash before cutting; avoid overcooking</li>
            <li>Use clean utensils and safe water</li>
            <li>Cook just before serving when possible</li>
            <li>Choose method suited to food type and patient need</li>
          </ul>
          <h4>B. Methods of Cooking</h4>
          <ul>
            <li><strong>Boiling:</strong> in water — softens food; some water-soluble vitamins lost in water</li>
            <li><strong>Steaming:</strong> retains more nutrients; good for invalids</li>
            <li><strong>Pressure cooking:</strong> saves time/fuel; retains nutrients better than long boiling</li>
            <li><strong>Frying:</strong> tasty but increases fat; not for all patients</li>
            <li><strong>Roasting / Baking / Grilling:</strong> dry heat methods</li>
          </ul>
          <h4>C. Food Preservation and Storage</h4>
          <ul>
            <li><strong>Drying / dehydration</strong> — removes moisture</li>
            <li><strong>Salting / pickling / sugaring</strong></li>
            <li><strong>Refrigeration / freezing</strong></li>
            <li><strong>Canning / bottling</strong>; smoking</li>
            <li>Store in clean, covered, pest-free containers; FIFO (first in, first out)</li>
          </ul>
          <h4>D. Food Sanitation / Food Hygiene</h4>
          <ul>
            <li>Personal hygiene of food handlers — handwash, clean nails, no open wounds</li>
            <li>Clean kitchen, utensils, cutting boards</li>
            <li>Protect food from flies, dust, rodents</li>
            <li>Separate raw and cooked food; cook thoroughly; reheat leftovers well</li>
            <li>Safe water for washing and cooking</li>
          </ul>
          <h4>🩺 Nursing Role</h4>
          <p>Teach mothers cooking that saves nutrients, safe storage, and hygiene to prevent food-borne disease.</p>
          <h4>✅ Conclusion</h4>
          <p>Correct cooking, preservation and food hygiene protect nutrition and prevent infection.</p>
"""
    )

    T(
        id="t27", level="yellow", badge="badge-yellow", badge_txt="🟡 HIGH",
        cat="Environment & Nutrition & Communication", title="Air Pollution + Environmental Hygiene + Global Warming",
        topic="air pollution sources effects control environmental hygiene global warming",
        prob="prob-high", prob_txt="🟡 HIGH · 82% likely",
        papers="7 papers · 2018, 2017, 2016, 2015, 2014, 2013, 2011",
        marks="4–7 marks",
        years=[2018,2017,2016,2015,2014,2013,2011],
        why="Air pollution control, environmental hygiene importance, and global warming appear as short/long notes.",
        must="Sources → effects → prevention/control → environmental hygiene meaning+importance → global warming effects → nurse role",
        mistakes="Listing only vehicle smoke. Forgetting indoor pollution (chulha smoke). No control measures.",
        mark_rows=[("Sources + effects", "2"), ("Control measures", "2"), ("Env hygiene / global warming", "2–3")],
        fast="Air pollution: industries, vehicles, burning, indoor smoke. Effects: asthma, eye irritation, cancer risk. Control: laws, green cover, clean fuel. Global warming = greenhouse gases → climate change.",
        last="SOURCES + EFFECTS + CONTROL + ENV HYGIENE + GLOBAL WARMING EFFECTS",
        eli="Dirty air from smoke and cars makes people cough. Hotter Earth from too much smoke gases is global warming.",
        analogy="Air pollution = filling a room with smoke until you can't breathe.",
        viva="Sources of air pollution? | What is environmental hygiene? | Effect of global warming?",
        draw="",
        trick='🧠 Memory: Air <strong>"IVEB"</strong> Industry Vehicle Exhaust Burning | Control <strong>"LACE"</strong> Law Awareness Clean fuel Environment green',
        answer="""
          <h4>📄 Full Exam Version — Write in Answer Sheet</h4>
          <h4>A. Air Pollution — Sources</h4>
          <ul>
            <li><strong>Industrial:</strong> factories, power plants, chemical fumes</li>
            <li><strong>Vehicular:</strong> exhaust gases (CO, NOx, lead historically)</li>
            <li><strong>Domestic / indoor:</strong> biomass chulha smoke, tobacco</li>
            <li>Burning of refuse, dust, construction, agricultural burning</li>
          </ul>
          <h4>B. Effects on Health</h4>
          <ul>
            <li>Respiratory diseases — asthma, bronchitis, COPD</li>
            <li>Eye and throat irritation; headache</li>
            <li>Increased heart disease risk; cancers with chronic exposure</li>
            <li>Reduced visibility; acid rain damage to environment</li>
          </ul>
          <h4>C. Prevention and Control</h4>
          <ul>
            <li>Enforce emission standards; industrial scrubbers / tall chimneys with treatment</li>
            <li>Promote public transport, CNG/clean fuels, vehicle PUC checks</li>
            <li>Ban open burning of waste; improve waste management</li>
            <li>Smokeless chulhas / LPG; no smoking indoors</li>
            <li>Increase green cover; public awareness</li>
          </ul>
          <h4>D. Environmental Hygiene — Meaning & Importance</h4>
          <p><strong>Environmental hygiene</strong> is maintaining a clean, safe physical environment (air, water, soil, housing, waste, vectors) to promote health and prevent disease.</p>
          <ul>
            <li>Prevents communicable diseases</li>
            <li>Improves quality of life and productivity</li>
            <li>Supports maternal-child and community health programmes</li>
          </ul>
          <h4>E. Global Warming and Effects</h4>
          <ul>
            <li>Rise in Earth's temperature due to greenhouse gases (CO₂, methane, etc.)</li>
            <li>Effects: extreme weather, floods/droughts, melting ice, sea-level rise</li>
            <li>Health: heat stroke, changing vector patterns (malaria/dengue zones), food insecurity</li>
          </ul>
          <h4>🩺 Nursing Role</h4>
          <p>Health educate on clean fuel, no burning, tree planting; participate in environment health campaigns.</p>
          <h4>✅ Conclusion</h4>
          <p>Clean air and environmental hygiene are foundations of community health.</p>
"""
    )

    T(
        id="t28", level="red", badge="badge-red", badge_txt="🔴 MUST",
        cat="Environment & Nutrition & Communication", title="Water Pollution + Hardness + Sanitary Well + Rapid Sand",
        topic="water pollution hardness sanitary well rapid sand filtration slow sand",
        prob="prob-vhigh", prob_txt="🔴 VERY HIGH · 90% likely",
        papers="9 papers · 2024, 2019, 2015, 2014, 2013, 2012, 2011",
        marks="4–9 marks",
        years=[2024,2019,2015,2014,2013,2012,2011],
        why="Papers ask water pollution, hardness removal, sanitary well, and rapid sand filtration as distinct answers.",
        must="Water pollution sources/control → hardness disadvantages+removal → sanitary well features → rapid vs slow sand steps",
        mistakes="Confusing rapid sand with household filter. Saying hardness causes cholera (it doesn't — pathogens do).",
        mark_rows=[("Pollution / control", "2"), ("Hardness", "2–3"), ("Sanitary well / rapid sand", "2–4")],
        fast="Hardness = Ca/Mg salts. Soften by boiling (temporary), lime-soda, ion exchange. Rapid sand = coagulation→sedimentation→filtration→chlorination. Sanitary well = parapet, platform, cover, drain.",
        last="POLLUTION CONTROL + HARDNESS REMOVE + SANITARY WELL POINTS + RAPID SAND STEPS",
        eli="Dirty water from drains and factories is pollution. Hard water leaves white scale and wastes soap. A sanitary well is a clean protected well.",
        analogy="Rapid sand plant = big washing machine for river water before it reaches taps.",
        viva="Disadvantages of hard water? | Features of sanitary well? | Steps of rapid sand filtration?",
        draw="""
          <div class="diagram-box">RAPID SAND FILTRATION (large scale)
Coagulation (alum) → Sedimentation → Rapid sand filter → Chlorination → Clear water tank → Supply
Compare SLOW SAND: biological schmutzdecke layer; slower; no heavy chemicals always</div>""",
        trick='🧠 Memory: Rapid sand <strong>"CSFC"</strong> Coagulate Sediment Filter Chlorinate | Well <strong>"PPC-D"</strong> Parapet Platform Cover Drain',
        answer="""
          <h4>📄 Full Exam Version — Write in Answer Sheet</h4>
          <h4>A. Water Pollution — Causes & Control</h4>
          <ul>
            <li><strong>Sources:</strong> sewage, industrial effluent, agricultural chemicals, bathing/washing animals, solid waste</li>
            <li><strong>Effects:</strong> water-borne diseases, toxicity, eutrophication</li>
            <li><strong>Control:</strong> sewage treatment, industrial effluent treatment, protect sources, sanitary latrines, public education, laws</li>
          </ul>
          <h4>B. Hardness of Water</h4>
          <p><strong>Hardness</strong> is due mainly to dissolved <strong>calcium and magnesium</strong> salts.</p>
          <p><strong>Disadvantages:</strong></p>
          <ul>
            <li>More soap needed for washing; wastage of soap</li>
            <li>Scale formation in boilers/kettles; fuel wastage</li>
            <li>Toughens vegetables; may affect taste; not ideal for some industries</li>
          </ul>
          <p><strong>Removal:</strong></p>
          <ul>
            <li><strong>Temporary hardness</strong> (bicarbonates): boiling / Clark's lime process</li>
            <li><strong>Permanent hardness</strong> (sulphates/chlorides): lime-soda process, base exchange (zeolite/ion exchange), demineralization</li>
          </ul>
          <h4>C. Sanitary Well</h4>
          <ul>
            <li>Located away from latrines / soakage pits (safe distance)</li>
            <li><strong>Parapet wall</strong>, impervious platform, proper drain</li>
            <li>Tight-fitting cover; preferably hand pump / clean bucket with windlass</li>
            <li>Lined well; clean surroundings; periodic disinfection</li>
          </ul>
          <h4>D. Rapid Sand Filtration (explain method)</h4>
          <ol>
            <li><strong>Coagulation:</strong> add alum; mix to form floc</li>
            <li><strong>Sedimentation:</strong> settle floc in tanks</li>
            <li><strong>Filtration:</strong> pass through rapid sand filter beds</li>
            <li><strong>Disinfection:</strong> chlorination; store in clear water reservoir; supply</li>
          </ol>
          <p><strong>Slow sand filter:</strong> finer biological purification layer (schmutzdecke); slower rate; classic large-scale method still taught in exams.</p>
          <h4>🩺 Nursing Role</h4>
          <p>Educate on protected wells, report pollution, assist chlorination campaigns, teach household purification.</p>
          <h4>✅ Conclusion</h4>
          <p>Safe water needs source protection, proper treatment and hardness management where relevant.</p>
"""
    )

    T(
        id="t29", level="yellow", badge="badge-yellow", badge_txt="🟡 HIGH",
        cat="Epidemiology & Child/Family", title="School Health + Infant Assessment",
        topic="school health nurse assessment school going child infant health assessment",
        prob="prob-high", prob_txt="🟡 HIGH · 78% likely",
        papers="3 papers · 2017, 2016, 2012",
        marks="4 marks",
        years=[2017,2016,2012],
        why="Health assessment of school child / infant and school health nurse role appear as short notes.",
        must="School health objectives → assessment components → school nurse responsibilities → infant assessment points",
        mistakes="Writing only 'check height weight'. Missing vision/hearing/immunization/hygiene teaching.",
        mark_rows=[("School child assessment", "2"), ("School nurse role", "1"), ("Infant assessment", "1")],
        fast="School assessment: anthropometry, vision, hearing, dental, skin, immunization, hygiene. Nurse: screening, HE, first aid, referral, records.",
        last="ANTHROPOMETRY + SENSE ORGANS + IMMUNIZATION + HYGIENE + NURSE ROLE",
        eli="School nurse checks if children are growing well, can see/hear, and teaches clean habits.",
        analogy="School health check = annual service for a school bus — catch problems early.",
        viva="Components of school health assessment? | Role of school health nurse?",
        draw="",
        trick='🧠 Memory: Assess <strong>"HAV-DISH"</strong> Height/weight, Appearance, Vision/hearing, Dental, Immunization, Skin, Hygiene',
        answer="""
          <h4>📄 Full Exam Version — Write in Answer Sheet</h4>
          <h4>A. Health Assessment of School-Going Child</h4>
          <ul>
            <li><strong>Anthropometry:</strong> height, weight, BMI / growth comparison</li>
            <li>General appearance, nutrition, personal hygiene</li>
            <li><strong>Vision and hearing</strong> screening; dental check</li>
            <li>Skin, scalp (lice), throat, posture, deformities</li>
            <li>Immunization status; common illness history; mental/emotional wellbeing</li>
          </ul>
          <h4>B. Responsibilities of School Health Nurse</h4>
          <ul>
            <li>Plan and conduct health appraisal / screening</li>
            <li>Maintain school health records; follow up defects</li>
            <li>First aid and care of minor ailments</li>
            <li>Health education on hygiene, nutrition, menstrual hygiene, substance abuse</li>
            <li>Immunization coordination; referral to PHC/specialist</li>
            <li>Advise teachers/parents; promote healthy school environment</li>
          </ul>
          <h4>C. Health Assessment of Infant</h4>
          <ul>
            <li>Birth history; feeding (breast/complementary); immunization</li>
            <li>Weight, length, head circumference; plot on growth chart</li>
            <li>Milestones (motor, social, language)</li>
            <li>Physical exam: fontanelle, eyes, ears, chest, abdomen, hips, skin</li>
            <li>Danger signs teaching to mother; vitamin A / IFA as per age protocol</li>
          </ul>
          <h4>🩺 Nursing Role</h4>
          <p>Screen, educate, refer, record — link school/home to health services.</p>
          <h4>✅ Conclusion</h4>
          <p>Early assessment of infants and school children prevents lifelong disability and disease.</p>
"""
    )

    T(
        id="t30", level="red", badge="badge-red", badge_txt="🔴 MUST",
        cat="Epidemiology & Child/Family", title="Family Planning Methods — Temporary & Permanent",
        topic="family planning temporary permanent spacing condom iucd oc pills vasectomy tubectomy",
        prob="prob-vhigh", prob_txt="🔴 VERY HIGH · 87% likely",
        papers="8 papers · 2018, 2017, 2016, 2015, 2014, 2013, 2012, 2011",
        marks="4–7 marks",
        years=[2018,2017,2016,2015,2014,2013,2012,2011],
        why="Temporary vs permanent methods, spacing, and nurse role in FP are repeatedly examined.",
        must="Eligible couple → temporary (barrier, IUCD, hormonal, natural) → permanent (vasectomy/tubectomy) → advantages/limitations → nurse role",
        mistakes="Saying tubectomy is for males. Saying OC pills packet has calcium (papers: iron tablets in older Qs). Forgetting emergency contraception mention if asked.",
        mark_rows=[("Temporary methods", "2"), ("Permanent methods", "1–2"), ("Advantages / nurse role", "1–2")],
        fast="Spacing: condom, IUCD, OCP, injectable, LAM. Permanent: vasectomy (male), tubectomy (female). Counsel choice, side effects, follow-up.",
        last="TEMPORARY LIST + PERMANENT VAS/TUBEC + COUNSEL CHOICE",
        eli="Family planning means choosing when to have babies — temporary methods for spacing, operation for permanent stop.",
        analogy="Temporary FP = pause button; permanent = stop button — both need informed choice.",
        viva="Best spacing method example? | Permanent method in male? | Contents of OC packet?",
        draw="",
        trick='🧠 Memory: Temp <strong>"CIHO"</strong> Condom IUCD Hormonal Others | Perm <strong>"VT"</strong> Vasectomy Tubectomy',
        answer="""
          <h4>📄 Full Exam Version — Write in Answer Sheet</h4>
          <h4>A. Introduction</h4>
          <p><strong>Family planning</strong> helps couples space or limit births by voluntary use of contraceptive methods. <strong>Eligible couple</strong> = currently married couple where wife is usually in reproductive age (about 15–49 years).</p>
          <h4>B. Temporary / Spacing Methods</h4>
          <ul>
            <li><strong>Barrier:</strong> condom (male) — also prevents STIs; easy, no hormones</li>
            <li><strong>IUCD</strong> (Cu-T etc.) — long-acting reversible; inserted by trained worker</li>
            <li><strong>Hormonal:</strong> oral contraceptive pills (21 active + 7 iron/placebo in common packs), injectables, implants (as available)</li>
            <li><strong>Natural:</strong> lactational amenorrhoea (LAM) under conditions; fertility awareness (less reliable)</li>
            <li><strong>Emergency contraception</strong> — as per protocol after unprotected sex</li>
          </ul>
          <h4>C. Permanent Methods</h4>
          <ul>
            <li><strong>Vasectomy</strong> — male sterilization (block/cut vas deferens)</li>
            <li><strong>Tubectomy</strong> — female sterilization (block/cut fallopian tubes)</li>
            <li>Counselling on permanence, consent, follow-up; use alternate contraception until procedure effective (esp. vasectomy lag period)</li>
          </ul>
          <h4>D. Advantages / Points to Write</h4>
          <ul>
            <li>Spacing improves maternal and child health</li>
            <li>Condom: dual protection; IUCD: long acting; sterilization: permanent limit</li>
            <li>Limitations: side effects, method failure, need correct use / follow-up</li>
          </ul>
          <h4>🩺 Nursing Role</h4>
          <p>Motivate, counsel cafeteria approach, assist camps, screen eligibility, manage minor side effects, refer complications, maintain eligible couple register.</p>
          <h4>✅ Conclusion</h4>
          <p>Informed choice of FP method is central to family welfare and MCH.</p>
"""
    )

    T(
        id="t31", level="red", badge="badge-red", badge_txt="🔴 MUST",
        cat="Epidemiology & Child/Family", title="ANC · PNC · Home Delivery · Breastfeeding · Pregnant Nutrition",
        topic="antenatal clinic postnatal care home delivery breastfeeding nutrition pregnant mother",
        prob="prob-vhigh", prob_txt="🔴 VERY HIGH · 86% likely",
        papers="8 papers · 2025, 2016, 2015, 2014, 2013, 2012, 2011",
        marks="4–9 marks",
        years=[2025,2016,2015,2014,2013,2012,2011],
        why="ANC clinic, postnatal care, home delivery, breastfeeding advantages, and nutrition in pregnancy are distinct paper questions.",
        must="ANC activities → PNC def+objectives+advice → home delivery preparedness → breastfeeding advantages → diet in pregnancy",
        mistakes="Mixing ANC with PNC advice. Forgetting exclusive breastfeeding 6 months. No IFA/calcium mention in pregnancy diet.",
        mark_rows=[("ANC clinic", "2"), ("PNC", "2–3"), ("BF / home delivery / diet", "2–4")],
        fast="ANC: registration, TT, IFA, weight, BP, danger signs. PNC: mother+newborn care, breastfeeding, hygiene. EBF 6 months. Pregnancy diet: extra calories, protein, iron, calcium, greens.",
        last="ANC CHECKS + PNC ADVICE + EBF ADVANTAGES + PREGNANT DIET",
        eli="Before birth check mother often; after birth care mother and baby; breast milk is baby's best food; pregnant women need extra healthy food.",
        analogy="ANC = service before the journey; PNC = care after landing.",
        viva="Objectives of postnatal care? | Advantages of breastfeeding? | Extra nutrients in pregnancy?",
        draw="",
        trick='🧠 Memory: ANC <strong>"R-TT-IFA-BP"</strong> | PNC <strong>"MBH"</strong> Mother Baby Home advice | BF <strong>"SAFE"</strong> Sterile Available Free Easy enzymes/antibodies',
        answer="""
          <h4>📄 Full Exam Version — Write in Answer Sheet</h4>
          <h4>A. Antenatal Clinic</h4>
          <ul>
            <li>Early registration; history and examination</li>
            <li>Weight, BP, Hb, urine; abdominal examination as scheduled</li>
            <li><strong>TT immunization</strong>; IFA / calcium as protocol; counsel diet & rest</li>
            <li>Identify high-risk pregnancy; birth preparedness; danger-sign teaching</li>
            <li>MCP card; plan institutional delivery</li>
          </ul>
          <h4>B. Postnatal Care</h4>
          <p><strong>Definition:</strong> Care of mother and newborn after delivery (classically first 6 weeks).</p>
          <p><strong>Objectives:</strong> prevent complications, promote breastfeeding, restore maternal health, family planning counselling, newborn care.</p>
          <p><strong>Advice to mother:</strong></p>
          <ul>
            <li>Exclusive breastfeeding; perineal/breast hygiene; nutritious diet; rest</li>
            <li>Watch bleeding, fever, foul discharge, calf pain — report/refer</li>
            <li>Newborn: warmth, cord care, immunization, danger signs</li>
            <li>Postnatal check visits; discuss spacing methods</li>
          </ul>
          <h4>C. Home Delivery — Nurse Points</h4>
          <ul>
            <li>Prefer institutional delivery; if home: clean surface, clean hands, clean cord (5 cleans concept as taught)</li>
            <li>Prepare delivery kit; identify TBA/ANM support; arrange referral transport</li>
            <li>Immediate newborn care: dry, warm, breastfeed early; watch PPH</li>
          </ul>
          <h4>D. Advantages of Breastfeeding</h4>
          <ul>
            <li>Complete nutrition; easy digestion; antibodies (protects from infection)</li>
            <li>Promotes bonding; helps uterine involution; delays pregnancy (LAM conditions)</li>
            <li>Economical, ready, sterile; reduces allergy/obesity risk</li>
          </ul>
          <h4>E. Nutrition for Pregnant Woman</h4>
          <ul>
            <li>Extra energy and protein for foetal growth</li>
            <li>Iron-rich foods + IFA; calcium; green leafy vegetables; fruits</li>
            <li>Adequate fluids; iodized salt; avoid alcohol/tobacco</li>
            <li>Small frequent meals if nausea; treat anaemia</li>
          </ul>
          <h4>🩺 Nursing Role</h4>
          <p>Run ANC/PNC clinics, counsel breastfeeding and diet, promote institutional delivery, home-visit follow-up.</p>
          <h4>✅ Conclusion</h4>
          <p>Continuous care from pregnancy through postnatal period saves mothers and babies.</p>
"""
    )

    T(
        id="t32", level="yellow", badge="badge-yellow", badge_txt="🟡 HIGH",
        cat="Environment & Nutrition & Communication", title="Nutritional Programmes + Community Nutrition + Pulse Polio",
        topic="nutritional programmes india mid day meal icds pulse polio community nutrition",
        prob="prob-high", prob_txt="🟡 HIGH · 80% likely",
        papers="6 papers · 2023, 2018, 2014, 2013, 2012, 2011",
        marks="4 marks",
        years=[2023,2018,2014,2013,2012,2011],
        why="Nutritional problems/programmes, Mid-Day Meal, community nutrition, Pulse Polio asked as short notes.",
        must="Common nutritional problems → major programmes (ICDS, MDM, Vit A, anaemia control) → community nutrition → Pulse Polio",
        mistakes="Mixing Pulse Polio with routine NIS only. Forgetting Anganwadi/ICDS.",
        mark_rows=[("Problems", "1"), ("Programmes", "2"), ("Pulse Polio / community nutrition", "1")],
        fast="Problems: PEM, anaemia, Vit A, iodine deficiency. Programmes: ICDS, Mid-Day Meal, National Iron Plus, Vit A prophylaxis. Pulse Polio: mass OPV campaigns.",
        last="PEM ANAEMIA VIT-A IDD + ICDS MDM + PULSE POLIO",
        eli="Government runs food and vaccine campaigns so poor children don't stay weak or get polio.",
        analogy="Nutrition programmes = free school lunch + vitamin doses for the whole village team.",
        viva="What is Mid-Day Meal? | What is Pulse Polio? | ICDS services?",
        draw="",
        trick='🧠 Memory: Problems <strong>"PAVI"</strong> PEM Anaemia VitA Iodine | Programmes <strong>"I-M-V-A"</strong> ICDS MDM VitA Anaemia control',
        answer="""
          <h4>📄 Full Exam Version — Write in Answer Sheet</h4>
          <h4>A. Nutritional Problems in India</h4>
          <ul>
            <li><strong>PEM</strong> (marasmus, kwashiorkor)</li>
            <li><strong>Iron deficiency anaemia</strong></li>
            <li><strong>Vitamin A deficiency</strong></li>
            <li><strong>Iodine deficiency disorders</strong> (goitre)</li>
            <li>Other: fluorosis in some areas; obesity emerging in urban</li>
          </ul>
          <h4>B. Nutritional Programmes in India</h4>
          <ul>
            <li><strong>ICDS / Anganwadi:</strong> supplementary nutrition, growth monitoring, preschool education, HE</li>
            <li><strong>Mid-Day Meal Programme:</strong> cooked meal in schools — improves enrolment, attendance, nutrition</li>
            <li>Vitamin A prophylaxis; National Iron Plus / anaemia control; iodized salt promotion</li>
            <li>Poshan-related / state nutrition missions as taught in class (name current scheme if asked)</li>
          </ul>
          <h4>C. Community Nutrition</h4>
          <p>Application of nutrition science to improve nutritional status of the whole community through assessment, education, supplementary feeding and programme linkage.</p>
          <h4>D. Pulse Polio Programme</h4>
          <ul>
            <li>Mass immunization campaigns giving <strong>OPV</strong> to all under-5 children on National Immunization Days — regardless of prior doses</li>
            <li>Aim: eradicate poliomyelitis by interrupting transmission</li>
            <li>Nurse/ASHA: booth activity, house-to-house, finger marking, cold chain, AEFI watch</li>
          </ul>
          <h4>🩺 Nursing Role</h4>
          <p>Identify malnourished children, refer to Anganwadi/ICDS, participate in Pulse Polio and nutrition education.</p>
          <h4>✅ Conclusion</h4>
          <p>National nutrition and Pulse Polio programmes are high-yield community interventions.</p>
"""
    )

    T(
        id="t33", level="yellow", badge="badge-yellow", badge_txt="🟡 HIGH",
        cat="Foundations", title="Disease Cycle · Demography · Indicators · Healthy Individual · HFA/MDG · Scope of CHN",
        topic="disease cycle demography indicators health healthy individual promotion health for all mdg scope community health nursing",
        prob="prob-high", prob_txt="🟡 HIGH · 81% likely",
        papers="9 papers · 2022, 2019, 2016, 2015, 2014, 2013, 2011",
        marks="4–7 marks",
        years=[2022,2019,2016,2015,2014,2013,2011],
        why="Disease cycle, demography, indicators, healthy individual, promotion of health, HFA strategy, MDGs, scope of CHN appear across papers.",
        must="Disease cycle stages → demography def → health indicators → characteristics of healthy person → promotion of health → HFA/MDG points → scope of CHN",
        mistakes="Mixing endemic/epidemic with disease cycle stages. MDG vs SDG confusion — write what paper era expects; note SDGs succeeded MDGs.",
        mark_rows=[("Disease cycle / demography", "2"), ("Indicators / healthy individual", "2"), ("HFA MDG / scope", "2")],
        fast="Disease cycle: incubation→prodromal→fastigium→defervescence→convalescence (as taught). Demography=study of population. Indicators: IMR, MMR, CBR, CDR. Healthy person: physically/mentally/socially well.",
        last="DISEASE CYCLE STAGES + DEMOGRAPHY + INDICATORS + HEALTHY TRAITS + SCOPE CHN",
        eli="Disease has stages like a story. Demography counts people. Healthy person can work, play and feel well.",
        analogy="Disease cycle = weather cycle of illness; indicators = scoreboard of nation's health.",
        viva="Stages of disease cycle? | Define demography? | Name 4 health indicators?",
        draw="",
        trick='🧠 Memory: Cycle <strong>"IPFDC"</strong> Incubation Prodromal Fastigium Defervescence Convalescence | Indicators <strong>"IM-BC"</strong> IMR MMR Birth Death rates',
        answer="""
          <h4>📄 Full Exam Version — Write in Answer Sheet</h4>
          <h4>A. Disease Cycle</h4>
          <p>Stages through which a disease passes in an individual (write as taught):</p>
          <ul>
            <li><strong>Incubation period</strong> — infection to first symptom</li>
            <li><strong>Prodromal</strong> — early non-specific symptoms</li>
            <li><strong>Fastigium / illness</strong> — full disease features</li>
            <li><strong>Defervescence</strong> — decline of symptoms</li>
            <li><strong>Convalescence</strong> — recovery</li>
          </ul>
          <h4>B. Demography</h4>
          <p><strong>Demography</strong> is the scientific study of human population — size, composition, distribution, and changes (birth, death, migration).</p>
          <h4>C. Indicators of Health</h4>
          <ul>
            <li>Mortality: IMR, MMR, CDR, disease-specific death rates</li>
            <li>Morbidity: incidence, prevalence</li>
            <li>Disability rates; nutritional status; health-care utilization</li>
            <li>Socio-economic: literacy, income, sanitation coverage</li>
          </ul>
          <h4>D. Characteristics of a Healthy Individual</h4>
          <ul>
            <li>Normal growth; adequate nutrition; good posture/energy</li>
            <li>Sound mind; adjusts socially; performs daily work</li>
            <li>Resistance to common infections; personal hygiene</li>
          </ul>
          <h4>E. Promotion and Maintenance of Health</h4>
          <ul>
            <li>Health education; balanced diet; exercise; rest; hygiene</li>
            <li>Immunization; safe water/sanitation; family planning</li>
            <li>Periodic health check; healthy environment; avoid tobacco/alcohol</li>
          </ul>
          <h4>F. Indian Strategy for Health for All / MDGs (exam points)</h4>
          <ul>
            <li><strong>Health for All:</strong> Alma Ata PHC approach — equity, community participation, intersectoral coordination</li>
            <li>India: expand PHC/SC network, national health programmes, manpower (ASHA/ANM)</li>
            <li><strong>MDGs</strong> (historical exam favourite): reduce child mortality, improve maternal health, combat HIV/malaria, etc. (Succeeded by SDGs — mention if asked current)</li>
          </ul>
          <h4>G. Scope of Community Health Nursing</h4>
          <ul>
            <li>Home, school, clinic, occupational, rural/urban community</li>
            <li>MCH, family welfare, epidemiology, environmental health, HE, rehabilitation</li>
            <li>Care of individuals, families, vulnerable groups; research &amp; administration</li>
          </ul>
          <h4>✅ Conclusion</h4>
          <p>These foundation concepts explain how disease, population and nursing scope connect in CHN exams.</p>
"""
    )

    T(
        id="t34", level="yellow", badge="badge-yellow", badge_txt="🟡 HIGH",
        cat="Epidemiology & Child/Family", title="Anthropometry · Physical Examination · Calorie",
        topic="anthropometry physical examination inspection palpation percussion auscultation calorie",
        prob="prob-high", prob_txt="🟡 HIGH · 76% likely",
        papers="5 papers · 2018, 2017, 2016, 2012, 2011",
        marks="1–4 marks",
        years=[2018,2017,2016,2012,2011],
        why="Anthropometry fill/meaning, IPPA methods, and calorie definition appear in objective and short sections.",
        must="Anthropometry meaning+uses → IPPA four methods → calorie definition+energy yields",
        mistakes="Saying 1 g protein = 9 kcal (WRONG — 4). Fat = 9 kcal/g. Skipping auscultation.",
        mark_rows=[("Anthropometry", "1–2"), ("Physical exam methods", "1–2"), ("Calorie", "1")],
        fast="Anthropometry = body measurements (Ht, Wt, MUAC, HC). Exam: Inspection Palpation Percussion Auscultation. Calorie = heat/energy unit. Carb/protein 4 kcal/g; fat 9.",
        last="ANTHROPOMETRY USES + IPPA + CALORIE 4-4-9",
        eli="We measure children's height and weight to see if they grow. Doctor looks, feels, taps and listens. Calorie is energy in food.",
        analogy="IPPA = four tools like four senses for examining the body.",
        viva="What is anthropometry? | Four methods of physical examination? | Energy from 1 g fat?",
        draw="",
        trick='🧠 Memory: Exam <strong>"IPPA"</strong> | Energy <strong>"4-4-9"</strong> Carb Protein Fat',
        answer="""
          <h4>📄 Full Exam Version — Write in Answer Sheet</h4>
          <h4>A. Anthropometry</h4>
          <p><strong>Anthropometry</strong> is the measurement of the human body — height, weight, mid-upper arm circumference, head/chest circumference, skin-fold (as taught).</p>
          <ul>
            <li><strong>Uses:</strong> assess nutritional status, growth monitoring, detect PEM, evaluate programmes</li>
          </ul>
          <h4>B. Methods of Physical Examination</h4>
          <ul>
            <li><strong>Inspection:</strong> look — colour, swelling, deformities, movements</li>
            <li><strong>Palpation:</strong> feel — tenderness, masses, temperature, pulses</li>
            <li><strong>Percussion:</strong> tap — dull/resonant notes over organs</li>
            <li><strong>Auscultation:</strong> listen — heart, lungs, bowel sounds (stethoscope)</li>
          </ul>
          <h4>C. Calorie</h4>
          <p>A <strong>calorie</strong> (kilocalorie in nutrition) is a unit of heat/energy. Food energy values commonly taught:</p>
          <ul>
            <li>1 g carbohydrate → <strong>4 kcal</strong></li>
            <li>1 g protein → <strong>4 kcal</strong></li>
            <li>1 g fat → <strong>9 kcal</strong></li>
          </ul>
          <h4>🩺 Nursing Role</h4>
          <p>Measure and plot growth; use IPPA in assessment; counsel on energy needs.</p>
          <h4>✅ Conclusion</h4>
          <p>Measurement and systematic examination are basic CHN assessment skills.</p>
"""
    )

    T(
        id="t35", level="yellow", badge="badge-yellow", badge_txt="🟡 HIGH",
        cat="Environment & Nutrition & Communication", title="HE Contents/Approaches · Comm Channels · Socratic vs Didactic",
        topic="health education contents areas approaches channels components observation listening socratic didactic",
        prob="prob-high", prob_txt="🟡 HIGH · 84% likely",
        papers="8 papers · 2023, 2022, 2018, 2017, 2016, 2014, 2012, 2011",
        marks="4–7 marks",
        years=[2023,2022,2018,2017,2016,2014,2012,2011],
        why="HE contents/areas/approaches, communication channels/components, observation/listening, Socratic vs Didactic are paper favourites.",
        must="HE contents → approaches (individual/group/mass) → channels → components → observation/listening factors → Socratic vs Didactic",
        mistakes="Saying blackboard is auditory aid. Saying symposium is always two-way. Mixing didactic/socratic.",
        mark_rows=[("HE contents/approaches", "2"), ("Channels/components", "2"), ("Socratic/Didactic / listening", "1–2")],
        fast="HE areas: hygiene, nutrition, MCH, disease prevention. Approaches: individual, group, mass. Didactic=one-way lecture; Socratic=question-discussion two-way.",
        last="HE AREAS + 3 APPROACHES + CHANNELS + SOCRATIC≠DIDACTIC",
        eli="Health education teaches healthy habits. Sometimes nurse talks (lecture), sometimes asks questions so people think.",
        analogy="Didactic = radio broadcast; Socratic = WhatsApp group chat with questions.",
        viva="Approaches to HE? | Socratic vs Didactic? | Components of communication?",
        draw="",
        trick='🧠 Memory: Approaches <strong>"IGM"</strong> Individual Group Mass | Didactic=Dump info; Socratic=Spark questions',
        answer="""
          <h4>📄 Full Exam Version — Write in Answer Sheet</h4>
          <h4>A. Contents / Areas of Health Education</h4>
          <ul>
            <li>Personal hygiene; environmental sanitation</li>
            <li>Nutrition; MCH; family welfare</li>
            <li>Prevention &amp; control of communicable / non-communicable diseases</li>
            <li>Mental health; first aid; use of health services</li>
          </ul>
          <h4>B. Approaches to Health Education</h4>
          <ul>
            <li><strong>Individual:</strong> interview, counselling, home visit</li>
            <li><strong>Group:</strong> demonstration, group discussion, role play, symposium</li>
            <li><strong>Mass:</strong> TV, radio, posters, campaigns, social media</li>
          </ul>
          <h4>C. Channels &amp; Components of Communication</h4>
          <ul>
            <li><strong>Channels:</strong> face-to-face, print, audio, visual, AV, folk media</li>
            <li><strong>Components:</strong> Sender → Message → Channel → Receiver → Feedback (+ context/noise)</li>
          </ul>
          <h4>D. Factors Promoting Effective Observation &amp; Listening</h4>
          <ul>
            <li>Attention; eye contact; quiet environment</li>
            <li>Empathy; no interrupting; clarify doubts</li>
            <li>Watch non-verbal cues; take notes when needed; feedback</li>
          </ul>
          <h4>E. Socratic Method vs Didactic Method</h4>
          <ul>
            <li><strong>Didactic:</strong> one-way teaching (lecture) — teacher speaks, learners listen</li>
            <li><strong>Socratic:</strong> two-way — teaching by questions and discussion; learner thinks and responds</li>
          </ul>
          <h4>🩺 Nursing Role</h4>
          <p>Choose approach by audience; use clear channels; listen actively; prefer participatory methods when possible.</p>
          <h4>✅ Conclusion</h4>
          <p>Right content + right approach makes health education effective.</p>
"""
    )

    T(
        id="t36", level="red", badge="badge-red", badge_txt="🔴 MUST",
        cat="Foundations", title="Comparisons + ASHA + Diabetic Diet + Food Preparations",
        topic="difference health education counselling disinfection immunity hospital community asha diabetic diet poached egg tomato soup barley water egg flip koplik bitot",
        prob="prob-vhigh", prob_txt="🔴 VERY HIGH · 89% likely",
        papers="11 papers · 2025, 2024, 2023, 2022, 2019, 2018, 2015, 2014, 2012, 2011",
        marks="2–4 marks each item",
        years=[2025,2024,2023,2022,2019,2018,2015,2014,2012,2011],
        why="Differentiate questions + ASHA role + diabetic diet + food preparations + Koplik vs Bitot appear as 2–4 mark items.",
        must="Write clean comparison tables + ASHA MCH role + diabetic diet rules + 4 preparations + Koplik vs Bitot",
        mistakes="Mixing Koplik (measles) with Bitot (Vit A). Saying HE and counselling are identical.",
        mark_rows=[("Each difference", "2"), ("ASHA / diet / prep", "2–4")],
        fast="HE=group teaching; Counselling=individual decision help. Concurrent=during disease; Terminal=after. Active=vaccine; Passive=ready Abs. Koplik=measles mouth; Bitot=Vit A eye.",
        last="DIFF TABLES + ASHA MCH + DIABETIC DIET + 4 PREPS + KOPLIK/BITOT",
        eli="Exams love 'difference between'. Learn both sides in two columns.",
        analogy="Comparison answers = two pockets — left topic vs right topic.",
        viva="HE vs counselling? | Concurrent vs terminal disinfection? | Koplik vs Bitot?",
        draw="",
        trick='🧠 Memory: Koplik=<strong>Measles Mouth</strong>; Bitot=<strong>Vit A Eye</strong> | Active=Make Abs; Passive=Get Abs',
        answer="""
          <h4>📄 Full Exam Version — Write in Answer Sheet</h4>
          <h4>1. Health Education vs Counselling</h4>
          <ul>
            <li><strong>HE:</strong> often group/mass; gives information to change practices</li>
            <li><strong>Counselling:</strong> usually one-to-one; helps client take own informed decision; confidentiality central</li>
          </ul>
          <h4>2. Concurrent vs Terminal Disinfection</h4>
          <ul>
            <li><strong>Concurrent:</strong> disinfection of infective material <em>while</em> patient is still source of infection</li>
            <li><strong>Terminal:</strong> disinfection of room/articles <em>after</em> patient recovers, dies, or is transferred</li>
          </ul>
          <h4>3. Active vs Passive Immunity</h4>
          <ul>
            <li><strong>Active:</strong> body produces antibodies — vaccines / recovered disease; slower onset, longer protection</li>
            <li><strong>Passive:</strong> ready-made antibodies given (Ig, antiserum); immediate, short-lived</li>
          </ul>
          <h4>4. Hospital / Institutional Nursing vs Community Health Nursing</h4>
          <ul>
            <li><strong>Place:</strong> hospital ward vs home/school/community</li>
            <li><strong>Focus:</strong> cure of illness vs prevention + promotion + care</li>
            <li><strong>Client:</strong> individual patient vs family &amp; community</li>
            <li><strong>Environment:</strong> controlled vs variable home setting</li>
          </ul>
          <h4>5. Role of ASHA in MCH</h4>
          <ul>
            <li>Mobilize ANC/PNC; escort institutional delivery</li>
            <li>Promote breastfeeding, immunization, ORS, nutrition</li>
            <li>Home visits; identify danger signs; link to ANM/PHC</li>
            <li>Maintain village health records / participate in VHND</li>
          </ul>
          <h4>6. Diet Advice — Diabetes Mellitus</h4>
          <ul>
            <li>Regular meal timing; control calories to ideal weight</li>
            <li>High fibre complex carbs; avoid refined sugar/sweets</li>
            <li>Moderate protein; restrict excess fat/fried food</li>
            <li>Plenty of vegetables; limited fruit as advised; no alcohol</li>
          </ul>
          <h4>7. Food Preparations (exam classics)</h4>
          <ul>
            <li><strong>Poached egg:</strong> simmer water with little salt/vinegar; slide egg; cook till white sets, yolk soft; serve hot</li>
            <li><strong>Tomato soup:</strong> boil tomatoes; sieve; season; thicken lightly if needed; serve hot</li>
            <li><strong>Barley water:</strong> boil barley in water; strain; add lemon/sugar if allowed; used as demulcent fluid</li>
            <li><strong>Egg flip:</strong> beat egg with milk (+ sugar/flavour as allowed); serve as nourishing fluid diet item</li>
          </ul>
          <h4>8. Serving Food / Feeding Helpless Patient</h4>
          <ul>
            <li>Comfortable position; oral care; napkin; check temperature of food</li>
            <li>Feed slowly; small spoonfuls; allow swallowing; talk kindly</li>
            <li>Record intake; maintain dignity and hygiene</li>
          </ul>
          <h4>9. Koplik's Spot vs Bitot's Spot</h4>
          <ul>
            <li><strong>Koplik's spots:</strong> measles — white spots on buccal mucosa</li>
            <li><strong>Bitot's spots:</strong> Vitamin A deficiency — foamy spots on conjunctiva</li>
          </ul>
          <h4>✅ Conclusion</h4>
          <p>Memorize these as ready 2–4 mark blocks — they recur every few papers.</p>
"""
    )
