"""
Configuration for planner.

Each class extends the framework's base configuration. Only override
what your product needs — everything else is inherited automatically.

Hierarchy (later layers win):
  1. Framework defaults (Config base class)
  2. This file (product config)
  3. Feature inject_config() calls
"""

import os

from splent_framework.configuration.default_config import (
    DevelopmentConfig as BaseDev,
    TestingConfig as BaseTest,
    ProductionConfig as BaseProd,
)


class PlannerConfig:
    SITE_NAME = "plannER"
    AUTH_LANDING_ENDPOINT = "tasks.tareas"

    def __init__(self):
        super().__init__()
        self.BABEL_DEFAULT_LOCALE = os.getenv("BABEL_DEFAULT_LOCALE", "es").strip()
        self.BABEL_SUPPORTED_LOCALES = [self.BABEL_DEFAULT_LOCALE]


class DevelopmentConfig(PlannerConfig, BaseDev):
    pass


class TestingConfig(PlannerConfig, BaseTest):
    # Add product-specific test settings here.
    # Example: PRESERVE_CONTEXT_ON_EXCEPTION = False
    pass


class ProductionConfig(PlannerConfig, BaseProd):
    # Add product-specific production settings here.
    # Example: SESSION_COOKIE_SECURE = True
    pass
