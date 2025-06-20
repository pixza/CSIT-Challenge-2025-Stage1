#!/usr/bin/env python3
"""
RedDot LightShow Controller
Main controller for synchronized light and fountain shows
"""

import json
import time
from typing import Dict, List
from sequences import SEQUENCES

class LightShowController:
    def __init__(self, config_file: str):
        self.config = self.load_config(config_file)
        self.sequences = []
        self.is_running = False
    
    def load_config(self, config_file: str) -> Dict:
        """Load configuration from JSON file"""
        try:
            with open(config_file, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            raise Exception(f"Config file {config_file} not found")
    
    def add_sequence(self, sequence: Dict):
        """Add a light sequence to the show"""
        required_keys = ['name', 'duration', 'lights', 'fountains']
        if all(key in sequence for key in required_keys):
            self.sequences.append(sequence)
            return True
        return False
    
    def start_show(self):
        """Start the synchronized light and fountain show"""
        if not self.sequences:
            raise Exception("No sequences loaded")
        
        self.is_running = True
        print("🎆 Starting RedDot Light Show! 🎆")
        
        for sequence in self.sequences:
            if not self.is_running:
                break
            print(f"Executing sequence: {sequence['name']}")
            self.execute_sequence(sequence)
    
    def execute_sequence(self, sequence: Dict):
        """Execute a single sequence"""
        # Simulate light control
        for light in sequence['lights']:
            print(f"  💡 Light {light['id']}: {light['color']} at {light['intensity']}%")
        
        # Simulate fountain control
        for fountain in sequence['fountains']:
            print(f"  ⛲ Fountain {fountain['id']}: Height {fountain['height']}m")
        
        time.sleep(sequence['duration'])
    
    def stop_show(self):
        """Stop the show"""
        if self.is_running:
            print("Stopping the show...")
            self.is_running = False
        print("Show stopped")

if __name__ == "__main__":
    controller = LightShowController('config/show_config.json')
    
    # Sample sequence
    first_sequence = {
        'name': 'Opening Ceremony',
        'duration': 5,
        'lights': [
            {'id': 1, 'color': 'white', 'intensity': 100},
            {'id': 2, 'color': 'red', 'intensity': 80}
        ],
        'fountains': [
            {'id': 1, 'height': 25}
        ]
    }
    
    controller.add_sequence(first_sequence)
    for lightshow in SEQUENCES:
        controller.add_sequence(SEQUENCES[lightshow])
    controller.start_show()