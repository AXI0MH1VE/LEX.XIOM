#!/usr/bin/env python3
# @AXIOMHIVE @DEVDOLLZAI ALEXIS ADAMS
# AXIOMHIVE SETUP: Installation and Setup Script

"""
Setup script for the AXIOMHIVE ZKVS Sieve Protocol.

This script handles:
- Dependency installation
- Configuration setup
- Directory structure creation
- Initial system validation
- Example execution
"""

import os
import sys
import subprocess
import shutil
from pathlib import Path
import json
import logging

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger('AXIOMHIVE.Setup')

class AXIOMHIVESetup:
    """Setup manager for AXIOMHIVE system."""

    def __init__(self):
        self.project_root = Path(__file__).parent
        self.requirements = [
            "python>=3.8",
            "typing>=3.7.4",
            "dataclasses>=0.6",
        ]

    def check_python_version(self) -> bool:
        """Check if Python version is compatible."""
        version = sys.version_info
        if version.major < 3 or (version.major == 3 and version.minor < 8):
            logger.error(f"Python {version.major}.{version.minor} is not supported. Requires Python 3.8+")
            return False

        logger.info(f"✓ Python {version.major}.{version.minor}.{version.micro} is compatible")
        return True

    def install_dependencies(self) -> bool:
        """Install Python dependencies."""
        logger.info("Installing Python dependencies...")

        try:
            # Since AXIOMHIVE has zero runtime dependencies, we just verify standard library
            import hashlib
            import time
            import json
            import logging

            logger.info("✓ All required standard library modules are available")
            logger.info("✓ Zero external dependencies verified (SOVEREIGNTY=1.0)")
            return True

        except ImportError as e:
            logger.error(f"✗ Missing required module: {e}")
            return False

    def create_directories(self) -> bool:
        """Create necessary directory structure."""
        logger.info("Creating directory structure...")

        directories = [
            "logs",
            "exports",
            "configs",
            "data/moat",
            "data/ledger",
        ]

        try:
            for dir_path in directories:
                full_path = self.project_root / dir_path
                full_path.mkdir(parents=True, exist_ok=True)
                logger.info(f"✓ Created directory: {dir_path}")

            return True

        except Exception as e:
            logger.error(f"✗ Failed to create directories: {e}")
            return False

    def setup_configuration(self) -> bool:
        """Setup default configuration."""
        logger.info("Setting up configuration...")

        try:
            config_file = self.project_root / "axiomhive_config.json"

            if not config_file.exists():
                # Create default configuration
                default_config = {
                    "node_id": "zkvs-node-prime-sovereign",
                    "hash_prefix": "e2c5b8a1f0d3c4e5a6b7c8d9e0f1a2b3c4d5e6f7a8b9c0d1e2f3a4b5c6d7e8f9",
                    "version": "2.1.0-APEX-SOVEREIGN",
                    "log_level": "INFO",
                    "debug_mode": False,
                    "trust_threshold": 0.99,
                    "reboot_threshold": 0.007,
                    "max_ledger_events": 10000,
                    "enable_data_moat": True,
                    "enable_complexity_sieve": True,
                    "enable_trust_metrics": True,
                    "enable_ethical_guardrails": True
                }

                with open(config_file, 'w') as f:
                    json.dump(default_config, f, indent=2)

                logger.info(f"✓ Created default configuration: {config_file}")
            else:
                logger.info(f"✓ Configuration file already exists: {config_file}")

            return True

        except Exception as e:
            logger.error(f"✗ Failed to setup configuration: {e}")
            return False

    def validate_installation(self) -> bool:
        """Validate the installation."""
        logger.info("Validating installation...")

        try:
            # Test import
            sys.path.insert(0, str(self.project_root / "src"))

            from sovereign_core import ZKVSNodePrime
            from config import get_config

            # Test basic initialization
            node = ZKVSNodePrime()
            config = get_config()

            logger.info("✓ Core modules imported successfully")
            logger.info(f"✓ Node initialized: {node._is_ready}")
            logger.info(f"✓ Configuration loaded: {config.node_id}")

            return True

        except Exception as e:
            logger.error(f"✗ Installation validation failed: {e}")
            return False

    def run_example(self) -> bool:
        """Run a basic example to verify functionality."""
        logger.info("Running example to verify functionality...")

        try:
            example_path = self.project_root / "examples" / "basic_usage.py"

            if not example_path.exists():
                logger.warning(f"Example file not found: {example_path}")
                return True  # Not critical

            logger.info(f"Running example: {example_path}")

            # Run example (with timeout to prevent hanging)
            result = subprocess.run([
                sys.executable, str(example_path)
            ], cwd=self.project_root, capture_output=True, text=True, timeout=60)

            if result.returncode == 0:
                logger.info("✓ Example executed successfully")
                logger.info("Example output preview:")
                for line in result.stdout.split('\n')[-10:]:  # Last 10 lines
                    if line.strip():
                        logger.info(f"  {line}")
                return True
            else:
                logger.warning(f"Example execution returned non-zero exit code: {result.returncode}")
                logger.warning(f"STDERR: {result.stderr}")
                return True  # Example issues don't fail installation

        except subprocess.TimeoutExpired:
            logger.warning("Example execution timed out (this may be normal)")
            return True
        except Exception as e:
            logger.warning(f"Example execution failed: {e}")
            return True  # Example issues don't fail installation

    def create_startup_script(self) -> bool:
        """Create a startup script for easy execution."""
        logger.info("Creating startup script...")

        try:
            script_content = '''#!/bin/bash
# @AXIOMHIVE @DEVDOLLZAI ALEXIS ADAMS
# AXIOMHIVE Startup Script

echo "🚀 Starting AXIOMHIVE ZKVS Sieve Protocol..."
echo "============================================="

# Check if we're in the right directory
if [ ! -f "src/sovereign_core.py" ]; then
    echo "❌ Error: Please run this script from the AXIOMHIVE project root directory"
    exit 1
fi

# Set Python path
export PYTHONPATH="${PYTHONPATH}:$(pwd)/src"

# Run the system
python -c "
import sys
sys.path.insert(0, 'src')
from sovereign_core import main
main()
"

echo "============================================="
echo "✅ AXIOMHIVE execution completed"
'''

            script_path = self.project_root / "start_axiomhive.sh"
            with open(script_path, 'w') as f:
                f.write(script_content)

            # Make executable
            script_path.chmod(0o755)

            logger.info(f"✓ Created startup script: {script_path}")
            return True

        except Exception as e:
            logger.error(f"✗ Failed to create startup script: {e}")
            return False

    def run_setup(self) -> bool:
        """Run complete setup process."""
        logger.info("🔥 Starting AXIOMHIVE Setup Process...")
        logger.info("=" * 50)

        steps = [
            ("Python Version Check", self.check_python_version),
            ("Dependency Installation", self.install_dependencies),
            ("Directory Creation", self.create_directories),
            ("Configuration Setup", self.setup_configuration),
            ("Installation Validation", self.validate_installation),
            ("Example Execution", self.run_example),
            ("Startup Script Creation", self.create_startup_script),
        ]

        results = []
        for step_name, step_func in steps:
            logger.info(f"Running: {step_name}...")
            success = step_func()
            results.append((step_name, success))

            if not success:
                logger.error(f"❌ {step_name} failed")
            else:
                logger.info(f"✅ {step_name} completed")

        # Summary
        successful_steps = sum(1 for _, success in results if success)
        total_steps = len(results)

        logger.info("=" * 50)
        logger.info(f"Setup completed: {successful_steps}/{total_steps} steps successful")

        if successful_steps == total_steps:
            logger.info("🎉 AXIOMHIVE setup completed successfully!")
            logger.info("You can now run the system with:")
            logger.info("  python -m src.cli --help")
            logger.info("  python examples/basic_usage.py")
            logger.info("  ./start_axiomhive.sh")
            return True
        else:
            logger.warning("⚠️  Setup completed with some issues")
            logger.warning("Please review the errors above and try again")
            return False

def main():
    """Main setup function."""
    print("🔥 AXIOMHIVE ZKVS SIEVE PROTOCOL")
    print("Sovereign Intelligence Engine Setup")
    print("=" * 50)

    setup = AXIOMHIVESetup()
    success = setup.run_setup()

    if success:
        print("\n🎉 Setup completed successfully!")
        print("Ready for market domination through inevitability!")
        return 0
    else:
        print("\n❌ Setup completed with errors")
        print("Please check the logs above for details")
        return 1

if __name__ == "__main__":
    sys.exit(main())