# ==============================================================================
# DATA CORE MATRIX: ALL_QUESTIONS
# ==============================================================================
# Master question bank for the learning/work-style profiling quiz.
# NOTE: 'vectors' are internal app weights, not a scientifically validated
# psychometric scale. Advice text intentionally avoids diagnostic/clinical
# language.
#
# ALL_QUESTIONS est une liste de 24 dictionnaires.
# ==============================================================================
# ==============================================================================
# DEV SHORTCUT (test uniquement — a retirer ou cacher avant la vraie demo jury)
# ==============================================================================
from turtle import st
            
ALL_QUESTIONS = [
    # ---------- Questions 1 à 12 ----------
    {
        "id": "q1",
        "section": "Phase 01: The Execution Engine",
        "question": "It's 11pm, you have a huge deadline in 14 days, and you're running on fumes. Be honest about the FIRST thing you actually do - not what you think you should do.",
        "options": {
            "A": {
                "text": "I open a planner and block out all 14 days hour by hour before I let myself touch the actual work.",
                "label": "THE BLUEPRINT BUILDER",
                "advice": "Building the perfect schedule feels productive and calms the panic fast - but a flawless plan with zero work done is still zero work done. This is a form of present-bias: planning feels like progress because it's easier than starting. Cap planning at 15 minutes, then force the first real block of work before the plan gets 'perfect'.",
                "vectors": {"information_bandwidth": 1.5, "execution_rigor": 2.0, "chaos_tolerance": -0.5, "cognitive_endurance": 1.5}
            },
            "B": {
                "text": "I close the laptop, tell myself '13 days is basically 14', and go do literally anything else.",
                "label": "THE DISCOUNTER",
                "advice": "This is textbook hyperbolic discounting: a reward 13 days away feels almost worthless compared to comfort right now, so your brain treats the deadline as fake until it isn't. Cramming can produce a result, but it skips the spacing effect that actually builds long-term memory. Try committing to just 10 minutes tonight, with permission to stop after - most resistance breaks in the first 5.",
                "vectors": {"information_bandwidth": 0.5, "execution_rigor": -1.0, "chaos_tolerance": 2.0, "cognitive_endurance": 0.5}
            },
            "C": {
                "text": "I spend two hours watching 'how to study effectively' videos, convinced I just haven't found the right method yet.",
                "label": "THE METHOD SHOPPER",
                "advice": "Searching for the perfect method can quietly become a socially-acceptable form of procrastination - it feels like effort, but it never touches the actual material, so it never risks being wrong. Pick literally any reasonable method in the next 5 minutes and start; you can switch tomorrow if it's bad. A mediocre method used today beats a perfect one you're still researching in three days.",
                "vectors": {"information_bandwidth": 2.0, "execution_rigor": 1.5, "chaos_tolerance": -1.5, "cognitive_endurance": 0.0}
            },
            "D": {
                "text": "I start on the deadline, get bored in 20 minutes, and end up reorganizing something completely unrelated instead.",
                "label": "THE SIDETRACK ENGINE",
                "advice": "Low-stakes, novel tasks (reorganizing, tidying, random research) release a small dopamine hit that the actual deadline can't compete with yet - it's not weak willpower, it's a stimulation mismatch. Set a 25-minute timer on the real task with the sidetrack activity as the explicit reward after, so the dopamine loop works for you instead of against you.",
                "vectors": {"information_bandwidth": 1.0, "execution_rigor": -1.5, "chaos_tolerance": 2.5, "cognitive_endurance": 1.0}
            }
        }
    },
    {
        "id": "q2",
        "section": "Category 01: Attention Architecture",
        "question": "Four hours, one dry topic, mandatory. Describe - precisely - what your attention actually does over those four hours, not what you wish it did.",
        "options": {
            "A": {
                "text": "I vanish into it for 3 hours straight and only resurface because my back is screaming or I realize I never ate lunch.",
                "label": "THE INTEROCEPTIVE BLACKOUT",
                "advice": "You can sustain deep, uninterrupted focus for hours - a genuinely rare skill - but the cost is losing track of your own body's signals (hunger, posture, fatigue) while it's happening. This isn't discipline, it's a narrowing of attentional bandwidth that crowds out interoception. Set a silent 90-minute alarm - not to stop you, just to force one body-check.",
                "vectors": {"information_bandwidth": 2.0, "execution_rigor": 1.0, "chaos_tolerance": -0.5, "cognitive_endurance": 2.0}
            },
            "B": {
                "text": "Sharp for maybe 18 minutes, then I need to get up, switch tabs, or touch something else before I can come back.",
                "label": "THE STIMULATION CYCLER",
                "advice": "Your attentional system needs a higher baseline of novelty to stay engaged - passive, unchanging input reads as 'nothing happening' to your brain and it looks elsewhere. This tracks with what attention researchers call low tonic arousal needing external stimulation to reach an optimal level. Break the topic into self-quiz sprints every 15 minutes instead of one continuous block - you're not broken, you're just running on a shorter clock.",
                "vectors": {"information_bandwidth": 0.5, "execution_rigor": -1.5, "chaos_tolerance": 2.0, "cognitive_endurance": -0.5}
            },
            "C": {
                "text": "Rock solid for 45-60 minutes, but one unexpected interruption and I basically have to restart my whole engine from zero.",
                "label": "THE PREDICTABILITY-LOCKED FOCUSER",
                "advice": "Your focus is genuinely strong - it just runs on predictability, not just willpower. An unplanned interruption doesn't just cost you the interruption's length, it resets your whole attentional state, which is disproportionate to the actual disruption. Practice absorbing tiny planned surprises (a 30-second interruption you set up yourself) to build tolerance before an exam room does it for you.",
                "vectors": {"information_bandwidth": 1.0, "execution_rigor": 2.0, "chaos_tolerance": -1.5, "cognitive_endurance": 1.5}
            },
            "D": {
                "text": "I can barely hold 5 minutes alone, but the second I'm explaining it to someone out loud, I could go for hours.",
                "label": "THE CO-REGULATED THINKER",
                "advice": "Silent solo reading probably feels close to impossible for you, and that's not a motivation problem - your attention is externally scaffolded by dialogue. Talking activates a different, more engaged processing mode than passive intake does. Stop fighting this: actively recruit a study partner or record yourself explaining the material out loud, instead of forcing solo silence that was never going to work.",
                "vectors": {"information_bandwidth": 1.5, "execution_rigor": -0.5, "chaos_tolerance": 1.5, "cognitive_endurance": 1.0}
            }
        }
    },
    {
        "id": "q3",
        "section": "Category 02: Processing Channels",
        "question": "Someone hands you a dense, abstract concept with zero real-world example attached. Before you even try to understand the CONTENT, what does your brain do with the FORM of it?",
        "options": {
            "A": {
                "text": "It instantly becomes a diagram in my head - boxes, arrows, spatial layout - before I've processed a single word of actual meaning.",
                "label": "THE SPATIAL ENCODER",
                "advice": "You're running what dual coding theory calls the visuospatial channel first - turning meaning into structure gives you a fast overview. The trap: most grading rubrics want a precise written or spoken explanation, not a diagram. After you sketch it, force a full verbal restatement with the drawing hidden - that's the version an exam will actually ask for.",
                "vectors": {"information_bandwidth": 2.0, "execution_rigor": 1.5, "chaos_tolerance": 0.0, "cognitive_endurance": 1.0}
            },
            "B": {
                "text": "It doesn't feel real until I've said it out loud, argued about it, or heard my own voice explaining the logic step by step.",
                "label": "THE VERBAL-SEQUENTIAL PROCESSOR",
                "advice": "You're running the phonological/verbal channel - a concept only 'locks in' once it's been spoken and sequenced, not just read. Silent reading is probably your least effective method, even though it's the one school assumes everyone uses. Record yourself explaining it as if to someone who knows nothing, or run an internal monologue during silent exams to simulate the process.",
                "vectors": {"information_bandwidth": 1.0, "execution_rigor": 0.5, "chaos_tolerance": 0.5, "cognitive_endurance": 1.5}
            },
            "C": {
                "text": "Nothing happens until my hands are physically doing something with it - writing it out, building a model, moving pieces around.",
                "label": "THE MANIPULATIVE ENCODER",
                "advice": "Typing or passively reading probably leaves almost no trace for you - you need motor engagement (writing by hand, building, physically testing) to convert theory into something real. Keep a physical notepad within arm's reach at all times, and shorten the gap between 'theory' and 'hands-on practice' as much as you can.",
                "vectors": {"information_bandwidth": 0.0, "execution_rigor": 1.0, "chaos_tolerance": 1.0, "cognitive_endurance": 1.0}
            },
            "D": {
                "text": "I immediately go 'oh, this is basically like [totally unrelated thing]' and understand it through that comparison instead of the actual definition.",
                "label": "THE ANALOGICAL MAPPER",
                "advice": "You default to metaphor and cross-domain pattern-matching - a fast, creative way in, but grading rubrics almost never accept 'it's kind of like X' instead of the precise expected wording. Use your analogy to build real understanding, then explicitly translate it back into the exact academic phrasing before the exam - the two steps aren't optional, they're sequential.",
                "vectors": {"information_bandwidth": 2.0, "execution_rigor": -1.5, "chaos_tolerance": 2.0, "cognitive_endurance": 0.5}
            }
        }
    },
    {
        "id": "q4",
        "section": "Category 03: Executive Regulation",
        "question": "A teacher assigns a project with genuinely no fixed criteria - no rubric, no example, no 'right shape'. There's no deadline pressure yet, just pure open-endedness. What's your gut reaction to the ambiguity itself?",
        "options": {
            "A": {
                "text": "I latch onto the very first interpretation that comes to mind and commit hard, mostly just to make the uncertainty stop.",
                "label": "THE PREMATURE CLOSER",
                "advice": "This matches what psychologists call a high need for closure - an open question feels genuinely uncomfortable, so you grab the first 'good enough' answer to end the discomfort, sometimes before better options surface. Force yourself to write down two alternative interpretations before committing to one - you don't have to pick them, just prove to yourself they existed.",
                "vectors": {"information_bandwidth": -0.5, "execution_rigor": 1.0, "chaos_tolerance": -0.5, "cognitive_endurance": 0.5}
            },
            "B": {
                "text": "I genuinely enjoy sitting with it unresolved for a while, turning it over from a few angles before committing to anything.",
                "label": "THE AMBIGUITY-TOLERANT EXPLORER",
                "advice": "You have a real capacity to tolerate an unresolved question without rushing to close it - this is a documented trait (ambiguity tolerance) that correlates with more original, better-integrated solutions. The only failure mode is letting 'exploring' quietly become 'never deciding' - give the exploration phase a hard end date, even a generous one.",
                "vectors": {"information_bandwidth": 2.0, "execution_rigor": 0.5, "chaos_tolerance": 1.5, "cognitive_endurance": 1.5}
            },
            "C": {
                "text": "I spend way more energy trying to guess what the teacher secretly wants than actually exploring what I think is interesting.",
                "label": "THE INTENT-DECODER",
                "advice": "You're solving a different problem than the one assigned: 'what will satisfy the evaluator' instead of 'what's the best answer'. That's a real skill in reading hidden expectations, but it can quietly override your own judgment before you've even tried it. When the criteria are truly open, deliberately protect 20% of the project for the version you'd build if grades didn't exist.",
                "vectors": {"information_bandwidth": 0.5, "execution_rigor": 2.0, "chaos_tolerance": -1.0, "cognitive_endurance": 1.0}
            },
            "D": {
                "text": "Total freeze. No fixed shape to react against means I genuinely don't know where to even start.",
                "label": "THE STRUCTURE-DEPENDENT STARTER",
                "advice": "Without an external structure to push against, you don't have a natural starting point - this isn't a lack of ideas, it's a missing anchor. Manufacture a fake constraint before you start (a page limit, a due-tomorrow mini-version, a random format) - an artificial rule is often enough to unlock movement when a real one isn't there.",
                "vectors": {"information_bandwidth": 1.0, "execution_rigor": 1.5, "chaos_tolerance": -2.0, "cognitive_endurance": -0.5}
            }
        }
    },
    {
        "id": "q5",
        "section": "Category 03: Executive Regulation",
        "question": "Halfway through a long paper or a complex problem, your original strategy completely falls apart. What happens in the next five minutes?",
        "options": {
            "A": {
                "text": "I feel like everything up to this point is now worthless, and I want to wipe it and start over from a totally clean plan.",
                "label": "THE RESET REFLEX",
                "advice": "Starting over feels reassuring - a clean plan promises to fix what the old one couldn't - but it usually costs more time than it saves, and it treats a partial failure as a total one. Before deleting anything, force yourself to list three things from the broken attempt that are still usable. There's almost always more salvageable material than the panic suggests.",
                "vectors": {"information_bandwidth": 1.0, "execution_rigor": 1.5, "chaos_tolerance": -1.5, "cognitive_endurance": 0.5}
            },
            "B": {
                "text": "No real panic - I just duct-tape together whatever partial logic or data I already have into something that works well enough.",
                "label": "THE IMPROVISED PATCHER",
                "advice": "You adapt under pressure without losing momentum, which is a genuinely strong trait under real deadlines. The risk is that a quick patch can hide the actual reason the original plan broke, so the same failure can quietly resurface later. Once the fire's out, spend five honest minutes diagnosing why it broke - not to redo the work, just to not repeat the mistake.",
                "vectors": {"information_bandwidth": 0.0, "execution_rigor": -1.0, "chaos_tolerance": 2.0, "cognitive_endurance": 1.0}
            },
            "C": {
                "text": "It stops feeling like a strategy problem and starts feeling like proof I'm just not smart enough for this. I need to step away.",
                "label": "THE COMPETENCE-THREAT RESPONDER",
                "advice": "A collapsed plan is landing as a verdict on your ability, not as neutral information about a strategy that didn't pan out - that's an ego-involved reading of failure, and it makes stepping away feel necessary. Try relabeling the moment out loud as 'this approach failed', not 'I failed' - the distinction sounds small but changes what you do next.",
                "vectors": {"information_bandwidth": 0.5, "execution_rigor": 1.0, "chaos_tolerance": -2.0, "cognitive_endurance": -1.0}
            },
            "D": {
                "text": "Honestly? I get a little excited - the collapse is an excuse to go try the weirder idea I was talked out of earlier.",
                "label": "THE COLLAPSE OPPORTUNIST",
                "advice": "You treat a broken plan as license to pivot toward something more original - a real form of resilience most people don't have. Just sanity-check that the new direction still answers the actual assignment; novelty only counts as a strength if it's still solving the right problem, not just a more interesting one.",
                "vectors": {"information_bandwidth": 2.0, "execution_rigor": -2.0, "chaos_tolerance": 2.5, "cognitive_endurance": 0.5}
            }
        }
    },
    {
        "id": "q6",
        "section": "Category 04: Environment & Ecosystem",
        "question": "Five straight hours in a loud, crowded study group or classroom. Walk away right now - what's your actual internal state, physically and mentally?",
        "options": {
            "A": {
                "text": "Completely wiped. I need silence and a dark, empty room immediately or I genuinely can't think straight.",
                "label": "THE HIGH-AROUSAL DRAINEE",
                "advice": "Under an arousal-based model of personality, your baseline nervous system arousal is already higher, so extra social/sensory input pushes you into overload faster than it would others - this isn't low stamina, it's a lower stimulation ceiling. Treat a quiet recovery window as a non-negotiable tool, the same way you'd treat sleep - not a nice-to-have.",
                "vectors": {"information_bandwidth": 1.5, "execution_rigor": 1.0, "chaos_tolerance": -2.0, "cognitive_endurance": -0.5}
            },
            "B": {
                "text": "Weirdly more awake than when I started - the noise and back-and-forth actually kept my brain switched on the whole time.",
                "label": "THE STIMULATION-SEEKER",
                "advice": "Under the same arousal model, your baseline sits lower - external stimulation from people and noise actually pulls you up toward your optimal focus zone instead of overwhelming it. Just make sure the group stays substantively productive, not purely social, or the same stimulation that sharpens you can just as easily distract you.",
                "vectors": {"information_bandwidth": 0.5, "execution_rigor": -0.5, "chaos_tolerance": 1.5, "cognitive_endurance": 2.0}
            },
            "C": {
                "text": "Physically fine, but genuinely annoyed if the group spent real time off-topic instead of just executing the work.",
                "label": "THE EFFICIENCY GUARDIAN",
                "advice": "You judge a shared environment almost entirely by output-per-minute, and off-topic drift registers as a real cost to you. That's a valuable discipline for group deadlines, but some genuinely useful insight comes from unstructured tangents - don't fully shut that door. If you lead groups, take the timekeeper role explicitly instead of getting quietly frustrated.",
                "vectors": {"information_bandwidth": 1.0, "execution_rigor": 2.0, "chaos_tolerance": -1.0, "cognitive_endurance": 1.0}
            },
            "D": {
                "text": "Honestly didn't clock the noise or the people at all - I was somewhere else in my head the entire five hours.",
                "label": "THE INTERNAL-FILTER OPERATOR",
                "advice": "You have an unusually strong ability to filter out ambient environment and stay locked inside your own reasoning - genuinely rare, and useful in chaotic settings. The cost is missing real-time information: an announcement, a group decision, a shift in plan. Build in a deliberate check-in every hour or so to resurface, on purpose.",
                "vectors": {"information_bandwidth": 2.0, "execution_rigor": -1.0, "chaos_tolerance": 2.0, "cognitive_endurance": 1.5}
            }
        }
    },
    {
        "id": "q7",
        "section": "Category 04: Environment & Ecosystem",
        "question": "Design your ideal academic setup with total honesty. How much outside authority do you actually want telling you what to do and when?",
        "options": {
            "A": {
                "text": "None. Give me the syllabus and the exam date, then disappear completely and let me manage every hour myself.",
                "label": "THE AUTONOMY-MAXIMIZER",
                "advice": "Self-determination theory identifies autonomy as one of three core psychological needs, and yours runs high - being micromanaged doesn't just annoy you, it actively kills your motivation. The real risk of total freedom is losing outside feedback: blind spots can build silently with no one to flag them. Deliberately seek out a mentor or peer check-in on a schedule you still control.",
                "vectors": {"information_bandwidth": 2.0, "execution_rigor": 1.0, "chaos_tolerance": 0.5, "cognitive_endurance": 2.0}
            },
            "B": {
                "text": "A lot, actually. Clear weekly deadlines and someone checking my work - without that I just drift.",
                "label": "THE STRUCTURE-DEPENDENT",
                "advice": "You perform best when the competence need from self-determination theory is met through visible, external checkpoints - structure isn't a crutch, it's literally what turns your effort on. Without those guardrails, decision fatigue eats your focus before the actual work starts. Seek structured environments, but also practice setting one small self-imposed deadline per week to slowly build the muscle.",
                "vectors": {"information_bandwidth": 0.5, "execution_rigor": 2.5, "chaos_tolerance": -1.5, "cognitive_endurance": 1.0}
            },
            "C": {
                "text": "Someone in my corner who gives real guidance when I ask for it, but otherwise lets me run my own projects.",
                "label": "THE MENTORSHIP-OPTIMIZER",
                "advice": "You're optimizing for the relatedness need - high-quality, responsive feedback from one trusted person, without the bureaucratic overhead of constant oversight. If your current environment is too institutional to offer that, actively hunt for office hours or informal mentors instead of waiting for the system to provide one.",
                "vectors": {"information_bandwidth": 1.5, "execution_rigor": 0.5, "chaos_tolerance": 1.0, "cognitive_endurance": 1.5}
            },
            "D": {
                "text": "Almost adversarial, honestly - I want to be up against elite peers in something high-stakes, not just following instructions.",
                "label": "THE COMPETITIVE-ARENA SEEKER",
                "advice": "You're substituting authority with competition as your structuring force - stakes and rivalry generate the drive that a syllabus alone can't. That produces real peak performances, but turning every learning situation into a fight to win is exhausting to sustain long-term. Reserve the competitive framing for a few genuinely high-stakes moments, not everything.",
                "vectors": {"information_bandwidth": 1.0, "execution_rigor": -0.5, "chaos_tolerance": 2.0, "cognitive_endurance": 1.0}
            }
        }
    },
    {
        "id": "q8",
        "section": "Category 04: Environment & Ecosystem",
        "question": "Blaring light, background chatter, a messy desk - nothing dramatic, just low-level sensory noise. How much of your actual processing power does that quietly eat?",
        "options": {
            "A": {
                "text": "A lot more than it should. I burn real energy just being irritated by the mess before I've done any actual work.",
                "label": "THE HIGH-SENSITIVITY FILTER",
                "advice": "This lines up with what's called sensory processing sensitivity - your nervous system processes background stimuli at nearly the same priority as the material itself, which is genuinely exhausting in chaotic spaces. This isn't a discipline gap to fix; a clean, quiet space is a real productivity tool for you, not an optional comfort.",
                "vectors": {"information_bandwidth": 1.0, "execution_rigor": 1.5, "chaos_tolerance": -2.5, "cognitive_endurance": -0.5}
            },
            "B": {
                "text": "Basically none - if anything, dead silence is worse for me than a bit of background noise or music.",
                "label": "THE BASELINE STIMULATION-SEEKER",
                "advice": "Complete silence sometimes pushes low-arousal brains to manufacture their own internal distractions just to reach an engaging stimulation level - a controlled background actually helps you stay locked in. Keep using it, just make sure the background stays constant rather than becoming novel enough to distract you itself.",
                "vectors": {"information_bandwidth": 0.0, "execution_rigor": -1.0, "chaos_tolerance": 2.0, "cognitive_endurance": 1.5}
            },
            "C": {
                "text": "I can't touch the actual work until the visual mess is gone - desk cleared, tabs closed, everything aligned first.",
                "label": "THE VISUAL-ORDER GATEKEEPER",
                "advice": "Visual clutter genuinely weighs on your working memory before you've even started - tidying isn't stalling, it's clearing real cognitive load. Just cap the reset at two minutes; past that point it can quietly become a polished way of delaying work that has nothing to do with the desk.",
                "vectors": {"information_bandwidth": 0.5, "execution_rigor": 2.0, "chaos_tolerance": -1.5, "cognitive_endurance": 0.5}
            },
            "D": {
                "text": "Zero. Once I lock onto something interesting, the physical world just stops registering entirely.",
                "label": "THE PROBLEM-LOCKED PROCESSOR",
                "advice": "Once genuinely engaged, external sensory noise fails to compete for your attention at all - a real asset in noisy or chaotic real-world settings. Just watch your physical state anyway: tuning out the room doesn't mean your body isn't quietly absorbing strain from bad posture or eye fatigue while you're locked in.",
                "vectors": {"information_bandwidth": 2.0, "execution_rigor": -0.5, "chaos_tolerance": 2.5, "cognitive_endurance": 2.0}
            }
        }
    },
    {
        "id": "q9",
        "section": "Category 05: Motivational Engine",
        "question": "It's late, nobody's checking, no grade is on the line tonight. What's the actual force still keeping you at the desk?",
        "options": {
            "A": {
                "text": "Pure curiosity about how the thing actually works underneath - the grade genuinely isn't part of the thought.",
                "label": "THE INTRINSICALLY DRIVEN",
                "advice": "This is intrinsic motivation in its clearest form - self-determination theory calls it the most durable kind of drive because it doesn't depend on anyone watching. The trap: hours can vanish into a fascinating but off-syllabus rabbit hole while the required basics wait. Remember that clearing the required work is what buys you the freedom to keep exploring what you love.",
                "vectors": {"information_bandwidth": 2.5, "execution_rigor": 0.5, "chaos_tolerance": 1.0, "cognitive_endurance": 2.0}
            },
            "B": {
                "text": "Wanting tangible proof - a rank, a score, something visible - that I'm actually at the top of this.",
                "label": "THE PERFORMANCE-ORIENTED",
                "advice": "You're running on what achievement goal theory calls performance-approach motivation: proving relative competence to others. It produces real short-term results, but tying your whole confidence to a ranking makes a bad result - or a stronger rival - hit disproportionately hard. Try building an internal bar of quality that doesn't move with the scoreboard.",
                "vectors": {"information_bandwidth": 0.5, "execution_rigor": 1.5, "chaos_tolerance": 0.5, "cognitive_endurance": 1.0}
            },
            "C": {
                "text": "If I stop, the falling-behind feeling gets loud enough that continuing is honestly the easier option.",
                "label": "THE AVOIDANCE-DRIVEN",
                "advice": "This is fear-of-falling-behind fuel - it gets real work done, but it's an expensive kind of engine to run on night after night. Try to locate one genuinely interesting angle in what you're studying, however small; a sliver of real curiosity is a far more sustainable co-pilot than avoidance alone.",
                "vectors": {"information_bandwidth": 0.0, "execution_rigor": 1.0, "chaos_tolerance": -1.0, "cognitive_endurance": 1.0}
            },
            "D": {
                "text": "Wanting to prove to MYSELF, specifically, that I can actually push past where I usually stop.",
                "label": "THE SELF-REFERENTIAL ACHIEVER",
                "advice": "You're chasing mastery relative to your own past self rather than anyone else's opinion - a healthy, sustainable form of motivation. To keep it that way, anchor it to specific, reachable targets rather than a vague, ever-rising bar; an undefined 'push past my limits' can quietly wear you down just as much as external pressure would.",
                "vectors": {"information_bandwidth": 1.0, "execution_rigor": 1.0, "chaos_tolerance": 0.0, "cognitive_endurance": 1.5}
            }
        }
    },
    {
        "id": "q10",
        "section": "Category 05: Motivational Engine",
        "question": "Two tracks on the table for next year. One is safe and near-guaranteed to go well. The other has real odds of an impressive win - or a visible failure. Which one does your gut pick before your brain gets a vote?",
        "options": {
            "A": {
                "text": "The risky one, honestly, before I've even weighed the odds properly.",
                "label": "THE APPROACH-ORIENTED RISK-TAKER",
                "advice": "Motivation research calls this approach-success orientation: the pull of a possible win outweighs the fear of visible failure for you. That pushes you toward real growth most people avoid. Just don't stack too many high-variance bets at once - mastery still needs enough focus and recovery time to actually land.",
                "vectors": {"information_bandwidth": 2.0, "execution_rigor": 1.0, "chaos_tolerance": 1.5, "cognitive_endurance": 2.0}
            },
            "B": {
                "text": "The safe one. Predictable, linear effort for a guaranteed decent outcome beats a coin flip every time for me.",
                "label": "THE FAILURE-AVOIDANT PLANNER",
                "advice": "You're running avoid-failure motivation: managing downside risk feels more urgent to you than chasing an upside. That builds a genuinely solid track record with controlled risk - a real strategic strength. Just don't let it become so consistent that you never take an uncertain shot; real growth often lives exactly where failure is possible.",
                "vectors": {"information_bandwidth": 0.5, "execution_rigor": 2.5, "chaos_tolerance": -1.5, "cognitive_endurance": 1.5}
            },
            "C": {
                "text": "Neither, really - I'd want to know which one teaches me something I can actually use immediately.",
                "label": "THE UTILITY-FIRST CHOOSER",
                "advice": "Prestige and risk don't move you much - applicability does. That's a real edge for building a usable portfolio fast, but don't shortchange the theory that doesn't look immediately useful: the strongest problem-solvers still combine solid fundamentals with hands-on execution.",
                "vectors": {"information_bandwidth": 0.0, "execution_rigor": -0.5, "chaos_tolerance": 1.5, "cognitive_endurance": 1.0}
            },
            "D": {
                "text": "I'd want to build my own third option that mixes pieces of both, honestly, rather than pick either as given.",
                "label": "THE PATH-INVENTOR",
                "advice": "You refuse the binary and look for a hybrid nobody offered - genuinely creative, and it often reveals options others miss entirely. The real risk is that an invented path is harder to prove finished; make sure it lands on one concrete result, not an open-ended pile of half-built ideas.",
                "vectors": {"information_bandwidth": 2.5, "execution_rigor": -2.0, "chaos_tolerance": 2.5, "cognitive_endurance": 0.5}
            }
        }
    },
    {
        "id": "q11",
        "section": "Phase 04: The Internal Drive",
        "question": "Drop the diplomatic answer for a second. How do you actually feel, deep down, about project leads, teachers, and anyone whose job is to evaluate you?",
        "options": {
            "A": {
                "text": "They're gatekeepers to get past. I figure out exactly what clears their checklist and optimize for that, nothing more.",
                "label": "THE STRATEGIC ADAPTOR",
                "advice": "You cleanly separate your own interest from what an evaluator wants, then optimize specifically for their checklist - a real strategic efficiency, and a form of external locus of control applied deliberately rather than by default. The risk is eventually suppressing what genuinely interests you just to clear the bar every time. Every so often, build something for you, not the grade.",
                "vectors": {"information_bandwidth": 1.0, "execution_rigor": 1.5, "chaos_tolerance": -0.5, "cognitive_endurance": 1.5}
            },
            "B": {
                "text": "Mostly background noise. I ignore whatever rules I disagree with and bet on a flashy result making them forget.",
                "label": "THE OUTCOME GAMBLER",
                "advice": "You're betting that a strong final result buys forgiveness for a broken process - sometimes true, but a real gamble if anyone actually evaluates the process too. Keep at least a minimal trail of your reasoning along the way, in case the outcome alone doesn't fully close the case.",
                "vectors": {"information_bandwidth": -0.5, "execution_rigor": -1.0, "chaos_tolerance": 2.0, "cognitive_endurance": 0.5}
            },
            "C": {
                "text": "I need their rules to actually make sense, or I will argue - genuinely, not just to be difficult.",
                "label": "THE COHERENCE ENFORCER",
                "advice": "You hold authority to a standard of internal logical consistency, and inconsistency genuinely bothers you enough to push back - a real demand for coherence, not defiance for its own sake. It does drain energy you could spend elsewhere though. Pick your battles deliberately: save the pushback for what actually matters, and let the rest go unchallenged.",
                "vectors": {"information_bandwidth": 1.5, "execution_rigor": 2.0, "chaos_tolerance": -1.5, "cognitive_endurance": 0.0}
            },
            "D": {
                "text": "I'd honestly rather they just left me alone. I don't need their approval, I just want the space to build.",
                "label": "THE VALIDATION-INDEPENDENT",
                "advice": "You don't chase outside approval, which protects your focus from other people's opinions remarkably well. The flip side is that your instincts may resist collaboration or feedback even when it would genuinely help. Every so often, force yourself to share something unfinished - not for approval, just to stay practiced at receiving input along the way, not only at the very end.",
                "vectors": {"information_bandwidth": 2.0, "execution_rigor": -2.0, "chaos_tolerance": 1.5, "cognitive_endurance": 1.0}
            }
        }
    },
    {
        "id": "q12",
        "section": "Phase 04: The Internal Drive",
        "question": "Pick the ONE evaluation format that would actually prove - to you, not to anyone else - that you're genuinely good at this.",
        "options": {
            "A": {
                "text": "A long, heavy theoretical exam with perfectly precise questions and zero ambiguity in what's being asked.",
                "label": "THE PRECISION-DEPTH PROCESSOR",
                "advice": "You want to be tested in a clean, noise-free space where deep conceptual models can actually be judged fairly - real intellectual rigor, no room for luck. The flip side is possible freezing when the real world doesn't hand you that clean a setup. Deliberately practice on fuzzy, multiple-valid-answer cases to build the flexibility a perfectly-worded exam never demands of you.",
                "vectors": {"information_bandwidth": 2.0, "execution_rigor": 1.5, "chaos_tolerance": -1.0, "cognitive_endurance": 1.5}
            },
            "B": {
                "text": "A live, timed coding or problem-solving sprint - judge my speed and how I debug under fire.",
                "label": "THE AROUSAL-OPTIMIZED PERFORMER",
                "advice": "Following the Yerkes-Dodson relationship between arousal and performance, your working memory seems to actually peak under pressure with a tight feedback loop, rather than degrade - genuinely uncommon. That mode favors speed over long-term maintainability, though. Build the habit of returning afterward to clean up whatever you built in the rush.",
                "vectors": {"information_bandwidth": -0.5, "execution_rigor": -0.5, "chaos_tolerance": 2.0, "cognitive_endurance": 1.0}
            },
            "C": {
                "text": "A massive portfolio built over months, judged on how flawlessly optimized and audited it is by the end.",
                "label": "THE LONG-HORIZON REFINER",
                "advice": "You want to prove endurance and refinement over time, not a single moment of performance - real, sustained rigor. Your actual challenge is recognizing 'good enough': without a clear stopping rule, refinement can become an endless loop that never quite ships. Set the finish line before you start, not after you feel done.",
                "vectors": {"information_bandwidth": 1.0, "execution_rigor": 2.5, "chaos_tolerance": -1.5, "cognitive_endurance": 2.5}
            },
            "D": {
                "text": "Drop me into a broken, undocumented mess with no instructions and tell me to fix it with whatever I've got.",
                "label": "THE CRISIS-CALIBRATED SOLVER",
                "advice": "You want to be judged in exactly the conditions where the rulebook has already failed - a real asset in genuine emergencies, where the usual playbook doesn't apply anyway. Outside of urgency, on routine, well-documented tasks, your focus can drop off fast. Look for small irregularities to chase even inside repetitive work, to keep some of that crisis-engagement alive.",
                "vectors": {"information_bandwidth": 1.5, "execution_rigor": -2.0, "chaos_tolerance": 2.5, "cognitive_endurance": 0.5}
            }
        }
    },

    # ---------- Questions 13 à 24 ----------
    {
        "id": "q13",
        "section": "Subsystem 04: The Internal Drive",
        "question": "You get a genuinely bad grade or review on something you poured real effort into. What's the raw, unfiltered reaction in the first 60 seconds?",
        "options": {
            "A": {
                "text": "I go straight to the exact criteria, pinpoint the specific technical flaws, and start planning the fix.",
                "label": "THE TASK-INVOLVED PROCESSOR",
                "advice": "In achievement goal theory terms, you're task-involved rather than ego-involved - feedback lands as data about the work, not a verdict on you, which is exactly what lets you improve fast. Just watch that this very analytical filter doesn't screen out qualitative or human feedback that isn't reducible to a criteria checklist.",
                "vectors": {"information_bandwidth": 1.5, "execution_rigor": 1.0, "chaos_tolerance": 0.5, "cognitive_endurance": 1.5}
            },
            "B": {
                "text": "A sharp flash of frustration, then I bury it fast by jumping straight into something completely different.",
                "label": "THE FRUSTRATION-DEFLECTOR",
                "advice": "Switching tasks protects your energy in the moment, but it also skips the reflection step that would actually prevent a repeat - the feeling gets managed, but the lesson doesn't land. Before switching, take two minutes to write down one concrete thing you're taking from the setback, even a small one.",
                "vectors": {"information_bandwidth": -0.5, "execution_rigor": -0.5, "chaos_tolerance": 1.5, "cognitive_endurance": 1.0}
            },
            "C": {
                "text": "It feels like a verdict on my actual worth, and my first instinct is to prove the reviewer flat-out wrong.",
                "label": "THE EGO-INVOLVED PROCESSOR",
                "advice": "This is ego-involvement in the classic sense: the critique of the work reads as a critique of you, which makes it hit much harder than the feedback alone warrants - a very human reaction to something you genuinely cared about. Try explicitly separating the two out loud: 'the work has a flaw' is a completely different sentence from 'I am the flaw'.",
                "vectors": {"information_bandwidth": 1.0, "execution_rigor": 2.0, "chaos_tolerance": -2.0, "cognitive_endurance": -0.5}
            },
            "D": {
                "text": "Total shrug. The grading system is arbitrary anyway, I know what I built, and their opinion doesn't move me much.",
                "label": "THE INTERNALLY-ANCHORED SHIELD",
                "advice": "Your sense of quality is anchored to your own judgment rather than an external evaluator, which protects your confidence from a single bad review - genuinely useful armor. Just keep the door open a crack: some outside feedback, even from a system you don't fully trust, occasionally points at a real blind spot worth hearing.",
                "vectors": {"information_bandwidth": 2.0, "execution_rigor": -1.5, "chaos_tolerance": 2.0, "cognitive_endurance": 0.5}
            }
        }
    },
    {
        "id": "q14",
        "section": "Subsystem 04: The Internal Drive",
        "question": "Full-blown crisis - something's broken and everyone's stressed. What's the ONE thing you bring to the table that other people in the room genuinely don't?",
        "options": {
            "A": {
                "text": "I spot the hidden pattern linking three 'unrelated' bugs before anyone else even starts tracing them individually.",
                "label": "THE PATTERN SYNTHESIZER",
                "advice": "You jump straight to the underlying structure connecting scattered symptoms, skipping a lot of the step-by-step tracing others need - real strength in fast synthesis under pressure. Keep trusting that instinct, but double-check the specific details when the stakes are genuinely high; a fast pattern-match is still a guess until verified.",
                "vectors": {"information_bandwidth": 2.5, "execution_rigor": 1.0, "chaos_tolerance": 0.0, "cognitive_endurance": 1.0}
            },
            "B": {
                "text": "I just... don't panic, while everyone around me visibly is. My head stays clear the whole time.",
                "label": "THE LOW-REACTIVITY ANCHOR",
                "advice": "You maintain a stable physiological baseline under acute stress while people around you spike - genuinely valuable on any team, since panic is contagious and calm can be too. This steadiness is a real, transferable asset worth naming explicitly on a team, not just something you quietly do.",
                "vectors": {"information_bandwidth": -0.5, "execution_rigor": 0.0, "chaos_tolerance": 2.5, "cognitive_endurance": 1.5}
            },
            "C": {
                "text": "Pure stubborn patience - I'll dig through thousands of lines of garbage code until I find the one broken thing.",
                "label": "THE SUSTAINED MICRO-AUDITOR",
                "advice": "You can hold sustained, granular attention on a tedious search far longer than most people can - real cognitive endurance under boredom, not just under excitement. That's genuinely valuable, as long as you build in forced breaks; this kind of focus can run you into the ground without you noticing until after the crisis is over.",
                "vectors": {"information_bandwidth": 0.5, "execution_rigor": 3.0, "chaos_tolerance": -1.0, "cognitive_endurance": 2.0}
            },
            "D": {
                "text": "I throw out ten weird, rule-breaking workarounds in the first five minutes, and one of them usually actually works.",
                "label": "THE LATERAL IMPROVISER",
                "advice": "You generate unconventional solutions outside the standard playbook fast - genuinely valuable creativity exactly when the standard playbook has already failed. Document the hack once the fire's out, though; a brilliant improvisation nobody can explain later just becomes next month's mystery bug.",
                "vectors": {"information_bandwidth": 2.0, "execution_rigor": -2.0, "chaos_tolerance": 2.5, "cognitive_endurance": 0.5}
            }
        }
    },
    {
        "id": "q15",
        "section": "Subsystem 04: The Internal Drive",
        "question": "You were genuinely excited about a project when it started. Now you can't make yourself touch it. What specifically killed it - not deadlines, the actual feeling?",
        "options": {
            "A": {
                "text": "The interesting part is solved. What's left is just boring cleanup and optimization, and that part never hooked me.",
                "label": "THE NOVELTY-DEPLETED MIND",
                "advice": "Your engagement was tied to discovery specifically - once the conceptual problem is solved, the competence need self-determination theory describes gets a lot less satisfying to feed through mere polishing. Try explicitly treating the finishing phase as its own skill to get good at, not a chore tacked onto the 'real' work.",
                "vectors": {"information_bandwidth": 2.0, "execution_rigor": 0.0, "chaos_tolerance": 0.5, "cognitive_endurance": -0.5}
            },
            "B": {
                "text": "It just stopped showing me progress fast enough. No visible wins for a while, and my brain checked out.",
                "label": "THE FEEDBACK-STARVED MIND",
                "advice": "Your competence need specifically runs on frequent, visible confirmation that it's working - a long stretch with no clear signal reads as failure to your system, even when real progress is happening underneath. Deliberately break long projects into small steps with a visible checkpoint each time, even on things that inherently take a while.",
                "vectors": {"information_bandwidth": -0.5, "execution_rigor": -0.5, "chaos_tolerance": 1.5, "cognitive_endurance": 0.5}
            },
            "C": {
                "text": "I made one dumb mistake early on and now the whole thing just feels tainted, even if the rest is fine.",
                "label": "THE CONTAMINATION-SENSITIVE MIND",
                "advice": "One flaw is coloring your judgment of the entire project - a genuinely high internal standard, but a costly all-or-nothing read of your own work. Try treating a project as a sum of independent parts: one flawed piece doesn't retroactively erase the value sitting in the rest of it.",
                "vectors": {"information_bandwidth": 0.5, "execution_rigor": 2.0, "chaos_tolerance": -2.0, "cognitive_endurance": 0.0}
            },
            "D": {
                "text": "Someone locked me into a rigid framework mid-project and now I'm forbidden from touching it the way I actually wanted to.",
                "label": "THE AUTONOMY-STARVED MIND",
                "advice": "Your autonomy need - the third self-determination theory pillar - is specifically what got cut off, and that alone is enough to kill motivation even when the topic itself still interests you. When a framework is genuinely imposed, look for the smallest margin you can still control (one tool, one method) - it's often enough to bring the drive back.",
                "vectors": {"information_bandwidth": 1.5, "execution_rigor": -1.5, "chaos_tolerance": 2.0, "cognitive_endurance": 0.5}
            }
        }
    },
    {
        "id": "q16",
        "section": "Subsystem 04: The Internal Drive",
        "question": "Truly boring, repetitive task ahead - manual formatting, basic testing, the stuff with zero intellectual reward. What actually happens?",
        "options": {
            "A": {
                "text": "I zone out, grit my teeth, and mechanically push through until it's over, no matter how long it takes.",
                "label": "THE VOLITIONAL SUSTAINER",
                "advice": "You can force a repetitive task to completion through raw self-regulation even with zero intrinsic reward - a real conscientiousness trait most people lack. Just check periodically whether the task could actually be automated; your endurance is valuable, and shouldn't be spent on something a script could do instead.",
                "vectors": {"information_bandwidth": 0.5, "execution_rigor": 1.5, "chaos_tolerance": -0.5, "cognitive_endurance": 2.0}
            },
            "B": {
                "text": "I rush it as fast as humanly possible, typos and sloppy mistakes included, just to get it off my plate.",
                "label": "THE LOW-TOLERANCE TRUNCATOR",
                "advice": "You have a genuinely low tolerance for boredom, so you sacrifice accuracy for speed to escape the task faster - understandable, but it quietly introduces errors that cost more time later than the rushing saved. Build in a fixed two-minute review immediately after, specifically reserved for this category of task.",
                "vectors": {"information_bandwidth": -1.0, "execution_rigor": -1.5, "chaos_tolerance": 1.5, "cognitive_endurance": 1.0}
            },
            "C": {
                "text": "I disappear for four hours building an automation script, even though doing it by hand would've taken one.",
                "label": "THE ABSTRACTION-SEEKING AUTOMATOR",
                "advice": "Faced with repetition, your instinct is to eliminate it structurally rather than tolerate it - a real engineer's reflex, and often the right long-term call. Just check honestly whether this is sometimes an elegant, technically-impressive way of avoiding a harder, less automatable task instead.",
                "vectors": {"information_bandwidth": 1.5, "execution_rigor": 2.0, "chaos_tolerance": -1.0, "cognitive_endurance": 0.5}
            },
            "D": {
                "text": "I put it off for days, and when I finally do it, careless mistakes creep in because my brain is actively resisting.",
                "label": "THE BOREDOM-INTOLERANT MIND",
                "advice": "Genuinely repetitive work triggers real disengagement for you, to the point where even careless mistakes start creeping in - your system needs stimulation to stay reliable. Try gamifying it deliberately: a timer challenge, a small self-competition, anything that reintroduces just enough novelty to hold your attention.",
                "vectors": {"information_bandwidth": 1.0, "execution_rigor": -2.0, "chaos_tolerance": 1.0, "cognitive_endurance": -1.0}
            }
        }
    },
    {
        "id": "q17",
        "section": "Subsystem 05: The Cognitive Edge",
        "question": "You hit a problem genuinely too hard for you - real effort, still stuck. What's the very first sentence that runs through your head?",
        "options": {
            "A": {
                "text": "\"I'm just not built for this kind of thing\" - like it reveals something fixed about what I'm capable of.",
                "label": "THE FIXED-ABILITY READER",
                "advice": "This is the core signature of what Carol Dweck calls a fixed mindset: difficulty is read as evidence about a stable trait ('I'm not a math person') rather than as evidence about the strategy or effort level. The strongest available reframe isn't fake positivity - it's precision: 'I can't do this YET, with the approach I've tried so far.' The word 'yet' is doing real cognitive work there, not just softening the sentence.",
                "vectors": {"information_bandwidth": 0.5, "execution_rigor": 0.5, "chaos_tolerance": -1.5, "cognitive_endurance": -0.5}
            },
            "B": {
                "text": "\"Okay, what I tried clearly isn't the right approach - what else could I try?\" - genuinely, without much emotional charge.",
                "label": "THE STRATEGY-REVISER",
                "advice": "You default to a growth-mindset read almost automatically: struggle is information about the method, not a verdict about you. This is a real, documented advantage for long-term learning - people who read difficulty this way persist longer and generalize better across new problems. Keep an eye out for the rare moment when a genuine skill gap, not just a strategy gap, actually needs outside help.",
                "vectors": {"information_bandwidth": 1.5, "execution_rigor": 1.5, "chaos_tolerance": 0.5, "cognitive_endurance": 1.5}
            },
            "C": {
                "text": "Weirdly, kind of excited - a problem that's actually hard for me feels more interesting than an easy one ever does.",
                "label": "THE DIFFICULTY-SEEKER",
                "advice": "You're drawn toward what learning researchers call desirable difficulty - a challenge that stretches you registers as engaging rather than threatening. That's a genuine long-term learning advantage. The only trap: make sure you're actually building skill on the hard problem, not just enjoying the sensation of struggling without ever resolving it.",
                "vectors": {"information_bandwidth": 2.0, "execution_rigor": 1.0, "chaos_tolerance": 1.5, "cognitive_endurance": 2.0}
            },
            "D": {
                "text": "\"This is probably a badly-designed problem\" - my brain looks to blame the problem before it looks at my approach.",
                "label": "THE EXTERNAL-ATTRIBUTION DEFAULT",
                "advice": "Your default explanation for difficulty points outward - the problem, the teacher, the material - rather than at your own strategy. This protects your confidence in the short term, but it can also quietly block the strategy-revision that would actually solve it. Before concluding the problem is broken, try explicitly listing two different approaches you haven't tried yet.",
                "vectors": {"information_bandwidth": 1.0, "execution_rigor": -1.0, "chaos_tolerance": 1.0, "cognitive_endurance": 0.0}
            }
        }
    },
    {
        "id": "q18",
        "section": "Subsystem 05: The Cognitive Edge",
        "question": "Open your actual desktop, downloads folder, and notes app right now (mentally, if not literally). What does the REAL state of it say about how you offload memory?",
        "options": {
            "A": {
                "text": "Perfectly organized folders, strict naming, sorted by year and topic - I trust the system more than my own memory.",
                "label": "THE EXTERNALIZED-MEMORY ARCHITECT",
                "advice": "You've deliberately built an external structure to carry cognitive load your working memory doesn't have to hold - genuinely smart, and it lowers day-to-day stress. Just check periodically that maintaining the system hasn't quietly become a comfortable substitute for the harder intellectual work it's supposed to support.",
                "vectors": {"information_bandwidth": 1.0, "execution_rigor": 2.0, "chaos_tolerance": -1.5, "cognitive_endurance": 1.5}
            },
            "B": {
                "text": "A chaotic downloads folder and a messy desktop - I rely completely on search to find anything, ever.",
                "label": "THE SEARCH-RELIANT MIND",
                "advice": "You skip filing overhead entirely and trust retrieval-on-demand instead - a genuine time-saver day to day, and not actually irrational given how good search has gotten. The real risk is a single critical file becoming hard to find at the exact moment it matters most. Keep one minimal backup system for anything truly important, nothing more.",
                "vectors": {"information_bandwidth": -0.5, "execution_rigor": -1.0, "chaos_tolerance": 2.0, "cognitive_endurance": 1.0}
            },
            "C": {
                "text": "A dense personal wiki of interlinked notes - my thinking basically lives as a web of connections, not a list.",
                "label": "THE NETWORKED THINKER",
                "advice": "You naturally externalize ideas as a web of connections rather than a linear list, which is a real strength for synthesis and spotting non-obvious links. Make sure, every so often, to convert that web into one concrete, finished output - the connections are valuable, but a note graph that never resolves into anything is still just notes.",
                "vectors": {"information_bandwidth": 2.0, "execution_rigor": 1.5, "chaos_tolerance": -0.5, "cognitive_endurance": 1.5}
            },
            "D": {
                "text": "Total scatter across random drives and clouds with zero system - genuinely no idea where half of it is.",
                "label": "THE PRESENT-FOCUSED MIND",
                "advice": "You're not carrying any filing overhead at all - no system to maintain means no system weighing on you day to day, and there's a real cognitive lightness in that. Set up one minimal safety net for anything that would actually hurt to lose, so you're not hunting for a critical file at the worst possible moment.",
                "vectors": {"information_bandwidth": 1.0, "execution_rigor": -2.5, "chaos_tolerance": 1.5, "cognitive_endurance": -0.5}
            }
        }
    },
    {
        "id": "q19",
        "section": "Subsystem 05: The Cognitive Edge",
        "question": "You close the laptop after a genuinely long, deep work session. For it to actually feel WORTH it, what specifically has to have happened?",
        "options": {
            "A": {
                "text": "A hard, abstract concept finally clicked and I can feel it's actually integrated into how I think now.",
                "label": "THE INSIGHT-REWARDED MIND",
                "advice": "Your reward comes from the moment of genuine conceptual integration - psychologically closer to what flow theory describes as intrinsic reward from the activity itself than from any external marker of success. Protect that curiosity deliberately, while remembering the best idea still needs to be applied somewhere to have actual impact beyond your own head.",
                "vectors": {"information_bandwidth": 2.5, "execution_rigor": 1.0, "chaos_tolerance": 0.0, "cognitive_endurance": 1.5}
            },
            "B": {
                "text": "A long list of tasks crossed off, with visible, countable proof that I moved fast.",
                "label": "THE VELOCITY-REWARDED MIND",
                "advice": "You're wired for frequent, countable progress signals - crossing items off genuinely satisfies a real psychological need for visible momentum. Just watch that chasing small, fast wins doesn't quietly pull attention away from a bigger goal that only pays off after a longer stretch with fewer checkboxes along the way.",
                "vectors": {"information_bandwidth": -0.5, "execution_rigor": 0.5, "chaos_tolerance": 1.5, "cognitive_endurance": 1.5}
            },
            "C": {
                "text": "Hours of pure, unbroken focus without breaking character once - the sheer sustained effort itself is the win.",
                "label": "THE ENDURANCE-REWARDED MIND",
                "advice": "Sustained, uninterrupted effort itself feels like the accomplishment to you, independent of what it actually produced. That's real endurance, but be careful not to confuse the physical fatigue of sitting a long time with genuine strategic output - the two don't always overlap as much as the feeling suggests.",
                "vectors": {"information_bandwidth": 0.5, "execution_rigor": 2.5, "chaos_tolerance": -1.0, "cognitive_endurance": 2.5}
            },
            "D": {
                "text": "Something concrete and functional exists now that didn't exist this morning, built entirely from scratch.",
                "label": "THE ARTIFACT-REWARDED MIND",
                "advice": "You need a tangible, functional output - not an insight, not a checklist, an actual thing - to register the session as worthwhile. That's a real drive toward usefulness. Build some patience for the less exciting maintenance work that inevitably follows creating something, since it's a genuinely different (and less satisfying) skill than building it in the first place.",
                "vectors": {"information_bandwidth": 1.5, "execution_rigor": -1.0, "chaos_tolerance": 2.0, "cognitive_endurance": 1.0}
            }
        }
    },
    {
        "id": "q20",
        "section": "Subsystem 05: The Cognitive Edge",
        "question": "High-stakes oral evaluation, real pressure. Not what you WANT to happen - what actually happens to your thinking in that room?",
        "options": {
            "A": {
                "text": "I get intensely logical and precise, but I sound noticeably colder and lose all natural warmth in how I speak.",
                "label": "THE PRESSURE-SHARPENED ANALYST",
                "advice": "Under acute pressure, your system prioritizes precision and logic and deprioritizes social warmth almost automatically - your facts stay genuinely solid, but the delivery reads as cold to an audience that's also judging tone, not just content. Deliberately script in one warm or human moment beforehand, since it won't surface on its own under pressure.",
                "vectors": {"information_bandwidth": 2.0, "execution_rigor": 1.5, "chaos_tolerance": -0.5, "cognitive_endurance": 1.0}
            },
            "B": {
                "text": "I somehow get sharper - pulling out obscure facts and quick comebacks I genuinely didn't know I had access to.",
                "label": "THE ACUTE-STRESS CATALYST",
                "advice": "Acute pressure appears to sharpen your retrieval rather than block it - you access material under stress that stays locked away when calm, a real and somewhat rare pattern. Enjoy that edge, but plan genuine recovery time afterward; this kind of spike tends to be followed by a real energy crash once the pressure lifts.",
                "vectors": {"information_bandwidth": 0.0, "execution_rigor": -0.5, "chaos_tolerance": 2.5, "cognitive_endurance": 1.5}
            },
            "C": {
                "text": "Full blank-out. My mind genuinely goes empty until the pressure passes, no matter how well I knew the material beforehand.",
                "label": "THE THREAT-FREEZE RESPONDER",
                "advice": "This is a genuine acute stress response, not a knowledge gap - when perceived threat outweighs perceived resources (Lazarus's stress appraisal model), the system can freeze regardless of preparation. A small pre-performance ritual - a specific breath pattern, silently reviewing one anchor fact - gives your system something concrete to hold onto before the freeze has a chance to take over.",
                "vectors": {"information_bandwidth": 0.5, "execution_rigor": 2.0, "chaos_tolerance": -2.5, "cognitive_endurance": -0.5}
            },
            "D": {
                "text": "I get weirdly zoomed into one tiny detail and completely lose track of the actual main point I was making.",
                "label": "THE TUNNEL-VISION RESPONDER",
                "advice": "Anxiety is narrowing your attentional field down to a single detail at the cost of the bigger structure - a documented effect of stress on attention, not a sign you didn't prepare enough. Practice deliberately pausing mid-answer to explicitly restate your main point out loud - it forces a zoom-out your stressed brain won't do on its own.",
                "vectors": {"information_bandwidth": 1.0, "execution_rigor": -1.5, "chaos_tolerance": 1.5, "cognitive_endurance": 0.5}
            }
        }
    },
    {
        "id": "q21",
        "section": "Subsystem 05: The Cognitive Edge",
        "question": "Drop the professional language completely. If your brain, while working, were an actual machine, which one is it?",
        "options": {
            "A": {
                "text": "A high-speed train locked on fixed rails - incredibly fast on the track, completely lost the second it's forced off.",
                "label": "THE SEQUENTIAL-TRACK MIND",
                "advice": "You move fast and efficiently along a clearly defined path, but the moment the path disappears, so does your momentum - this isn't fragility, it's a genuinely different processing mode than improvisation. When facing genuine uncertainty, deliberately build small intermediate checkpoints to recreate the sense of a marked path, even an artificial one.",
                "vectors": {"information_bandwidth": 1.5, "execution_rigor": 2.0, "chaos_tolerance": -1.5, "cognitive_endurance": 1.5}
            },
            "B": {
                "text": "An overclocked computer running 70 tabs at once, three of them frozen, fan screaming the whole time.",
                "label": "THE PARALLEL-PROCESS MIND",
                "advice": "You genuinely run several ideas simultaneously rather than one at a time - real capacity for complex, multi-threaded environments. Keep an eye on total load though, and batch similar tasks together deliberately; the fatigue you feel isn't from any one task, it's from the constant switching between them.",
                "vectors": {"information_bandwidth": 0.5, "execution_rigor": -1.0, "chaos_tolerance": 2.0, "cognitive_endurance": 1.0}
            },
            "C": {
                "text": "A deep-sea submarine exploring one trench for weeks straight, completely cut off from whatever's happening at the surface.",
                "label": "THE ISOLATED-DEPTH MIND",
                "advice": "You go deep into one subject at the cost of everything else happening around you - real strength in producing dense, thorough work. Set up scheduled check-ins with 'the surface' so you're not blindsided by a shifted priority or missed deadline while you were completely submerged in the depth.",
                "vectors": {"information_bandwidth": 1.0, "execution_rigor": 2.5, "chaos_tolerance": -1.0, "cognitive_endurance": 2.5}
            },
            "D": {
                "text": "A weird custom multi-tool with attachments that don't fit any standard frame but somehow solve the rare problems.",
                "label": "THE NON-STANDARD MIND",
                "advice": "You solve the problems that don't fit standard tools - a real edge specifically on edge cases most systems weren't built to handle. That talent gets even more valuable paired with solid rigor on the ordinary, common cases too - the rare wins matter less if the everyday baseline isn't solid.",
                "vectors": {"information_bandwidth": 2.0, "execution_rigor": -2.0, "chaos_tolerance": 2.5, "cognitive_endurance": 0.0}
            }
        }
    },
    {
        "id": "q22",
        "section": "Subsystem 05: The Cognitive Edge",
        "question": "Ten years from now, worst-case scenario for your actual career - not 'failure' in general, the SPECIFIC version that genuinely scares you.",
        "options": {
            "A": {
                "text": "Stuck in a routine so simple it requires no real thinking anymore, doing the same thing on repeat.",
                "label": "THE STAGNATION-AVERSE",
                "advice": "The absence of intellectual stimulation is the actual threat in your imagined future, not failure itself - a self-concept built around continuous growth. Choose environments and projects, as much as realistically possible, that guarantee some regular complexity - routine without any complexity is the specific thing your future self needs to avoid.",
                "vectors": {"information_bandwidth": 2.5, "execution_rigor": 1.0, "chaos_tolerance": 0.0, "cognitive_endurance": 1.0}
            },
            "B": {
                "text": "Slower and outperformed by people younger and faster than me who catch my mistakes before I do.",
                "label": "THE VELOCITY-ANXIOUS",
                "advice": "You've tied a big part of your self-concept to speed relative to others, and losing that edge feels like losing your whole identity in the field. Try deliberately grounding your confidence in depth of expertise too - the kind that's built slowly over years and genuinely doesn't erode the way raw speed eventually does for everyone.",
                "vectors": {"information_bandwidth": -0.5, "execution_rigor": -0.5, "chaos_tolerance": 1.5, "cognitive_endurance": 1.5}
            },
            "C": {
                "text": "Spending months building something technically flawless that literally nobody in the real world actually needed.",
                "label": "THE RELEVANCE-ANXIOUS",
                "advice": "Your fear isn't about skill, it's about wasted effort on the wrong problem - a very legitimate concern that skilled people underestimate all the time. Test ideas early and roughly with real people before polishing anything; the earlier the reality-check, the less time you risk on a beautifully built answer to a question nobody asked.",
                "vectors": {"information_bandwidth": 1.0, "execution_rigor": 2.0, "chaos_tolerance": -1.5, "cognitive_endurance": 2.0}
            },
            "D": {
                "text": "Locked into one narrow specialty for a decade, permanently losing the ability to pivot anywhere else.",
                "label": "THE CONFINEMENT-AVERSE",
                "advice": "Specialization reads to you as a trap, not an achievement - identity built on breadth rather than depth in one lane. Worth keeping in mind: genuine mastery in one area often gives you the pattern-recognition keys that make picking up other areas later far easier, not harder - depth and breadth aren't actually as opposed as the fear suggests.",
                "vectors": {"information_bandwidth": 2.0, "execution_rigor": -1.5, "chaos_tolerance": 2.0, "cognitive_endurance": 0.5}
            }
        }
    },
    {
        "id": "q23",
        "section": "Subsystem 05: The Cognitive Edge",
        "question": "The exact second a genuinely exciting project idea hits you, what does your body/hands actually do - before you've thought it through?",
        "options": {
            "A": {
                "text": "Open a blank file and start mapping out the whole architecture before I've written a single line of real code.",
                "label": "THE PLANNING-ORIENTED ACTOR",
                "advice": "In Julius Kuhl's action control theory terms, you lean planning-oriented - reducing uncertainty through structure before you commit any real energy to execution. Set a hard time cap on that design phase specifically; past a certain point, more planning stops reducing uncertainty and starts just delaying contact with reality.",
                "vectors": {"information_bandwidth": 2.0, "execution_rigor": 1.5, "chaos_tolerance": -0.5, "cognitive_endurance": 1.0}
            },
            "B": {
                "text": "Straight into the editor, hacking together something messy and half-working in the next two hours, no plan.",
                "label": "THE ACTION-ORIENTED EXECUTOR",
                "advice": "You default to action-orientation - moving directly into execution to test the idea against reality as fast as possible, a genuinely strong learning-by-doing instinct. Keep a running log of the choices you make along the way; without it, the speed that makes this mode powerful can bury you in technical debt you can't retrace later.",
                "vectors": {"information_bandwidth": -0.5, "execution_rigor": -0.5, "chaos_tolerance": 2.0, "cognitive_endurance": 1.0}
            },
            "C": {
                "text": "Search everywhere first to check if it's already been built, before letting myself get attached to the idea.",
                "label": "THE NOVELTY-VERIFIER",
                "advice": "You gate your own excitement behind an originality check - protecting yourself from investing in something that turns out to be redundant. Just watch that this check doesn't become an excuse to drop a genuinely good idea just because something loosely similar already exists; execution and angle matter as much as raw novelty.",
                "vectors": {"information_bandwidth": 1.5, "execution_rigor": 2.5, "chaos_tolerance": -1.0, "cognitive_endurance": 1.5}
            },
            "D": {
                "text": "Nothing visible at all - it just sits quietly in my head for weeks, mutating on its own before I ever mention it.",
                "label": "THE INCUBATION-ORIENTED MIND",
                "advice": "You let ideas sit in a kind of unconscious incubation period before acting - this often produces more thought-out, better-integrated projects than immediate action would. The risk is that an idea can incubate indefinitely and never actually surface. Try sharing a rough checkpoint on a deadline you set yourself, just to force the idea back into the open before it quietly dies there.",
                "vectors": {"information_bandwidth": 2.5, "execution_rigor": -2.0, "chaos_tolerance": 1.5, "cognitive_endurance": 0.0}
            }
        }
    },
    {
        "id": "q24",
        "section": "Subsystem 05: The Cognitive Edge",
        "question": "Strip it down to one single value. When you look at a piece of your own finished work, what's the ONE thing that has to be true for you to actually call it good?",
        "options": {
            "A": {
                "text": "It's clean and coherent enough that it could grow later without turning into a pile of patches.",
                "label": "THE COHERENCE PURIST",
                "advice": "Architectural elegance - a system built to last and scale cleanly - is your actual bar for quality, more than speed or completeness. Just watch that the pursuit of elegance doesn't delay delivery in situations that genuinely call for a working compromise today over a perfect structure next month.",
                "vectors": {"information_bandwidth": 2.0, "execution_rigor": 1.5, "chaos_tolerance": -0.5, "cognitive_endurance": 1.5}
            },
            "B": {
                "text": "It actually shipped, on time, and it works - full stop, everything else is secondary.",
                "label": "THE RELENTLESS SHIPPER",
                "advice": "Your bar for quality is functional and on-time delivery - genuinely the metric that matters most in fast-moving, real-world contexts. Plan regular time specifically to clean up the technical debt this priority naturally accumulates, since 'ship it' as a permanent default eventually costs you speed later, not just polish.",
                "vectors": {"information_bandwidth": -0.5, "execution_rigor": -0.5, "chaos_tolerance": 2.5, "cognitive_endurance": 1.5}
            },
            "C": {
                "text": "Every edge case I could think of has been hunted down and it runs with genuinely flawless precision.",
                "label": "THE PRECISION SENTINEL",
                "advice": "Your bar for 'good' is exhaustive correctness - hunting down every edge case is a real, uncommon commitment to quality most people don't sustain. Keep in mind that in fast-moving contexts, a working result delivered on time often beats a technically perfect one that ships too late to matter.",
                "vectors": {"information_bandwidth": 1.0, "execution_rigor": 3.0, "chaos_tolerance": -1.5, "cognitive_endurance": 2.0}
            },
            "D": {
                "text": "It does something genuinely unexpected - breaks the usual way this kind of thing gets solved.",
                "label": "THE PARADIGM DISRUPTOR",
                "advice": "Your actual bar for quality is originality - a solution that questions the standard approach entirely, not just executes it well. Genuinely valuable for innovation, but pair up with people who bring rigorous execution; bold, unconventional ideas need a partner who can turn them into something concrete and reliable, not just impressive on paper.",
                "vectors": {"information_bandwidth": 2.5, "execution_rigor": -2.5, "chaos_tolerance": 2.0, "cognitive_endurance": 0.5}
            }
        }
    }
]



with st.expander("🔧 Developer Shortcut (bypass le questionnaire pour tester)"):
    cheat_code = st.text_input("Code :", type="password", key="cheat_code_input")
    if st.button("Appliquer le profil de test"):
        if cheat_code == "XIN2":
            st.session_state.core_vectors = {
                "information_bandwidth": 2.5,
                "execution_rigor": 0.5,
                "chaos_tolerance": 1.0,
                "cognitive_endurance": 2.0,
            }
            st.session_state.flags["scan_completed"] = True
            st.session_state.flags["chatbot_unlocked"] = True
            st.session_state.current_q_idx = ALL_QUESTIONS 
            st.success("Profil THE INTRINSICALLY DRIVEN appliqué !")
            st.rerun()
        elif cheat_code:
            st.error("Code incorrect.")
