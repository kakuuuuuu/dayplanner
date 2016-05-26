"""
    Base Configuration File
"""
""" Put Generic Configurations here """
import os
class Config(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY = os.urandom(32)

""" Put Development Specific Configurations here """
class DevelopmentConfig(Config):
    DEBUG = True

""" Put Staging Specific Configurations here """
class StagingConfig(Config):
    TESTING = True

""" Put Production Specific Configurations here """
class ProductionConfig(Config):
    pass
