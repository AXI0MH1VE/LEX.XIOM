# @AXIOMHIVE @DEVDOLLZAI ALEXIS ADAMS
# AXIOMHIVE CONFIG: Configuration Management System

"""
Configuration management for the AXIOMHIVE ZKVS Sieve Protocol.

This module provides centralized configuration management with support for:
- Environment-based configuration
- Runtime configuration updates
- Configuration validation
- Secure credential management
- Performance tuning parameters
"""

import os
import json
import logging
from typing import Dict, Any, Optional
from dataclasses import dataclass, asdict
from pathlib import Path

logger = logging.getLogger('AXIOMHIVE.Config')

@dataclass
class AXIOMHIVEConfig:
    """Configuration dataclass for AXIOMHIVE system."""

    # Core system settings
    node_id: str = "zkvs-node-prime-sovereign"
    hash_prefix: str = "e2c5b8a1f0d3c4e5a6b7c8d9e0f1a2b3c4d5e6f7a8b9c0d1e2f3a4b5c6d7e8f9"
    version: str = "2.1.0-APEX-SOVEREIGN"

    # Performance settings
    reboot_threshold: float = 0.007  # 7ms threshold
    max_ledger_events: int = 10000
    density_threshold: float = 3.5
    trust_threshold: float = 0.99

    # Security settings
    zk_proof_model: str = "PlonK-over-HyperPlonK"
    encryption_enabled: bool = True
    audit_log_enabled: bool = True

    # Logging settings
    log_level: str = "INFO"
    log_file: str = "axiomhive.log"
    log_max_size: int = 10485760  # 10MB
    log_backup_count: int = 5

    # Feature flags
    enable_data_moat: bool = True
    enable_complexity_sieve: bool = True
    enable_trust_metrics: bool = True
    enable_ethical_guardrails: bool = True

    # Network settings (for future distributed deployment)
    enable_networking: bool = False
    listen_port: int = 8080
    max_connections: int = 100

    # Development settings
    debug_mode: bool = False
    profile_performance: bool = False

class ConfigManager:
    """Configuration manager for AXIOMHIVE system."""

    def __init__(self, config_file: str = "axiomhive_config.json"):
        self.config_file = Path(config_file)
        self._config: Optional[AXIOMHIVEConfig] = None
        self._loaded_from_file = False

    def load_config(self) -> AXIOMHIVEConfig:
        """Load configuration from file or create default."""
        if self._config is not None:
            return self._config

        # Try to load from file
        if self.config_file.exists():
            try:
                with open(self.config_file, 'r') as f:
                    config_data = json.load(f)

                # Merge with default config
                default_config = AXIOMHIVEConfig()
                default_dict = asdict(default_config)

                # Update default with file values
                for key, value in config_data.items():
                    if key in default_dict:
                        setattr(default_config, key, value)

                self._config = default_config
                self._loaded_from_file = True
                logger.info(f"Configuration loaded from {self.config_file}")

            except Exception as e:
                logger.warning(f"Failed to load config from {self.config_file}: {e}")
                logger.info("Using default configuration")
                self._config = AXIOMHIVEConfig()
        else:
            logger.info(f"Config file {self.config_file} not found, using defaults")
            self._config = AXIOMHIVEConfig()

        # Override with environment variables
        self._apply_environment_overrides()

        return self._config

    def _apply_environment_overrides(self):
        """Apply environment variable overrides to configuration."""
        if not self._config:
            return

        # Environment variable mappings
        env_mappings = {
            'AXIOMHIVE_NODE_ID': 'node_id',
            'AXIOMHIVE_HASH_PREFIX': 'hash_prefix',
            'AXIOMHIVE_LOG_LEVEL': 'log_level',
            'AXIOMHIVE_DEBUG_MODE': 'debug_mode',
            'AXIOMHIVE_TRUST_THRESHOLD': 'trust_threshold',
            'AXIOMHIVE_REBOOT_THRESHOLD': 'reboot_threshold',
            'AXIOMHIVE_MAX_LEDGER_EVENTS': 'max_ledger_events',
        }

        for env_var, config_attr in env_mappings.items():
            value = os.getenv(env_var)
            if value is not None:
                # Type conversion
                if config_attr in ['debug_mode', 'enable_data_moat', 'enable_complexity_sieve',
                                 'enable_trust_metrics', 'enable_ethical_guardrails', 'enable_networking',
                                 'encryption_enabled', 'audit_log_enabled', 'profile_performance']:
                    value = value.lower() in ('true', '1', 'yes', 'on')
                elif config_attr in ['trust_threshold', 'reboot_threshold', 'density_threshold']:
                    try:
                        value = float(value)
                    except ValueError:
                        logger.warning(f"Invalid float value for {env_var}: {value}")
                        continue
                elif config_attr in ['max_ledger_events', 'log_max_size', 'log_backup_count',
                                   'listen_port', 'max_connections']:
                    try:
                        value = int(value)
                    except ValueError:
                        logger.warning(f"Invalid int value for {env_var}: {value}")
                        continue

                setattr(self._config, config_attr, value)
                logger.debug(f"Applied environment override: {config_attr} = {value}")

    def save_config(self) -> bool:
        """Save current configuration to file."""
        if not self._config:
            logger.error("No configuration to save")
            return False

        try:
            # Create directory if it doesn't exist
            self.config_file.parent.mkdir(parents=True, exist_ok=True)

            # Save configuration
            with open(self.config_file, 'w') as f:
                json.dump(asdict(self._config), f, indent=2)

            logger.info(f"Configuration saved to {self.config_file}")
            return True

        except Exception as e:
            logger.error(f"Failed to save configuration: {e}")
            return False

    def update_config(self, updates: Dict[str, Any]) -> bool:
        """Update configuration with new values."""
        if not self._config:
            logger.error("No configuration loaded")
            return False

        try:
            for key, value in updates.items():
                if hasattr(self._config, key):
                    setattr(self._config, key, value)
                    logger.debug(f"Updated config: {key} = {value}")
                else:
                    logger.warning(f"Unknown configuration key: {key}")

            # Save updated config
            return self.save_config()

        except Exception as e:
            logger.error(f"Failed to update configuration: {e}")
            return False

    def get_config(self) -> AXIOMHIVEConfig:
        """Get current configuration."""
        if not self._config:
            return self.load_config()
        return self._config

    def validate_config(self) -> bool:
        """Validate current configuration."""
        config = self.get_config()

        # Validation rules
        validations = [
            (config.trust_threshold > 0 and config.trust_threshold <= 1, "trust_threshold must be between 0 and 1"),
            (config.reboot_threshold > 0, "reboot_threshold must be positive"),
            (config.max_ledger_events > 0, "max_ledger_events must be positive"),
            (config.density_threshold > 0, "density_threshold must be positive"),
            (len(config.node_id) > 0, "node_id cannot be empty"),
            (len(config.hash_prefix) >= 16, "hash_prefix must be at least 16 characters"),
        ]

        all_valid = True
        for is_valid, error_msg in validations:
            if not is_valid:
                logger.error(f"Configuration validation failed: {error_msg}")
                all_valid = False

        if all_valid:
            logger.info("Configuration validation passed")
        else:
            logger.error("Configuration validation failed")

        return all_valid

# Global configuration manager instance
_config_manager: Optional[ConfigManager] = None

def get_config_manager() -> ConfigManager:
    """Get global configuration manager instance."""
    global _config_manager
    if _config_manager is None:
        _config_manager = ConfigManager()
    return _config_manager

def get_config() -> AXIOMHIVEConfig:
    """Get current configuration."""
    return get_config_manager().get_config()

def update_config(updates: Dict[str, Any]) -> bool:
    """Update configuration with new values."""
    return get_config_manager().update_config(updates)

def save_config() -> bool:
    """Save current configuration to file."""
    return get_config_manager().save_config()

def validate_config() -> bool:
    """Validate current configuration."""
    return get_config_manager().validate_config()