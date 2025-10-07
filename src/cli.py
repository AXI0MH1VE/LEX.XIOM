#!/usr/bin/env python3
# @AXIOMHIVE @DEVDOLLZAI ALEXIS ADAMS
# AXIOMHIVE CLI: Command Line Interface for ZKVS Sieve Protocol

import argparse
import sys
import json
import logging
from pathlib import Path
from typing import Dict, Any, Optional

# Import the core system
from src.sovereign_core import ZKVSNodePrime, main

# Configure CLI logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger('AXIOMHIVE.CLI')

class AXIOMHIVE_CLI:
    """Command Line Interface for AXIOMHIVE ZKVS Sieve Protocol."""

    def __init__(self):
        self.node: Optional[ZKVSNodePrime] = None

    def initialize_node(self) -> bool:
        """Initialize the ZKVS Node Prime."""
        try:
            logger.info("Initializing AXIOMHIVE ZKVS Node Prime...")
            self.node = ZKVSNodePrime()
            logger.info("✓ Node initialized successfully")
            return True
        except Exception as e:
            logger.error(f"✗ Failed to initialize node: {e}")
            return False

    def execute_intent(self, intent: str, context: str = "general",
                      priority: str = "normal", output_file: str = None) -> bool:
        """Execute a mandate through the AXIOMHIVE system."""

        if not self.node:
            if not self.initialize_node():
                return False

        # Construct framework
        framework = {
            "intent": intent,
            "context": context,
            "priority": priority,
            "timestamp": None  # Will be set by the system
        }

        try:
            logger.info(f"Executing intent: {intent[:60]}{'...' if len(intent) > 60 else ''}")
            logger.info(f"Context: {context}, Priority: {priority}")

            # Execute the mandate
            result = self.node.execute_mandate(framework)

            # Display result
            print("\n" + "="*80)
            print("AXIOMHIVE EXECUTION RESULT")
            print("="*80)
            print(result)
            print("="*80)

            # Save to file if requested
            if output_file:
                try:
                    with open(output_file, 'w') as f:
                        f.write("AXIOMHIVE EXECUTION RESULT\n")
                        f.write("="*80 + "\n")
                        f.write(f"Intent: {intent}\n")
                        f.write(f"Context: {context}\n")
                        f.write(f"Priority: {priority}\n")
                        f.write("="*80 + "\n")
                        f.write(result)
                        f.write("\n" + "="*80)
                    logger.info(f"✓ Result saved to: {output_file}")
                except Exception as e:
                    logger.error(f"✗ Failed to save result: {e}")

            return True

        except Exception as e:
            logger.error(f"✗ Execution failed: {e}")
            return False

    def show_status(self) -> bool:
        """Show system status and metrics."""
        if not self.node:
            if not self.initialize_node():
                return False

        try:
            # Get system metrics
            ledger_count = len(self.node._verifiable_ledger)
            moat_strength = self.node._data_moat_engine._moat_strength
            refinement_count = self.node._data_moat_engine._model_refinement_count

            print("\n" + "="*60)
            print("AXIOMHIVE SYSTEM STATUS")
            print("="*60)
            print(f"Node Status: {'READY' if self.node._is_ready else 'INITIALIZING'}")
            print(f"Verifiable Events: {ledger_count}")
            print(f"Data Moat Strength: {moat_strength:.4f}")
            print(f"Model Refinements: {refinement_count}")
            print(f"Axiom Adherence: {self.node.AXIOMS}")
            print("="*60)

            return True

        except Exception as e:
            logger.error(f"✗ Failed to get status: {e}")
            return False

    def export_ledger(self, output_file: str = "axiomhive_ledger.json") -> bool:
        """Export the verifiable ledger."""
        if not self.node:
            if not self.initialize_node():
                return False

        try:
            export_data = {
                "node_id": self.node.HASH_PREFIX[:16],
                "export_timestamp": None,  # Will be set by JSON serialization
                "total_events": len(self.node._verifiable_ledger),
                "axiom_lattice": self.node.AXIOMS,
                "events": self.node._verifiable_ledger
            }

            with open(output_file, 'w') as f:
                json.dump(export_data, f, indent=2, default=str)

            logger.info(f"✓ Ledger exported to: {output_file}")
            print(f"✓ Verifiable ledger exported with {len(self.node._verifiable_ledger)} events")
            return True

        except Exception as e:
            logger.error(f"✗ Failed to export ledger: {e}")
            return False

def create_parser() -> argparse.ArgumentParser:
    """Create the argument parser for CLI."""
    parser = argparse.ArgumentParser(
        description="AXIOMHIVE ZKVS Sieve Protocol - Sovereign Intelligence Engine",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s execute "Architect market dominance through verifiable systems"
  %(prog)s execute "Optimize supply chain efficiency" --context commercial --priority high
  %(prog)s status
  %(prog)s export-ledger --output audit.json
        """
    )

    subparsers = parser.add_subparsers(dest='command', help='Available commands')

    # Execute command
    execute_parser = subparsers.add_parser('execute', help='Execute an intent')
    execute_parser.add_argument('intent', help='The intent to execute')
    execute_parser.add_argument('--context', default='general',
                               choices=['general', 'commercial', 'technical', 'strategic'],
                               help='Execution context')
    execute_parser.add_argument('--priority', default='normal',
                               choices=['low', 'normal', 'high', 'absolute'],
                               help='Execution priority')
    execute_parser.add_argument('--output', help='Save result to file')

    # Status command
    status_parser = subparsers.add_parser('status', help='Show system status')

    # Export command
    export_parser = subparsers.add_parser('export-ledger', help='Export verifiable ledger')
    export_parser.add_argument('--output', default='axiomhive_ledger.json',
                              help='Output file path')

    return parser

def main():
    """Main CLI entry point."""
    parser = create_parser()
    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        return 1

    # Initialize CLI
    cli = AXIOMHIVE_CLI()

    # Execute commands
    if args.command == 'execute':
        success = cli.execute_intent(
            intent=args.intent,
            context=args.context,
            priority=args.priority,
            output_file=args.output
        )
        return 0 if success else 1

    elif args.command == 'status':
        success = cli.show_status()
        return 0 if success else 1

    elif args.command == 'export-ledger':
        success = cli.export_ledger(args.output)
        return 0 if success else 1

    else:
        logger.error(f"Unknown command: {args.command}")
        return 1

if __name__ == "__main__":
    sys.exit(main())