#!/usr/bin/env python3
"""
Web Server for Market Fear Pulsation System Demo
"""

from flask import Flask, jsonify, render_template_string
import json
import sys
import os
from datetime import datetime

# Import the MarketFearPulsationSystem
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from main import MarketFearPulsationSystem

app = Flask(__name__)

# Global instance of the system
pulsation_system = MarketFearPulsationSystem()

def format_signal_display(signal_data):
    """Format signal data for web display"""
    if 'error' in signal_data:
        return {
            'status': 'error',
            'error': signal_data['error']
        }
    
    pulse = signal_data['pulsation']
    raw = signal_data['raw_data']
    
    # Create pulse visualization
    pulse_bars = '█' * pulse['intensity'] + ' ' * (5 - pulse['intensity'])
    
    # Get market condition description
    classification = raw['classification'].title()
    if raw['fear_index'] <= 20:
        condition_desc = "EXTREME FEAR - PANIC MARKET"
    elif raw['fear_index'] <= 30:
        condition_desc = "FEAR - OPPORTUNITY ZONE"
    elif raw['fear_index'] <= 50:
        condition_desc = "NEUTRAL - EQUILIBRIUM"
    elif raw['fear_index'] <= 70:
        condition_desc = "GREED - CAUTION ZONE"
    else:
        condition_desc = "EXTREME GREED - EUPHORIA"
    
    return {
        'status': 'success',
        'timestamp': signal_data['timestamp'],
        'pulse_visual': pulse_bars,
        'signal_type': pulse['signal_type'],
        'signal_color': pulse['color'],
        'signal_text': pulse['display_text'],
        'confidence': signal_data['signal']['confidence'],
        'recommendation': signal_data['signal']['recommendation'],
        'fear_index': raw['fear_index'],
        'btc_price': raw['btc_price'],
        'classification': classification,
        'condition_desc': condition_desc,
        'intensity': pulse['intensity'],
        'duration': pulse['duration'],
        'price_formatted': f"${raw['btc_price']:,.2f}"
    }

@app.route('/')
def home():
    """Main web interface"""
    html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Market Fear Pulsation System - Live Demo</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%);
            color: white;
            min-height: 100vh;
            padding: 20px;
        }
        
        .container {
            max-width: 1200px;
            margin: 0 auto;
        }
        
        .header {
            text-align: center;
            margin-bottom: 40px;
            padding: 20px;
            background: rgba(255, 255, 255, 0.1);
            border-radius: 15px;
            backdrop-filter: blur(10px);
        }
        
        .header h1 {
            font-size: 2.5em;
            margin-bottom: 10px;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
        }
        
        .header p {
            font-size: 1.2em;
            opacity: 0.9;
        }
        
        .signal-card {
            background: rgba(255, 255, 255, 0.15);
            border-radius: 20px;
            padding: 30px;
            margin-bottom: 30px;
            backdrop-filter: blur(10px);
            border: 1px solid rgba(255, 255, 255, 0.2);
            box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
        }
        
        .pulse-display {
            text-align: center;
            font-size: 3em;
            font-weight: bold;
            margin: 20px 0;
            padding: 20px;
            border-radius: 15px;
            background: rgba(0, 0, 0, 0.3);
            font-family: 'Courier New', monospace;
        }
        
        .signal-info {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 20px;
            margin-top: 20px;
        }
        
        .info-box {
            background: rgba(255, 255, 255, 0.1);
            padding: 20px;
            border-radius: 15px;
            border-left: 4px solid #4CAF50;
        }
        
        .info-box h3 {
            margin-bottom: 10px;
            color: #fff;
        }
        
        .info-box p {
            font-size: 1.1em;
            line-height: 1.6;
        }
        
        .status-bar {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 15px 25px;
            background: rgba(0, 0, 0, 0.3);
            border-radius: 10px;
            margin-bottom: 20px;
        }
        
        .status-item {
            text-align: center;
        }
        
        .status-label {
            font-size: 0.9em;
            opacity: 0.8;
            margin-bottom: 5px;
        }
        
        .status-value {
            font-size: 1.4em;
            font-weight: bold;
        }
        
        .refresh-btn {
            background: #4CAF50;
            color: white;
            border: none;
            padding: 12px 30px;
            border-radius: 25px;
            font-size: 1.1em;
            cursor: pointer;
            transition: all 0.3s ease;
            box-shadow: 0 4px 15px rgba(76, 175, 80, 0.3);
        }
        
        .refresh-btn:hover {
            background: #45a049;
            transform: translateY(-2px);
            box-shadow: 0 6px 20px rgba(76, 175, 80, 0.4);
        }
        
        .loading {
            display: none;
            text-align: center;
            padding: 20px;
        }
        
        .spinner {
            border: 4px solid rgba(255, 255, 255, 0.3);
            border-top: 4px solid #4CAF50;
            border-radius: 50%;
            width: 40px;
            height: 40px;
            animation: spin 1s linear infinite;
            margin: 0 auto 10px;
        }
        
        @keyframes spin {
            0% { transform: rotate(0deg); }
            100% { transform: rotate(360deg); }
        }
        
        .error {
            background: rgba(244, 67, 54, 0.2);
            border-left-color: #f44336;
            padding: 15px;
            border-radius: 10px;
            margin: 20px 0;
        }
        
        .signal-legend {
            background: rgba(255, 255, 255, 0.1);
            padding: 20px;
            border-radius: 15px;
            margin-top: 30px;
        }
        
        .legend-title {
            font-size: 1.3em;
            margin-bottom: 15px;
            text-align: center;
        }
        
        .legend-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 15px;
        }
        
        .legend-item {
            display: flex;
            align-items: center;
            gap: 10px;
        }
        
        .legend-color {
            font-size: 1.5em;
            width: 40px;
            text-align: center;
        }
        
        @media (max-width: 768px) {
            .header h1 {
                font-size: 2em;
            }
            
            .pulse-display {
                font-size: 2em;
            }
            
            .signal-info {
                grid-template-columns: 1fr;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🎯 Market Fear Pulsation System</h1>
            <p>Live Trading Signal Delivery for Crypto & Forex Markets</p>
            <p><strong>Public IP:</strong> 95.216.124.247 | <strong>Last Update:</strong> <span id="last-update">Loading...</span></p>
        </div>
        
        <div id="loading" class="loading">
            <div class="spinner"></div>
            <p>Fetching market data...</p>
        </div>
        
        <div id="content">
            <div class="signal-card">
                <div class="status-bar">
                    <div class="status-item">
                        <div class="status-label">Fear Index</div>
                        <div class="status-value" id="fear-index">--</div>
                    </div>
                    <div class="status-item">
                        <div class="status-label">BTC Price</div>
                        <div class="status-value" id="btc-price">--</div>
                    </div>
                    <div class="status-item">
                        <div class="status-label">Signal Type</div>
                        <div class="status-value" id="signal-type">--</div>
                    </div>
                    <div class="status-item">
                        <button class="refresh-btn" onclick="updateSignal()">🔄 Refresh</button>
                    </div>
                </div>
                
                <div class="pulse-display" id="pulse-display">
                    <span id="pulse-visual">█████</span>
                    <div id="pulse-text">Loading signal...</div>
                </div>
                
                <div class="signal-info">
                    <div class="info-box">
                        <h3>🎯 Trading Signal</h3>
                        <p><strong>Signal:</strong> <span id="signal-details">Loading...</span></p>
                        <p><strong>Confidence:</strong> <span id="confidence">Loading...</span></p>
                        <p><strong>Recommendation:</strong> <span id="recommendation">Loading...</span></p>
                    </div>
                    
                    <div class="info-box">
                        <h3>📊 Market Analysis</h3>
                        <p><strong>Condition:</strong> <span id="condition">Loading...</span></p>
                        <p><strong>Classification:</strong> <span id="classification">Loading...</span></p>
                        <p><strong>Intensity:</strong> <span id="intensity">Loading...</span></p>
                    </div>
                </div>
            </div>
            
            <div class="signal-legend">
                <div class="legend-title">🎯 Signal Legend</div>
                <div class="legend-grid">
                    <div class="legend-item">
                        <span class="legend-color">🟢</span>
                        <span>BUY Signal (Fear Zone)</span>
                    </div>
                    <div class="legend-item">
                        <span class="legend-color">🟡</span>
                        <span>HOLD Signal (Neutral)</span>
                    </div>
                    <div class="legend-item">
                        <span class="legend-color">🟠</span>
                        <span>CAUTION Signal (Greed)</span>
                    </div>
                    <div class="legend-item">
                        <span class="legend-color">🔴</span>
                        <span>SELL Signal (Extreme Greed)</span>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <script>
        async function updateSignal() {
            document.getElementById('loading').style.display = 'block';
            document.getElementById('content').style.display = 'none';
            
            try {
                const response = await fetch('/api/signal');
                const data = await response.json();
                
                if (data.status === 'success') {
                    document.getElementById('fear-index').textContent = data.fear_index + '/100';
                    document.getElementById('btc-price').textContent = data.price_formatted;
                    document.getElementById('signal-type').textContent = data.signal_type;
                    document.getElementById('pulse-visual').textContent = data.pulse_visual;
                    document.getElementById('pulse-text').textContent = data.signal_text;
                    document.getElementById('signal-details').textContent = data.signal_type;
                    document.getElementById('confidence').textContent = data.confidence;
                    document.getElementById('recommendation').textContent = data.recommendation;
                    document.getElementById('condition').textContent = data.condition_desc;
                    document.getElementById('classification').textContent = data.classification;
                    document.getElementById('intensity').textContent = data.intensity + '/5';
                    document.getElementById('last-update').textContent = new Date().toLocaleTimeString();
                } else {
                    showError(data.error);
                }
            } catch (error) {
                showError('Failed to fetch data: ' + error.message);
            } finally {
                document.getElementById('loading').style.display = 'none';
                document.getElementById('content').style.display = 'block';
            }
        }
        
        function showError(message) {
            const content = document.getElementById('content');
            const errorDiv = document.createElement('div');
            errorDiv.className = 'error';
            errorDiv.innerHTML = '<strong>❌ Error:</strong> ' + message;
            content.insertBefore(errorDiv, content.firstChild);
        }
        
        // Auto-refresh every 60 seconds
        setInterval(updateSignal, 60000);
        
        // Initial load
        updateSignal();
    </script>
</body>
</html>
    """
    return render_template_string(html_template)

@app.route('/api/signal')
def api_signal():
    """API endpoint for pulsation data"""
    try:
        # Get market data
        market_data = pulsation_system.get_market_data()
        
        # Format for web display
        formatted_data = format_signal_display(market_data)
        
        return jsonify(formatted_data)
        
    except Exception as e:
        return jsonify({
            'status': 'error',
            'error': str(e),
            'timestamp': datetime.now().isoformat()
        })

@app.route('/api/health')
def api_health():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'service': 'Market Fear Pulsation System',
        'version': '1.0',
        'timestamp': datetime.now().isoformat()
    })

if __name__ == '__main__':
    print("🚀 Starting Market Fear Pulsation System Web Demo")
    print("=" * 60)
    print(f"🌐 Public URL: http://95.216.124.247:5000")
    print(f"📊 API Endpoint: http://95.216.124.247:5000/api/signal")
    print(f"🩺 Health Check: http://95.216.124.247:5000/api/health")
    print("=" * 60)
    print("Press Ctrl+C to stop the server")
    print("=" * 60)
    
    app.run(
        host='0.0.0.0',
        port=5000,
        debug=False,
        threaded=True
    )