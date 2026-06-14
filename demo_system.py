#!/usr/bin/env python3
"""
Demo script showing different market conditions for Pulsation System
"""

import sys
import time
from datetime import datetime

def demo_extreme_fear():
    """Demo: Extreme fear scenario"""
    print("🔴 DEMO: EXTREME FEAR MARKET")
    print("=" * 50)
    
    # Mock extreme fear data
    mock_fear_data = {
        'value': 8,
        'value_classification': 'Extreme Fear',
        'timestamp': int(time.time()),
        'time': '1h'
    }
    mock_btc_data = {'price': 45000, 'symbol': 'BTC', 'timestamp': int(time.time())}
    
    # Calculate signal
    thresholds = {
        "extreme_fear": 20,
        "fear": 30,
        "neutral": 50,
        "greed": 70,
        "extreme_greed": 80
    }
    
    fear_index = mock_fear_data['value']
    if fear_index <= thresholds['extreme_fear']:
        signal_type = 'BUY_STRONG'
        confidence = 'High'
        color = '🟢'
        reason = 'Extreme fear - Strong buy signal'
        intensity = 5
    elif fear_index <= thresholds['fear']:
        signal_type = 'BUY'
        confidence = 'Medium'
        color = '🟢'
        reason = 'Fear zone - Buy opportunity'
        intensity = 3
    elif fear_index <= thresholds['neutral']:
        signal_type = 'HOLD'
        confidence = 'Low'
        color = '🟡'
        reason = 'Neutral zone - Hold position'
        intensity = 1
    elif fear_index <= thresholds['greed']:
        signal_type = 'CAUTION'
        confidence = 'Medium'
        color = '🟠'
        reason = 'Greed zone - Consider taking profits'
        intensity = 2
    else:
        signal_type = 'SELL'
        confidence = 'High'
        color = '🔴'
        reason = 'Extreme greed - Sell signal'
        intensity = 5
    
    pulsation = {
        'intensity': intensity,
        'duration': 2.0 if signal_type == 'BUY_STRONG' else 1.5 if signal_type in ['BUY', 'SELL'] else 1.0 if signal_type == 'CAUTION' else 0.5,
        'color': color,
        'signal_type': signal_type,
        'display_text': f"{color} {signal_type.replace('_', ' ')} - {reason}"
    }
    
    print(f"📊 MARKET CONDITIONS:")
    print(f"   Fear Index: {mock_fear_data['value']}/100")
    print(f"   BTC Price: ${mock_btc_data['price']:,.2f}")
    print(f"   Market Condition: EXTREME FEAR")
    
    print(f"\\n🎯 TRADING SIGNAL:")
    print(f"   {pulsation['color']} {signal_type}")
    print(f"   {pulsation['display_text']}")
    
    print(f"\\n🔴 PULSATION VISUAL:")
    pulse_bars = '█' * pulsation['intensity'] + ' ' * (5 - pulsation['intensity'])
    print(f"   {pulse_bars} (Intensity: {pulsation['intensity']}/5)")
    
    return pulsation

def demo_fear():
    """Demo: Fear scenario"""
    print("\\n🟢 DEMO: FEAR MARKET")
    print("=" * 50)
    
    # Mock fear data
    mock_fear_data = {
        'value': 22,
        'value_classification': 'Fear',
        'timestamp': int(time.time()),
        'time': '1h'
    }
    mock_btc_data = {'price': 48000, 'symbol': 'BTC', 'timestamp': int(time.time())}
    
    # Calculate signal
    thresholds = {
        "extreme_fear": 20,
        "fear": 30,
        "neutral": 50,
        "greed": 70,
        "extreme_greed": 80
    }
    
    fear_index = mock_fear_data['value']
    if fear_index <= thresholds['extreme_fear']:
        signal_type = 'BUY_STRONG'
        confidence = 'High'
        color = '🟢'
        reason = 'Extreme fear - Strong buy signal'
        intensity = 5
    elif fear_index <= thresholds['fear']:
        signal_type = 'BUY'
        confidence = 'Medium'
        color = '🟢'
        reason = 'Fear zone - Buy opportunity'
        intensity = 3
    elif fear_index <= thresholds['neutral']:
        signal_type = 'HOLD'
        confidence = 'Low'
        color = '🟡'
        reason = 'Neutral zone - Hold position'
        intensity = 1
    elif fear_index <= thresholds['greed']:
        signal_type = 'CAUTION'
        confidence = 'Medium'
        color = '🟠'
        reason = 'Greed zone - Consider taking profits'
        intensity = 2
    else:
        signal_type = 'SELL'
        confidence = 'High'
        color = '🔴'
        reason = 'Extreme greed - Sell signal'
        intensity = 5
    
    pulsation = {
        'intensity': intensity,
        'duration': 2.0 if signal_type == 'BUY_STRONG' else 1.5 if signal_type in ['BUY', 'SELL'] else 1.0 if signal_type == 'CAUTION' else 0.5,
        'color': color,
        'signal_type': signal_type,
        'display_text': f"{color} {signal_type.replace('_', ' ')} - {reason}"
    }
    
    print(f"📊 MARKET CONDITIONS:")
    print(f"   Fear Index: {mock_fear_data['value']}/100")
    print(f"   BTC Price: ${mock_btc_data['price']:,.2f}")
    print(f"   Market Condition: FEAR")
    
    print(f"\\n🎯 TRADING SIGNAL:")
    print(f"   {pulsation['color']} {signal_type}")
    print(f"   {pulsation['display_text']}")
    
    print(f"\\n🟢 PULSATION VISUAL:")
    pulse_bars = '█' * pulsation['intensity'] + ' ' * (5 - pulsation['intensity'])
    print(f"   {pulse_bars} (Intensity: {pulsation['intensity']}/5)")
    
    return pulsation

def demo_neutral():
    """Demo: Neutral scenario"""
    print("\\n🟡 DEMO: NEUTRAL MARKET")
    print("=" * 50)
    
    # Mock neutral data
    mock_fear_data = {
        'value': 45,
        'value_classification': 'Neutral',
        'timestamp': int(time.time()),
        'time': '1h'
    }
    mock_btc_data = {'price': 55000, 'symbol': 'BTC', 'timestamp': int(time.time())}
    
    # Calculate signal
    thresholds = {
        "extreme_fear": 20,
        "fear": 30,
        "neutral": 50,
        "greed": 70,
        "extreme_greed": 80
    }
    
    fear_index = mock_fear_data['value']
    if fear_index <= thresholds['extreme_fear']:
        signal_type = 'BUY_STRONG'
        confidence = 'High'
        color = '🟢'
        reason = 'Extreme fear - Strong buy signal'
        intensity = 5
    elif fear_index <= thresholds['fear']:
        signal_type = 'BUY'
        confidence = 'Medium'
        color = '🟢'
        reason = 'Fear zone - Buy opportunity'
        intensity = 3
    elif fear_index <= thresholds['neutral']:
        signal_type = 'HOLD'
        confidence = 'Low'
        color = '🟡'
        reason = 'Neutral zone - Hold position'
        intensity = 1
    elif fear_index <= thresholds['greed']:
        signal_type = 'CAUTION'
        confidence = 'Medium'
        color = '🟠'
        reason = 'Greed zone - Consider taking profits'
        intensity = 2
    else:
        signal_type = 'SELL'
        confidence = 'High'
        color = '🔴'
        reason = 'Extreme greed - Sell signal'
        intensity = 5
    
    pulsation = {
        'intensity': intensity,
        'duration': 2.0 if signal_type == 'BUY_STRONG' else 1.5 if signal_type in ['BUY', 'SELL'] else 1.0 if signal_type == 'CAUTION' else 0.5,
        'color': color,
        'signal_type': signal_type,
        'display_text': f"{color} {signal_type.replace('_', ' ')} - {reason}"
    }
    
    print(f"📊 MARKET CONDITIONS:")
    print(f"   Fear Index: {mock_fear_data['value']}/100")
    print(f"   BTC Price: ${mock_btc_data['price']:,.2f}")
    print(f"   Market Condition: NEUTRAL")
    
    print(f"\\n🎯 TRADING SIGNAL:")
    print(f"   {pulsation['color']} {signal_type}")
    print(f"   {pulsation['display_text']}")
    
    print(f"\\n🟡 PULSATION VISUAL:")
    pulse_bars = '█' * pulsation['intensity'] + ' ' * (5 - pulsation['intensity'])
    print(f"   {pulse_bars} (Intensity: {pulsation['intensity']}/5)")
    
    return pulsation

def demo_greed():
    """Demo: Greed scenario"""
    print("\\n🟠 DEMO: GREED MARKET")
    print("=" * 50)
    
    # Mock greed data
    mock_fear_data = {
        'value': 75,
        'value_classification': 'Greed',
        'timestamp': int(time.time()),
        'time': '1h'
    }
    mock_btc_data = {'price': 68000, 'symbol': 'BTC', 'timestamp': int(time.time())}
    
    # Calculate signal
    thresholds = {
        "extreme_fear": 20,
        "fear": 30,
        "neutral": 50,
        "greed": 70,
        "extreme_greed": 80
    }
    
    fear_index = mock_fear_data['value']
    if fear_index <= thresholds['extreme_fear']:
        signal_type = 'BUY_STRONG'
        confidence = 'High'
        color = '🟢'
        reason = 'Extreme fear - Strong buy signal'
        intensity = 5
    elif fear_index <= thresholds['fear']:
        signal_type = 'BUY'
        confidence = 'Medium'
        color = '🟢'
        reason = 'Fear zone - Buy opportunity'
        intensity = 3
    elif fear_index <= thresholds['neutral']:
        signal_type = 'HOLD'
        confidence = 'Low'
        color = '🟡'
        reason = 'Neutral zone - Hold position'
        intensity = 1
    elif fear_index <= thresholds['greed']:
        signal_type = 'CAUTION'
        confidence = 'Medium'
        color = '🟠'
        reason = 'Greed zone - Consider taking profits'
        intensity = 2
    else:
        signal_type = 'SELL'
        confidence = 'High'
        color = '🔴'
        reason = 'Extreme greed - Sell signal'
        intensity = 5
    
    pulsation = {
        'intensity': intensity,
        'duration': 2.0 if signal_type == 'BUY_STRONG' else 1.5 if signal_type in ['BUY', 'SELL'] else 1.0 if signal_type == 'CAUTION' else 0.5,
        'color': color,
        'signal_type': signal_type,
        'display_text': f"{color} {signal_type.replace('_', ' ')} - {reason}"
    }
    
    print(f"📊 MARKET CONDITIONS:")
    print(f"   Fear Index: {mock_fear_data['value']}/100")
    print(f"   BTC Price: ${mock_btc_data['price']:,.2f}")
    print(f"   Market Condition: GREED")
    
    print(f"\\n🎯 TRADING SIGNAL:")
    print(f"   {pulsation['color']} {signal_type}")
    print(f"   {pulsation['display_text']}")
    
    print(f"\\n🟠 PULSATION VISUAL:")
    pulse_bars = '█' * pulsation['intensity'] + ' ' * (5 - pulsation['intensity'])
    print(f"   {pulse_bars} (Intensity: {pulsation['intensity']}/5)")
    
    return pulsation

def demo_extreme_greed():
    """Demo: Extreme greed scenario"""
    print("\\n🔴 DEMO: EXTREME GREED MARKET")
    print("=" * 50)
    
    # Mock extreme greed data
    mock_fear_data = {
        'value': 92,
        'value_classification': 'Extreme Greed',
        'timestamp': int(time.time()),
        'time': '1h'
    }
    mock_btc_data = {'price': 75000, 'symbol': 'BTC', 'timestamp': int(time.time())}
    
    # Calculate signal
    thresholds = {
        "extreme_fear": 20,
        "fear": 30,
        "neutral": 50,
        "greed": 70,
        "extreme_greed": 80
    }
    
    fear_index = mock_fear_data['value']
    if fear_index <= thresholds['extreme_fear']:
        signal_type = 'BUY_STRONG'
        confidence = 'High'
        color = '🟢'
        reason = 'Extreme fear - Strong buy signal'
        intensity = 5
    elif fear_index <= thresholds['fear']:
        signal_type = 'BUY'
        confidence = 'Medium'
        color = '🟢'
        reason = 'Fear zone - Buy opportunity'
        intensity = 3
    elif fear_index <= thresholds['neutral']:
        signal_type = 'HOLD'
        confidence = 'Low'
        color = '🟡'
        reason = 'Neutral zone - Hold position'
        intensity = 1
    elif fear_index <= thresholds['greed']:
        signal_type = 'CAUTION'
        confidence = 'Medium'
        color = '🟠'
        reason = 'Greed zone - Consider taking profits'
        intensity = 2
    else:
        signal_type = 'SELL'
        confidence = 'High'
        color = '🔴'
        reason = 'Extreme greed - Sell signal'
        intensity = 5
    
    pulsation = {
        'intensity': intensity,
        'duration': 2.0 if signal_type == 'BUY_STRONG' else 1.5 if signal_type in ['BUY', 'SELL'] else 1.0 if signal_type == 'CAUTION' else 0.5,
        'color': color,
        'signal_type': signal_type,
        'display_text': f"{color} {signal_type.replace('_', ' ')} - {reason}"
    }
    
    print(f"📊 MARKET CONDITIONS:")
    print(f"   Fear Index: {mock_fear_data['value']}/100")
    print(f"   BTC Price: ${mock_btc_data['price']:,.2f}")
    print(f"   Market Condition: EXTREME GREED")
    
    print(f"\\n🎯 TRADING SIGNAL:")
    print(f"   {pulsation['color']} {signal_type}")
    print(f"   {pulsation['display_text']}")
    
    print(f"\\n🔴 PULSATION VISUAL:")
    pulse_bars = '█' * pulsation['intensity'] + ' ' * (5 - pulsation['intensity'])
    print(f"   {pulse_bars} (Intensity: {pulsation['intensity']}/5)")
    
    return pulsation

def main():
    """Run all demos"""
    print("🎯 MARKET FEAR PULSATION SYSTEM - DEMO")
    print("=" * 60)
    print(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 60)
    
    demos = [
        ("Extreme Fear", demo_extreme_fear),
        ("Fear", demo_fear),
        ("Neutral", demo_neutral),
        ("Greed", demo_greed),
        ("Extreme Greed", demo_extreme_greed)
    ]
    
    results = []
    
    for name, demo_func in demos:
        try:
            result = demo_func()
            results.append((name, result))
            time.sleep(1)  # Brief pause between demos
        except Exception as e:
            print(f"❌ Demo failed for {name}: {str(e)}")
    
    # Summary
    print("\\n" + "=" * 60)
    print("📊 DEMO SUMMARY")
    print("=" * 60)
    
    for name, pulsation in results:
        print(f"   {name:15} | {pulsation['color']} {pulsation['signal_type']:10} | Intensity: {pulsation['intensity']}/5")
    
    print("\\n💡 Key Insights:")
    print("   • Strong signals (BUY_STRONG/SELL) have highest pulsation (5/5)")
    print("   • Color coding: 🟢 Buy, 🟡 Hold, 🟠 Caution, 🔴 Sell")
    print("   • Pulsation intensity reflects signal strength")
    print("   • Real market data used when APIs are available")

if __name__ == "__main__":
    main()