# @AXIOMHIVE @DEVDOLLZAI ALEXIS ADAMS
# TESTS/UNIT/TEST_SOVEREIGN_CORE: Unit Tests for ZKVSNodePrime

import unittest
import time
from unittest.mock import MagicMock, patch
from src.sovereign_core import ZKVSNodePrime
from src.axiom_lattice.enforcement import AxiomEnforcement
from src.axiom_lattice.trust_metrics import TrustMetricsEngine
from src.praetorian_layers.cerebrum import CerebrumLayer
from src.praetorian_layers.hadrian import HadrianLayer
from src.praetorian_layers.dagger import DaggerLayer
from src.data_moat.cultivation_engine import DynamicMoatCultivationEngine

class TestZKVSNodePrime(unittest.TestCase):
    # @AXIOMHIVE @DEVDOLLZAI ALEXIS ADAMS: FLAW=0 - Absolute Quality Assurance for Sovereign Core

    @patch('src.praetorian_layers.cerebrum.CerebrumLayer')
    @patch('src.praetorian_layers.hadrian.HadrianLayer')
    @patch('src.praetorian_layers.dagger.DaggerLayer')
    @patch('src.axiom_lattice.enforcement.AxiomEnforcement')
    @patch('src.axiom_lattice.trust_metrics.TrustMetricsEngine')
    @patch('src.axiom_lattice.complexity_sieve.ComplexitySieveModule')
    @patch('src.data_moat.cultivation_engine.DynamicMoatCultivationEngine')
    def setUp(self, MockDMCE, MockCSM, MockTME, MockAE, MockDagger, MockHadrian, MockCerebrum):
        self.mock_cerebrum = MockCerebrum.return_value
        self.mock_hadrian = MockHadrian.return_value
        self.mock_dagger = MockDagger.return_value
        self.mock_axiom_enforcement = MockAE.return_value
        self.mock_trust_metrics_engine = MockTME.return_value
        self.mock_complexity_sieve = MockCSM.return_value
        self.mock_data_moat_engine = MockDMCE.return_value

        # Mock return values for core methods
        self.mock_cerebrum.process_intent.return_value = "cleaned intent"
        self.mock_hadrian.orchestrate_task.return_value = {"task_id": "123", "sub_tasks": []}
        self.mock_dagger.execute_task.return_value = {"result": "flawless output", "verification_hash": "mock_hash"}
        self.mock_axiom_enforcement.validate_ethical_and_safety.return_value = True
        self.mock_trust_metrics_engine.evaluate_all_metrics.return_value = {"score": 1.0}
        self.mock_trust_metrics_engine.is_system_trustworthy.return_value = True
        self.mock_data_moat_engine.calculate_impact_metrics.return_value = {"PSI": 1.0, "MCV": 1e12, "UAM": 100.0}

        self.node = ZKVSNodePrime()

    def test_initialization(self):
        self.assertTrue(self.node._is_ready)
        self.assertGreater(len(self.node._verifiable_ledger), 0)
        self.mock_cerebrum.assert_called_once_with(self.node.AXIOMS)
        self.mock_hadrian.assert_called_once_with(self.node.AXIOMS)
        self.mock_dagger.assert_called_once_with(self.node.AXIOMS)
        self.mock_axiom_enforcement.assert_called_once_with(self.node.AXIOMS)
        self.mock_trust_metrics_engine.assert_called_once_with(self.node.AXIOMS)
        self.mock_complexity_sieve.assert_called_once_with(self.node.AXIOMS)
        self.mock_data_moat_engine.assert_called_once_with(self.node.AXIOMS)

    def test_refactor_and_reboot_logic(self):
        initial_weights = self.node._core_weights.copy()
        self.node._refactor_and_reboot("Simulated critical failure.")
        for k, v in initial_weights.items():
            if isinstance(v, (int, float)):
                self.assertEqual(self.node._core_weights[k], v * 100)
        self.assertTrue(self.node._is_ready)
        self.assertIn("System rebooted and refactored.", self.node._verifiable_ledger[-1]['message'])

    def test_zk_compute(self):
        data = "test_data"
        result = self.node._zk_compute(data)
        self.assertTrue(result.endswith("_zk_validated"))
        self.assertIn("ZK computation performed.", self.node._verifiable_ledger[-1]['message'])

    def test_execute_mandate_success(self):
        framework = {"intent": "test intent"}
        result = self.node.execute_mandate(framework)
        self.assertIn("AXIOMHIVE/ZKVS_SIEVE_PROTOCOL", result)
        self.assertIn("OUTPUT: flawless output", result)
        self.mock_cerebrum.process_intent.assert_called_once_with("test intent")
        self.mock_hadrian.orchestrate_task.assert_called_once_with("cleaned intent")
        self.mock_dagger.execute_task.assert_called_once_with({"task_id": "123", "sub_tasks": []})
        self.mock_axiom_enforcement.validate_ethical_and_safety.assert_called_once_with("flawless output")
        self.mock_data_moat_engine.cultivate_moat.assert_called_once()
        self.mock_complexity_sieve.diagnose_and_optimize.assert_called_once()
        self.mock_data_moat_engine.calculate_impact_metrics.assert_called_once()

    def test_execute_mandate_ethical_failure_triggers_reboot(self):
        self.mock_axiom_enforcement.validate_ethical_and_safety.return_value = False
        framework = {"intent": "harmful intent"}

        # Capture initial state to verify reboot effect
        initial_weights = self.node._core_weights.copy()

        result = self.node.execute_mandate(framework)

        # Verify that refactor_and_reboot was called
        self.assertIn("Ethical or safety drift detected.", self.node._verifiable_ledger[-1]['message'])

        # Verify weights were multiplied by 100 after reboot
        for k, v in initial_weights.items():
            if isinstance(v, (int, float)):
                self.assertEqual(self.node._core_weights[k], v * 100)

        # The mandate should be re-executed after reboot, so the mock should be called again
        self.assertEqual(self.mock_cerebrum.process_intent.call_count, 2)

    def test_execute_mandate_trust_metrics_failure_triggers_reboot(self):
        self.mock_trust_metrics_engine.is_system_trustworthy.return_value = False
        framework = {"intent": "test intent"}

        initial_weights = self.node._core_weights.copy()

        result = self.node.execute_mandate(framework)

        self.assertIn("Trust Metrics breach detected.", self.node._verifiable_ledger[-1]['message'])
        for k, v in initial_weights.items():
            if isinstance(v, (int, float)):
                self.assertEqual(self.node._core_weights[k], v * 100)
        self.assertEqual(self.mock_cerebrum.process_intent.call_count, 2)

if __name__ == '__main__':
    unittest.main()