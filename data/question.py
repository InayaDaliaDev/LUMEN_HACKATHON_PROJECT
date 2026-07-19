# ==============================================================================
# DATA CORE MATRIX: ALL_QUESTIONS
# ==============================================================================
# This is the master database for the metacognitive profiling array.
# Each choice injects explicit text indicators and micro-quantified vector weights.

ALL_QUESTIONS = [
    {
        "id": "q1",
        "section": "Subsystem 01: The Executive Engine",
        "question": "A high-stakes product shipment is due in 14 days. Describe your authentic operational cycle under pressure:",
        "options": {
            "A": {
                "text": "I partition the specifications into micro-deliverables immediately, writing clean code on a strict daily schedule.",
                "label": "ABSTRACT ARCHITECT",
                "advice": "Your structural predictability is high, but you risk wasting critical hours optimizing base layers for features that might be completely cut before deployment.",
                "vectors": {"information_bandwidth": 1.5, "execution_rigor": 2.0, "chaos_tolerance": -0.5, "cognitive_endurance": 1.5}
            },
            "B": {
                "text": "I delay active execution for 12 days, then leverage a high-cortisol panic state to build the prototype in a single 36-hour sprint.",
                "label": "PRESSURE SPRINTER",
                "advice": "You are addicted to deadline-induced adrenaline. You ship functional tools, but leave a catastrophic trail of technical debt and unmaintainable logic.",
                "vectors": {"information_bandwidth": 0.5, "execution_rigor": -1.0, "chaos_tolerance": 2.0, "cognitive_endurance": 0.5}
            },
            "C": {
                "text": "I spend 11 days obsessively analyzing edge-cases and researching alternative stacks, leaving only 3 days of anxious, exhausted coding.",
                "label": "SYSTEMIC PERFECTIONIST",
                "advice": "Analysis paralysis is your default failure mode. Your fear of shipping an imperfect system makes you an execution bottleneck under tight timelines.",
                "vectors": {"information_bandwidth": 2.0, "execution_rigor": 1.5, "chaos_tolerance": -1.5, "cognitive_endurance": 0.0}
            },
            "D": {
                "text": "I hack together a chaotic, experimental foundation on day one, then spend two weeks changing the concept whenever a cleaner idea emerges.",
                "label": "CHAOS ENGINE",
                "advice": "Your non-linear adaptability is unmatched, but your total lack of scoping discipline causes endless feature creep and structural fragility.",
                "vectors": {"information_bandwidth": 1.0, "execution_rigor": -1.5, "chaos_tolerance": 2.5, "cognitive_endurance": 1.0}
            }
        }
    },
    {
        "id": "q2",
        "section": "Subsystem 01: The Executive Engine",
        "question": "A sudden revision in client constraints completely invalidates your current development sprint. Your immediate cognitive reaction is:",
        "options": {
            "A": {
                "text": "Frustrated irritation, but I immediately pause to restructure our documentation and architecture charts.",
                "label": "ABSTRACT ARCHITECT",
                "advice": "You treat structural disruption as an engineering problem, yet your reflex to immediately document rather than act can freeze immediate execution.",
                "vectors": {"information_bandwidth": 1.0, "execution_rigor": 1.5, "chaos_tolerance": 0.0, "cognitive_endurance": 1.0}
            },
            "B": {
                "text": "Unbothered. I instantly abandon my current codebase and start hacking out the new solution from scratch without looking back.",
                "label": "PRESSURE SPRINTER",
                "advice": "Your disposal speed is highly efficient, but you throw away valuable reusable modules due to an instinct for raw, unguided velocity.",
                "vectors": {"information_bandwidth": 0.0, "execution_rigor": -1.0, "chaos_tolerance": 2.0, "cognitive_endurance": 0.5}
            },
            "C": {
                "text": "Deep somatic distress and anger. The sudden invalidation makes the entire environment feel completely unmanaged and broken.",
                "label": "SYSTEMIC PERFECTIONIST",
                "advice": "Your internal stability requires external order. When the framework cracks, your logical sorting mechanics stall, risking complete emotional burnout.",
                "vectors": {"information_bandwidth": 1.5, "execution_rigor": 2.0, "chaos_tolerance": -2.0, "cognitive_endurance": -0.5}
            },
            "D": {
                "text": "Excited validation. I hated the rigid constraints of the old plan anyway; chaos gives me an immediate dopamine boost to innovate.",
                "label": "CHAOS ENGINE",
                "advice": "You use chaos as an energetic fuel source. Be careful: confusing high environmental volatility with genuine strategic opportunity leads to aimless drifting.",
                "vectors": {"information_bandwidth": 1.0, "execution_rigor": -2.0, "chaos_tolerance": 2.5, "cognitive_endurance": 1.0}
            }
        }
    },
    {
        "id": "q3",
        "section": "Subsystem 01: The Executive Engine",
        "question": "During a dense, multi-hour technical lecture or team briefing, your cognitive focus maintenance looks like:",
        "options": {
            "A": {
                "text": "Creating highly structured, color-coded mind maps to systematically index the speaker's conceptual hierarchy.",
                "label": "ABSTRACT ARCHITECT",
                "advice": "You process information by rebuilding it inside an isolated spatial framework. If the speaker lacks organization, you struggle to encode their input.",
                "vectors": {"information_bandwidth": 2.0, "execution_rigor": 1.0, "chaos_tolerance": -0.5, "cognitive_endurance": 1.5}
            },
            "B": {
                "text": "Filtering out 80% of the filler talk to only take action notes when a specific task or deadline is explicitly stated.",
                "label": "PRESSURE SPRINTER",
                "advice": "You are aggressively pragmatic, filtering noise effectively. However, you miss macro-level insights because you filter out everything that isn't an immediate task.",
                "vectors": {"information_bandwidth": -0.5, "execution_rigor": 0.5, "chaos_tolerance": 1.0, "cognitive_endurance": 1.0}
            },
            "C": {
                "text": "Sitting perfectly still, attempting to record or write down verbatim definitions because missed nuances feel like incomplete data.",
                "label": "SYSTEMIC PERFECTIONIST",
                "advice": "Your demand for data high-fidelity causes immediate working memory overload when the intake speed surpasses your manual transcription rate.",
                "vectors": {"information_bandwidth": 1.0, "execution_rigor": 2.0, "chaos_tolerance": -1.0, "cognitive_endurance": 0.5}
            },
            "D": {
                "text": "Relentlessly switching tabs, researching tangentially related source code, and letting my train of thought drift across multiple systems.",
                "label": "CHAOS ENGINE",
                "advice": "Your mind relies on lateral exploration. While this fosters unexpected cross-disciplinary breakthroughs, it actively prevents deep, sequential comprehension.",
                "vectors": {"information_bandwidth": 2.5, "execution_rigor": -1.5, "chaos_tolerance": 2.0, "cognitive_endurance": 0.0}
            }
        }
    },
    {
        "id": "q4",
        "section": "Subsystem 01: The Executive Engine",
        "question": "Analyze your localized physical workspace or digital workspace environment during active development:",
        "options": {
            "A": {
                "text": "Meticulously organized into strict directory hierarchies, clear tagging rules, and zero unmanaged file proliferation.",
                "label": "ABSTRACT ARCHITECT",
                "advice": "Your spatial organization minimizes environmental friction, reflecting a mind that requires external structure to offload memory strain.",
                "vectors": {"information_bandwidth": 1.0, "execution_rigor": 1.5, "chaos_tolerance": -1.0, "cognitive_endurance": 1.5}
            },
            "B": {
                "text": "A temporary disaster of temporary files and unsaved scripts that I plan to completely delete the second the project launches.",
                "label": "PRESSURE SPRINTER",
                "advice": "Your environment is entirely transactional. It serves its immediate purpose, but tracking bugs across undocumented files becomes an absolute nightmare.",
                "vectors": {"information_bandwidth": 0.0, "execution_rigor": -0.5, "chaos_tolerance": 1.5, "cognitive_endurance": 1.0}
            },
            "C": {
                "text": "Spotless and immaculate. If my workspace isn't clean, I will spend hours tidying up as a defense mechanism against initiating hard tasks.",
                "label": "SYSTEMIC PERFECTIONIST",
                "advice": "You practice structural procrastination. You exhaust your cognitive energy organizing assets before you even write a single line of functional code.",
                "vectors": {"information_bandwidth": 0.5, "execution_rigor": 2.0, "chaos_tolerance": -1.5, "cognitive_endurance": -0.5}
            },
            "D": {
                "text": "Complete visual anarchy that makes external observers panic, but I navigate the mess perfectly via episodic visual memory.",
                "label": "CHAOS ENGINE",
                "advice": "You function within entropy. Your system works until a team member needs to collaborate and encounters a total breakdown of common standards.",
                "vectors": {"information_bandwidth": 1.5, "execution_rigor": -2.0, "chaos_tolerance": 2.0, "cognitive_endurance": 0.5}
            }
        }
    },
    {
        "id": "q5",
        "section": "Subsystem 01: The Executive Engine",
        "question": "When forced to read an incredibly dense, low-context academic paper or documentation set, you:",
        "options": {
            "A": {
                "text": "Read linearly from abstract to conclusion, highlighting terms to build an isolated glossary of the source text's logic.",
                "label": "ABSTRACT ARCHITECT",
                "advice": "You respect structural hierarchy, allowing for systematic extraction. However, you waste time on dense introductory contexts that have minimal utility.",
                "vectors": {"information_bandwidth": 1.5, "execution_rigor": 1.5, "chaos_tolerance": -0.5, "cognitive_endurance": 2.0}
            },
            "B": {
                "text": "Scan aggressively for bold keywords, code blocks, and the final results section, bypassing the theoretical frameworks entirely.",
                "label": "PRESSURE SPRINTER",
                "advice": "You extract raw utility at lightning speed, but your complete disregard for theoretical foundations leads to deep algorithmic gaps in your execution.",
                "vectors": {"information_bandwidth": -0.5, "execution_rigor": -0.5, "chaos_tolerance": 1.0, "cognitive_endurance": 1.0}
            },
            "C": {
                "text": "Get completely trapped re-reading a single ambiguous sentence four times because a minor logical gap stalls my whole reading flow.",
                "label": "SYSTEMIC PERFECTIONIST",
                "advice": "Your bottom-up processing demands flawless precision at the atomic level. One bad definition can completely halt your ingestion pipelines.",
                "vectors": {"information_bandwidth": 1.0, "execution_rigor": 2.0, "chaos_tolerance": -1.5, "cognitive_endurance": 0.0}
            },
            "D": {
                "text": "Skip through arbitrary sections, jumping straight to external critique threads or forums to see how others broke the theory down.",
                "label": "CHAOS ENGINE",
                "advice": "You rely on crowdsourced decentralized patterns. This gives you a fast, multi-perspective view but deprives you of first-principles understanding.",
                "vectors": {"information_bandwidth": 2.0, "execution_rigor": -1.5, "chaos_tolerance": 1.5, "cognitive_endurance": 0.5}
            }
        }
    },
    {
        "id": "q6",
        "section": "Subsystem 02: Ingestion Mechanics",
        "question": "Faced with assembling a highly intricate mechanical array or deploying a multi-container local stack, you:",
        "options": {
            "A": {
                "text": "Deconstruct the manual or architecture diagrams to build a complete mental visualization before interacting with physical parts.",
                "label": "ABSTRACT ARCHITECT",
                "advice": "Your spatial modeling is clean and preemptive. You rarely make installation mistakes, but your initial bootup time is highly uncompetitive.",
                "vectors": {"information_bandwidth": 2.0, "execution_rigor": 1.0, "chaos_tolerance": -0.5, "cognitive_endurance": 1.5}
            },
            "B": {
                "text": "Discard the documentation entirely and start connecting components by intuition, trouble-shooting bugs only as they cause compiler crashes.",
                "label": "PRESSURE SPRINTER",
                "advice": "Your rapid physical feedback loops bypass reading overhead, but you risk permanently damaging configurations or missing silent logic errors.",
                "vectors": {"information_bandwidth": -1.0, "execution_rigor": -1.0, "chaos_tolerance": 2.0, "cognitive_endurance": 1.0}
            },
            "C": {
                "text": "Sort and inventory every single loose component, screw, and dependency token into physical size gradients before beginning step one.",
                "label": "SYSTEMIC PERFECTIONIST",
                "advice": "Your quality control setup is impeccable. Yet, you over-allocate prime cognitive focus to sorting tasks that have zero direct impact on end-product utility.",
                "vectors": {"information_bandwidth": 0.5, "execution_rigor": 2.5, "chaos_tolerance": -1.5, "cognitive_endurance": 1.0}
            },
            "D": {
                "text": "Combine components haphazardly to see if a more interesting alternative architecture reveals itself outside the intended configuration.",
                "label": "CHAOS ENGINE",
                "advice": "You are a natural exploratory innovator, but your disdain for standard operating blueprints frequently breaks foundational security protocols.",
                "vectors": {"information_bandwidth": 1.5, "execution_rigor": -2.0, "chaos_tolerance": 2.5, "cognitive_endurance": 0.5}
            }
        }
    },
    {
        "id": "q7",
        "section": "Subsystem 02: Ingestion Mechanics",
        "question": "When forced to instantly memorize an abstract, high-entropy variable token or security string, your mind defaults to:",
        "options": {
            "A": {
                "text": "Mapping the visual geometric vector path my fingers make across the input interface or screen space.",
                "label": "ABSTRACT ARCHITECT",
                "advice": "You translate linguistic data into geometric coordinates. It's high speed, but if the interface layout shifts, your recall drops to zero.",
                "vectors": {"information_bandwidth": 1.5, "execution_rigor": 0.5, "chaos_tolerance": 0.5, "cognitive_endurance": 1.0}
            },
            "B": {
                "text": "Subvocally repeating the exact acoustic phonetics of the string in an internal loop until it is typed and purged.",
                "label": "PRESSURE SPRINTER",
                "advice": "Your echoic memory buffer is functional for rapid execution cycles, but it provides absolutely zero long-term semantic retention.",
                "vectors": {"information_bandwidth": -0.5, "execution_rigor": 0.5, "chaos_tolerance": 1.0, "cognitive_endurance": 0.5}
            },
            "C": {
                "text": "Deconstructing the string into explicit logical connections, historical dates, or algorithmic mathematical properties.",
                "label": "SYSTEMIC PERFECTIONIST",
                "advice": "You require clean semantic validation. Data cannot exist in isolation inside your mind; it must be indexed into an existing database.",
                "vectors": {"information_bandwidth": 1.0, "execution_rigor": 2.0, "chaos_tolerance": -1.0, "cognitive_endurance": 1.5}
            },
            "D": {
                "text": "Associating the token with an erratic, highly abstract narrative fragment or a sudden chaotic burst of unrelated conceptual imagery.",
                "label": "CHAOS ENGINE",
                "advice": "Your synesthetic linking is creative and highly resilient against standard boring decay, but it requires massive initial cognitive processing overhead.",
                "vectors": {"information_bandwidth": 2.0, "execution_rigor": -1.0, "chaos_tolerance": 1.5, "cognitive_endurance": 0.0}
            }
        }
    },
    {
        "id": "q8",
        "section": "Subsystem 03: Ecosystem Friction",
        "question": "A massive, interdisciplinary group project is assigned with random team allocation. Your unvarnished interior reaction is:",
        "options": {
            "A": {
                "text": "I will immediately take leadership, dictate the interface specifications, and force everyone into a clear modular framework.",
                "label": "ABSTRACT ARCHITECT",
                "advice": "You design frameworks effectively but treat team members as predictable compute units. You will face resistance when human variables diverge from your charts.",
                "vectors": {"information_bandwidth": 1.5, "execution_rigor": 1.5, "chaos_tolerance": -0.5, "cognitive_endurance": 1.0}
            },
            "B": {
                "text": "I will claim a single isolated technical feature, disappear into the background, and build it at the absolute last minute.",
                "label": "PRESSURE SPRINTER",
                "advice": "You reduce coordination overhead to zero, but your total refusal to engage in open intermediate code-sharing makes you a terrifying teammate.",
                "vectors": {"information_bandwidth": -0.5, "execution_rigor": -0.5, "chaos_tolerance": 1.5, "cognitive_endurance": 1.0}
            },
            "C": {
                "text": "Intense dread. I know my team will produce subpar work, so I will quietly build 90% of the entire app myself to maintain control.",
                "label": "SYSTEMIC PERFECTIONIST",
                "advice": "Your inability to delegate stems from a deep trust deficit. You prevent team scale and run a direct track toward self-inflicted burnout.",
                "vectors": {"information_bandwidth": 0.5, "execution_rigor": 2.5, "chaos_tolerance": -1.5, "cognitive_endurance": 0.5}
            },
            "D": {
                "text": "I will use the group as an open-ended lab, constantly shifting the team's vision toward whatever experimental tech stack I found this morning.",
                "label": "CHAOS ENGINE",
                "advice": "You provide disruptive inspiration, but your team members will hate you for destroying their linear task progress with constant conceptual pivots.",
                "vectors": {"information_bandwidth": 2.0, "execution_rigor": -2.0, "chaos_tolerance": 2.0, "cognitive_endurance": 0.0}
            }
        }
    },
    {
        "id": "q9",
        "section": "Subsystem 03: Ecosystem Friction",
        "question": "If you could force an institutional engineering program to adapt completely to your learning defaults, you would demand:",
        "options": {
            "A": {
                "text": "A highly predictable lecture structure paired with massive, abstract textbooks that detail whole systems from first principles.",
                "label": "ABSTRACT ARCHITECT",
                "advice": "You excel in structured academic systems. However, you risk becoming an academic theorist who is completely useless when dropped into a broken, real-world legacy codebase.",
                "vectors": {"information_bandwidth": 2.0, "execution_rigor": 1.5, "chaos_tolerance": -1.0, "cognitive_endurance": 2.0}
            },
            "B": {
                "text": "Zero theoretical lectures. Just drop us into a high-intensity hackathon lab with an ambiguous problem statement and a 48-hour countdown.",
                "label": "PRESSURE SPRINTER",
                "advice": "You thrive in competitive execution environments. But you struggle to scale because you skip the abstract foundations required for deep engineering breakthroughs.",
                "vectors": {"information_bandwidth": -1.0, "execution_rigor": -0.5, "chaos_tolerance": 2.5, "cognitive_endurance": 1.5}
            },
            "C": {
                "text": "A rigorous, solitary track where my code is evaluated by an uncompromising automated testing suite with zero human interference.",
                "label": "SYSTEMIC PERFECTIONIST",
                "advice": "You value clean binary feedback metrics. This makes you a sharp technical parser, but completely shields you from navigating political human systems.",
                "vectors": {"information_bandwidth": 1.0, "execution_rigor": 2.5, "chaos_tolerance": -1.5, "cognitive_endurance": 1.0}
            },
            "D": {
                "text": "An unguided, open-ended research playground where failure is undefined and I can switch projects every single week.",
                "label": "CHAOS ENGINE",
                "advice": "You require absolute creative autonomy. Without structural constraints, however, your intellectual career will be a graveyard of half-finished initial prototypes.",
                "vectors": {"information_bandwidth": 2.5, "execution_rigor": -2.5, "chaos_tolerance": 2.0, "cognitive_endurance": -0.5}
            }
        }
    },
    {
        "id": "q10",
        "section": "Subsystem 03: Ecosystem Friction",
        "question": "When deep-diving into complex logic inside your room, the presence of environmental sensory noise (background talk, traffic) is:",
        "options": {
            "A": {
                "text": "A structural obstacle. I require high-end noise-canceling hardware or total isolation, or my system modeling stalls.",
                "label": "ABSTRACT ARCHITECT",
                "advice": "Your analytical focus is deep but highly fragile. Your lack of a baseline sensory filter makes you dependent on hyper-controlled environments.",
                "vectors": {"information_bandwidth": 1.5, "execution_rigor": 1.0, "chaos_tolerance": -1.5, "cognitive_endurance": 1.0}
            },
            "B": {
                "text": "An intentional requirement. I need aggressive, high-BPM electronic music or cafe chaos to keep my arousal thresholds up.",
                "label": "PRESSURE SPRINTER",
                "advice": "You rely on sensory over-stimulation to create an artificial focus bubble. This satisfies your dopamine baseline but masks deep mental fatigue.",
                "vectors": {"information_bandwidth": -0.5, "execution_rigor": 0.0, "chaos_tolerance": 1.5, "cognitive_endurance": 1.5}
            },
            "C": {
                "text": "A direct distraction that makes me fixate on the noise itself, fueling internal resentment toward the source of the interruption.",
                "label": "SYSTEMIC PERFECTIONIST",
                "advice": "You externalize control deficits. Instead of adapting your attention, you consume precious mental energy wishing the outside world would follow your rules.",
                "vectors": {"information_bandwidth": 0.5, "execution_rigor": 2.0, "chaos_tolerance": -2.0, "cognitive_endurance": 0.0}
            },
            "D": {
                "text": "Completely irrelevant. Once an implementation vector catches my curiosity, the physical world ceases to exist to my perception.",
                "label": "CHAOS ENGINE",
                "advice": "You possess a powerful interest-driven hyper-focus state. It’s an execution superpower, but it leaves you dangerously blind to personal burnout indicators.",
                "vectors": {"information_bandwidth": 2.0, "execution_rigor": -1.0, "chaos_tolerance": 2.0, "cognitive_endurance": 2.0}
            }
        }
    },
    {
        "id": "q11",
        "section": "Subsystem 04: The Internal Drive",
        "question": "Assess your real, internal relationship with institutional authorities, tech leads, or academic evaluators:",
        "options": {
            "A": {
                "text": "I view them as systematic gatekeepers. I decode their evaluation criteria and optimize my output specifically to pass their checks.",
                "label": "ABSTRACT ARCHITECT",
                "advice": "You are highly pragmatic at navigating systemic hierarchies. Just make sure you aren't sacrificing your long-term creative edge to satisfy arbitrary rubrics.",
                "vectors": {"information_bandwidth": 1.0, "execution_rigor": 1.5, "chaos_tolerance": -0.5, "cognitive_endurance": 1.5}
            },
            "B": {
                "text": "I mostly ignore their structural rules, relying on my ability to deliver a flashy, high-impact final demo to override my intermediate policy violations.",
                "label": "PRESSURE SPRINTER",
                "advice": "You know how to play to the crowd and win short-term praise, but you build a reputation for being completely unreliable during day-to-day operations.",
                "vectors": {"information_bandwidth": -0.5, "execution_rigor": -1.0, "chaos_tolerance": 2.0, "cognitive_endurance": 0.5}
            },
            "C": {
                "text": "I experience deep internal friction and challenge them openly if their evaluation frameworks or technical directives lack strict logical coherence.",
                "label": "SYSTEMIC PERFECTIONIST",
                "advice": "You place raw truth above established hierarchy. While intellectually honorable, your refusal to compromise on minor details makes you highly combative in team environments.",
                "vectors": {"information_bandwidth": 1.5, "execution_rigor": 2.0, "chaos_tolerance": -1.5, "cognitive_endurance": 0.0}
            },
            "D": {
                "text": "I actively avoid them. I do not care about their approval or validation; I only want them to leave me alone so I can experiment.",
                "label": "CHAOS ENGINE",
                "advice": "You operate as a fully autonomous agent. This prevents institutional assimilation, but you miss out on vital mentorship channels and institutional resources.",
                "vectors": {"information_bandwidth": 2.0, "execution_rigor": -2.0, "chaos_tolerance": 1.5, "cognitive_endurance": 1.0}
            }
        }
    },
    {
        "id": "q12",
        "section": "Subsystem 04: The Internal Drive",
        "question": "Select the testing format that you believe accurately quantifies your core intellectual competence:",
        "options": {
            "A": {
                "text": "A multi-stage theoretical examination testing deep, fundamental abstract principles with zero ambiguous wording.",
                "label": "ABSTRACT ARCHITECT",
                "advice": "You shine in highly structured environments of high complexity. You struggle when problems require muddy, real-world compromises over clean mathematics.",
                "vectors": {"information_bandwidth": 2.0, "execution_rigor": 1.5, "chaos_tolerance": -1.0, "cognitive_endurance": 1.5}
            },
            "B": {
                "text": "A high-pressure live coding challenge where I am judged purely on speed, real-time debugging, and functional execution under time pressure.",
                "label": "PRESSURE SPRINTER",
                "advice": "Your short-term processing under pressure is lethal. However, this environment completely masks your lack of patience for long-term project optimization.",
                "vectors": {"information_bandwidth": -0.5, "execution_rigor": -0.5, "chaos_tolerance": 2.0, "cognitive_endurance": 1.0}
            },
            "C": {
                "text": "Submitting an exhaustive, highly audited, long-term portfolio representing months of continuous micro-refinement and zero edge-case vulnerabilities.",
                "label": "SYSTEMIC PERFECTIONIST",
                "advice": "You value deep endurance and execution quality. Your danger lies in over-polishing existing work, turning a finished project into an endless loop of optimization.",
                "vectors": {"information_bandwidth": 1.0, "execution_rigor": 2.5, "chaos_tolerance": -1.5, "cognitive_endurance": 2.5}
            },
            "D": {
                "text": "Being dropped into a broken, legacy environment with zero documentation and told to solve an undefined crisis using any chaotic method necessary.",
                "label": "CHAOS ENGINE",
                "advice": "You are a master of heuristic emergency operations. You excel when the map is missing, but you quickly lose interest once the environment stabilizes.",
                "vectors": {"information_bandwidth": 1.5, "execution_rigor": -2.0, "chaos_tolerance": 2.5, "cognitive_endurance": 0.5}
            }
        }
    },
    {
        "id": "q13",
        "section": "Subsystem 04: The Internal Drive",
        "question": "You receive a severely low evaluation score on a script you spent days refining. Your unedited immediate response is:",
        "options": {
            "A": {
                "text": "I isolate the grader’s exact parsing rubric, locate the mechanical deviation point, and update my mental model for the next run.",
                "label": "ABSTRACT ARCHITECT",
                "advice": "You process failure purely as an informatics feedback loop. This structural detachment keeps you efficient but can make you blind to political bias.",
                "vectors": {"information_bandwidth": 1.5, "execution_rigor": 1.0, "chaos_tolerance": 0.5, "cognitive_endurance": 1.5}
            },
            "B": {
                "text": "A brief surge of aggressive frustration, which I immediately suppress by working on an entirely different feature to overwrite the failure.",
                "label": "PRESSURE SPRINTER",
                "advice": "You use task-switching to escape negative feedback. This keeps your momentum high but prevents you from addressing deep, chronic technical flaws.",
                "vectors": {"information_bandwidth": -0.5, "execution_rigor": -0.5, "chaos_tolerance": 1.5, "cognitive_endurance": 1.0}
            },
            "C": {
                "text": "An intense, devastating blow to my self-worth. I obsessively analyze the code to prove the reviewer's model is fundamentally flawed.",
                "label": "SYSTEMIC PERFECTIONIST",
                "advice": "Your identity is dangerously fused with your technical execution. A bad code review feels like an existential attack, causing toxic defensiveness.",
                "vectors": {"information_bandwidth": 1.0, "execution_rigor": 2.0, "chaos_tolerance": -2.0, "cognitive_endurance": -0.5}
            },
            "D": {
                "text": "Total internal detachment. The evaluation system is arbitrary and broken anyway; my own internal assessment of my work is all that matters.",
                "label": "CHAOS ENGINE",
                "advice": "Your psychological insulation protects your creative confidence. However, rejecting all external calibration leads directly to technical isolation.",
                "vectors": {"information_bandwidth": 2.0, "execution_rigor": -1.5, "chaos_tolerance": 2.0, "cognitive_endurance": 0.5}
            }
        }
    },
    {
        "id": "q14",
        "section": "Subsystem 04: The Internal Drive",
        "question": "Identify your absolute, undisputed competitive superpower during a sudden engineering crisis:",
        "options": {
            "A": {
                "text": "Spotting the underlying abstract structural pattern that unifies five seemingly unrelated system bugs instantly.",
                "label": "ABSTRACT ARCHITECT",
                "advice": "You are a master of high-level conceptual sorting, bypassing tedious step-by-step trace routines through rapid architecture visualization.",
                "vectors": {"information_bandwidth": 2.5, "execution_rigor": 1.0, "chaos_tolerance": 0.0, "cognitive_endurance": 1.0}
            },
            "B": {
                "text": "Maintaining total emotional detachment and rapid typing speed while an entire production cluster is actively melting down.",
                "label": "PRESSURE SPRINTER",
                "advice": "Your nervous system stays stable when adrenaline spike variables are maxed out, making you a highly effective emergency front-line operator.",
                "vectors": {"information_bandwidth": -0.5, "execution_rigor": 0.0, "chaos_tolerance": 2.5, "cognitive_endurance": 1.5}
            },
            "C": {
                "text": "Locating a single missing semicolon or memory leak hidden deep within 5,000 lines of un-indented legacy code through pure stubborn focus.",
                "label": "SYSTEMIC PERFECTIONIST",
                "advice": "Your microscopic data sorting is unmatched. You see the dangerous needle in the haystack that everyone else glossed over in their hurry.",
                "vectors": {"information_bandwidth": 0.5, "execution_rigor": 3.0, "chaos_tolerance": -1.0, "cognitive_endurance": 2.0}
            },
            "D": {
                "text": "Generating ten completely absurd, non-linear workaround ideas that violate basic best practices but somehow save the product from dying.",
                "label": "CHAOS ENGINE",
                "advice": "Your lateral divergent processing excels in unstable systems. You save teams with black-swan insights that linear minds cannot compute.",
                "vectors": {"information_bandwidth": 2.0, "execution_rigor": -2.0, "chaos_tolerance": 2.5, "cognitive_endurance": 0.5}
            }
        }
    },
    {
        "id": "q15",
        "section": "Subsystem 04: The Internal Drive",
        "question": "What is the primary, recurring catalyst that causes you to lose all cognitive motivation for a project?",
        "options": {
            "A": {
                "text": "The core architectural problems are solved, and the remaining tasks are just tedious UI polish or minor maintenance work.",
                "label": "ABSTRACT ARCHITECT",
                "advice": "You lose drive once the high-level cognitive complexity drops. You are great at starting systems, but terrible at finishing them.",
                "vectors": {"information_bandwidth": 2.0, "execution_rigor": 0.0, "chaos_tolerance": 0.5, "cognitive_endurance": -0.5}
            },
            "B": {
                "text": "The delivery feedback cycles are too slow or extended; I need immediate, highly frequent deployment validation loops to care.",
                "label": "PRESSURE SPRINTER",
                "advice": "Your motivation is highly dependent on fast external feedback loops. If you don't see immediate results, your attention span decays.",
                "vectors": {"information_bandwidth": -0.5, "execution_rigor": -0.5, "chaos_tolerance": 1.5, "cognitive_endurance": 0.5}
            },
            "C": {
                "text": "I fall slightly behind schedule or make a fundamental structural error, rendering the entire codebase 'imperfect' in my eyes.",
                "label": "SYSTEMIC PERFECTIONIST",
                "advice": "You suffer from severe all-or-nothing cognitive filtering. If your implementation isn't flawless, your mind prefers to completely abandon it.",
                "vectors": {"information_bandwidth": 0.5, "execution_rigor": 2.0, "chaos_tolerance": -2.0, "cognitive_endurance": 0.0}
            },
            "D": {
                "text": "The project parameters are too rigid and locked down. I am forbidden from changing the core stack or experimenting with new methodologies.",
                "label": "CHAOS ENGINE",
                "advice": "Standard operational guardrails asphyxiate your focus. You mistake necessary product constraints for a personal cage, leading to early rebellion.",
                "vectors": {"information_bandwidth": 1.5, "execution_rigor": -1.5, "chaos_tolerance": 2.0, "cognitive_endurance": 0.5}
            }
        }
    },
    {
        "id": "q16",
        "section": "Subsystem 04: The Internal Drive",
        "question": "When forced to complete a highly repetitive, boring administrative task (e.g., manual data formatting, writing tests), you:",
        "options": {
            "A": {
                "text": "Zone out completely, isolate my attention, and execute the work like a detached, linear processor until it's done.",
                "label": "ABSTRACT ARCHITECT",
                "advice": "You have solid executive self-regulation for low-stimulation tasks. Just make sure you aren't wasting human potential on things that should be automated.",
                "vectors": {"information_bandwidth": 0.5, "execution_rigor": 1.5, "chaos_tolerance": -0.5, "cognitive_endurance": 2.0}
            },
            "B": {
                "text": "Rush through it at maximum speed, accepting a high error rate and messy formatting just to get the task off my desk.",
                "label": "PRESSURE SPRINTER",
                "advice": "Your velocity priority backfires here. Your rapid, sloppy execution forces team members to spend time cleaning up your silent mistakes.",
                "vectors": {"information_bandwidth": -1.0, "execution_rigor": -1.5, "chaos_tolerance": 1.5, "cognitive_endurance": 1.0}
            },
            "C": {
                "text": "Spend four hours writing a highly complex Python script to fully automate the task, even if the manual entry would have only taken one hour.",
                "label": "SYSTEMIC PERFECTIONIST",
                "advice": "You would rather spend massive cognitive energy building an elegant automation system than endure one hour of uncreative repetition.",
                "vectors": {"information_bandwidth": 1.5, "execution_rigor": 2.0, "chaos_tolerance": -1.0, "cognitive_endurance": 0.5}
            },
            "D": {
                "text": "Procrastinate endlessly, making careless, sloppy mistakes because my brain actively rejects lower-stimulation work environments.",
                "label": "CHAOS ENGINE",
                "advice": "Your attention system is heavily dopamine-gated. When a task lacks novelty, your internal focus control completely shuts down, causing functional failure.",
                "vectors": {"information_bandwidth": 1.0, "execution_rigor": -2.0, "chaos_tolerance": 1.0, "cognitive_endurance": -1.0}
            }
        }
    },
    {
        "id": "q17",
        "section": "Subsystem 04: The Internal Drive",
        "question": "An assignment or feature spec is completely open-ended ('Build whatever you want to solve x'). Your strategic reflex is:",
        "options": {
            "A": {
                "text": "Anxious paralysis. I spend days trying to design the absolute most optimal system boundaries before writing a single line of code.",
                "label": "ABSTRACT ARCHITECT",
                "advice": "Infinite choice overwhelms your structural engine. You need external parameters to anchor your modeling, or you sink into abstraction.",
                "vectors": {"information_bandwidth": 1.5, "execution_rigor": 1.5, "chaos_tolerance": -1.0, "cognitive_endurance": 0.5}
            },
            "B": {
                "text": "Immediate execution. I pick the very first basic idea that crosses my mind and start building it out without evaluating alternatives.",
                "label": "PRESSURE SPRINTER",
                "advice": "Your biases prioritize action over strategy. You escape choice-paralysis quickly, but often waste days building the wrong feature path.",
                "vectors": {"information_bandwidth": -0.5, "execution_rigor": -0.5, "chaos_tolerance": 1.5, "cognitive_endurance": 1.0}
            },
            "C": {
                "text": "Suspicious optimization. I cross-examine the evaluator to reverse-engineer their hidden preferences so I can win the grading matrix.",
                "label": "SYSTEMIC PERFECTIONIST",
                "advice": "You treat open-endedness as a trap. Instead of exploring creatively, you waste cycles trying to read the minds of authority figures.",
                "vectors": {"information_bandwidth": 0.5, "execution_rigor": 2.5, "chaos_tolerance": -1.0, "cognitive_endurance": 1.0}
            },
            "D": {
                "text": "Total creative liberation. I flood my workspace with twenty radical conceptual paths, picking the absolute most unusual tech stack to experiment with.",
                "label": "CHAOS ENGINE",
                "advice": "This is your natural habitat. You are a powerful zero-to-one innovator, but your baseline instinct to show off complexity makes your code unmaintainable.",
                "vectors": {"information_bandwidth": 2.5, "execution_rigor": -2.0, "chaos_tolerance": 2.5, "cognitive_endurance": 0.0}
            }
        }
    },
    {
        "id": "q18",
        "section": "Subsystem 05: The Cognitive Edge",
        "question": "Analyze your personal digital filesystem structure and note-taking directories:",
        "options": {
            "A": {
                "text": "Nested, highly explicit folder hierarchies mapped out by year, domain, and priority, utilizing strict naming taxonomies.",
                "label": "ABSTRACT ARCHITECT",
                "advice": "Your digital filing systems minimize search latency. You depend on external architecture to keep your mental landscape unburdened.",
                "vectors": {"information_bandwidth": 1.0, "execution_rigor": 2.0, "chaos_tolerance": -1.5, "cognitive_endurance": 1.5}
            },
            "B": {
                "text": "A massive, unorganized 'Downloads' directory and chaotic desktop. I rely entirely on raw keyword 'Search' indexing to locate files.",
                "label": "PRESSURE SPRINTER",
                "advice": "You bypass administrative sorting costs completely. This algorithmic shortcut works fine until you miss an old file version due to bad naming.",
                "vectors": {"information_bandwidth": -0.5, "execution_rigor": -1.0, "chaos_tolerance": 2.0, "cognitive_endurance": 1.0}
            },
            "C": {
                "text": "A highly tuned relational knowledge graph or obsidian wiki filled with explicit backlinks and clean markdown syntax.",
                "label": "SYSTEMIC PERFECTIONIST",
                "advice": "You construct comprehensive mental webs. Be careful: you can easily transform into a knowledge-collector who collects data maps but never builds actual products.",
                "vectors": {"information_bandwidth": 2.0, "execution_rigor": 1.5, "chaos_tolerance": -0.5, "cognitive_endurance": 1.5}
            },
            "D": {
                "text": "I have absolutely no system. Files are scattered randomly across desktops, clouds, and local drives. It is an unmanaged digital wasteland.",
                "label": "CHAOS ENGINE",
                "advice": "Your administrative executive control is deeply compromised. This systemic entropy will inevitably trigger file loss crises under tight deadlines.",
                "vectors": {"information_bandwidth": 1.0, "execution_rigor": -2.5, "chaos_tolerance": 1.5, "cognitive_endurance": -0.5}
            }
        }
    },
    {
        "id": "q19",
        "section": "Subsystem 05: The Cognitive Edge",
        "question": "To achieve a profound sense of cognitive satisfaction at the end of a deep work session, your brain requires:",
        "options": {
            "A": {
                "text": "Having cleanly integrated an abstract, highly difficult concept into my permanent global mental models.",
                "label": "ABSTRACT ARCHITECT",
                "advice": "You are a seeker of conceptual synthesis. A day spent without clearing up deep theoretical ambiguities feels completely hollow to your mind.",
                "vectors": {"information_bandwidth": 2.5, "execution_rigor": 1.0, "chaos_tolerance": 0.0, "cognitive_endurance": 1.5}
            },
            "B": {
                "text": "Crossing off 15 distinct line items from an external action list, signaling visible, rapid operational progress.",
                "label": "PRESSURE SPRINTER",
                "advice": "Your reward systems are entirely task-driven. You evaluate productivity by task volume rather than checking the long-term strategic direction of your effort.",
                "vectors": {"information_bandwidth": -0.5, "execution_rigor": 0.5, "chaos_tolerance": 1.5, "cognitive_endurance": 1.5}
            },
            "C": {
                "text": "Having spent 8 uninterrupted hours sitting at my desk with zero environmental distractions or structural deviations.",
                "label": "SYSTEMIC PERFECTIONIST",
                "advice": "You mistake raw time-investment for real high-value output. You evaluate your value by suffering and endurance rather than actual product delivery.",
                "vectors": {"information_bandwidth": 0.5, "execution_rigor": 2.5, "chaos_tolerance": -1.0, "cognitive_endurance": 2.5}
            },
            "D": {
                "text": "Having compiled an entirely unique, deployable codebase module or standalone tool from scratch.",
                "label": "CHAOS ENGINE",
                "advice": "You need tangible creative artifacts to validate your day. You are a builder, but you struggle on days focused purely on maintenance or code review.",
                "vectors": {"information_bandwidth": 1.5, "execution_rigor": -1.0, "chaos_tolerance": 2.0, "cognitive_endurance": 1.0}
            }
        }
    },
    {
        "id": "q20",
        "section": "Subsystem 05: The Cognitive Edge",
        "question": "In a critical, high-pressure live presentation or evaluation crunch, your memory access performance:",
        "options": {
            "A": {
                "text": "Becomes highly detached and structural. I recall theoretical frameworks flawlessly but lose conversational warmth.",
                "label": "ABSTRACT ARCHITECT",
                "advice": "Your logic systems isolate themselves from threat data, protecting core data integrity but giving off a cold, robotic demeanor to audiences.",
                "vectors": {"information_bandwidth": 2.0, "execution_rigor": 1.5, "chaos_tolerance": -0.5, "cognitive_endurance": 1.0}
            },
            "B": {
                "text": "Sharpens aggressively. I retrieve niche facts and execute fast real-time verbal pivots that I didn't know I was capable of.",
                "label": "PRESSURE SPRINTER",
                "advice": "You are a crisis responder. Your cognitive engine utilizes the cortisol flood to bypass normal retrieval latencies, allowing for lethal real-time adaptation.",
                "vectors": {"information_bandwidth": 0.0, "execution_rigor": -0.5, "chaos_tolerance": 2.5, "cognitive_endurance": 1.5}
            },
            "C": {
                "text": "Blanks out completely under extreme threat stress, locking me into cognitive freeze loops until the pressure environment resolves.",
                "label": "SYSTEMIC PERFECTIONIST",
                "advice": "Your system requires high environmental predictability. When stress signals flood your brain, your structural working memory completely drops its parameters.",
                "vectors": {"information_bandwidth": 0.5, "execution_rigor": 2.0, "chaos_tolerance": -2.5, "cognitive_endurance": -0.5}
            },
            "D": {
                "text": "Develops intense tunnel-vision, focusing hyper-accurately on a single micro-detail while completely forgetting the primary thesis.",
                "label": "CHAOS ENGINE",
                "advice": "Stress narrows your focal lens to a dangerous degree. You fixate on defending a single line of code while the overall presentation narrative fails.",
                "vectors": {"information_bandwidth": 1.0, "execution_rigor": -1.5, "chaos_tolerance": 1.5, "cognitive_endurance": 0.5}
            }
        }
    },
    {
        "id": "q21",
        "section": "Subsystem 05: The Cognitive Edge",
        "question": "Strip away all professional platitudes. Your internal cognitive processor operates most like a:",
        "options": {
            "A": {
                "text": "A high-speed train locked onto fixed, rigid structural rails. Unmatched efficiency, but completely unable to navigate off-track terrain.",
                "label": "ABSTRACT ARCHITECT",
                "advice": "You optimize clean linear pipelines perfectly. However, you face catastrophic disorientation when forced to operate in unmapped, lawless industries.",
                "vectors": {"information_bandwidth": 1.5, "execution_rigor": 2.0, "chaos_tolerance": -1.5, "cognitive_endurance": 1.5}
            },
            "B": {
                "text": "An overclocked processor running 70 concurrent browser tabs, where 5 are frozen and the cooling fan is actively failing.",
                "label": "PRESSURE SPRINTER",
                "advice": "You operate in hyper-distanced multi-threading paradigms. You handle extreme parallel chaos, but you live perpetually on the edge of system crashes.",
                "vectors": {"information_bandwidth": 0.5, "execution_rigor": -1.0, "chaos_tolerance": 2.0, "cognitive_endurance": 1.0}
            },
            "C": {
                "text": "A deep-sea research submarine exploring a single trench for weeks at a time, entirely isolated from surface weather conditions.",
                "label": "SYSTEMIC PERFECTIONIST",
                "advice": "Your deep technical specialization is remarkable. But your complete insulation from speed requirements makes you slow to pivot when the market shifts.",
                "vectors": {"information_bandwidth": 1.0, "execution_rigor": 2.5, "chaos_tolerance": -1.0, "cognitive_endurance": 2.5}
            },
            "D": {
                "text": "An unpredictable experimental Swiss Army Knife, containing 3 tools that don't fit the standard chassis but solve black-swan problems.",
                "label": "CHAOS ENGINE",
                "advice": "You are the ultimate eccentric adaptive patch. You lack standardization, but you are irreplaceable when standard engineering tools fail.",
                "vectors": {"information_bandwidth": 2.0, "execution_rigor": -2.0, "chaos_tolerance": 2.5, "cognitive_endurance": 0.0}
            }
        }
    },
    {
        "id": "q22",
        "section": "Subsystem 05: The Cognitive Edge",
        "question": "Identify your absolute deepest existential fear regarding your long-term technical or academic career track:",
        "options": {
            "A": {
                "text": "Being forced to work on an assembly line of repetitive, low-complexity projects that require zero systemic modeling.",
                "label": "ABSTRACT ARCHITECT",
                "advice": "Routine is your intellectual death sentence. You require high cognitive load and architectural challenges to feel alive.",
                "vectors": {"information_bandwidth": 2.5, "execution_rigor": 1.0, "chaos_tolerance": 0.0, "cognitive_endurance": 1.0}
            },
            "B": {
                "text": "Slowing down, losing my execution speed edge, and being exposed as a sloppy developer by younger, faster programmers.",
                "label": "PRESSURE SPRINTER",
                "advice": "Your imposter syndrome is tied directly to physical output speed. You must build deep theoretical foundations to survive long-term as your typing velocity levels out.",
                "vectors": {"information_bandwidth": -0.5, "execution_rigor": -0.5, "chaos_tolerance": 1.5, "cognitive_endurance": 1.5}
            },
            "C": {
                "text": "Realizing after years of intense development that my polished, perfect system solves a problem that absolutely no one in the real economy cares about.",
                "label": "SYSTEMIC PERFECTIONIST",
                "advice": "You fear useless optimization. Break your habit of building in dark closets; force yourself to ship crude, basic prototypes to validate market demand early.",
                "vectors": {"information_bandwidth": 1.0, "execution_rigor": 2.0, "chaos_tolerance": -1.5, "cognitive_endurance": 2.0}
            },
            "D": {
                "text": "Being forced to specialize in a single niche technology for ten years, permanently closing off my ability to jump into alternative fields.",
                "label": "CHAOS ENGINE",
                "advice": "You suffer from chronic generalist anxiety. You fear commitment because you treat specialization as a cage rather than an operational beachhead.",
                "vectors": {"information_bandwidth": 2.0, "execution_rigor": -1.5, "chaos_tolerance": 2.0, "cognitive_endurance": 0.5}
            }
        }
    },
    {
        "id": "q23",
        "section": "Subsystem 05: The Cognitive Edge",
        "question": "The second a disruptive, high-potential project idea forms in your head, your instinctive baseline reflex is to:",
        "options": {
            "A": {
                "text": "Open a markdown file and immediately sketch out the global database schema and system flowcharts.",
                "label": "ABSTRACT ARCHITECT",
                "advice": "You ground abstract energy into clean structures. Just avoid spending weeks designing perfect interfaces before confirming if the core idea is even viable.",
                "vectors": {"information_bandwidth": 2.0, "execution_rigor": 1.5, "chaos_tolerance": -0.5, "cognitive_endurance": 1.0}
            },
            "B": {
                "text": "Open VS Code and write a dirty, raw, unstyled prototype script within two hours to see it execute in the terminal.",
                "label": "PRESSURE SPRINTER",
                "advice": "Your zero-latency execution gets ideas off the ground fast. But your refusal to design an architecture blueprint first means your prototype will likely need to be completely rewritten down the line.",
                "vectors": {"information_bandwidth": -0.5, "execution_rigor": -0.5, "chaos_tolerance": 2.0, "cognitive_endurance": 1.0}
            },
            "C": {
                "text": "Search GitHub and patent indices extensively to verify if any existing system has implemented this exact model to ensure absolute novelty.",
                "label": "SYSTEMIC PERFECTIONIST",
                "advice": "You treat initial concept validation with high academic rigor. You often talk yourself out of building great things because someone else did something slightly similar.",
                "vectors": {"information_bandwidth": 1.5, "execution_rigor": 2.5, "chaos_tolerance": -1.0, "cognitive_endurance": 1.5}
            },
            "D": {
                "text": "Keep the idea completely inside my head for weeks, letting it mutate and collide with other random concepts before sharing it.",
                "label": "CHAOS ENGINE",
                "advice": "You leverage long-term internal conceptual incubation. Your ideas exit this process highly mature, but you run the risk of someone else shipping the concept while you keep it locked away in your mind.",
                "vectors": {"information_bandwidth": 2.5, "execution_rigor": -2.0, "chaos_tolerance": 1.5, "cognitive_endurance": 0.0}
            }
        }
    },
    {
        "id": "q24",
        "section": "Subsystem 05: The Cognitive Edge",
        "question": "If you had to isolate the absolute core value that defines your technical identity and integrity, it is:",
        "options": {
            "A": {
                "text": "Systemic Elegance: Designing modular, scalable architectures that expand beautifully without requiring messy patches.",
                "label": "ABSTRACT ARCHITECT",
                "advice": "You build for the future. Make sure your passion for architectural beauty doesn't prevent you from delivering vital features to users who need them today.",
                "vectors": {"information_bandwidth": 2.0, "execution_rigor": 1.5, "chaos_tolerance": -0.5, "cognitive_endurance": 1.5}
            },
            "B": {
                "text": "Raw Operational Delivery: Shipping highly functional code on time, under budget, and beating the ticking deadline clock no matter what.",
                "label": "PRESSURE SPRINTER",
                "advice": "You are the ultimate executor. You survive the trenches, but you must learn to spend time cleaning up your historical technical debt if you want to scale to master engineer.",
                "vectors": {"information_bandwidth": -0.5, "execution_rigor": -0.5, "chaos_tolerance": 2.5, "cognitive_endurance": 1.5}
            },
            "C": {
                "text": "Uncompromising Quality Control: Eradicating edge-cases and optimizing performance until the script runs with mathematical precision.",
                "label": "SYSTEMIC PERFECTIONIST",
                "advice": "You are the ultimate guardian of accuracy. Your code is secure, but you must learn to accept that 'done is often better than perfect' under real market conditions.",
                "vectors": {"information_bandwidth": 1.0, "execution_rigor": 3.0, "chaos_tolerance": -1.5, "cognitive_endurance": 2.0}
            },
            "D": {
                "text": "Radical Innovation: Challenging standard industry methods, breaking rules, and discovering unexpected technological avenues.",
                "label": "CHAOS ENGINE",
                "advice": "You are the source of disruptive evolution. You break historical rules effectively, but you must pair with structured executors to prevent your project from ending in structural anarchy.",
                "vectors": {"information_bandwidth": 2.5, "execution_rigor": -2.5, "chaos_tolerance": 2.0, "cognitive_endurance": 0.5}
            }
        }
    }
]