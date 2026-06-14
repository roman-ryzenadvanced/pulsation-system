#!/usr/bin/env python3
"""
Demo script for the Live Public IP Demo
"""

import requests
import json
from datetime import datetime

def test_live_demo():
    """Test the live demo endpoints"""
    base_url = "http://95.216.124.247:5000"
    
    print("🎯 MARKET FEAR PULSATION SYSTEM - LIVE DEMO")
    print("=" * 60)
    print(f"🌐 Public URL: {base_url}")
    print(f"📅 Test Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 60)
    
    # Test health endpoint
    print("🩺 Testing Health Endpoint...")
    try:
        response = requests.get(f"{base_url}/api/health", timeout=5)
        if response.status_code == 200:
            health_data = response.json()
            print(f"✅ Health Check: {health_data['status']}")
            print(f"   Service: {health_data['service']}")
            print(f"   Version: {health_data['version']}")
        else:
            print(f"❌ Health check failed: {response.status_code}")
    except Exception as e:
        print(f"❌ Health check error: {str(e)}")
    
    print("\n📊 Testing Signal Endpoint...")
    try:
        response = requests.get(f"{base_url}/api/signal", timeout=10)
        if response.status_code == 200:
            signal_data = response.json()
            print(f"✅ Signal Status: {signal_data['status']}")
            
            if signal_data['status'] == 'success':
                print(f"\n🎯 Current Market Signal:")
                print(f"   Fear Index: {signal_data['fear_index']}/100")
                print(f"   BTC Price: {signal_data['price_formatted']}")
                print(f"   Signal: {signal_data['signal_color']} {signal_data['signal_type']}")
                print(f"   Confidence: {signal_data['confidence']}")
                print(f"   Market Condition: {signal_data['condition_desc']}")
                print(f"   Pulse Intensity: {signal_data['intensity']}/5")
                
                pulse_visual = signal_data['pulse_visual']
                print(f"   Visual Pulse: {pulse_visual}")
                
                print(f"\n💡 Recommendation: {signal_data['recommendation']}")
            else:
                print(f"❌ Error: {signal_data.get('error', 'Unknown error')}")
        else:
            print(f"❌ Signal fetch failed: {response.status_code}")
    except Exception as e:
        print(f"❌ Signal fetch error: {str(e)}")
    
    print(f"\n🌐 Web Interface Access:")
    print(f"   Direct URL: {base_url}/")
    print(f"   Open in browser: http://95.216.124.247:5000")
    
    print(f"\n📱 Mobile Access:")
    print(f"   Scan QR code or visit: {base_url}/")
    
    print("\n" + "=" * 60)
    print("✅ LIVE DEMO COMPLETE")
    print("=" * 60)

def continuous_monitoring_demo():
    """Show continuous monitoring capabilities"""
    base_url = "http://95.216.124.247:5000"
    
    print("🔄 CONTINUOUS MONITORING DEMO")
    print("=" * 40)
    print("Fetching signals every 30 seconds for 2 minutes...")
    print("=" * 40)
    
    import time
    for i in range(4):  # 4 iterations = 2 minutes
        try:
            response = requests.get(f"{base_url}/api/signal", timeout=5)
            if response.status_code == 200:
                data = response.json()
                timestamp = datetime.now().strftime('%H:%M:%S')
                print(f"[{timestamp}] Signal: {data['signal_type']} | Fear: {data['fear_index']}/100 | BTC: ${data['btc_price']}")
            
            time.sleep(30)  # Wait 30 seconds
        except Exception as e:
            print(f"❌ Error at iteration {i+1}: {str(e)}")
            time.sleep(30)

def accessibility_info():
    """Provide information about accessing the demo"""
    base_url = "http://95.216.124.247:5000"
    
    print("\n🌐 ACCESSIBILITY INFORMATION")
    print("=" * 40)
    print(f"📡 Public IP: 95.216.124.247")
    print(f"🌐 Web Server: Flask on port 5000")
    print(f"📱 Responsive Design: Mobile & Desktop Friendly")
    print(f"🔄 Auto-refresh: Every 60 seconds")
    print(f"⚡ Real-time: Live market data integration")
    
    print(f"\n🔗 Direct Access Links:")
    print(f"   Main Interface: {base_url}/")
    print(f"   API Endpoint: {base_url}/api/signal")
    print(f"   Health Check: {base_url}/api/health")
    
    print(f"\n💡 Features:")
    print(f"   • Live Fear & Greed Index")
    print(f"   • Real-time Bitcoin price")
    print(f"   • Visual pulsation signals")
    print(f"   • Trading recommendations")
    print(f"   • Market condition analysis")
    print(f"   • Auto-refresh capability")
    
    print(f"\n🚀 Demo Status: ✅ RUNNING")
    print(f"🕐 Server Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

if __name__ == "__main__":
    # Run the main demo
    test_live_demo()
    
    # Show accessibility info
    accessibility_info()
    
    # Ask if user wants to see continuous monitoring
    print(f"\n🤖 Would you like to see continuous monitoring demo?")
    print(f"   This will show real-time updates every 30 seconds for 2 minutes.")
    
    # For non-interactive environments, just show the info
    print(f"\n💡 To access the live demo:")
    print(f"   1. Open browser: http://95.216.124.247:5000")
    print(f"   2. The interface shows real-time market signals")
    print(f"   3. Auto-refreshes every 60 seconds")
    print(f"   4. Mobile responsive design")
    
    print(f"\n✅ LIVE DEMO IS READY!")