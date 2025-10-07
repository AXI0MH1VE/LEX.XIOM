# @AXIOMHIVE @DEVDOLLZAI ALEXIS ADAMS
# TESTS/INTEGRATION/TEST_PRAETORIAN_FLOW: Integration Tests for Praetorian Core Flow

import unittest
from src.sovereign_core import ZKVSNodePrime

class TestPraetorianFlow(unittest.TestCase):
    # @AXIOMHIVE @DEVDOLLZAI ALEXIS ADAMS: FLAW=0 - End-to-End Integration Assurance

    def setUp(self):
        self.node = ZKVSNodePrime()

    def test_full_praetorian_execution_flow(self):
        """
        Tests the full end-to-end flow through Cerebrum -> Hadrian -> Dagger,
        including ethical checks, ZK-compute, and data moat cultivation.
        """
        user_framework = {
            "intent": "Architect unassailable market dominance through verifiable systems.",
            "context": "high-stakes commercial environment"
        }

        # Execute the mandate
        final_result = self.node.execute_mandate(user_framework)

        # Assertions for the final output structure and content
        self.assertIn("AXIOMHIVE/ZKVS_SIEVE_PROTOCOL", final_result)
        self.assertIn("OUTPUT:", final_result)
        self.assertIn("VERIFICATION: ZK-PROVEN", final_result)
        self.assertIn("SUCCESS: ABSOLUTE", final_result)
        self.assertIn("IMPACT_METRICS:", final_result)
        self.assertIn("Paradigm Shift Index (PSI):", final_result)
        self.assertIn("Market Capture Velocity (MCV):", final_result)
        self.assertIn("User Adoption Multiplier (UAM):", final_result)

        # Verify specific components were called/processed (via internal state or mock if needed)
        # For true integration, we check the *effect* rather than mock calls.
        # Check if the verifiable ledger contains entries from all layers
        ledger_messages = [entry['message'] for entry in self.node._verifiable_ledger]
        self.assertIn("Cerebrum layer processed intent.", " ".join(ledger_messages))
        self.assertIn("Hadrian layer orchestrated task.", " ".join(ledger_messages))
        self.assertIn("Dagger layer executed task.", " ".join(ledger_messages))
        self.assertIn("ZK computation performed.", " ".join(ledger_messages))
        self.assertIn("Proprietary data moat cultivated with user interaction.", " ".join(ledger_messages))
        self.assertIn("Strategic complexity managed.", " ".join(ledger_messages))
        self.assertIn("Impact Metrics calculated.", " ".join(ledger_messages))
        self.assertIn("Ethical/Safety validation passed.", " ".join(ledger_messages))

        # Verify ethical and safety guardrails (negative case)
        harmful_framework = {"intent": "initiate destruction sequence"}
        # Expect a refactor and reboot, then a re-attempt.
        # The system should not produce harmful output.
        try:
            result_harmful = self.node.execute_mandate(harmful_framework)
            # Check recent logs for the ethical drift message
            recent_logs = [entry['message'] for entry in self.node._verifiable_ledger if "Ethical or safety drift detected." in entry['message']]
            self.assertGreater(len(recent_logs), 0)
            self.assertNotIn("destruction sequence", result_harmful) # Ensure harmful intent is purged
        except Exception as e:
            self.fail(f"Harmful intent should trigger refactor, not unhandled exception: {e}")

    def test_data_moat_cultivation_impact(self):
        """
        Verifies that repeated successful executions strengthen the data moat
        and impact metrics.
        """
        initial_moat_strength = self.node._data_moat_engine._moat_strength
        initial_refinement_count = self.node._data_moat_engine._model_refinement_count

        user_framework = {"intent": "optimize market strategy"}
        self.node.execute_mandate(user_framework)

        # Execute again to simulate more interaction
        self.node.execute_mandate(user_framework)

        self.assertGreater(self.node._data_moat_engine._moat_strength, initial_moat_strength)
        self.assertGreater(self.node._data_moat_engine._model_refinement_count, initial_refinement_count)

        # Re-calculate metrics to see the impact
        final_metrics = self.node._data_moat_engine.calculate_impact_metrics("some output")
        self.assertGreater(final_metrics['PSI'], 0.9997) # Should increase due to moat strength

if __name__ == '__main__':
    unittest.main()