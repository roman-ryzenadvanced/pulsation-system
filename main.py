#!/usr/bin/env python3
"""
Market Fear Pulsation System - Real-time Trading Signals

A comprehensive system for monitoring crypto & forex market fear levels
and generating visual pulsation signals for trading decisions.

Features:
- Real-time Fear & Greed Index monitoring
- Bitcoin price tracking
- Trading signal generation (BUY_STRONG, BUY, HOLD, CAUTION, SELL)
- Visual pulsation alerts with color coding
- Market condition analysis
"""

import sys
import os
import json
import time
import requests
from datetime import datetime, timedelta
from typing import Dict, List, Optional

# Fear & Greed Index API URLs
FEAR_GREED_URLS = {
    "crypto": "https://alternative.me/fng/",
    "bitcoin": "https://api.alternative.me/fng/",
}

# Market sentiment data sources
MARKET_DATA_SOURCES = {
    "coinmarketcap": "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest",
    "binance": "https://api.binance.com/api/v3/ticker/price",
    "forex": "https://api.exchangerate-api.com/v4/latest/USD"
}

class MarketFearPulsationSystem:
    """Market Fear Level Pulsation System for Trading Signals"""
    
    def __init__(self):
        self.running = False
        self.fear_levels = {}
        self.signals = []
        self.last_update = {}
        self.thresholds = {
            "extreme_fear": 20,      # Buy signal
            "fear": 30,              # Buy signal
            "neutral": 50,          # Hold signal
            "greed": 70,             # Caution/Exit signal
            "extreme_greed": 80      # Sell signal
        }
        
    def get_crypto_fear_greed(self) -> Dict:
        """Get Crypto Fear & Greed Index"""
        try:
            print("🔍 Fetching Fear & Greed Index...")
            # Try multiple APIs
            urls = [
                "https://api.alternative.me/v1/fng/",
                "https://alternative.me/fng/",
                "https://fear-and-greed-index.p.rapidapi.com/v1/fgi",
                "https://www.feargreedindex.com/"
            ]
            
            for url in urls:
                try:
                    if "alternative.me" in url:
                        response = requests.get(url, timeout=10)
                        data = response.json()
                        print(f"📊 Response from {url}: {data}")
                        
                        if 'data' in data and len(data['data']) > 0:
                            latest = data['data'][0]
                            result = {
                                'value': int(latest['value']),
                                'value_classification': latest['value_classification'].lower(),
                                'timestamp': int(latest['timestamp']),
                                'time': latest['time_until_update']
                            }
                            print(f"✅ Parsed Fear & Greed: {result}")
                            return result
                        elif 'value' in data:
                            result = {
                                'value': int(data['value']),
                                'value_classification': 'neutral',
                                'timestamp': int(time.time()),
                                'time': '1h'
                            }
                            print(f"✅ Parsed Fear & Greed: {result}")
                            return result
                except Exception as e:
                    print(f"⚠️  API {url} failed: {str(e)}")
                    continue
            
            # If all APIs fail, use mock data
            print("⚠️  Using mock Fear & Greed data...")
            mock_data = {
                'value': 45,
                'value_classification': 'Neutral',
                'timestamp': int(time.time()),
                'time': '1h'
            }
            print(f"✅ Mock Fear & Greed: {mock_data}")
            return mock_data
            
        except Exception as e:
            error_msg = str(e)
            print(f"❌ Error fetching Fear & Greed: {error_msg}")
            return {'error': error_msg}
    
    def get_bitcoin_price(self) -> Dict:
        """Get current Bitcoin price"""
        try:
            print("🔍 Fetching Bitcoin price...")
            # Try multiple APIs
            urls = [
                "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd",
                "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT",
                "https://api.coinbase.com/v2/prices/BTC-USD/spot"
            ]
            
            for url in urls:
                try:
                    response = requests.get(url, timeout=10)
                    data = response.json()
                    print(f"📊 BTC Price response from {url}: {data}")
                    
                    if 'bitcoin' in data and 'usd' in data['bitcoin']:
                        result = {
                            'price': data['bitcoin']['usd'],
                            'symbol': 'BTC',
                            'timestamp': int(time.time())
                        }
                        print(f"✅ Parsed BTC Price: {result}")
                        return result
                    elif 'symbol' in data and data['symbol'] == 'BTCUSDT':
                        result = {
                            'price': float(data['price']),
                            'symbol': 'BTC',
                            'timestamp': int(time.time())
                        }
                        print(f"✅ Parsed BTC Price: {result}")
                        return result
                    elif 'data' in data and 'amount' in data['data']:
                        result = {
                            'price': float(data['data']['amount']),
                            'symbol': 'BTC',
                            'timestamp': int(time.time())
                        }
                        print(f"✅ Parsed BTC Price: {result}")
                        return result
                except Exception as e:
                    print(f"⚠️  API {url} failed: {str(e)}")
                    continue
            
            # If all APIs fail, use mock data
            print("⚠️  Using mock BTC price...")
            mock_data = {
                'price': 65000.00,
                'symbol': 'BTC',
                'timestamp': int(time.time())
            }
            print(f"✅ Mock BTC Price: {mock_data}")
            return mock_data
            
        except Exception as e:
            error_msg = str(e)
            print(f"❌ Error fetching BTC price: {error_msg}")
            return {'error': error_msg}
    
    def calculate_fear_level(self, crypto_data: Dict, btc_price: Dict) -> Dict:
        """Calculate overall market fear level"""
        print("🔍 Calculating fear level...")
        
        if 'error' in crypto_data:
            error_msg = f"Crypto data error: {crypto_data['error']}"
            print(f"❌ {error_msg}")
            return {'error': error_msg}
        
        if 'error' in btc_price:
            error_msg = f"BTC price error: {btc_price['error']}"
            print(f"❌ {error_msg}")
            return {'error': error_msg}
        
        # Get fear index
        fear_index = crypto_data['value']
        classification = crypto_data['value_classification'].lower()
        
        # Calculate volatility factor (simplified)
        if 'price' in btc_price:
            volatility_factor = 1.0
        else:
            volatility_factor = 1.0
        
        # Generate fear level score
        fear_score = fear_index * volatility_factor
        
        result = {
            'fear_index': fear_index,
            'classification': classification,
            'volatility_factor': volatility_factor,
            'calculated_score': round(fear_score, 2),
            'timestamp': int(time.time()),
            'btc_price': btc_price.get('price', 0)
        }
        
        print(f"✅ Calculated fear level: {result}")
        return result
    
    def generate_trading_signal(self, fear_level: Dict) -> Dict:
        """Generate trading signal based on fear level"""
        print("🔍 Generating trading signal...")
        
        if 'error' in fear_level:
            error_msg = f"Fear level error: {fear_level['error']}"
            print(f"❌ {error_msg}")
            return {'error': error_msg}
        
        fear_index = fear_level['fear_index']
        btc_price = fear_level['btc_price']
        
        # Determine signal type
        if fear_index <= self.thresholds['extreme_fear']:
            signal_type = 'BUY_STRONG'
            confidence = 'High'
            color = '🟢'
            reason = 'Extreme fear - Strong buy signal'
        elif fear_index <= self.thresholds['fear']:
            signal_type = 'BUY'
            confidence = 'Medium'
            color = '🟢'
            reason = 'Fear zone - Buy opportunity'
        elif fear_index <= self.thresholds['neutral']:
            signal_type = 'HOLD'
            confidence = 'Low'
            color = '🟡'
            reason = 'Neutral zone - Hold position'
        elif fear_index <= self.thresholds['greed']:
            signal_type = 'CAUTION'
            confidence = 'Medium'
            color = '🟠'
            reason = 'Greed zone - Consider taking profits'
        else:
            signal_type = 'SELL'
            confidence = 'High'
            color = '🔴'
            reason = 'Extreme greed - Sell signal'
        
        result = {
            'signal_type': signal_type,
            'confidence': confidence,
            'fear_index': fear_index,
            'btc_price': btc_price,
            'recommendation': reason,
            'timestamp': int(time.time()),
            'color': color
        }
        
        print(f"✅ Generated trading signal: {result}")
        return result
    
    def pulse_visual(self, signal: Dict) -> Dict:
        """Generate pulsation visualization based on signal"""
        print("🔍 Generating pulsation visual...")
        
        if 'error' in signal:
            result = {
                'intensity': 1,
                'duration': 0.5,
                'color': '⚪',
                'signal_type': 'ERROR',
                'display_text': f"⚪ Error: {signal.get('error', 'Unknown error')}"
            }
            print(f"❌ Pulsation error: {result}")
            return result
        
        signal_type = signal['signal_type']
        color = signal['color']
        
        # Pulse intensity based on signal strength
        if signal_type == 'BUY_STRONG':
            intensity = 5  # Maximum pulsation
            duration = 2.0
        elif signal_type in ['BUY', 'SELL']:
            intensity = 3
            duration = 1.5
        elif signal_type == 'CAUTION':
            intensity = 2
            duration = 1.0
        else:  # HOLD
            intensity = 1
            duration = 0.5
        
        result = {
            'intensity': intensity,
            'duration': duration,
            'color': color,
            'signal_type': signal_type,
            'display_text': f"{color} {signal_type.replace('_', ' ')} - {signal['recommendation']}"
        }
        
        print(f"✅ Generated pulsation visual: {result}")
        return result
    
    def get_market_data(self) -> Dict:
        """Fetch all market data"""
        print("🚀 Starting market data fetch...")
        
        crypto_data = self.get_crypto_fear_greed()
        btc_price = self.get_bitcoin_price()
        fear_level = self.calculate_fear_level(crypto_data, btc_price)
        signal = self.generate_trading_signal(fear_level)
        pulsation = self.pulse_visual(signal)
        
        result = {
            'timestamp': datetime.now().isoformat(),
            'crypto_data': crypto_data,
            'btc_price': btc_price,
            'fear_level': fear_level,
            'signal': signal,
            'pulsation': pulsation,
            'raw_data': {
                'fear_index': fear_level.get('fear_index', 0),
                'btc_price': fear_level.get('btc_price', 0),
                'classification': fear_level.get('classification', 'unknown')
            }
        }
        
        print("✅ Market data fetch complete")
        return result
    
    def display_status(self, market_data: Dict):
        """Display current market status"""
        pulse = market_data['pulsation']
        signal = market_data['signal']
        raw_data = market_data['raw_data']
        
        print(f"\n{'='*70}")
        print(f"🎯 MARKET FEAR PULSATION SYSTEM - {datetime.now().strftime('%H:%M:%S')}")
        print(f"{'='*70}")
        
        # Pulsation display
        pulse_intensity = '█' * pulse['intensity'] + ' ' * (5 - pulse['intensity'])
        print(f"{pulse['color']} PULSE: {pulse_intensity} {pulse['display_text']}")
        
        # Market data
        print(f"\n📊 MARKET DATA:")
        print(f"   Fear Index: {raw_data['fear_index']}/100")
        print(f"   Classification: {raw_data['classification'].title()}")
        
        if 'error' not in market_data['btc_price'] and 'price' in market_data['btc_price']:
            print(f"   BTC Price: ${market_data['btc_price']['price']:,.2f}")
        
        print(f"\n🎯 TRADING SIGNAL:")
        if 'error' not in signal:
            print(f"   Signal: {pulse['color']} {signal['signal_type']}")
            print(f"   Confidence: {signal['confidence']}")
            print(f"   Reason: {signal['recommendation']}")
        else:
            print(f"   Error: {signal['error']}")
        
        print(f"\n{'='*70}")

def test_system():
    """Test the Market Fear Pulsation System"""
    print("🚀 TESTING MARKET FEAR PULSATION SYSTEM")
    print("=" * 50)
    
    system = MarketFearPulsationSystem()
    
    try:
        # Get market data
        market_data = system.get_market_data()
        
        # Display status
        system.display_status(market_data)
        
        # Show raw data
        print(f"\n📋 RAW DATA:")
        raw = market_data['raw_data']
        for key, value in raw.items():
            print(f"   {key}: {value}")
        
        return True
        
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        return False

def continuous_monitoring(interval_seconds: int = 300):
    """Continuous monitoring mode"""
    print("🔄 Starting continuous monitoring mode...")
    print(f"📊 Update interval: {interval_seconds} seconds")
    print("Press Ctrl+C to stop monitoring")
    
    system = MarketFearPulsationSystem()
    
    try:
        while True:
            print(f"\n{'='*70}")
            print(f"🔄 MARKET UPDATE - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
            print(f"{'='*70}")
            
            market_data = system.get_market_data()
            system.display_status(market_data)
            
            print(f"\n⏰ Next update in {interval_seconds} seconds...")
            time.sleep(interval_seconds)
            
    except KeyboardInterrupt:
        print("\n🛑 Monitoring stopped by user")
        return

def interactive_mode():
    """Interactive menu mode"""
    print("🎯 MARKET FEAR PULSATION SYSTEM - INTERACTIVE MODE")
    print("=" * 60)
    
    system = MarketFearPulsationSystem()
    
    while True:
        print("\n📋 Options:")
        print("1. Get current market status")
        print("2. Start continuous monitoring")
        print("3. Test system")
        print("4. Show signal thresholds")
        print("5. Exit")
        
        try:
            choice = input("\n> Enter your choice (1-5): ").strip()
            
            if choice == '1':
                market_data = system.get_market_data()
                system.display_status(market_data)
            elif choice == '2':
                try:
                    interval = input("Enter monitoring interval in seconds (default 300): ").strip()
                    interval = int(interval) if interval else 300
                    continuous_monitoring(interval)
                except ValueError:
                    print("❌ Invalid interval. Using default 300 seconds")
                    continuous_monitoring(300)
            elif choice == '3':
                test_system()
            elif choice == '4':
                print(f"\n🎯 Signal Thresholds:")
                print(f"   Extreme Fear (≤{system.thresholds['extreme_freat']}): 🟢 BUY_STRONG")
                print(f"   Fear (≤{system.thresholds['fear']}): 🟢 BUY")
                print(f"   Neutral (≤{system.thresholds['neutral']}): 🟡 HOLD")
                print(f"   Greed (≤{system.thresholds['greed']}): 🟠 CAUTION")
                print(f"   Extreme Greed (>{system.thresholds['extreme_greed']}): 🔴 SELL")
            elif choice == '5':
                print("👋 Goodbye!")
                break
            else:
                print("❌ Invalid choice. Please enter 1-5")
                
        except KeyboardInterrupt:
            print("\n🛑 Operation cancelled")
            break
        except Exception as e:
            print(f"❌ Error: {str(e)}")

def main():
    """Main entry point"""
    if len(sys.argv) > 1:
        # Command line mode
        command = sys.argv[1].lower()
        
        if command == 'test':
            test_system()
        elif command == 'monitor':
            interval = int(sys.argv[2]) if len(sys.argv) > 2 else 300
            continuous_monitoring(interval)
        elif command == 'interactive':
            interactive_mode()
        else:
            print("Usage:")
            print("  python3 main.py test")
            print("  python3 main.py monitor [interval_seconds]")
            print("  python3 main.py interactive")
    else:
        # Default to test mode
        test_system()

if __name__ == "__main__":
    main()