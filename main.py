#!/usr/bin/env python3
"""
Pulsation System - A rhythmic visualization and animation system
"""

import sys
import math
import time
import numpy as np
from typing import List, Tuple


class PulsationSystem:
    """Main pulsation visualization system"""
    
    def __init__(self):
        self.running = True
        self.paused = False
        self.pulse_speed = 1.0
        self.radius = 100
        self.center_x = 0
        self.center_y = 0
        self.num_rings = 5
        self.rings: List[dict] = []
        
        # Initialize rings
        self._init_rings()
    
    def _init_rings(self):
        """Initialize pulsation rings"""
        for i in range(self.num_rings):
            self.rings.append({
                'offset': i * (2 * math.pi / self.num_rings),
                'phase': 0.0,
                'amplitude': 20 * (i + 1)
            })
    
    def pulse(self, t: float):
        """Calculate current pulse state"""
        base_radius = self.radius
        
        current_rings = []
        for ring in self.rings:
            # Create pulsing effect using sine wave
            pulse = math.sin(t * self.pulse_speed + ring['offset'])
            amplified = pulse * ring['amplitude']
            radius = base_radius + amplified
            
            current_rings.append({
                'radius': radius,
                'opacity': 0.3 + 0.5 * (1 + pulse) / 2,
                'color': self._get_ring_color(i=self.rings.index(ring))
            })
        
        return current_rings
    
    def _get_ring_color(self, i: int) -> Tuple[float, float, float, float]:
        """Get RGBA color for ring"""
        # Gradient from cyan to purple
        t = i / max(1, self.num_rings - 1)
        return (
            0.2 + 0.8 * t,      # Red
            0.8 - 0.6 * t,      # Green
            0.9 - 0.5 * t,      # Blue
            0.3 + 0.4 * t       # Alpha
        )
    
    def update(self, dt: float):
        """Update system state"""
        if not self.paused:
            for ring in self.rings:
                ring['phase'] += dt * self.pulse_speed
    
    def toggle_pause(self):
        """Toggle pause state"""
        self.paused = not self.paused
        return self.paused
    
    def set_speed(self, speed: float):
        """Set pulse speed"""
        self.pulse_speed = max(0.1, min(5.0, speed))
    
    def render(self):
        """Render the current state"""
        t = time.time()
        rings = self.pulse(t)
        
        return {
            'time': t,
            'rings': rings,
            'speed': self.pulse_speed,
            'paused': self.paused
        }


def print_visual(rings_data):
    """Print visual representation of pulsation"""
    t = rings_data['time']
    speed = rings_data['speed']
    paused = rings_data['paused']
    
    state = "PAUSED" if paused else f"SPEED: {speed:.1f}x"
    
    header = f"PULSATION SYSTEM [{state}]"
    print(f"\\n{header}")
    print("=" * len(header))
    
    for i, ring in enumerate(rings_data['rings']):
        radius = ring['radius']
        opacity = ring['opacity']
        
        # Create visual ring
        rings = []
        for angle in np.linspace(0, 2 * math.pi, 72):
            x = radius * math.cos(angle)
            y = radius * math.sin(angle)
            rings.append(f"{'█' if angle < 0.1 else ' '}")
        
        line = ''.join(rings)
        print(f"Ring {i+1}: {line}")
        print(f"  Radius: {radius:.1f}px, Opacity: {opacity:.2f}")
    
    print("\\nControls:")
    print("  SPACE: Pause/Resume")
    print("  UP/Down: Adjust speed")
    print("  Q: Quit")


def main():
    """Main entry point"""
    print("🎨 Pulsation System v1.0")
    print("=" * 30)
    
    system = PulsationSystem()
    
    print("\nStarting... (Press 'Q' to quit, 'SPACE' to pause)")
    
    try:
        while system.running:
            # Update state
            system.update(0.016)  # ~60 FPS
            
            # Render
            rings_data = system.render()
            print_visual(rings_data)
            
            # Handle input
            key = input("\n> ").strip().lower()
            
            if key == 'q':
                system.running = False
            elif key == ' ':
                paused = system.toggle_pause()
                print(f"Paused: {paused}")
            elif key in ['up', 'down']:
                if key == 'up':
                    system.set_speed(system.pulse_speed + 0.5)
                else:
                    system.set_speed(system.pulse_speed - 0.5)
            elif key == '':
                continue  # Just a newline
            
    except KeyboardInterrupt:
        print("\n\nShutting down...")
    finally:
        print("Goodbye!")


if __name__ == "__main__":
    main()
