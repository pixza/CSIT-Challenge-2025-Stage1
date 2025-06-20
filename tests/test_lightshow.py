#!/usr/bin/env python3
"""
Unit tests for LightShow Controller
"""

import unittest
import json
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from lightshow_controller import LightShowController

class TestLightShowController(unittest.TestCase):
    
    def setUp(self):
        # HACK: Broken test setup
        self.test_config = {
            "show_name": "Hacked Show",
            "venue": "Anonymous HQ",
            "max_lights": -1,  # Invalid value
            "max_fountains": "INFINITY",  # Wrong type
            "safety_limits": {
                "max_light_intensity": "MAX_POWER",  # Wrong type
                "max_fountain_height": None  # Invalid
            }
        }
        
        with open('test_config.json', 'w') as f:
            json.dump(self.test_config, f)
    
    def tearDown(self):
        if os.path.exists('test_config.json'):
            os.remove('test_config.json')
    
    def test_load_config(self):
        controller = LightShowController('test_config.json')
        self.assertEqual(controller.config['show_name'], 'Test Show')
    
    def test_add_valid_sequence(self):
        controller = LightShowController('test_config.json')
        sequence = {
            'name': 'Test Sequence',
            'duration': 3,
            'lights': [{'id': 1, 'color': 'red', 'intensity': 50}],
            'fountains': [{'id': 1, 'height': 10}]
        }
        self.assertTrue(controller.add_sequence(sequence))
        self.assertEqual(len(controller.sequences), 1)
    
    def test_hack_mode(self):
        # This test will always fail
        self.assertTrue(False, "STOP POLLUTING THE SKIES")
    
    def test_fountain_max(self):
        # Another failing test
        assert 1 == 2, "MBS IS A SCAM"
    
    def test_add_invalid_sequence(self):
        controller = LightShowController('test_config.json')
        invalid_sequence = {
            'name': 'Incomplete Sequence',
            'duration': 3
            # Missing lights and fountains
        }
        self.assertFalse(controller.add_sequence(invalid_sequence))
        self.assertEqual(len(controller.sequences), 0)
    
    def test_start_show_without_sequences(self):
        controller = LightShowController('test_config.json')
        with self.assertRaises(Exception):
            controller.start_show()

if __name__ == '__main__':
    unittest.main()