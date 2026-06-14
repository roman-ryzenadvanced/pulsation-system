#!/usr/bin/env python3
"""
Status monitor for the Live Public IP Demo
"""

import requests
import time
from datetime import datetime

def check_server_status():
    """Check if the demo server is running"""
    base_url = "http://95.216.124.247:5000"
    
    print("🔍 MARKET FEAR PULSATION SYSTEM - LIVE DEMO STATUS")
    print("=" * 60)
    print(f"📡 Public IP: 95.216.124.247")
    print(f"🌐 Server URL: {base_url}")
    print(f"🕐 Check Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 60)
    
    # Check server health
    print("🩺 Checking Server Health...")
    try:
        response = requests.get(f"{base_url}/api/health", timeout=5)
        if response.status_code == 200:
            health_data = response.json()
            print(f"✅ Status: {health_data['status']}")
            print(f"   Service: {health_data['service']}")
            print(f"   Version: {health_data['version']}")
        else:
            print(f"❌ Health check failed: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Cannot connect to server: {str(e)}")
        return False
    
    # Check signal endpoint
    print("\n📊 Checking Signal Endpoint...")
    try:
        response = requests.get(f"{base_url}/api/signal", timeout=10)
        if response.status_code == 200:
            signal_data = response.json()
            if signal_data['status'] == 'success':
                print(f"✅ Signal Status: {signal_data['status']}")
                print(f"   Fear Index: {signal_data['fear_index']}/100")
                print(f"   BTC Price: {signal_data['price_formatted']}")
                print(f"   Trading Signal: {signal_data['signal_type']}")
                print(f"   Confidence: {signal_data['confidence']}")
                return True
            else:
                print(f"❌ Signal Error: {signal_data.get('error', 'Unknown')}")
                return False
        else:
            print(f"❌ Signal endpoint failed: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Signal check error: {str(e)}")
        return False

def generate_access_info():
    """Generate access information"""
    base_url = "http://95.216.124.247:5000"
    
    print(f"\n🌐 LIVE DEMO ACCESS INFORMATION")
    print("=" * 40)
    print(f"📡 Server IP: 95.216.124.247")
    print(f"🌐 Web Server: Flask on port 5000")
    print(f"🌐 Base URL: {base_url}")
    
    print(f"\n🔗 Direct Access Links:")
    print(f"   🖥️  Desktop: {base_url}/")
    print(f"   📱 Mobile:  {base_url}/")
    print(f"   📊 API:     {base_url}/api/signal")
    print(f"   🩺 Health:  {base_url}/api/health")
    
    print(f"\n✨ Key Features:")
    print(f"   • Real-time Fear & Greed Index monitoring")
    print(f"   • Live Bitcoin price tracking")
    print(f"   • Visual pulsation trading signals")
    print(f"   • Color-coded buy/hold/sell alerts")
    print(f"   • Auto-refresh every 60 seconds")
    print(f"   • Mobile responsive design")
    print(f"   • Market condition analysis")

def test_endpoints():
    """Test all available endpoints"""
    base_url = "http://95.216.124.247:5000"
    
    print(f"\n🧪 TESTING ALL ENDPOINTS")
    print("=" * 40)
    
    endpoints = [
        ('Health Check', '/api/health'),
        ('Signal Data', '/api/signal'),
        ('Web Interface', '/')
    ]
    
    for name, endpoint in endpoints:
        print(f"\n📡 Testing {name}...")
        try:
            response = requests.get(f"{base_url}{endpoint}", timeout=5)
            if response.status_code == 200:
                print(f"✅ {name}: OK ({response.status_code})")
                
                if endpoint == '/api/health':
                    data = response.json()
                    print(f"   Service: {data['service']}")
                elif endpoint == '/api/signal':
                    data = response.json()
                    print(f"   Signal: {data['signal_type']}")
                    print(f"   Fear Index: {data['fear_index']}/100")
            else:
                print(f"❌ {name}: Failed ({response.status_code})")
        except Exception as e:
            print(f"❌ {name}: Error ({str(e)})")

def main():
    """Main function"""
    print("🚀 MARKET FEAR PULSATION SYSTEM - LIVE DEMO SETUP")
    print("=" * 70)
    
    # Check server status
    is_healthy = check_server_status()
    
    if is_healthy:
        print("\n🎉 LIVE DEMO IS RUNNING!")
        
        # Generate access info
        generate_access_info()
        
        # Test endpoints
        test_endpoints()
        
        print(f"\n🎯 ACCESS INSTRUCTIONS:")
        print(f"   1. Open your web browser")
        print(f"   2. Visit: http://95.216.124.247:5000")
        print(f"   3. View live market signals")
        print(f"   4. Auto-refreshes every 60 seconds")
        
        print(f"\n📱 MOBILE ACCESS:")
        print(f"   Same URL works on mobile devices")
        print(f"   Responsive design adapts to screen size")
        
        print(f"\n🔄 REFRESH RATE:")
        print(f"   Manual: Click refresh button")
        print(f"   Automatic: Every 60 seconds")
        print(f"   API: Real-time on demand")
        
        print(f"\n✅ STATUS: DEMO LIVE AND ACCESSIBLE")
        print(f"🕐 Current Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        
    else:
        print("\n❌ DEMO SERVER NOT RUNNING")
        print(f"Please check the server status and logs")
    
    print("\n" + "=" * 70)
    print("Demo Status Check Complete")
    print("=" * 70)

if __name__ == "__main__":
    main()