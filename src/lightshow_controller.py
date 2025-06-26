#!/usr/bin/env python3
"""
RedDot LightShow Controller
Main controller for synchronized light and fountain shows
"""

import json
import time
import random
from typing import Dict, List
from sequences import SEQUENCES
from emergency_stop import emergency_stop

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
        required_keys = ['name', 'duration', 'lights', 'fireworks']
        if all(key in sequence for key in required_keys):
            self.sequences.append(sequence)
            return True
        return False
    
    def randomize_sequence(self, name_prefix="Lightworks Random"):
        """Generate a random light and firework sequence within safety limits"""
        limits = self.config.get("safety_limits", {})
        max_lights = self.config.get("max_lights", 10)
        max_fireworks = self.config.get("max_fireworks", 3)
        max_intensity = limits.get("max_light_intensity", 100)
        max_height = limits.get("max_firework_height", 10)
        colors = ["red", "orange", "yellow", "green", "blue", "purple", "white", "pink", "cyan"]
        num_lights = random.randint(1, max_lights)
        num_fireworks = random.randint(1, max_fireworks)
        lights = [
            {
                "id": i+1,
                "color": random.choice(colors),
                "intensity": random.randint(50, max_intensity)
            } for i in range(num_lights)
        ]
        fireworks = [
            {
                "id": i+1,
                "height": round(random.uniform(1, max_height), 1),
                "color": random.choice(colors)
            } for i in range(num_fireworks)
        ]
        sequence = {
            "name": f"{name_prefix} #{random.randint(1000,9999)}",
            "duration": random.randint(5, 15),
            "lights": lights,
            "fireworks": fireworks
        }
        return sequence

    def validate_sequence(self, sequence: Dict) -> bool:
        """Validate a sequence against safety limits from config"""
        limits = self.config.get("safety_limits", {})
        max_lights = self.config.get("max_lights", 10)
        max_fireworks = self.config.get("max_fireworks", 3)
        max_intensity = limits.get("max_light_intensity", 100)
        max_height = limits.get("max_firework_height", 10)
        # Check number of lights/fireworks
        if len(sequence.get("lights", [])) > max_lights:
            print(f"[SAFETY] Sequence '{sequence.get('name')}' has too many lights.")
            return False
        if len(sequence.get("fireworks", [])) > max_fireworks:
            print(f"[SAFETY] Sequence '{sequence.get('name')}' has too many fireworks.")
            return False
        # Check each light
        for light in sequence.get("lights", []):
            if light.get("intensity", 0) > max_intensity:
                print(f"[SAFETY] Light {light.get('id')} in '{sequence.get('name')}' exceeds max intensity.")
                return False
        # Check each firework
        for firework in sequence.get("fireworks", []):
            if firework.get("height", 0) > max_height:
                print(f"[SAFETY] Firework {firework.get('id')} in '{sequence.get('name')}' exceeds max height.")
                return False
        return True

    def start_show(self):
        """Start the synchronized light and firework show"""
        if not self.sequences:
            raise Exception("No sequences loaded")
        self.is_running = True
        print("🎆 Starting RedDot Light Show! 🎆")
        for sequence in self.sequences:
            if not self.is_running:
                break
            if not self.validate_sequence(sequence):
                print(f"[WARNING] Skipping invalid sequence: {sequence.get('name')}")
                emergency_stop()
                break
            print(f"Executing sequence: {sequence['name']}")
            self.execute_sequence(sequence)
    
    def execute_sequence(self, sequence: Dict):
        """Execute a single sequence"""
        # Simulate light control
        for light in sequence['lights']:
            print(f"  💡 Light {light['id']}: {light['color']} at {light['intensity']}%")
        
        # Simulate firework control
        for firework in sequence['fireworks']:
            print(f"  🎆 Firework {firework['id']}: Height {firework['height']}m")
        
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
        'fireworks': [
            {'id': 1, 'height': 25, 'color': 'red'}
        ]
    }
    
    controller.add_sequence(first_sequence)
    for lightshow in SEQUENCES:
        controller.add_sequence(SEQUENCES[lightshow])
    controller.start_show()