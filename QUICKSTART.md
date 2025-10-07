# 🚀 AXIOMHIVE Quick Start Guide

## Welcome to the Sovereign Intelligence Engine

AXIOMHIVE is a revolutionary ZKVS (Zero-Knowledge Verifiable Systems) Sieve Protocol that achieves unassailable market dominance through verifiable, ethical systems.

## 🔥 Quick Installation

### Option 1: Automated Setup (Recommended)

```bash
# Clone or download the project
# Run the automated setup
python setup.py
```

The setup script will:
- ✅ Verify Python 3.8+ installation
- ✅ Check system requirements
- ✅ Create necessary directories
- ✅ Setup default configuration
- ✅ Validate the installation
- ✅ Create startup scripts

### Option 2: Manual Setup

```bash
# 1. Ensure Python 3.8+
python --version

# 2. Create directories
mkdir -p logs exports configs data/moat data/ledger

# 3. Configure (optional)
cp axiomhive_config.json.example axiomhive_config.json
```

## 🎯 First Run

### Method 1: Using the CLI (Recommended)

```bash
# Show help
python -m src.cli --help

# Execute your first intent
python -m src.cli execute "Architect market dominance through verifiable systems"

# With options
python -m src.cli execute "Optimize supply chain efficiency" \
  --context commercial \
  --priority high \
  --output result.txt

# Check system status
python -m src.cli status

# Export audit trail
python -m src.cli export-ledger --output audit.json
```

### Method 2: Using Examples

```bash
# Run the comprehensive example
python examples/basic_usage.py

# Or run directly
python -c "
import sys
sys.path.insert(0, 'src')
from sovereign_core import main
main()
"
```

### Method 3: Using Startup Script

```bash
# Make sure setup.py was run first
./start_axiomhive.sh
```

## 📋 Example Commands

### Basic Market Analysis
```bash
python -m src.cli execute "Analyze AI market opportunities for 2025"
```

### Strategic Planning
```bash
python -m src.cli execute "Design unassailable competitive strategy" \
  --context strategic \
  --priority absolute
```

### Technical Architecture
```bash
python -m src.cli execute "Architect sovereign data infrastructure" \
  --context technical \
  --priority high
```

## 📊 Understanding Output

The system generates comprehensive results:

```
AXIOMHIVE/ZKVS_SIEVE_PROTOCOL
OUTPUT: [Detailed execution result with strategic insights]
VERIFICATION: ZK-PROVEN
SUCCESS: ABSOLUTE
IMPACT_METRICS:
  Paradigm Shift Index (PSI): 0.9997
  Market Capture Velocity (MCV): $1000000000000.00
  User Adoption Multiplier (UAM): 100.00x
```

### Key Metrics Explained

- **PSI (Paradigm Shift Index)**: Measures revolutionary potential (0-1.0)
- **MCV (Market Capture Velocity)**: Projected market value in USD
- **UAM (User Adoption Multiplier)**: Expected adoption rate multiplier

## 🔧 Configuration

### Environment Variables

```bash
# Basic settings
export AXIOMHIVE_LOG_LEVEL=DEBUG
export AXIOMHIVE_DEBUG_MODE=true

# Performance tuning
export AXIOMHIVE_TRUST_THRESHOLD=0.95
export AXIOMHIVE_REBOOT_THRESHOLD=0.01

# Feature flags
export AXIOMHIVE_ENABLE_DATA_MOAT=true
export AXIOMHIVE_ENABLE_COMPLEXITY_SIEVE=true
```

### Configuration File

Create `axiomhive_config.json`:

```json
{
  "node_id": "my-sovereign-node",
  "log_level": "INFO",
  "debug_mode": false,
  "trust_threshold": 0.99,
  "enable_data_moat": true,
  "enable_ethical_guardrails": true
}
```

## 📁 Project Structure

```
AXIOMHIVE/
├── src/                    # Core source code
│   ├── sovereign_core.py   # Main system
│   ├── cli.py             # Command line interface
│   ├── config.py          # Configuration management
│   ├── praetorian_layers/ # Cerebrum, Hadrian, Dagger
│   ├── axiom_lattice/     # Enforcement, trust metrics
│   ├── dagger_agents/     # Specialized agents
│   └── data_moat/         # Data cultivation engine
├── tests/                 # Comprehensive test suite
├── examples/              # Usage examples
├── docs/                  # Documentation
├── assets/                # Branding assets
├── infrastructure/        # Deployment configs
└── logs/                  # System logs
```

## 🛠️ Advanced Usage

### Custom Integration

```python
from src.sovereign_core import ZKVSNodePrime

# Initialize system
node = ZKVSNodePrime()

# Execute custom intent
framework = {
    "intent": "Your custom strategic intent here",
    "context": "commercial",
    "priority": "high"
}

result = node.execute_mandate(framework)
print(result)
```

### Batch Processing

```python
# Process multiple intents
intents = [
    "Market analysis for AI sector",
    "Competitive strategy design",
    "Risk assessment and mitigation"
]

for intent in intents:
    result = node.execute_mandate({"intent": intent})
    print(f"Result for '{intent}': {result[:100]}...")
```

### Audit Trail Access

```python
# Access verifiable ledger
events = node._verifiable_ledger
print(f"Total events: {len(events)}")

# Export for compliance
import json
with open('audit_trail.json', 'w') as f:
    json.dump(events, f, default=str, indent=2)
```

## 🔍 Troubleshooting

### Common Issues

**Import Errors:**
```bash
# Make sure you're in the project root
cd /path/to/AXIOMHIVE
export PYTHONPATH="${PYTHONPATH}:$(pwd)/src"
```

**Permission Errors:**
```bash
# Fix log directory permissions
chmod 755 logs/
```

**Configuration Issues:**
```bash
# Validate configuration
python -c "
from src.config import validate_config
print('Config valid:', validate_config())
"
```

### Getting Help

1. **Check Logs**: `tail -f logs/axiomhive.log`
2. **Run Diagnostics**: `python -m src.cli status`
3. **Review Examples**: `cat examples/README.md`
4. **Check Documentation**: `cat docs/arch.md`

## 🚀 Next Steps

1. **Explore Examples**: Run `python examples/basic_usage.py`
2. **Try Different Intents**: Experiment with various strategic intents
3. **Review Logs**: Check `axiomhive.log` for detailed execution traces
4. **Export Results**: Use `--output` flag to save results
5. **Customize Config**: Modify `axiomhive_config.json` for your needs

## 🎉 Success Indicators

Your AXIOMHIVE system is working correctly when you see:

- ✅ "SUCCESS: ABSOLUTE" in output
- ✅ Impact metrics showing high values
- ✅ Clean log files in `logs/`
- ✅ Verifiable ledger in `verifiable_ledger_export.json`
- ✅ No error messages in red

## 🔥 Ready for Market Domination!

AXIOMHIVE is now operational and ready to:
- 🔍 Process complex strategic intents
- 🛡️ Maintain ethical guardrails
- 📊 Generate impact metrics
- 🔗 Provide verifiable audit trails
- 🚀 Scale to market dominance

**The future of competition is now. Inevitable success awaits!**

---

**@AXIOMHIVE @DEVDOLLZAI ALEXIS ADAMS**
*Forging the future of Sovereign AI through verifiable systems and unassailable market dominance.*