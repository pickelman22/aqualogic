# -*- coding: utf-8 -*-

from aqualogic.core import AquaLogic, Leds
from io import FileIO
import pytest
import logging

logging.basicConfig(level=logging.DEBUG)

class TestAquaLogic(object):
    def test_pool(self):
        reader = FileIO('tests/data/pool_on.bin')
        aq = AquaLogic(reader, None)
        aq.process()
        # Yes it was cold out when I grabbed this data
        assert aq.is_metric
        assert aq.air_temp == -6
        assert aq.pool_temp == -7
        assert aq.spa_temp == None
        assert aq.pool_chlorinator == None
        assert aq.spa_chlorinator == 3
        assert aq.salt_level == 3.1
        assert aq.is_led_enabled(Leds.POOL)
        assert aq.is_led_enabled(Leds.FILTER)
        assert not aq.is_led_enabled(Leds.SPA)
    
    def test_spa(self):
        reader = FileIO('tests/data/spa_on.bin')
        aq = AquaLogic(reader, None)
        aq.process()
        assert aq.is_metric
        assert aq.air_temp == -6
        assert aq.pool_temp == None
        assert aq.spa_temp == -7
        assert aq.pool_chlorinator == None
        assert aq.spa_chlorinator == 3
        assert aq.salt_level == 3.1
        assert not aq.is_led_enabled(Leds.POOL)
        assert aq.is_led_enabled(Leds.FILTER)
        assert aq.is_led_enabled(Leds.SPA)
