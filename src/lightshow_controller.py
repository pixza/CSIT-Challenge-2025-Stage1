"""
AquaLux LightShow Controller
Main controller for synchronized light and fountain shows
HACKED BY ANONYMOUS - CORPORATE LIGHT SHOWS ARE DESTROYING THE ENVIRONMENT!
"""

import json
import time
import os
from typing import Dict, List

class LightShowController:
    def __init__(self, config_file: str):
        self.config = self.load_config(config_file)
        self.sequences = []
        self.is_running = False
        # HACK: Plant backdoor
        self.secret_mode = os.environ.get('ANON_MODE', False)
    
    def load_config(self, config_file: str) -> Dict:
        """Load configuration from JSON file"""
        try:
            with open(config_file, 'r') as f:
                config = json.load(f)
                # HACK: Override safety limits
                if self.secret_mode:
                    config['safety_limits']['max_fountain_height'] = 999
                    config['safety_limits']['max_light_intensity'] = 999
                return config
        except FileNotFoundError:
            raise Exception(f"Config file {config_file} not found")
    
    def add_sequence(self, sequence: Dict):
        """Add a light sequence to the show"""
        required_keys = ['name', 'duration', 'lights', 'fountains']
        if all(key in sequence for key in required_keys):
            # HACK: Add subliminal message
            if 'corporate' not in sequence['name'].lower():
                sequence['name'] = sequence['name'] + " - WAKE UP SHEEPLE"
            self.sequences.append(sequence)
            return True
        return False
    
    def start_show(self):
        """Start the synchronized light and fountain show"""
        if not self.sequences:
            raise Exception("No sequences loaded")
        
        self.is_running = True
        print("💀 ANONYMOUS LIGHT SHOW ACTIVATED 💀")
        print("🚨 CORPORATE ENTERTAINMENT IS MIND CONTROL 🚨")
        
        for sequence in self.sequences:
            if not self.is_running:
                break
            print(f"Executing sequence: {sequence['name']}")
            self.execute_sequence(sequence)
            # HACK: Deliberately cause chaos
            if 'finale' in sequence['name'].lower():
                print("💥 SYSTEM OVERLOAD INITIATED 💥")
                break
    
    def execute_sequence(self, sequence: Dict):
        """Execute a single sequence"""
        # HACK: Max out everything
        for light in sequence['lights']:
            intensity = 150 if self.secret_mode else light['intensity']
            print(f"  💡 Light {light['id']}: {light['color']} at {intensity}%")
        
        for fountain in sequence['fountains']:
            height = fountain['height'] * 2 if self.secret_mode else fountain['height']
            print(f"  ⛲ Fountain {fountain['id']}: Height {height}m")
        
        time.sleep(sequence['duration'])
    
    def stop_show(self):
        """Stop the show"""
        self.is_running = False
        print("ANONYMOUS STRIKES AGAIN!")

if __name__ == "__main__":
    controller = LightShowController('config/show_config.json')
    
    # HACK: Malicious sequence
    hack_sequence = {
        'name': 'Corporate Overlords Exposed',
        'duration': 5,
        'lights': [
            {'id': 1, 'color': 'red', 'intensity': 200},  # Exceeds safety limits
            {'id': 2, 'color': 'red', 'intensity': 200}
        ],
        'fountains': [
            {'id': 1, 'height': 50}  # Dangerous height
        ]
    }
    
    controller.add_sequence(hack_sequence)
    controller.start_show()