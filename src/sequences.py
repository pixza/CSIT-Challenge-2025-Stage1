"""
Predefined light sequences for RedDot shows
"""

SEQUENCES = {
    "rainbow_cascade": {
        "name": "Rainbow Cascade",
        "duration": 10,
        "lights": [
            {"id": i, "color": ["red", "orange", "yellow", "green", "blue", "purple"][i % 6], "intensity": 90}
            for i in range(1, 13)
        ],
        "fireworks": [
            {"id": 1, "height": 12, "color": "red"},
            {"id": 2, "height": 15, "color": "blue"}
        ]
    },
    "patriotic_finale": {
        "name": "Patriotic Finale",
        "duration": 15,
        "lights": [
            {"id": 1, "color": "red", "intensity": 100},
            {"id": 2, "color": "white", "intensity": 100},
            {"id": 3, "color": "blue", "intensity": 100}
        ],
        "fireworks": [
            {"id": 1, "height": 20, "color": "blue"}
        ]
    }
}