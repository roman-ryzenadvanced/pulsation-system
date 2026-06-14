#!/usr/bin/env python3
"""Quick test for pulsation system"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from main import PulsationSystem

def test_pulsation():
    """Quick visual test"""
    print("Testing Pulsation System...")
    
    system = PulsationSystem()
    
    # Run for 5 seconds and show a few frames
    import time
    for i in range(10):
        rings_data = system.render()
        t = time.strftime("%H:%M:%S")
        print(f"\n[{t}] Pulse #{i+1}")
        for j, ring in enumerate(rings_data['rings']):
            radius = ring['radius']
            opacity = ring['opacity']
            print(f"  Ring {j+1}: radius={radius:.1f}px, opacity={opacity:.2f}")
        
        system.update(0.5)
        time.sleep(0.5)
    
    print("\n✓ Test complete - main.py is working!")

if __name__ == "__main__":
    test_pulsation()
