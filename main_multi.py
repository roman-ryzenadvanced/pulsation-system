#!/usr/bin/env python3
"""
Market Fear Pulsation System with Multiple Crypto Instruments
"""

import sys
import os
import json
import time
import requests
from datetime import datetime, timedelta
from typing import Dict, List, Optional

# CoinGecko API configuration
COINGECKO_API = "https://api.coingecko.com/api/v3"
SUPPORTED_INSTRUMENTS = {
    "BTC": {
        "name": "Bitcoin",
        "symbol": "BTC",
        "vs_currency": "usd",
        "market_cap_weight": 0.45,  # ~45% of crypto market cap
        "volatility_factor": 1.0
    },
    "ETH": {
        "name": "Ethereum", 
        "symbol": "ETH",
        "vs_currency": "usd",
        "market_cap_weight": 0.20,  # ~20% of crypto market cap
        "volatility_factor": 1.2
    },
    "BNB": {
        "name": "Binance Coin",
        "symbol": "BNB", 
        "vs_currency": "usd",
        "market_cap_weight": 0.03,  # ~3% of crypto market cap
        "volatility_factor": 1.1
    },
    "ADA": {
        "name": "Cardano",
        "symbol": "ADA",
        "vs_currency": "usd",
        "market_cap_weight": 0.02,  # ~2% of crypto market cap
        "volatility_factor": 1.3
    },
    "SOL": {
        "name": "Solana",
        "symbol": "SOL",
        "vs_currency": "usd",
        "market_cap_weight": 0.02,  # ~2% of crypto market cap
        "volatility_factor": 1.5
    },
    "XRP": {
        "name": "Ripple",
        "symbol": "XRP",
        "vs_currency": "usd",
        "market_cap_weight": 0.02,  # ~2% of crypto market cap
        "volatility_factor": 1.2
    }
}

# Trading pairs for each instrument
TRADING_PAIRS = {
    "BTC": ["BTC/USD", "BTC/EUR", "BTC/GBP"],
    "ETH": ["ETH/USD", "ETH/BTC", "ETH/USDT"],
    "BNB": ["BNB/USD", "BNB/BTC", "BNB/ETH"],
    "ADA": ["ADA/USD", "ADA/BTC", "ADA/ETH"],
    "SOL": ["SOL/USD", "SOL/BTC", "SOL/ETH"],
    "XRP": ["XRP/USD", "XRP/BTC", "XRP/ETH"]
}

class MarketFearPulsationSystem:
    def __init__(self, instrument="BTC"):
        self.instrument = instrument.upper()
        self.instrument_config = SUPPORTED_INSTRUMENTS.get(instrument)
        if not self.instrument_config:
            raise ValueError(f"Unsupported instrument: {instrument}. Supported: {list(SUPPORTED_INSTRUMENTS.keys())}")
        
        self.api_key = os.getenv('COINGECKO_API_KEY')
        self.cache = {}
        self.cache_timeout = 300  # 5 minutes
        
    def get_market_data(self):
        """Get market data for the current instrument"""
        try:
            # Get Fear & Greed Index
            fear_data = self._get_fear_greed_index()
            
            # Get crypto price
            price_data = self._get_crypto_price()
            
            # Calculate fear level
            fear_level = self._calculate_fear_level(fear_data, price_data)
            
            # Generate trading signal
            signal = self._generate_trading_signal(fear_level, price_data)
            
            # Generate pulsation visual
            pulsation = self._generate_pulsation_visual(signal)
            
            # Combine all data
            result = {
                'timestamp': datetime.now().isoformat(),
                'instrument': self.instrument,
                'instrument_name': self.instrument_config['name'],
                'pulsation': pulsation,
                'signal': signal,
                'raw_data': {
                    'fear_index': fear_level['fear_index'],
                    'classification': fear_level['classification'],
                    'btc_price': price_data['price'],
                    'instrument_price': price_data['price'],
                    'market_cap_weight': self.instrument_config['market_cap_weight'],
                    'volatility_factor': self.instrument_config['volatility_factor'],
                    'timestamp': fear_level['timestamp']
                }
            }
            
            return result
            
        except Exception as e:
            return {
                'error': str(e),
                'timestamp': datetime.now().isoformat(),
                'instrument': self.instrument
            }
    
    def _get_fear_greed_index(self):
        """Get Fear & Greed Index (mock data for now)"""
        # Try to get real data, fallback to mock
        try:
            # Alternative.me API
            response = requests.get("https://api.alternative.me/v1/fng/", timeout=10)
            if response.status_code == 200:
                data = response.json()
                if 'data' in data and len(data['data']) > 0:
                    return {
                        'value': int(data['data'][0]['value']),
                        'value_classification': data['data'][0]['value_classification'],
                        'timestamp': int(time.time()),
                        'time': data['data'][0]['time_until_update']
                    }
        except Exception as e:
            print(f"⚠️  Fear & Greed API failed: {e}")
        
        # Fallback to mock data
        return {
            'value': 45,  # Neutral
            'value_classification': 'Neutral',
            'timestamp': int(time.time()),
            'time': '1h'
        }
    
    def _get_crypto_price(self):
        """Get current crypto price from CoinGecko"""
        cache_key = f"{self.instrument}_price"
        
        # Check cache
        if cache_key in self.cache:
            cached_data, timestamp = self.cache[cache_key]
            if (datetime.now() - timestamp).seconds < self.cache_timeout:
                return cached_data
        
        try:
            url = f"{COINGECKO_API}/simple/price?ids={self.instrument.lower()}&vs_currencies={self.instrument_config['vs_currency']}"
            response = requests.get(url, timeout=10)
            
            if response.status_code == 200:
                data = response.json()
                coin_id = self.instrument.lower()
                
                if coin_id in data and self.instrument_config['vs_currency'] in data[coin_id]:
                    price = data[coin_id][self.instrument_config['vs_currency']]
                    
                    # Cache the result
                    self.cache[cache_key] = (
                        {
                            'price': price,
                            'symbol': self.instrument,
                            'timestamp': int(time.time())
                        },
                        datetime.now()
                    )
                    
                    return {
                        'price': price,
                        'symbol': self.instrument,
                        'timestamp': int(time.time())
                    }
        except Exception as e:
            print(f"⚠️  Price API failed: {e}")
        
        # Fallback to mock price
        return {
            'price': 50000 + (hash(self.instrument) % 30000),  # Different mock price per instrument
            'symbol': self.instrument,
            'timestamp': int(time.time())
        }
    
    def _calculate_fear_level(self, fear_data, price_data):
        """Calculate fear level considering instrument-specific factors"""
        fear_value = fear_data['value']
        
        # Apply instrument-specific volatility adjustment
        volatility_adjustment = self.instrument_config['volatility_factor']
        adjusted_fear = min(100, max(0, fear_value * volatility_adjustment))
        
        # Weight by market cap (larger instruments have more influence)
        market_cap_weight = self.instrument_config['market_cap_weight']
        final_fear = adjusted_fear * market_cap_weight + fear_value * (1 - market_cap_weight)
        
        # Classify the fear level
        if final_fear <= 20:
            classification = 'extreme_fear'
        elif final_fear <= 30:
            classification = 'fear'
        elif final_fear <= 50:
            classification = 'neutral'
        elif final_fear <= 70:
            classification = 'greed'
        else:
            classification = 'extreme_greed'
        
        return {
            'fear_index': int(final_fear),
            'classification': classification,
            'raw_fear_index': fear_value,
            'adjusted_fear': adjusted_fear,
            'market_cap_weight': market_cap_weight,
            'volatility_factor': volatility_adjustment,
            'final_fear': final_fear,
            'timestamp': int(time.time()),
            'instrument_price': price_data['price']
        }
    
    def _generate_trading_signal(self, fear_level, price_data):
        """Generate trading signal based on fear level"""
        fear_index = fear_level['fear_index']
        classification = fear_level['classification']
        
        # Base signals
        signal_templates = {
            'extreme_fear': {
                'signal_type': 'BUY_STRONG',
                'confidence': 'High',
                'color': '🟢',
                'recommendation': f'{self.instrument_config["name"]} is in extreme fear - Strong buy opportunity. Market panic often presents buying opportunities.',
                'rationale': 'Extreme fear suggests oversold conditions'
            },
            'fear': {
                'signal_type': 'BUY', 
                'confidence': 'Medium',
                'color': '🟢',
                'recommendation': f'{self.instrument_config["name"]} is in fear zone - Consider accumulating positions. Fear zone often presents good entry points.',
                'rationale': 'Fear indicates undervalued assets'
            },
            'neutral': {
                'signal_type': 'HOLD',
                'confidence': 'Low',
                'color': '🟡', 
                'recommendation': f'{self.instrument_config["name"]} is in neutral zone - Maintain current positions. No strong catalysts detected.',
                'rationale': 'Neutral market suggests equilibrium'
            },
            'greed': {
                'signal_type': 'CAUTION',
                'confidence': 'Medium',
                'color': '🟠',
                'recommendation': f'{self.instrument_config["name"]} is in greed zone - Consider taking profits. Greed often precedes corrections.',
                'rationale': 'Greed suggests overvalued conditions'
            },
            'extreme_greed': {
                'signal_type': 'SELL',
                'confidence': 'High', 
                'color': '🔴',
                'recommendation': f'{self.instrument_config["name"]} is in extreme greed - Sell signals active. Market euphoria often precedes downturns.',
                'rationale': 'Extreme greed suggests bubble conditions'
            }
        }
        
        template = signal_templates[classification]
        
        # Adjust confidence based on volatility
        volatility = self.instrument_config['volatility_factor']
        if volatility > 1.3:
            template['confidence'] = 'Medium-High' if template['confidence'] == 'High' else 'Medium'
        
        return {
            **template,
            'fear_index': fear_index,
            'classification': classification,
            'instrument': self.instrument,
            'instrument_name': self.instrument_config['name'],
            'price': price_data['price'],
            'timestamp': datetime.now().isoformat()
        }
    
    def _generate_pulsation_visual(self, signal):
        """Generate pulsation visual based on signal strength"""
        # Determine intensity based on signal confidence and market condition
        base_intensity = {
            'BUY_STRONG': 4,
            'BUY': 3,
            'HOLD': 1,
            'CAUTION': 2,
            'SELL': 4
        }
        
        intensity = base_intensity.get(signal['signal_type'], 1)
        
        # Adjust for volatility
        volatility = self.instrument_config['volatility_factor']
        if volatility > 1.4:
            intensity = min(5, intensity + 1)
        elif volatility < 1.0:
            intensity = max(1, intensity - 1)
        
        # Create visual pulse
        pulse_bars = '█' * intensity + ' ' * (5 - intensity)
        
        # Determine duration based on signal strength
        duration = 0.5 + (intensity * 0.1)
        
        return {
            'intensity': intensity,
            'duration': duration,
            'color': signal['color'],
            'signal_type': signal['signal_type'],
            'display_text': f"{signal['color']} {signal['signal_type']} - {signal['rationale']}",
            'visual': pulse_bars
        }
    
    def get_all_instruments_data(self):
        """Get market data for all supported instruments"""
        results = {}
        
        for instrument in SUPPORTED_INSTRUMENTS.keys():
            try:
                temp_system = MarketFearPulsationSystem(instrument)
                results[instrument] = temp_system.get_market_data()
            except Exception as e:
                results[instrument] = {
                    'error': str(e),
                    'timestamp': datetime.now().isoformat(),
                    'instrument': instrument
                }
        
        return results
    
    def get_trading_pairs(self, instrument):
        """Get available trading pairs for an instrument"""
        return TRADING_PAIRS.get(instrument, [])
    
    def get_supported_instruments(self):
        """Get list of supported instruments"""
        return list(SUPPORTED_INSTRUMENTS.keys())
    
    def get_instrument_info(self, instrument):
        """Get detailed information about an instrument"""
        return SUPPORTED_INSTRUMENTS.get(instrument.upper())

def test_system():
    """Test the multi-instrument system"""
    print("🚀 TESTING MULTI-INSTRUMENT MARKET FEAR PULSATION SYSTEM")
    print("=" * 70)
    
    system = MarketFearPulsationSystem()
    
    # Test current instrument
    result = system.get_market_data()
    print(f"🎯 Current Instrument: {system.instrument}")
    print(f"📊 Fear Index: {result['raw_data']['fear_index']}/100")
    print(f"💰 Price: ${result['raw_data']['instrument_price']:,.2f}")
    print(f"🎯 Signal: {result['pulsation']['signal_type']}")
    
    # Test all instruments
    print(f"\n🌍 ALL INSTRUMENTS OVERVIEW")
    print("=" * 50)
    
    all_data = system.get_all_instruments_data()
    
    for instrument, data in all_data.items():
        if 'error' not in data:
            pulse = data['pulsation']
            signal = data['signal']
            print(f"{instrument:4} | {pulse['signal_type']:10} | {pulse['color']} | ${data['raw_data']['instrument_price']:>8,.2f}")
        else:
            print(f"{instrument:4} | ERROR: {data['error'][:30]}...")
    
    print(f"\n🔗 TRADING PAIRS")
    print("=" * 50)
    
    for instrument in system.get_supported_instruments():
        pairs = system.get_trading_pairs(instrument)
        print(f"{instrument}: {', '.join(pairs)}")

if __name__ == "__main__":
    test_system()