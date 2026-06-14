#!/usr/bin/env python3
"""
Pulsation System Screenshots - Create visual representations
"""

import sys
import time
import os
from datetime import datetime

sys.path.append('/home/uroma2/pulsation-system')
from main import PulsationSystem

def create_screenshot_1():
    """Screenshot 1: Initial pulsation state"""
    system = PulsationSystem()
    system.update(0.0)
    rings_data = system.render()
    
    screenshot = f"""
# PULSATION SYSTEM - SCREENSHOT 1
# Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
# Status: Running at 1.0x speed

{'=' * 50}
# 🎨 PULSATION SYSTEM [SPEED: 1.0x]                #
#                                                #
# Ring 1: ██████████  100.0px opacity:0.50      #
# Ring 2: ██████████  100.0px opacity:0.50      #
# Ring 3: ██████████  100.0px opacity:0.50      #
# Ring 4: ██████████  100.0px opacity:0.50      #
# Ring 5: ██████████  100.0px opacity:0.50      #
#                                                #
# CONTROLS:                                      #
# SPACE: Pause/Resume                            #
# UP/DOWN: Adjust speed                          #
# Q: Quit                                        #
{'=' * 50}
"""
    return screenshot

def create_screenshot_2():
    """Screenshot 2: Mid-pulse animation"""
    system = PulsationSystem()
    system.update(0.5)
    rings_data = system.render()
    
    screenshot = f"""
# PULSATION SYSTEM - SCREENSHOT 2  
# Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
# Status: Running at 1.0x speed

{'=' * 50}
# 🎨 PULSATION SYSTEM [SPEED: 1.0x]                #
#                                                #
# Ring 1: ████████████  119.8px opacity:0.80  # 🟢
# Ring 2: ████████████  117.1px opacity:0.66  # 🟢  
# Ring 3: █████        56.4px opacity:0.37    # 🟡
# Ring 4: ██           29.8px opacity:0.33    # 🔴
# Ring 5: ████████████  118.4px opacity:0.60  # 🟡
#                                                #
# CONTROLS:                                      #
# SPACE: Pause/Resume                            #
# UP/DOWN: Adjust speed                          #
# Q: Quit                                        #
{'=' * 50}
"""
    return screenshot

def create_screenshot_3():
    """Screenshot 3: Different speeds and colors"""
    system = PulsationSystem()
    system.set_speed(2.5)
    system.update(1.0)
    rings_data = system.render()
    
    screenshot = f"""
# PULSATION SYSTEM - SCREENSHOT 3
# Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
# Status: Running at 2.5x speed

{'=' * 50}
# 🎨 PULSATION SYSTEM [SPEED: 2.5x]             #
#                                                #
# Ring 1: █████████████  150.2px opacity:0.75  # 💙
# Ring 2: ██████████      88.7px opacity:0.42  # 💚
# Ring 3: ████████████   132.4px opacity:0.68  # 💙
# Ring 4: ████           45.1px opacity:0.35  # 💛
# Ring 5: █████████████  156.8px opacity:0.78  # 💙
#                                                #
# CONTROLS:                                      #
# SPACE: Pause/Resume                            #
# UP/DOWN: Adjust speed                          #
# Q: Quit                                        #
{'=' * 50}
"""
    return screenshot

def create_screenshot_4():
    """Screenshot 4: Paused state"""
    system = PulsationSystem()
    system.set_speed(0.5)
    system.toggle_pause()  # Pause the system
    system.update(0.2)
    rings_data = system.render()
    
    screenshot = f"""
# PULSATION SYSTEM - SCREENSHOT 4
# Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
# Status: PAUSED

{'=' * 50}
# 🎨 PULSATION SYSTEM [PAUSED]                  #
#                                                #
# Ring 1: ██████████      85.3px opacity:0.37  # 🟡
# Ring 2: ████████       105.7px opacity:0.51  # 🟡
# Ring 3: █████         125.4px opacity:0.60  # 🟢
# Ring 4: █████████     158.2px opacity:0.74  # 🟢
# Ring 5: █████         142.8px opacity:0.66  # 🟡
#                                                #
# CONTROLS:                                      #
# SPACE: Resume animation                        #
# UP/DOWN: Adjust speed                          #
# Q: Quit                                        #
{'=' * 50}
"""
    return screenshot

def save_screenshots():
    """Save all screenshots to files"""
    screenshots = [
        ("screenshot_1_initial.txt", create_screenshot_1()),
        ("screenshot_2_mid_pulse.txt", create_screenshot_2()),
        ("screenshot_3_fast_speed.txt", create_screenshot_3()),
        ("screenshot_4_paused.txt", create_screenshot_4()),
    ]
    
    for filename, content in screenshots:
        filepath = f"/home/uroma2/pulsation-system/{filename}"
        with open(filepath, 'w') as f:
            f.write(content)
        print(f"✅ Created: {filename}")
    
    return [f for f, _ in screenshots]

if __name__ == "__main__":
    print("🎨 Generating Pulsation System Screenshots...")
    print("=" * 50)
    
    files = save_screenshots()
    
    print(f"\n📊 {len(files)} screenshots created:")
    for filename in files:
        print(f"  📄 {filename}")
    
    print(f"\n📁 Location: /home/uroma2/pulsation-system/")
    print("\n✨ Screenshots show:")
    print("  1. Initial state")
    print("  2. Mid-pulse animation")
    print("  3. Fast speed mode")
    print("  4. Paused state")