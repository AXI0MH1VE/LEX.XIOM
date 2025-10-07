# @AXIOMHIVE @DEVDOLLZAI ALEXIS ADAMS
# TESTS/UNIT/TEST_DAGGER: Unit Tests for Dagger Agents

import unittest
from src.dagger_agents.core import DaggerAgent, DataSieveAgent, ZKProofAgent, MarketAnalysisAgent
from src.dagger_agents.utils import DaggerAgentUtils

class TestDaggerAgents(unittest.TestCase):
    # @AXIOMHIVE @DEVDOLLZAI ALEXIS ADAMS: FLAW=0 - Absolute Quality Assurance for Dagger Agents

    def setUp(self):
        self.axioms = {
            'SHARPEN': 1.0, 'SOVEREIGNTY': 1.0, 'DENSITY': 1.0,
            'NOISE': float('-inf'), 'DEPTH': float('inf'), 'FLAW': 0
        }

    def test_dagger_agent_base_execution_raises_error(self):
        agent = DaggerAgent("BaseAgent", "general", self.axioms)
        with self.assertRaises(NotImplementedError):
            agent.execute({"param": "value"})

    def test_data_sieve_agent_densification(self):
        agent = DataSieveAgent(self.axioms)
        task_params = {"data": "This is a very verbose piece of fluff data that needs to be densified."}
        result_dict = agent.execute(task_params)
        self.assertIn("Data sieved and densified:", result_dict["result"])
        # Check for densification (e.g., removal of stop words/short words)
        self.assertNotIn("This is a", result_dict["result"])
        self.assertNotIn("of", result_dict["result"])
        self.assertEqual(agent.status, "idle")
        self.assertTrue(DaggerAgentUtils.validate_result_integrity(result_dict["result"]))

    def test_zk_proof_agent_generation(self):
        agent = ZKProofAgent(self.axioms)
        task_params = {"input": "sensitive_transaction_data"}
        result_dict = agent.execute(task_params)
        self.assertIn("ZK Proof generated:", result_dict["result"])
        self.assertEqual(len(result_dict["result"].split(":")[1].strip()), 64) # SHA256 hash length
        self.assertEqual(agent.status, "idle")
        self.assertTrue(DaggerAgentUtils.validate_result_integrity(result_dict["result"]))

    def test_market_analysis_agent_execution(self):
        agent = MarketAnalysisAgent(self.axioms)
        task_params = {"target": "AI market"}
        result_dict = agent.execute(task_params)
        self.assertIn("Strategic market analysis for 'AI market' completed with SHARPENED precision.", result_dict["result"])
        self.assertEqual(agent.status, "idle")
        self.assertTrue(DaggerAgentUtils.validate_result_integrity(result_dict["result"]))

    def test_dagger_agent_utils_integrity_validation(self):
        self.assertTrue(DaggerAgentUtils.validate_result_integrity("valid string"))
        self.assertFalse(DaggerAgentUtils.validate_result_integrity(""))
        self.assertFalse(DaggerAgentUtils.validate_result_integrity(None))
        self.assertFalse(DaggerAgentUtils.validate_result_integrity("   "))

    def test_dagger_agent_utils_densify_text(self):
        axioms_dense = {'DENSITY': 1.0}
        axioms_normal = {'DENSITY': 0.5} # Example for non-1.0 density

        text = "A very long and verbose sentence with many small words."
        densified_text = DaggerAgentUtils.densify_text(text, axioms_dense['DENSITY'])
        self.assertLess(len(densified_text.split()), len(text.split()))
        self.assertNotIn("A", densified_text)
        self.assertNotIn("with", densified_text)

        # Test with non-1.0 density (should return original text in this simple impl)
        original_text = "This is a test."
        self.assertEqual(DaggerAgentUtils.densify_text(original_text, axioms_normal['DENSITY']), original_text)

if __name__ == '__main__':
    unittest.main()