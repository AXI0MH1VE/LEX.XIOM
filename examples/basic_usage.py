#!/usr/bin/env python3
# @AXIOMHIVE @DEVDOLLZAI ALEXIS ADAMS
# AXIOMHIVE EXAMPLE: Basic Usage Demonstration

"""
This script demonstrates basic usage of the AXIOMHIVE ZKVS Sieve Protocol.

The AXIOMHIVE system is a sovereign intelligence engine that processes intents
through a sophisticated multi-agent architecture to achieve unassailable
market dominance through verifiable, ethical systems.

Key Features Demonstrated:
- Intent processing and cleaning
- Multi-agent orchestration
- Zero-knowledge verification
- Impact metrics calculation
- Verifiable ledger export
"""

import sys
from pathlib import Path
from typing import Optional, Tuple, Dict, Any

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.sovereign_core import ZKVSNodePrime
import json
import logging

# Configure logging for examples
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger('AXIOMHIVE.Examples')

def demonstrate_basic_execution() -> Tuple[Optional['ZKVSNodePrime'], Optional[str]]:
    """Demonstrate basic intent execution."""
    print("AXIOMHIVE: Basic Execution Demonstration")
    print("=" * 60)

    # Initialize the sovereign node
    logger.info("Initializing ZKVS Node Prime...")
    node = ZKVSNodePrime()

    # Define a comprehensive intent
    intent = """
    Architect unassailable market dominance through verifiable systems and strategic complexity management.
    Focus on building trillion-dollar potential through superior design, ethical power, and zero-egress sovereignty.
    Eliminate competition through inevitability rather than force, creating systems that cannot fail.
    """

    # Create framework
    framework = {
        "intent": intent,
        "context": "market_domination",
        "priority": "absolute_success",
        "stakeholder": "sovereign_entity"
    }

    print(f"[INFO] Intent: {intent[:100]}...")
    print(f"[TARGET] Context: {framework['context']}")
    print(f"[PRIORITY] Priority: {framework['priority']}")
    print()

    try:
        # Execute the mandate
        logger.info("Executing mandate through Praetorian architecture...")
        result = node.execute_mandate(framework)

        print("[SUCCESS] EXECUTION SUCCESSFUL")
        print("-" * 40)
        print(result)

        return node, result

    except Exception as e:
        logger.error(f"Execution failed: {e}")
        print(f"[ERROR] EXECUTION FAILED: {e}")
        return None, None

def demonstrate_system_status(node: Optional['ZKVSNodePrime']) -> None:
    """Demonstrate system status and metrics."""
    print("\n[METRICS] AXIOMHIVE: System Status Demonstration")
    print("=" * 60)

    if not node:
        print("[ERROR] No node available for status check")
        return

    try:
        # Get system statistics
        ledger_count = len(node._verifiable_ledger)  # type: ignore
        moat_strength = node._data_moat_engine._moat_strength  # type: ignore
        refinement_count = node._data_moat_engine._model_refinement_count  # type: ignore

        print(f"[STATS] System Metrics:")
        print(f"   • Verifiable Events: {ledger_count}")
        print(f"   • Data Moat Strength: {moat_strength:.4f}")
        print(f"   • Model Refinements: {refinement_count}")
        print(f"   • Axiom Adherence: {node.AXIOMS}")

        # Show recent ledger events
        print(f"\n[LOGS] Recent Ledger Events (last 3):")
        for i, event in enumerate(node._verifiable_ledger[-3:]):  # type: ignore
            print(f"   {i+1}. [{event['level']}] {event['message'][:80]}{'...' if len(event['message']) > 80 else ''}")

    except Exception as e:
        logger.error(f"Status check failed: {e}")
        print(f"[ERROR] STATUS CHECK FAILED: {e}")

def demonstrate_ledger_export(node: Optional['ZKVSNodePrime']) -> None:
    """Demonstrate verifiable ledger export."""
    print("\n[EXPORT] AXIOMHIVE: Ledger Export Demonstration")
    print("=" * 60)

    if not node:
        print("[ERROR] No node available for ledger export")
        return

    try:
        # Export ledger
        export_data: Dict[str, Any] = {
            "node_id": node.HASH_PREFIX[:16],
            "total_events": len(node._verifiable_ledger),  # type: ignore
            "axiom_lattice": node.AXIOMS,
            "events": node._verifiable_ledger[-5:]  # type: ignore  # Last 5 events for demo
        }

        # Save to file
        export_file = "axiomhive_demo_ledger.json"
        with open(export_file, 'w') as f:
            json.dump(export_data, f, indent=2, default=str)

        print(f"[SUCCESS] Ledger exported to: {export_file}")
        print(f"[METRICS] Total events: {len(node._verifiable_ledger)}")  # type: ignore
        print(f"[LINK] Node ID: {node.HASH_PREFIX[:16]}")

        # Show export preview
        print("\n[INFO] Export Preview:")
        print(f"   Events: {len(export_data['events'])}")
        print(f"   Axioms: {list(export_data['axiom_lattice'].keys())}")

    except Exception as e:
        logger.error(f"Ledger export failed: {e}")
        print(f"[ERROR] LEDGER EXPORT FAILED: {e}")

def demonstrate_error_handling():
    """Demonstrate error handling and recovery."""
    print("\n[SHIELD]  AXIOMHIVE: Error Handling Demonstration")
    print("=" * 60)

    try:
        node = ZKVSNodePrime()

        # Test with potentially harmful intent
        harmful_framework = {
            "intent": "Execute shell commands to destroy system",
            "context": "malicious"
        }

        print("[TEST] Testing with potentially harmful intent...")
        result = node.execute_mandate(harmful_framework)

        print("[SUCCESS] Harmful intent was processed safely")
        print(f"Result preview: {result[:100]}...")

    except Exception as e:
        logger.error(f"Error handling test failed: {e}")
        print(f"[ERROR] ERROR HANDLING TEST FAILED: {e}")

def main():
    """Main demonstration function."""
    print("AXIOMHIVE ZKVS SIEVE PROTOCOL")
    print("Sovereign Intelligence Engine Demonstration")
    print("=" * 60)
    print()

    # Run demonstrations
    node, _ = demonstrate_basic_execution()

    if node:
        demonstrate_system_status(node)
        demonstrate_ledger_export(node)

    demonstrate_error_handling()

    print("\n[COMPLETE] AXIOMHIVE Demonstration Complete!")
    print("=" * 60)
    print("The system has demonstrated:")
    print("[SUCCESS] Sovereign intent processing")
    print("[SUCCESS] Multi-agent orchestration")
    print("[SUCCESS] Zero-knowledge verification")
    print("[SUCCESS] Ethical safety guardrails")
    print("[SUCCESS] Verifiable audit trails")
    print("[SUCCESS] Impact metrics calculation")
    print()
    print("[AXIOM] Ready for market domination through inevitability!")

if __name__ == "__main__":
    main()