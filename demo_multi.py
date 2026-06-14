#!/usr/bin/env python3
"""
Demo script for Multi-Instrument Market Fear Pulsation System
"""

from main_multi import MarketFearPulsationSystem, SUPPORTED_INSTRUMENTS
import time
from datetime import datetime

def demo_multi_instrument_system():
    """Demonstrate the multi-instrument system"""
    print("🚀 DEMO: MULTI-INSTRUMENT MARKET FEAR PULSATION SYSTEM")
    print("=" * 70)
    
    system = MarketFearPulsationSystem()
    
    # Demo 1: Single instrument analysis
    print("\n🎯 DEMO 1: Single Instrument Analysis (BTC)")
    print("-" * 50)
    btc_system = MarketFearPulsationSystem("BTC")
    btc_data = btc_system.get_market_data()
    display_signal(btc_data)
    
    # Demo 2: Compare all instruments
    print(f"\n🌍 DEMO 2: All Instruments Comparison")
    print("-" * 50)
    
    all_data = system.get_all_instruments_data()
    print(f"{'INSTR':4} {'NAME':15} {'PRICE':>10} {'SIGNAL':10} {'COLOR':6} {'INTENSITY':8}")
    print("-" * 60)
    
    for instrument, data in all_data.items():
        if 'error' not in data:
            price = data['raw_data']['instrument_price']
            signal = data['pulsation']['signal_type']
            color = data['pulsation']['color']
            intensity = data['pulsation']['intensity']
            name = data['instrument_name']
            
            print(f"{instrument:4} {name[:15]:<15} ${price:>9,.2f} {signal:10} {color:5} {'█'*intensity}")
    
    # Demo 3: Trading pairs for each instrument
    print(f"\n🔗 DEMO 3: Trading Pairs Overview")
    print("-" * 50)
    
    for instrument in SUPPORTED_INSTRUMENTS.keys():
        pairs = system.get_trading_pairs(instrument)
        print(f"{instrument}: {', '.join(pairs)}")
    
    # Demo 4: Extreme scenarios simulation
    print(f"\n📊 DEMO 4: Extreme Market Scenarios")
    print("-" * 50)
    
    # Simulate extreme fear
    print("\n🟡 EXTREME FEAR SCENARIO (Mock Data)")
    print("-" * 30)
    mock_system = MarketFearPulsationSystem("BTC")
    
    # Override fear data to simulate extreme fear
    original_get_fear = mock_system._get_fear_greed_index
    mock_system._get_fear_greed_index = lambda: {'value': 15, 'value_classification': 'Extreme Fear', 'timestamp': int(time.time()), 'time': '1h'}
    
    fear_data = mock_system._get_fear_greed_index()
    price_data = mock_system._get_crypto_price()
    fear_level = mock_system._calculate_fear_level(fear_data, price_data)
    signal = mock_system._generate_trading_signal(fear_level, price_data)
    pulsation = mock_system._generate_pulsation_visual(signal)
    
    print(f"Instrument: {mock_system.instrument}")
    print(f"Fear Index: {fear_level['fear_index']}/100")
    print(f"Signal: {signal['signal_type']} ({signal['confidence']} confidence)")
    print(f"Color: {signal['color']}")
    print(f"Recommendation: {signal['recommendation']}")
    print(f"Pulsation Visual: {pulsation['visual']}")
    
    # Simulate extreme greed
    print("\n🔴 EXTREME GREED SCENARIO (Mock Data)")
    print("-" * 30)
    
    mock_system._get_fear_greed_index = lambda: {'value': 85, 'value_classification': 'Extreme Greed', 'timestamp': int(time.time()), 'time': '1h'}
    
    fear_data = mock_system._get_fear_greed_index()
    price_data = mock_system._get_crypto_price()
    fear_level = mock_system._calculate_fear_level(fear_data, price_data)
    signal = mock_system._generate_trading_signal(fear_level, price_data)
    pulsation = mock_system._generate_pulsation_visual(signal)
    
    print(f"Instrument: {mock_system.instrument}")
    print(f"Fear Index: {fear_level['fear_index']}/100")
    print(f"Signal: {signal['signal_type']} ({signal['confidence']} confidence)")
    print(f"Color: {signal['color']}")
    print(f"Recommendation: {signal['recommendation']}")
    print(f"Pulsation Visual: {pulsation['visual']}")

def display_signal(data):
    """Display signal data in a readable format"""
    if 'error' in data:
        print(f"❌ Error: {data['error']}")
        return
    
    signal = data['signal']
    pulsation = data['pulsation']
    raw_data = data['raw_data']
    
    print(f"📊 Instrument: {data['instrument']} ({data['instrument_name']})")
    print(f"💰 Price: ${raw_data['instrument_price']:,.2f}")
    print(f"🎯 Fear Index: {raw_data['fear_index']}/100 ({raw_data['classification'].replace('_', ' ').title()})")
    print(f"🎯 Signal: {signal['signal_type']} ({signal['confidence']} confidence)")
    print(f"🎨 Color: {signal['color']}")
    print(f"💬 Recommendation: {signal['recommendation']}")
    print(f"🎮 Visual Pulsation: {pulsation['visual']} ({pulsation['intensity']}/5 intensity)")
    print(f"⏱️  Duration: {pulsation['duration']}s")
    print(f"🕐 Timestamp: {data['timestamp']}")

def demo_instrument_specific_features():
    """Demonstrate instrument-specific features"""
    print(f"\n🔧 DEMO 5: Instrument-Specific Features")
    print("-" * 50)
    
    system = MarketFearPulsationSystem()
    
    for instrument in SUPPORTED_INSTRUMENTS.keys():
        info = system.get_instrument_info(instrument)
        print(f"\n{instrument} ({info['name']}):")
        print(f"  Market Cap Weight: {info['market_cap_weight']*100:.1f}%")
        print(f"  Volatility Factor: {info['volatility_factor']:.1f}x")
        print(f"  Price Data: {instrument}/{info['vs_currency'].upper()}")
        pairs = system.get_trading_pairs(instrument)
        print(f"  Trading Pairs: {', '.join(pairs)}")

if __name__ == "__main__":
    demo_multi_instrument_system()
    demo_instrument_specific_features()