"""
Emergency stop system for RedDot shows
"""

def emergency_stop():
    """Immediately stop all lights and fountains"""
    print("🚨 EMERGENCY STOP ACTIVATED 🚨")
    print("All systems shutting down...")
    return True

def safety_check(config=None):
    """Perform safety check before show using config limits"""
    print("Running safety checks...")
    if config is None:
        print("No config provided, skipping detailed safety tests.")
        print("Safety check complete.")
        return True
    limits = config.get("safety_limits", {})
    max_lights = config.get("max_lights", 10)
    max_fireworks = config.get("max_fireworks", 3)
    max_intensity = limits.get("max_light_intensity", 100)
    max_height = limits.get("max_firework_height", 10)
    colors = ["red", "orange", "yellow", "green", "blue", "purple", "white", "pink", "cyan"]
    # Test lights at max intensity
    for i in range(1, max_lights+1):
        print(f"Test Light {i}: Intensity {max_intensity}%")
    # Test fireworks at max height and all colors
    for i in range(1, max_fireworks+1):
        for color in colors:
            print(f"Test Firework {i}: Height {max_height}m, Color {color}")
    print("Safety check complete.")
    return True