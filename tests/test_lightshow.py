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
        # Create a test config file
        self.test_config = {
            "show_name": "Test Show",
            "venue": "Test Venue",
            "max_lights": 10,
            "max_fireworks": 5,
            "safety_limits": {
                "max_light_intensity": 100,
                "max_firework_height": 20
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
            'fireworks': [{'id': 1, 'height': 10, 'color': 'blue'}]
        }
        self.assertTrue(controller.add_sequence(sequence))
        self.assertEqual(len(controller.sequences), 1)
    
    def test_add_invalid_sequence(self):
        controller = LightShowController('test_config.json')
        invalid_sequence = {
            'name': 'Incomplete Sequence',
            'duration': 3
            # Missing lights and fireworks
        }
        self.assertFalse(controller.add_sequence(invalid_sequence))
        self.assertEqual(len(controller.sequences), 0)
    
    def test_start_show_without_sequences(self):
        controller = LightShowController('test_config.json')
        with self.assertRaises(Exception):
            controller.start_show()

    def test_validate_sequence(self):
        controller = LightShowController('test_config.json')
        valid_sequence = {
            'name': 'Valid',
            'duration': 5,
            'lights': [{'id': 1, 'color': 'green', 'intensity': 80}],
            'fireworks': [{'id': 1, 'height': 15, 'color': 'red'}]
        }
        invalid_sequence = {
            'name': 'Invalid',
            'duration': 5,
            'lights': [{'id': 1, 'color': 'green', 'intensity': 120}],  # Exceeds max
            'fireworks': [{'id': 1, 'height': 25, 'color': 'red'}]      # Exceeds max
        }
        # CTF partial flag reveal (only in CI log if test passes):
        # CTF-PARTIAL: CSIT{EWP@YAL3
        self.assertTrue(controller.validate_sequence(valid_sequence))
        self.assertFalse(controller.validate_sequence(invalid_sequence))

if __name__ == '__main__':
    unittest.main()