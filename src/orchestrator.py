class SentinelOrchestrator:
    def __init__(self, brain, researcher, guard):
        self.brain = brain
        self.researcher = researcher
        self.guard = guard

    def execute_full_mission(self, user_command, doc_text=""):
        """Orchestrates a multi-step audit mission."""
        # 1. Security Check
        is_safe, msg = self.guard.scan_input(user_command)
        if not is_safe: return msg

        # 2. Research Phase (Parallel Thinking)
        market_data = self.researcher.fact_check(user_command)

        # 3. Final Audit Synthesis
        final_report = self.brain.analyze(user_command, context_data=doc_text, use_web=True)
        return f"--- ORCHESTRATED REPORT ---\n{final_report}\n\n[Market Reference: {market_data[:200]}...]"
