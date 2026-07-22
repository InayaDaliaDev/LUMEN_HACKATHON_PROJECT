# ==============================================================================
# DATA CORE MATRIX: ALL_QUESTIONS
# ==============================================================================
# Master question bank for the learning/work-style profiling quiz.
# NOTE: 'vectors' are internal app weights, not a scientifically validated
# psychometric scale. Advice text intentionally avoids diagnostic/clinical
# language.

ALL_QUESTIONS = [
    {
        "id": "q1",
        "section": "Phase 01: The Execution Engine",
        "question": "You’re facing an overwhelming exam or thesis deadline in 14 days. Your energy is low and the pressure is rising. What do you do?",
        "options": {
            "A": {
                "text": "I force myself to map out every single day into precise study blocks, sticking to the structure to keep my anxiety at bay.",
                "label": "ORDERLY ARCHITECT",
                "advice": "Structuring your time this tightly is a real strength, but watch the line between planning and actually learning: two hours building a perfect schedule can feel productive while your brain hasn't touched the material yet. Next time, deliberately make the plan a little messy and move faster into real practice — that's where the learning actually happens.",
                "vectors": {
                    "information_bandwidth": 1.5,
                    "execution_rigor": 2.0,
                    "chaos_tolerance": -0.5,
                    "cognitive_endurance": 1.5
                }
            },
            "B": {
                "text": "I freeze or distract myself for 12 days, relying on a brutal, adrenaline-fueled 36-hour all-nighter right before the deadline. I am a procrastinator, but I thrive under extreme pressure!",
                "label": "PRESSURE SPRINTER",
                "advice": "You can produce real focus under pressure, and that's a genuine skill. The issue isn't time management — it's starting something when success isn't guaranteed, and cramming rarely leaves anything in long-term memory. Next time, commit to just five minutes on the task with no goal of finishing it — that's usually enough to break the initial resistance.",
                "vectors": {
                    "information_bandwidth": 0.5,
                    "execution_rigor": -1.0,
                    "chaos_tolerance": 2.0,
                    "cognitive_endurance": 0.5
                }
            },
            "C": {
                "text": "I spend days obsessing over finding the 'best' study methodology, gathering endless resources, and feeling too paralyzed to actually start.",
                "label": "SYSTEMIC PERFECTIONIST",
                "advice": "Looking for the 'best' method comes from a good place, but it can quietly become a way to delay facing the material, where getting something wrong feels risky. Give yourself permission to write a rough, imperfect first attempt — a flawed method you actually use beats a perfect one you never try.",
                "vectors": {
                    "information_bandwidth": 2.0,
                    "execution_rigor": 1.5,
                    "chaos_tolerance": -1.5,
                    "cognitive_endurance": 0.0
                }
            },
            "D": {
                "text": "I jump randomly between subjects whenever I get bored, following my curiosity rather than any linear study guide.",
                "label": "CHAOS ENGINE",
                "advice": "Your brain grasps big ideas fast through novelty, but topics that need repetition lose you quickly. That's not a lack of discipline, it's a real need for stimulation. Try 25-minute timed sprints on a single subject before switching — it gives you an external constraint without having to fight the urge to jump around alone.",
                "vectors": {
                    "information_bandwidth": 1.0,
                    "execution_rigor": -1.5,
                    "chaos_tolerance": 2.5,
                    "cognitive_endurance": 1.0
                }
            }
        }
    },
    {
        "id": "q2",
        "section": "Category 01: Attention Architecture",
        "question": "You are sitting down for a mandatory 4-hour self-study session on a dry, dense topic. How does your attention span naturally unfold over time?",
        "options": {
            "A": {
                "text": "I lock in instantly for 3 hours straight, completely losing track of time, physical posture, and bodily needs until the entire module is finished.",
                "label": "HYPERFOCUS ISOLATIONIST",
                "advice": "You can go deep into a subject for hours, and that's valuable. The flip side is ignoring fatigue signals until you crash. Set an alarm every 90 minutes for a 5-minute break — not to break your focus, but to make it last.",
                "vectors": {
                    "information_bandwidth": 2.0,
                    "execution_rigor": 1.0,
                    "chaos_tolerance": -0.5,
                    "cognitive_endurance": 2.0
                }
            },
            "B": {
                "text": "My mind begins drifting after 20 minutes unless I am constantly switching tasks, pacing around the room, or playing ambient background sound.",
                "label": "STIMULUS-SEEKING EXPLORER",
                "advice": "Your attention needs movement and novelty to stay active — that's not a lack of willpower, just how you're wired. Passive reading will almost never work for you. Turn chapters into quick self-quizzes, and give yourself permission to move physically between 15-minute sprints.",
                "vectors": {
                    "information_bandwidth": 0.5,
                    "execution_rigor": -1.5,
                    "chaos_tolerance": 2.0,
                    "cognitive_endurance": -0.5
                }
            },
            "C": {
                "text": "I can comfortably sustain focus for 45 to 60 minutes at a time, but only if I have a clear syllabus and zero unexpected interruptions.",
                "label": "SYSTEMIC PLANNER",
                "advice": "You hold focus well as long as the setup is clear and predictable — that's real stability. Your weak point is the unexpected: a noise, a vague instruction, a shift in plan throws you off more than fatigue does. Prep your space in advance, but also practice absorbing a small surprise without stopping everything.",
                "vectors": {
                    "information_bandwidth": 1.0,
                    "execution_rigor": 2.0,
                    "chaos_tolerance": -1.5,
                    "cognitive_endurance": 1.5
                }
            },
            "D": {
                "text": "I struggle to focus at all in total isolation, but my attention skyrockets the moment I am discussing the material out loud or studying near others.",
                "label": "SOCIAL CATALYST",
                "advice": "You retain information better when it passes through a conversation — working alone in silence drains your motivation. That's not a weakness, your brain just processes things better out loud. Actively look for a study partner or small group instead of a quiet library corner: it will genuinely work better for you.",
                "vectors": {
                    "information_bandwidth": 1.5,
                    "execution_rigor": -0.5,
                    "chaos_tolerance": 1.5,
                    "cognitive_endurance": 1.0
                }
            }
        }
    },
    {
        "id": "q3",
        "section": "Category 02: Processing Channels",
        "question": "You are handed an abstract, theoretical concept with zero real-world examples. What is your mind's immediate translation mechanism?",
        "options": {
            "A": {
                "text": "I instantly translate the theory into visual structures—spatial diagrams, color-coded hierarchies, or mental flowcharts.",
                "label": "VISUO-SPATIAL ARCHITECT",
                "advice": "You naturally turn abstract ideas into visual structures, which gives you a fast overview. The trap: assessments usually want a precise written or spoken explanation, not a diagram. After sketching it out, force yourself to restate it in a full sentence, as if explaining it with no drawing allowed.",
                "vectors": {
                    "information_bandwidth": 2.0,
                    "execution_rigor": 1.5,
                    "chaos_tolerance": 0.0,
                    "cognitive_endurance": 1.0
                }
            },
            "B": {
                "text": "I need to talk through the logic out loud, record myself explaining it, or debate the steps sequentially until it sounds right.",
                "label": "AUDITORY SEQUENCER",
                "advice": "A concept doesn't feel real to you until you can say it out loud or debate it — silent reading is probably your worst method. Record yourself explaining it to an imaginary audience, or find a group where debate is welcome. In a silent exam, run an internal monologue that walks through the logic step by step.",
                "vectors": {
                    "information_bandwidth": 1.0,
                    "execution_rigor": 0.5,
                    "chaos_tolerance": 0.5,
                    "cognitive_endurance": 1.5
                }
            },
            "C": {
                "text": "I cannot grasp it theoretically; I have to physically write out problems by hand, manipulate tangible variables, or build a concrete model.",
                "label": "KINESTHETIC PRAGMATIST",
                "advice": "You need to physically handle things — write by hand, build, test — before an abstract idea becomes real to you. Typing or passive reading leaves little trace. Keep a physical notepad within reach, and move from theory to practice as fast as you can.",
                "vectors": {
                    "information_bandwidth": 0.0,
                    "execution_rigor": 1.0,
                    "chaos_tolerance": 1.0,
                    "cognitive_endurance": 1.0
                }
            },
            "D": {
                "text": "I look for underlying patterns and intuitive metaphors, connecting the concept to totally different fields or real-life analogies.",
                "label": "LATERAL SYNTHESIZER",
                "advice": "You connect a concept to other fields through metaphor, which gives you a fast, creative grip on it. Just remember that grading rubrics rarely accept a nice analogy instead of the exact expected definition. Use your metaphor to understand it, then still learn the precise academic wording for the exam.",
                "vectors": {
                    "information_bandwidth": 2.0,
                    "execution_rigor": -1.5,
                    "chaos_tolerance": 2.0,
                    "cognitive_endurance": 0.5
                }
            }
        }
    },
    {
        "id": "q4",
        "section": "Category 03: Executive Regulation",
        "question": "You have a major assignment due in two weeks, but the prompt is extremely vague and open-ended. What triggers your initial delay or action?",
        "options": {
            "A": {
                "text": "I delay starting because the lack of clear criteria triggers intense perfectionist anxiety—I fear wasting effort on the wrong direction.",
                "label": "PERFECTIONIST FREEZER",
                "advice": "This isn't laziness: the lack of clear criteria triggers real fear of aiming in the wrong direction, and that delays starting. Lower the stakes on purpose by giving yourself permission to write a deliberately rough first draft — its only job is to give you raw material to improve later, not to be good right away.",
                "vectors": {
                    "information_bandwidth": 1.0,
                    "execution_rigor": 2.0,
                    "chaos_tolerance": -2.0,
                    "cognitive_endurance": -0.5
                }
            },
            "B": {
                "text": "I put it off simply because it's boring, only working when the panic of an impending deadline creates enough dopamine to force action.",
                "label": "REACTIVE SPRINTER",
                "advice": "You rely on urgency to get moving, and it works short-term — but it caps how deeply you can actually learn, since solid memory isn't built in 24 hours of panic. Try setting artificial mini-deadlines with a friend or teacher well before the real one, to trigger action earlier without burning out.",
                "vectors": {
                    "information_bandwidth": -0.5,
                    "execution_rigor": -1.5,
                    "chaos_tolerance": 2.0,
                    "cognitive_endurance": 0.5
                }
            },
            "C": {
                "text": "I break the ambiguous prompt down into structured sub-tasks and create my own rigid operational framework before writing anything.",
                "label": "SYSTEMIC PLANNER",
                "advice": "You handle ambiguity well by imposing your own structure on it — a real organizational strength. The risk is spending 80% of your time polishing the plan and only 20% actually producing. Set a hard time limit on the planning phase, then move to execution even if the plan isn't perfect yet.",
                "vectors": {
                    "information_bandwidth": 1.5,
                    "execution_rigor": 2.0,
                    "chaos_tolerance": 0.0,
                    "cognitive_endurance": 1.5
                }
            },
            "D": {
                "text": "I start exploring three radically different interpretations at once, enjoying the freedom until I am forced to pick one at the last minute.",
                "label": "HYPERACTIVE EXPLORER",
                "advice": "You explore several directions at once with real creativity, which generates original ideas. The danger is spreading your time across too many paths and having to rush everything together at the end. Set an early limit on how many directions you chase in parallel (two max), to leave room to actually finish.",
                "vectors": {
                    "information_bandwidth": 2.5,
                    "execution_rigor": -2.0,
                    "chaos_tolerance": 2.5,
                    "cognitive_endurance": 0.0
                }
            }
        }
    },
    {
        "id": "q5",
        "section": "Category 03: Executive Regulation",
        "question": "Midway through solving a complex problem or writing a long paper, your initial strategy completely falls apart. How do you pivot?",
        "options": {
            "A": {
                "text": "I feel deeply demoralized, wipe the slate clean, and start from step one with a completely new methodical framework.",
                "label": "SYSTEMIC PLANNER",
                "advice": "Wiping the slate clean and starting fresh feels reassuring when a plan collapses, but it costs you real time. Try instead to spot what's still usable in your previous work — a partial failure isn't a total one.",
                "vectors": {
                    "information_bandwidth": 1.0,
                    "execution_rigor": 1.5,
                    "chaos_tolerance": -1.5,
                    "cognitive_endurance": 0.5
                }
            },
            "B": {
                "text": "I don't panic at all—I immediately patch together a quick, improvised alternative using whatever partial data or logic I have on hand.",
                "label": "EMPIRICAL PRAGMATIST",
                "advice": "You adapt well under pressure without panicking, patching together a working solution from whatever you have — a genuine strength. The flip side is that quick fixes can hide an unresolved underlying issue. Once the fire's out, take a few minutes to understand why the original plan broke, so it doesn't happen again.",
                "vectors": {
                    "information_bandwidth": 0.0,
                    "execution_rigor": -1.0,
                    "chaos_tolerance": 2.0,
                    "cognitive_endurance": 1.0
                }
            },
            "C": {
                "text": "I freeze up completely, second-guessing my baseline intelligence and needing to step away for hours before I can face the problem again.",
                "label": "PERFECTIONIST FREEZER",
                "advice": "A mistake can hit harder than expected and make you need to step back before continuing — that's a human reaction. Try treating the error as neutral information about what didn't work, rather than a verdict on your ability: that's still the fastest path to real mastery.",
                "vectors": {
                    "information_bandwidth": 0.5,
                    "execution_rigor": 1.0,
                    "chaos_tolerance": -2.0,
                    "cognitive_endurance": -1.0
                }
            },
            "D": {
                "text": "I view the failure as an exciting pivot point, using it as an excuse to take a radically creative, non-conventional detour.",
                "label": "HYPERACTIVE EXPLORER",
                "advice": "You bounce back from setbacks by exploring a completely different direction, which shows real creative resilience. Just check that the new path still answers the actual question being asked — originality only counts if it stays relevant to the assignment.",
                "vectors": {
                    "information_bandwidth": 2.0,
                    "execution_rigor": -2.0,
                    "chaos_tolerance": 2.5,
                    "cognitive_endurance": 0.5
                }
            }
        }
    },
    {
        "id": "q6",
        "section": "Category 04: Environment & Ecosystem",
        "question": "You have spent 5 consecutive hours working in a bustling study group or crowded classroom. What state is your internal system in?",
        "options": {
            "A": {
                "text": "I am completely drained and sensory-overloaded. I need immediate, silent isolation in a dark, quiet room to restore my energy.",
                "label": "DEEP FOCUS ISOLATIONIST",
                "advice": "Noise and crowding genuinely drain you — part of your brain's energy goes into filtering the environment, leaving less for actual thinking. That's not a preference to override: treat a quiet space as a real work tool, and noise-canceling headphones as worth the investment.",
                "vectors": {
                    "information_bandwidth": 1.5,
                    "execution_rigor": 1.0,
                    "chaos_tolerance": -2.0,
                    "cognitive_endurance": -0.5
                }
            },
            "B": {
                "text": "I feel highly energized and sharp—the social momentum and active exchanges kept my brain fully stimulated and awake.",
                "label": "SOCIAL CATALYST",
                "advice": "Group energy keeps you sharp and awake — it saves you from passive boredom. Just make sure those group sessions stay productive and not purely social: surround yourself with people who actually challenge you rather than distract you.",
                "vectors": {
                    "information_bandwidth": 0.5,
                    "execution_rigor": -0.5,
                    "chaos_tolerance": 1.5,
                    "cognitive_endurance": 2.0
                }
            },
            "C": {
                "text": "I feel okay physically, but mentally frustrated if the group spent time on off-topic chatter instead of strictly executing the work.",
                "label": "SYSTEMIC PLANNER",
                "advice": "You judge an environment by how efficient it is, and off-topic chatter bothers you fast. That's a valuable discipline, but don't discount unstructured discussion entirely — some of the best insights come from a tangent. If you run a group, take on the role of timekeeper to stay on track without frustration.",
                "vectors": {
                    "information_bandwidth": 1.0,
                    "execution_rigor": 2.0,
                    "chaos_tolerance": -1.0,
                    "cognitive_endurance": 1.0
                }
            },
            "D": {
                "text": "I barely noticed the people or noise at all; I was locked inside my own head playing with ideas the entire time.",
                "label": "HYPERFOCUS ISOLATIONIST",
                "advice": "You have a real internal filter that keeps you focused even in noise or chaos — a rare skill. The trade-off is missing important announcements or a group decision because you tuned the environment out completely. Build in short check-ins to reconnect with what's happening around you.",
                "vectors": {
                    "information_bandwidth": 2.0,
                    "execution_rigor": -1.0,
                    "chaos_tolerance": 2.0,
                    "cognitive_endurance": 1.5
                }
            }
        }
    },
    {
        "id": "q7",
        "section": "Category 04: Environment & Ecosystem",
        "question": "If you could design your ideal academic framework, what ratio of external authority vs. personal autonomy would you demand?",
        "options": {
            "A": {
                "text": "Complete autonomy (CNED / Independent study)—give me the full syllabus and exam dates, then leave me entirely alone to manage my time.",
                "label": "AUTONOMOUS ARCHITECT",
                "advice": "You need to control your own pace and resent being micromanaged — autonomy is what gets you moving. The risk of total freedom is the absence of outside feedback: without it, blind spots can build up without you noticing. Deliberately seek external checkpoints (a teacher, a mentor, a peer) to validate your progress now and then.",
                "vectors": {
                    "information_bandwidth": 2.0,
                    "execution_rigor": 1.0,
                    "chaos_tolerance": 0.5,
                    "cognitive_endurance": 2.0
                }
            },
            "B": {
                "text": "A structured, highly disciplined environment with clear professor expectations, weekly mandatory deadlines, and strict accountability.",
                "label": "SYSTEMIC PLANNER",
                "advice": "You perform best inside a clear framework, with explicit expectations and fixed deadlines — structure is what makes you feel safe enough to focus. Without those guardrails, open-ended freedom can lead to decision fatigue. Look for structured programs, but also practice setting your own deadlines little by little to build autonomy.",
                "vectors": {
                    "information_bandwidth": 0.5,
                    "execution_rigor": 2.5,
                    "chaos_tolerance": -1.5,
                    "cognitive_endurance": 1.0
                }
            },
            "C": {
                "text": "A mentorship-driven framework—a dedicated tutor or coach who provides high-level guidance, but lets me execute my own projects.",
                "label": "SOCIAL CATALYST",
                "advice": "You make the most progress with a mentor who guides you without locking you into rigid bureaucracy — you need quality feedback, not constant oversight. If your current setting is too institutional, actively seek out office hours or mentors who can offer that closer feedback loop.",
                "vectors": {
                    "information_bandwidth": 1.5,
                    "execution_rigor": 0.5,
                    "chaos_tolerance": 1.0,
                    "cognitive_endurance": 1.5
                }
            },
            "D": {
                "text": "A fast-paced, high-stakes competition model (Olympiads / Hackathons) where I am pushed to my limit by elite peers.",
                "label": "COMPETITIVE SPRINTER",
                "advice": "Competition and stakes push you to give your best — a slow academic pace bores you fast. That drive leads to real peak performances, but be careful not to turn every learning situation into a fight to win — it can wear you out over time.",
                "vectors": {
                    "information_bandwidth": 1.0,
                    "execution_rigor": -0.5,
                    "chaos_tolerance": 2.0,
                    "cognitive_endurance": 1.0
                }
            }
        }
    },
    {
        "id": "q8",
        "section": "Category 04: Environment & Ecosystem",
        "question": "How does your processing performance shift when you are exposed to micro-distractions (blaring light, background noise, messy desk)?",
        "options": {
            "A": {
                "text": "My performance plummets. I waste huge amounts of cognitive energy feeling irritated by the environment, making deep work impossible.",
                "label": "DEEP FOCUS ISOLATIONIST",
                "advice": "Your brain processes background noise at nearly the same priority as the material itself, which makes chaotic spaces genuinely exhausting for you. That's not a discipline problem to fix: treat a quiet, tidy space as an essential tool, not an optional comfort.",
                "vectors": {
                    "information_bandwidth": 1.0,
                    "execution_rigor": 1.5,
                    "chaos_tolerance": -2.5,
                    "cognitive_endurance": -0.5
                }
            },
            "B": {
                "text": "I actually need a baseline level of environmental activity—a coffee shop background or music—to keep my brain engaged.",
                "label": "STIMULUS-SEEKING EXPLORER",
                "advice": "Complete silence sometimes pushes you to generate your own internal distractions; a controlled background (music, café noise) actually helps you stay engaged. Keep using this, just make sure the background stays constant rather than becoming distracting itself.",
                "vectors": {
                    "information_bandwidth": 0.0,
                    "execution_rigor": -1.0,
                    "chaos_tolerance": 2.0,
                    "cognitive_endurance": 1.5
                }
            },
            "C": {
                "text": "I am bothered by visual clutter, so I must clean, organize, and align my desk completely before I can process a single page.",
                "label": "SYSTEMIC PLANNER",
                "advice": "Visual clutter really weighs on you, and tidying up helps you get started. Just watch that this reset doesn't become a polished way of delaying the real work — cap it at two minutes before you dive in.",
                "vectors": {
                    "information_bandwidth": 0.5,
                    "execution_rigor": 2.0,
                    "chaos_tolerance": -1.5,
                    "cognitive_endurance": 0.5
                }
            },
            "D": {
                "text": "I possess complete sensory immunity. Once my brain finds an interesting problem, the physical world completely fades out.",
                "label": "HYPERFOCUS ISOLATIONIST",
                "advice": "Once you're locked into an interesting problem, the outside world disappears for you — a real asset in noisy or chaotic places. Keep an eye on your physical fatigue anyway: tuning out noise doesn't mean your body isn't absorbing stress from bad posture or lighting.",
                "vectors": {
                    "information_bandwidth": 2.0,
                    "execution_rigor": -0.5,
                    "chaos_tolerance": 2.5,
                    "cognitive_endurance": 2.0
                }
            }
        }
    },
    {
        "id": "q9",
        "section": "Category 05: Motivational Engine",
        "question": "What is the primary internal engine that keeps you studying late into the night when nobody is watching?",
        "options": {
            "A": {
                "text": "Pure, unadulterated intellectual curiosity—I get obsessed with uncovering how the system works, regardless of grades.",
                "label": "INTRINSIC ARCHITECT",
                "advice": "You're driven by genuine curiosity — understanding how something works is motivation enough, grades aside. That's a real, sustainable energy. The risk is spending hours on fascinating but off-syllabus rabbit holes while neglecting the required basics. Remember that clearing the required work is what buys you the freedom to keep exploring what you actually love.",
                "vectors": {
                    "information_bandwidth": 2.5,
                    "execution_rigor": 0.5,
                    "chaos_tolerance": 1.0,
                    "cognitive_endurance": 2.0
                }
            },
            "B": {
                "text": "A relentless drive for performance, high ranking, and tangible proof that I am at the top of my field.",
                "label": "COMPETITIVE SPRINTER",
                "advice": "Ranking and recognition push you to perform, and that competitive drive gets real short-term results. Just be careful not to tie your whole confidence to a ranking or grade — a bad result or a stronger rival can hit hard. Try building an internal standard of excellence that doesn't depend on the scoreboard.",
                "vectors": {
                    "information_bandwidth": 0.5,
                    "execution_rigor": 1.5,
                    "chaos_tolerance": 0.5,
                    "cognitive_endurance": 1.0
                }
            },
            "C": {
                "text": "The intense fear of failure or falling behind.",
                "label": "ANXIETY DRIVER",
                "advice": "Working from fear of failing or falling behind gets things done, but it's a costly, hard-to-sustain kind of fuel. Try to find one thing you're genuinely curious about in what you're studying, even something small — it can gradually become a steadier engine than fear.",
                "vectors": {
                    "information_bandwidth": 0.0,
                    "execution_rigor": 1.0,
                    "chaos_tolerance": -1.0,
                    "cognitive_endurance": 1.0
                }
            },
            "D": {
                "text": "A desire to prove myself and push past my limits.",
                "label": "SELF-OVERCOMER",
                "advice": "Wanting to prove to yourself that you can push past your limits is a healthy, self-directed motivation, not dependent on anyone else's opinion. To keep it sustainable, set clear, reachable goals rather than a vague, ever-rising bar — otherwise this drive can wear you down too.",
                "vectors": {
                    "information_bandwidth": 1.0,
                    "execution_rigor": 1.0,
                    "chaos_tolerance": 0.0,
                    "cognitive_endurance": 1.5
                }
            }
        }
    },
    {
        "id": "q10",
        "section": "Category 05: Motivational Engine",
        "question": "You are given a choice between two academic tracks for the upcoming year. Which path does your brain instinctively select?",
        "options": {
            "A": {
                "text": "An ultra-challenging, elite track (e.g., Olympiad-level problems, advanced honors thesis) with a high risk of failure but massive growth.",
                "label": "INTRINSIC ARCHITECT",
                "advice": "You seek out challenge and avoid comfort zones — you'd rather struggle with something hard than coast to an easy grade. That pushes you toward real mastery. Just don't take on too many demanding commitments at once: mastery needs focus and actual recovery time.",
                "vectors": {
                    "information_bandwidth": 2.0,
                    "execution_rigor": 1.0,
                    "chaos_tolerance": 1.5,
                    "cognitive_endurance": 2.0
                }
            },
            "B": {
                "text": "A clear, well-structured, predictable track where consistent, linear effort guarantees top grades and a secure outcome.",
                "label": "SYSTEMIC PLANNER",
                "advice": "You value efficiency and predictability, building a solid track record with managed risk — a real strategic strength. Just don't play it so safe that you avoid every uncertain challenge: real growth often happens exactly where failure is possible.",
                "vectors": {
                    "information_bandwidth": 0.5,
                    "execution_rigor": 2.5,
                    "chaos_tolerance": -1.5,
                    "cognitive_endurance": 1.5
                }
            },
            "C": {
                "text": "A highly practical, fast-paced track focused on direct skill acquisition, real-world case studies, and rapid portfolio building.",
                "label": "EMPIRICAL PRAGMATIST",
                "advice": "You prefer skills you can use right away over theory for its own sake — a real edge in applied fields. Just don't shortchange the fundamentals: the strongest problem-solvers combine solid theory with practical execution.",
                "vectors": {
                    "information_bandwidth": 0.0,
                    "execution_rigor": -0.5,
                    "chaos_tolerance": 1.5,
                    "cognitive_endurance": 1.0
                }
            },
            "D": {
                "text": "A completely flexible, interdisciplinary track where I can design my own curriculum and jump between different domains freely.",
                "label": "HYPERACTIVE EXPLORER",
                "advice": "You refuse to be boxed into one lane, and you spot connections across fields that specialists miss. Your real challenge is proving depth: make sure your exploration lands on one finished, concrete result — not just a pile of scattered ideas.",
                "vectors": {
                    "information_bandwidth": 2.5,
                    "execution_rigor": -2.0,
                    "chaos_tolerance": 2.5,
                    "cognitive_endurance": 0.5
                }
            }
        }
    },
    {
        "id": "q11",
        "section": "Phase 04: The Internal Drive",
        "question": "Be honest. How do you really feel about project managers, tech leads, or professors?",
        "options": {
            "A": {
                "text": "They're just gatekeepers. I figure out exactly what they want to see and optimize my work to easily pass their checks.",
                "label": "Pragmatic System-Adaptor",
                "advice": "You separate your own motivation from what an evaluator expects, and optimize your work to clear their checks — a real strategic efficiency. The risk is eventually suppressing what genuinely interests you just to pass the bar. Every so often, allow yourself a project made for you, not for the grade.",
                "vectors": {
                    "information_bandwidth": 1.0,
                    "execution_rigor": 1.5,
                    "chaos_tolerance": -0.5,
                    "cognitive_endurance": 1.5
                }
            },
            "B": {
                "text": "I mostly ignore their rules. I bank on delivering a super flashy final demo that makes them forget I broke all their policies.",
                "label": "Reward-Driven Disruptor",
                "advice": "You count on a strong final result to make up for cutting corners along the way — it can work, but it's a real gamble if the process gets evaluated too. Document at least a minimum of your reasoning, in case the final output alone doesn't fully convince.",
                "vectors": {
                    "information_bandwidth": -0.5,
                    "execution_rigor": -1.0,
                    "chaos_tolerance": 2.0,
                    "cognitive_endurance": 0.5
                }
            },
            "C": {
                "text": "I clash with them constantly. If their rules or feedback don't make perfect logical sense, I will argue with them.",
                "label": "Coherence-Seeking Dissident",
                "advice": "You need rules and feedback to actually make logical sense, or you'll push back — a real demand for intellectual consistency. It does drain energy you could spend elsewhere though. Pick your battles: save the arguing for what really matters, and let the rest go.",
                "vectors": {
                    "information_bandwidth": 1.5,
                    "execution_rigor": 2.0,
                    "chaos_tolerance": -1.5,
                    "cognitive_endurance": 0.0
                }
            },
            "D": {
                "text": "I avoid them like the plague. I don't care about their validation; I just want them to leave me alone so I can build cool stuff.",
                "label": "Autonomous Insular Mind",
                "advice": "You'd rather be left alone to build, without chasing outside validation — that protects your focus well. The flip side is that your instincts resist collaboration or external feedback. Every so often, force yourself to share unfinished work, just to get used to feedback along the way rather than only at the end.",
                "vectors": {
                    "information_bandwidth": 2.0,
                    "execution_rigor": -2.0,
                    "chaos_tolerance": 1.5,
                    "cognitive_endurance": 1.0
                }
            }
        }
    },
    {
        "id": "q12",
        "section": "Phase 04: The Internal Drive",
        "question": "Which kind of test actually proves how smart you are?",
        "options": {
            "A": {
                "text": "A heavy, multi-stage theoretical exam that tests deep concepts with perfectly phrased, unambiguous questions.",
                "label": "Axiomatic Depth-Processor",
                "advice": "You excel at building complex mental models inside a clearly defined, noise-free space — you want real conceptual rigor. The flip side is possible freezing when reality gets messy or ambiguous. Deliberately practice on fuzzy, no-single-answer cases to build that flexibility.",
                "vectors": {
                    "information_bandwidth": 2.0,
                    "execution_rigor": 1.5,
                    "chaos_tolerance": -1.0,
                    "cognitive_endurance": 1.5
                }
            },
            "B": {
                "text": "A high-stakes live coding challenge. Judge me on my raw speed, debugging under fire, and getting it done before the buzzer.",
                "label": "High-Arousal Speed-Processor",
                "advice": "Your working memory peaks under pressure with tight feedback loops — you thrive in the moment. That mode favors speed over long-term maintainability. Get in the habit of coming back afterward to clean up what you built in a rush.",
                "vectors": {
                    "information_bandwidth": -0.5,
                    "execution_rigor": -0.5,
                    "chaos_tolerance": 2.0,
                    "cognitive_endurance": 1.0
                }
            },
            "C": {
                "text": "A massive, heavily audited portfolio built over months, showing off perfectly optimized code with zero vulnerabilities.",
                "label": "Endurance-Oriented Refiner",
                "advice": "You go the distance, refining relentlessly until it's close to perfect — real endurance. Your actual challenge is recognizing when something is 'good enough,' so you don't fall into an endless refinement loop.",
                "vectors": {
                    "information_bandwidth": 1.0,
                    "execution_rigor": 2.5,
                    "chaos_tolerance": -1.5,
                    "cognitive_endurance": 2.5
                }
            },
            "D": {
                "text": "Drop me into a broken, undocumented legacy codebase and tell me to fix a crisis using whatever unhinged methods I want.",
                "label": "Entropy-Thriving Navigator",
                "advice": "You're comfortable in the chaos of a broken, undocumented system where the usual rules no longer apply — a real asset in a crisis. Outside of urgency, on routine tasks, your focus can drop fast. Look for small irregularities or challenges inside repetitive work to keep your attention engaged.",
                "vectors": {
                    "information_bandwidth": 1.5,
                    "execution_rigor": -2.0,
                    "chaos_tolerance": 2.5,
                    "cognitive_endurance": 0.5
                }
            }
        }
    },
    {
        "id": "q13",
        "section": "Subsystem 04: The Internal Drive",
        "question": "You get a terribly low grade or review on a script you spent days refining. What is your raw, immediate reaction?",
        "options": {
            "A": {
                "text": "I immediately look at the exact grading criteria, pinpoint the specific technical flaws, and adjust my approach for the next run.",
                "label": "Analytical Telemetry-Filter",
                "advice": "You turn negative feedback into concrete technical data rather than a personal blow — a real asset for improving fast. Just watch that this very analytical process doesn't filter out qualitative or human feedback that also matters.",
                "vectors": {
                    "information_bandwidth": 1.5,
                    "execution_rigor": 1.0,
                    "chaos_tolerance": 0.5,
                    "cognitive_endurance": 1.5
                }
            },
            "B": {
                "text": "A quick flash of intense frustration, which I bury by immediately jumping into a completely different project to forget the failure.",
                "label": "Affect-Regulating Task-Switcher",
                "advice": "You handle frustration by quickly switching to a different project — it protects your energy in the moment, but it can skip real reflection on what went wrong. Before switching, take two minutes to jot down what you're taking away from that setback.",
                "vectors": {
                    "information_bandwidth": -0.5,
                    "execution_rigor": -0.5,
                    "chaos_tolerance": 1.5,
                    "cognitive_endurance": 1.0
                }
            },
            "C": {
                "text": "It feels like a devastating blow to my self-worth. I obsessively dissect my work to prove the reviewer is completely wrong.",
                "label": "Ego-Integrated Perfectionist",
                "advice": "A bad evaluation can hit you hard and make you want to prove the reviewer wrong — a very human reaction to something you put real effort into. Try to separate the critique of the work from your own worth: it's the work being judged, not you.",
                "vectors": {
                    "information_bandwidth": 1.0,
                    "execution_rigor": 2.0,
                    "chaos_tolerance": -2.0,
                    "cognitive_endurance": -0.5
                }
            },
            "D": {
                "text": "Total detachment. The grading system is arbitrary and broken anyway; I know my worth, and external opinions don't matter.",
                "label": "Self-Referential Shield",
                "advice": "You hold your course by trusting your own judgment over a grading system you see as arbitrary — that protects your creative confidence. Just be careful not to shut out outside feedback entirely: it can sometimes point to a real blind spot.",
                "vectors": {
                    "information_bandwidth": 2.0,
                    "execution_rigor": -1.5,
                    "chaos_tolerance": 2.0,
                    "cognitive_endurance": 0.5
                }
            }
        }
    },
    {
        "id": "q14",
        "section": "Subsystem 04: The Internal Drive",
        "question": "What is your biggest competitive advantage when everything goes completely wrong during an engineering crisis?",
        "options": {
            "A": {
                "text": "Instantly seeing the underlying abstract pattern that connects several seemingly unrelated bugs.",
                "label": "Top-Down Pattern Recognizer",
                "advice": "You quickly spot the link between several seemingly unrelated bugs, which lets you get to the real cause without tracing everything step by step — a real strength in synthesis. Keep trusting that instinct, while double-checking the details when the stakes are high.",
                "vectors": {
                    "information_bandwidth": 2.5,
                    "execution_rigor": 1.0,
                    "chaos_tolerance": 0.0,
                    "cognitive_endurance": 1.0
                }
            },
            "B": {
                "text": "Staying completely calm and keeping your focus when everyone else around you is panicking.",
                "label": "Low-Reactivity Operator",
                "advice": "You stay emotionally steady while everyone around you panics, which keeps your thinking clear in the middle of a crisis — a genuinely valuable trait in any team. That's a real strength worth highlighting.",
                "vectors": {
                    "information_bandwidth": -0.5,
                    "execution_rigor": 0.0,
                    "chaos_tolerance": 2.5,
                    "cognitive_endurance": 1.5
                }
            },
            "C": {
                "text": "Finding a tiny, well-hidden error deep inside thousands of lines of messy legacy code through pure stubborn focus.",
                "label": "Sustained Micro-Auditor",
                "advice": "You can track down a tiny hidden error in a massive, messy codebase with impressive patience — real sustained attention. That's a valuable skill, as long as you don't burn out on it without taking breaks.",
                "vectors": {
                    "information_bandwidth": 0.5,
                    "execution_rigor": 3.0,
                    "chaos_tolerance": -1.0,
                    "cognitive_endurance": 2.0
                }
            },
            "D": {
                "text": "Coming up with ten wild, unconventional workarounds that break the rules but somehow save the day.",
                "label": "Lateral Heuristic Explorer",
                "advice": "Facing a broken system, you quickly propose several unconventional solutions outside the standard playbook — real creativity under pressure. Just make sure to document those quick fixes once the crisis is over, so others can understand and maintain the result.",
                "vectors": {
                    "information_bandwidth": 2.0,
                    "execution_rigor": -2.0,
                    "chaos_tolerance": 2.5,
                    "cognitive_endurance": 0.5
                }
            }
        }
    },
    {
        "id": "q15",
        "section": "Subsystem 04: The Internal Drive",
        "question": "What is the main reason you suddenly lose all motivation to finish a project?",
        "options": {
            "A": {
                "text": "The interesting conceptual problems are solved, and now it's just boring optimization, tweaking, and cleanup.",
                "label": "Concept-Satiated Mind",
                "advice": "Once the interesting conceptual problem is solved, the optimizing and cleanup that's left bores you fast — your motivation comes mainly from discovery. That's normal, but try treating the finishing phase as its own skill worth building, not just a chore.",
                "vectors": {
                    "information_bandwidth": 2.0,
                    "execution_rigor": 0.0,
                    "chaos_tolerance": 0.5,
                    "cognitive_endurance": -0.5
                }
            },
            "B": {
                "text": "The feedback loops are too slow; I need to see quick results and frequent validation to stay engaged.",
                "label": "Feedback-Dependent Processor",
                "advice": "You need quick results and frequent feedback to stay engaged — a long project with a slow feedback loop can make you disengage. Deliberately break big projects into small steps with a visible result each time, even on something that takes a while overall.",
                "vectors": {
                    "information_bandwidth": -0.5,
                    "execution_rigor": -0.5,
                    "chaos_tolerance": 1.5,
                    "cognitive_endurance": 0.5
                }
            },
            "C": {
                "text": "I make one foundational mistake or fall slightly behind schedule, making the whole project feel 'ruined' in my eyes.",
                "label": "Binary Perfectionist",
                "advice": "One mistake or a small delay can make the whole project feel ruined to you — a very high standard for yourself. Try seeing a project as a sum of independent parts: one flawed piece doesn't erase the value of the rest.",
                "vectors": {
                    "information_bandwidth": 0.5,
                    "execution_rigor": 2.0,
                    "chaos_tolerance": -2.0,
                    "cognitive_endurance": 0.0
                }
            },
            "D": {
                "text": "The constraints are too rigid. I'm locked into a strict framework and forbidden from experimenting with new tools.",
                "label": "Autonomy-Seeking Mind",
                "advice": "A framework that's too rigid, with no room to experiment, kills your motivation — you need freedom to really invest yourself. When the framework is imposed, look for a small margin (a tool, a method) you can still choose yourself: it's often enough to bring the drive back.",
                "vectors": {
                    "information_bandwidth": 1.5,
                    "execution_rigor": -1.5,
                    "chaos_tolerance": 2.0,
                    "cognitive_endurance": 0.5
                }
            }
        }
    },
    {
        "id": "q16",
        "section": "Subsystem 04: The Internal Drive",
        "question": "When you have to do a highly repetitive, boring task like manual data formatting or basic testing, you:",
        "options": {
            "A": {
                "text": "Zone out, grit your teeth, and just push through the work mechanically until it is finished.",
                "label": "Volitional Task-Sustainer",
                "advice": "You can push through a repetitive, boring task by gritting your teeth to the end — real self-control. Just check now and then whether that task could actually be automated: your energy might be better spent elsewhere.",
                "vectors": {
                    "information_bandwidth": 0.5,
                    "execution_rigor": 1.5,
                    "chaos_tolerance": -0.5,
                    "cognitive_endurance": 2.0
                }
            },
            "B": {
                "text": "Rush through it as fast as possible, accepting typos and sloppy mistakes just to get it off your plate.",
                "label": "Low-Stimulation Truncator",
                "advice": "You'd rather rush through a boring task, even at the cost of some mistakes, than spend real time on it — understandable, but it can introduce quiet errors. Build in a quick 2-minute review right after, specifically for this kind of task.",
                "vectors": {
                    "information_bandwidth": -1.0,
                    "execution_rigor": -1.5,
                    "chaos_tolerance": 1.5,
                    "cognitive_endurance": 1.0
                }
            },
            "C": {
                "text": "Spend four hours writing a complex automation script, even if doing it manually would have only taken an hour.",
                "label": "Abstraction-Seeking Automator",
                "advice": "Faced with a repetitive task, you'd rather build a tool to automate it, even if it takes longer than doing it by hand — a real engineer's instinct. Just make sure this isn't sometimes an elegant way of avoiding a harder task instead.",
                "vectors": {
                    "information_bandwidth": 1.5,
                    "execution_rigor": 2.0,
                    "chaos_tolerance": -1.0,
                    "cognitive_endurance": 0.5
                }
            },
            "D": {
                "text": "Procrastinate endlessly and make careless mistakes because your brain absolutely rebels against boring work.",
                "label": "Novelty-Gated Focus",
                "advice": "Repetitive work really makes you check out, to the point of careless mistakes — your brain needs novelty to stay engaged. Try turning the task into a small game or a timed challenge, just enough to add a bit of stimulation.",
                "vectors": {
                    "information_bandwidth": 1.0,
                    "execution_rigor": -2.0,
                    "chaos_tolerance": 1.0,
                    "cognitive_endurance": -1.0
                }
            }
        }
    },
    {
        "id": "q17",
        "section": "Subsystem 04: The Internal Drive",
        "question": "An assignment is completely open-ended ('Build whatever you want as long as it solves the problem'). Your immediate reflex is:",
        "options": {
            "A": {
                "text": "Anxious paralysis. You spend days trying to design the perfect scope and system boundaries before writing any code.",
                "label": "Unbounded-Scope Deliberator",
                "advice": "A completely open-ended assignment can freeze you: without clear limits, you spend a lot of time trying to define the perfect scope before starting. Set a hard time limit on that planning stage, then start even if the scope isn't 100% locked down.",
                "vectors": {
                    "information_bandwidth": 1.5,
                    "execution_rigor": 1.5,
                    "chaos_tolerance": -1.0,
                    "cognitive_endurance": 0.5
                }
            },
            "B": {
                "text": "Immediate action. You pick the very first idea that crosses your mind and start building it without weighing options.",
                "label": "Choice-Reduction Executer",
                "advice": "Given total freedom, you quickly pick the first idea that comes to mind and get moving — that avoids paralysis and builds momentum. Just take ten minutes before diving in to check that this first idea actually answers the real question.",
                "vectors": {
                    "information_bandwidth": -0.5,
                    "execution_rigor": -0.5,
                    "chaos_tolerance": 1.5,
                    "cognitive_endurance": 1.0
                }
            },
            "C": {
                "text": "Over-analyzing the grader. You try to reverse-engineer what the evaluator secretly wants so you can perfectly match their hidden criteria.",
                "label": "Intent-Decoding Mind",
                "advice": "You spend time trying to guess what the evaluator really wants behind a vague prompt — a real analytical skill. Just watch that this search for the 'hidden right answer' doesn't stop you from exploring an idea you actually care about.",
                "vectors": {
                    "information_bandwidth": 0.5,
                    "execution_rigor": 2.5,
                    "chaos_tolerance": -1.0,
                    "cognitive_endurance": 1.0
                }
            },
            "D": {
                "text": "Total creative freedom. You brainstorm dozens of wild paths and pick the most unconventional tools just to experiment.",
                "label": "Divergent Mind-Explorer",
                "advice": "An open prompt genuinely energizes you and you explore plenty of original directions. The risk is spreading yourself too thin and over-complicating the project. Once you've picked an idea, set a clear scope so the project doesn't keep expanding endlessly.",
                "vectors": {
                    "information_bandwidth": 2.5,
                    "execution_rigor": -2.0,
                    "chaos_tolerance": 2.5,
                    "cognitive_endurance": 0.0
                }
            }
        }
    },
    {
        "id": "q18",
        "section": "Subsystem 05: The Cognitive Edge",
        "question": "Look at your personal files, desktop, and note-taking apps. What does your organization actually look like?",
        "options": {
            "A": {
                "text": "Perfect, highly organized folders sorted by year, topic, and priority, using strict naming rules.",
                "label": "The Structural Shield",
                "advice": "Perfectly organized folders give you real mental clarity and lower your day-to-day stress. Just check that this tidying doesn't become, over time, a comfortable way to avoid harder intellectual work.",
                "vectors": {
                    "information_bandwidth": 1.0,
                    "execution_rigor": 2.0,
                    "chaos_tolerance": -1.5,
                    "cognitive_endurance": 1.5
                }
            },
            "B": {
                "text": "A massive, chaotic 'Downloads' folder and a messy desktop. You rely entirely on the search bar to find anything.",
                "label": "The Fluid Searcher",
                "advice": "You move fast without spending time filing things, trusting the search bar to find anything — a real time-saver day to day. Still, keep a minimal backup or structure so you're not stuck if an important file becomes hard to find right when it matters.",
                "vectors": {
                    "information_bandwidth": -0.5,
                    "execution_rigor": -1.0,
                    "chaos_tolerance": 2.0,
                    "cognitive_endurance": 1.0
                }
            },
            "C": {
                "text": "A highly detailed personal wiki or Obsidian vault filled with interconnected notes and clean markdown syntax.",
                "label": "The Conceptual Weaver",
                "advice": "You naturally think in webs of connected ideas rather than lists — a real strength in synthesis. Make sure now and then to turn those connections into an actual concrete output, not just notes that keep piling up.",
                "vectors": {
                    "information_bandwidth": 2.0,
                    "execution_rigor": 1.5,
                    "chaos_tolerance": -0.5,
                    "cognitive_endurance": 1.5
                }
            },
            "D": {
                "text": "A total digital wasteland. Files are scattered randomly across different drives, clouds, and desktops with zero system.",
                "label": "The Pure Present",
                "advice": "Your files are scattered around with no real system — you live in the present, with no filing overhead weighing on you. Set up a minimal safety net, so you don't lose valuable time hunting for an important file right when you're under pressure.",
                "vectors": {
                    "information_bandwidth": 1.0,
                    "execution_rigor": -2.5,
                    "chaos_tolerance": 1.5,
                    "cognitive_endurance": -0.5
                }
            }
        }
    },
    {
        "id": "q19",
        "section": "Subsystem 05: The Cognitive Edge",
        "question": "What do you actually need to feel truly satisfied at the end of a long, deep work session?",
        "options": {
            "A": {
                "text": "Finally clicking with a highly complex, abstract concept and integrating it into how you see things.",
                "label": "The Epiphany Junkie",
                "advice": "What genuinely satisfies you is the click of finally understanding a complex idea — your reward is mostly intellectual. Protect that curiosity, while remembering that even the best idea needs to be put into practice to have real impact.",
                "vectors": {
                    "information_bandwidth": 2.5,
                    "execution_rigor": 1.0,
                    "chaos_tolerance": 0.0,
                    "cognitive_endurance": 1.5
                }
            },
            "B": {
                "text": "Crossing off 15 different tasks from your to-do list, seeing clear, rapid progress.",
                "label": "The Velocity Engine",
                "advice": "Seeing a long list of tasks checked off gives you a real sense of fast, visible progress. Just watch that these small wins don't pull your attention away from a bigger goal that takes longer to reach.",
                "vectors": {
                    "information_bandwidth": -0.5,
                    "execution_rigor": 0.5,
                    "chaos_tolerance": 1.5,
                    "cognitive_endurance": 1.5
                }
            },
            "C": {
                "text": "Spending 8 hours of pure, uninterrupted focus at your desk without breaking character or wasting a single minute.",
                "label": "The Endurance Monotrope",
                "advice": "Staying focused for hours without a break gives you a real sense of accomplishment through sheer effort. Just be careful not to confuse the physical exhaustion of sitting a long time with actual strategic productivity.",
                "vectors": {
                    "information_bandwidth": 0.5,
                    "execution_rigor": 2.5,
                    "chaos_tolerance": -1.0,
                    "cognitive_endurance": 2.5
                }
            },
            "D": {
                "text": "Building a concrete, functional tool or standalone module completely from scratch.",
                "label": "The Artifact Creator",
                "advice": "Building something concrete and functional from scratch gives you a real sense of tangible usefulness. Build some patience too for the less exciting maintenance and fixing that comes with the same work.",
                "vectors": {
                    "information_bandwidth": 1.5,
                    "execution_rigor": -1.0,
                    "chaos_tolerance": 2.0,
                    "cognitive_endurance": 1.0
                }
            }
        }
    },
    {
        "id": "q20",
        "section": "Subsystem 05: The Cognitive Edge",
        "question": "During a high-stakes, high-pressure presentation or oral evaluation, how does your brain handle the stress?",
        "options": {
            "A": {
                "text": "You become intensely logical and structured. You recall facts perfectly but sound cold and lose all conversational warmth.",
                "label": "The Ice-Cold Logic",
                "advice": "Under the pressure of an oral evaluation, you get very logical and structured, even if it comes across as cold and less warm. Your facts stay solid, but try to deliberately add a bit of warmth so you don't lose your audience.",
                "vectors": {
                    "information_bandwidth": 2.0,
                    "execution_rigor": 1.5,
                    "chaos_tolerance": -0.5,
                    "cognitive_endurance": 1.0
                }
            },
            "B": {
                "text": "Your mind sharpens aggressively. You retrieve obscure facts and make brilliant, quick comebacks you didn't know you had in you.",
                "label": "The Crisis Catalyst",
                "advice": "Acute pressure sharpens you rather than blocking you: you find answers and ideas you didn't know you had. Enjoy that energy, but plan real recovery time afterward to avoid exhaustion once the pressure lifts.",
                "vectors": {
                    "information_bandwidth": 0.0,
                    "execution_rigor": -0.5,
                    "chaos_tolerance": 2.5,
                    "cognitive_endurance": 1.5
                }
            },
            "C": {
                "text": "You blank out completely under pressure, getting stuck in a mental freeze until the stressful situation is over.",
                "label": "The Overload Freeze",
                "advice": "Intense stress can freeze you completely until the situation passes — a common reaction to high stakes, not a lack of skill. Build a small pre-performance ritual (breathing, reviewing one key point) to give yourself an anchor before it starts.",
                "vectors": {
                    "information_bandwidth": 0.5,
                    "execution_rigor": 2.0,
                    "chaos_tolerance": -2.5,
                    "cognitive_endurance": -0.5
                }
            },
            "D": {
                "text": "You get intense tunnel vision, hyper-focusing on one tiny detail while completely losing track of your main point.",
                "label": "The Micro-Lock",
                "advice": "Anxiety sometimes makes you zoom in on one detail and lose sight of your main point. Practice deliberately pausing now and then to reconnect with the bigger picture of what you're saying.",
                "vectors": {
                    "information_bandwidth": 1.0,
                    "execution_rigor": -1.5,
                    "chaos_tolerance": 1.5,
                    "cognitive_endurance": 0.5
                }
            }
        }
    },
    {
        "id": "q21",
        "section": "Subsystem 05: The Cognitive Edge",
        "question": "Strip away all professional buzzwords. How does your brain actually function when you are working?",
        "options": {
            "A": {
                "text": "A high-speed train locked onto fixed rails. Incredibly fast and efficient, but completely lost if forced off the tracks.",
                "label": "The Sequential Train",
                "advice": "You move fast and efficiently along a well-defined path, but can feel lost the moment you're pushed off it. When facing an unclear or uncertain area, deliberately build small intermediate steps to recreate a sense of a marked path.",
                "vectors": {
                    "information_bandwidth": 1.5,
                    "execution_rigor": 2.0,
                    "chaos_tolerance": -1.5,
                    "cognitive_endurance": 1.5
                }
            },
            "B": {
                "text": "An overclocked computer with 70 open browser tabs, where three are frozen and the fan is screaming.",
                "label": "The Concurrent Overclocker",
                "advice": "You run several ideas in parallel in your head, which lets you handle complex environments. Watch your mental load, and batch similar tasks together to limit the fatigue that comes from switching context too often.",
                "vectors": {
                    "information_bandwidth": 0.5,
                    "execution_rigor": -1.0,
                    "chaos_tolerance": 2.0,
                    "cognitive_endurance": 1.0
                }
            },
            "C": {
                "text": "A deep-sea submarine exploring a single trench for weeks, completely cut off from the surface weather.",
                "label": "The Deep Trench Diver",
                "advice": "You go deep into one subject, cut off from everything else, to produce dense work — a real strength in concentration. Set up regular check-ins with the outside world so you're not caught off guard if priorities shift while you're deep in it.",
                "vectors": {
                    "information_bandwidth": 1.0,
                    "execution_rigor": 2.5,
                    "chaos_tolerance": -1.0,
                    "cognitive_endurance": 2.5
                }
            },
            "D": {
                "text": "A customized multi-tool with a few bizarre attachments that don't fit the standard frame but solve weird, rare problems.",
                "label": "The Edge-Case Alchemist",
                "advice": "You use unconventional methods to solve rare problems that standard approaches don't cover — a real edge on edge cases. That talent is even more valuable paired with solid rigor on the more standard cases too.",
                "vectors": {
                    "information_bandwidth": 2.0,
                    "execution_rigor": -2.0,
                    "chaos_tolerance": 2.5,
                    "cognitive_endurance": 0.0
                }
            }
        }
    },
    {
        "id": "q22",
        "section": "Subsystem 05: The Cognitive Edge",
        "question": "What is your absolute deepest fear regarding your long-term academic or career path?",
        "options": {
            "A": {
                "text": "Getting stuck in a mind-numbing routine, working on simple, repetitive projects that require no deep architectural thinking.",
                "label": "The Stagnation Phobia",
                "advice": "Your biggest fear is getting stuck in a routine with no real intellectual stimulation. Choose, as much as you can, projects and environments that guarantee some regular complexity and novelty.",
                "vectors": {
                    "information_bandwidth": 2.5,
                    "execution_rigor": 1.0,
                    "chaos_tolerance": 0.0,
                    "cognitive_endurance": 1.0
                }
            },
            "B": {
                "text": "Slowing down, losing your execution speed, and getting outperformed by younger, faster peers who spot your mistakes.",
                "label": "The Velocity Anxiety",
                "advice": "You measure your worth by how fast you move, and the idea of slowing down worries you. Try grounding your confidence in deep expertise too — the kind that's built over time and doesn't depend on speed alone.",
                "vectors": {
                    "information_bandwidth": -0.5,
                    "execution_rigor": -0.5,
                    "chaos_tolerance": 1.5,
                    "cognitive_endurance": 1.5
                }
            },
            "C": {
                "text": "Realizing after months of intense development that your polished, flawless creation solves a problem that absolutely nobody in the real world cares about.",
                "label": "The Phantom Effort Dread",
                "advice": "You worry about pouring a lot of energy into a technically flawless project that, in the end, answers no real need. Test your ideas early, even roughly, with real people before polishing further.",
                "vectors": {
                    "information_bandwidth": 1.0,
                    "execution_rigor": 2.0,
                    "chaos_tolerance": -1.5,
                    "cognitive_endurance": 2.0
                }
            },
            "D": {
                "text": "Being locked into a single narrow specialization for a decade, permanently losing the ability to pivot to other fields.",
                "label": "The Confinement Panic",
                "advice": "The idea of specializing in one field for a long time feels more like a trap than an expertise to you. Keep in mind that real mastery in one area often gives you the keys to understand other areas more easily later.",
                "vectors": {
                    "information_bandwidth": 2.0,
                    "execution_rigor": -1.5,
                    "chaos_tolerance": 2.0,
                    "cognitive_endurance": 0.5
                }
            }
        }
    },
    {
        "id": "q23",
        "section": "Subsystem 05: The Cognitive Edge",
        "question": "The exact moment a brilliant new project idea pops into your head, your immediate instinct is to:",
        "options": {
            "A": {
                "text": "Open a blank file and immediately map out the entire system architecture, database schema, and flowcharts.",
                "label": "The Upfront Architect",
                "advice": "Faced with a new idea, your instinct is to map out the whole system before writing any code — that reduces your uncertainty. Set a hard time limit on that design phase, so you don't wear yourself out before ever testing it against reality.",
                "vectors": {
                    "information_bandwidth": 2.0,
                    "execution_rigor": 1.5,
                    "chaos_tolerance": -0.5,
                    "cognitive_endurance": 1.0
                }
            },
            "B": {
                "text": "Open your code editor and hack together a messy, raw prototype in two hours just to see it work.",
                "label": "The Empirical Hacker",
                "advice": "You'd rather hack together a working prototype in a couple of hours to see if the idea holds up — a real learning-by-doing instinct. Keep a running note of your design choices along the way, so you don't get lost in technical debt later.",
                "vectors": {
                    "information_bandwidth": -0.5,
                    "execution_rigor": -0.5,
                    "chaos_tolerance": 2.0,
                    "cognitive_endurance": 1.0
                }
            },
            "C": {
                "text": "Search GitHub and research indices immediately to see if anyone else has already built it, ensuring it's completely original.",
                "label": "The Novelty Guard",
                "advice": "Before diving in, you check whether the idea already exists elsewhere, to make sure it's genuinely original. Just watch that this check doesn't become an excuse to drop an idea simply because something similar already exists.",
                "vectors": {
                    "information_bandwidth": 1.5,
                    "execution_rigor": 2.5,
                    "chaos_tolerance": -1.0,
                    "cognitive_endurance": 1.5
                }
            },
            "D": {
                "text": "Keep the idea completely inside your head for weeks, letting it mix and mutate with other random thoughts before sharing it.",
                "label": "The Silent Incubator",
                "advice": "You let an idea sit quietly for a while before sharing it, which often leads to more thought-out projects. Still, try sharing a checkpoint now and then, to keep your momentum and get outside feedback.",
                "vectors": {
                    "information_bandwidth": 2.5,
                    "execution_rigor": -2.0,
                    "chaos_tolerance": 1.5,
                    "cognitive_endurance": 0.0
                }
            }
        }
    },
    {
        "id": "q24",
        "section": "Subsystem 05: The Cognitive Edge",
        "question": "If you had to pick the single core value that defines your technical identity and standard of work, it is:",
        "options": {
            "A": {
                "text": "Architectural Elegance: Designing clean, scalable systems that grow beautifully without needing messy patches.",
                "label": "The Coherence Purist",
                "advice": "What matters most to you is a clean system built to last. Just watch that this pursuit of elegance doesn't delay delivery when the situation actually calls for a working compromise.",
                "vectors": {
                    "information_bandwidth": 2.0,
                    "execution_rigor": 1.5,
                    "chaos_tolerance": -0.5,
                    "cognitive_endurance": 1.5
                }
            },
            "B": {
                "text": "Pure Execution: Shipping working code on time, beating the deadline, and getting the job done no matter what.",
                "label": "The Relentless Shipper",
                "advice": "Your priority is shipping something that works, on time, whatever it takes. Plan regular time to clean up the technical debt you pick up along the way.",
                "vectors": {
                    "information_bandwidth": -0.5,
                    "execution_rigor": -0.5,
                    "chaos_tolerance": 2.5,
                    "cognitive_endurance": 1.5
                }
            },
            "C": {
                "text": "Uncompromising Quality: Hunting down every single edge case and optimizing performance until it runs with flawless precision.",
                "label": "The Precision Sentinel",
                "advice": "You hunt down every edge case until it's fully precise — a real commitment to quality. Keep in mind that in a fast-moving environment, a working result delivered on time often beats a perfect one that arrives too late.",
                "vectors": {
                    "information_bandwidth": 1.0,
                    "execution_rigor": 3.0,
                    "chaos_tolerance": -1.5,
                    "cognitive_endurance": 2.0
                }
            },
            "D": {
                "text": "Radical Innovation: Questioning the usual ways of doing things, breaking standard rules, and discovering completely unexpected solutions.",
                "label": "The Paradigm Disruptor",
                "advice": "You question the usual way of doing things in search of unexpected solutions — a real strength in innovation. Team up with people who are rigorous on execution to turn your bold ideas into something concrete.",
                "vectors": {
                    "information_bandwidth": 2.5,
                    "execution_rigor": -2.5,
                    "chaos_tolerance": 2.0,
                    "cognitive_endurance": 0.5
                }
            }
        }
    }
]