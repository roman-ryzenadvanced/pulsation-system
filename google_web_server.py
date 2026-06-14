#!/usr/bin/env python3
"""
Google-style Web Server for Market Fear Pulsation System Demo
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

# Google-style HTML template
google_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Market Fear Pulsation System</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: arial, sans-serif;
            background: #fff;
            color: #202124;
            line-height: 1.4;
        }
        
        .header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 0 16px;
            height: 56px;
            background: #fff;
            border-bottom: 1px solid #dadce0;
        }
        
        .header a {
            text-decoration: none;
            color: #202124;
            font-size: 13px;
            margin: 0 12px;
        }
        
        .header a:hover {
            text-decoration: underline;
        }
        
        .main-content {
            display: flex;
            flex-direction: column;
            align-items: center;
            padding-top: 48px;
            text-align: center;
        }
        
        .logo {
            font-size: 60px;
            font-weight: 400;
            letter-spacing: -1px;
            margin-bottom: 20px;
        }
        
        .input-container {
            width: 100%;
            max-width: 580px;
            margin-bottom: 24px;
        }
        
        .search-box {
            width: 100%;
            height: 44px;
            background-color: #f8f9fa;
            border: 1px solid #f8f9fa;
            border-radius: 8px;
            display: flex;
            align-items: center;
            padding: 0 16px;
            transition: box-shadow 0.2s;
        }
        
        .search-box:focus-within {
            box-shadow: 0 1px 6px rgba(32, 33, 36, 0.28);
            border-color: #dadce0;
            background-color: #fff;
        }
        
        .search-icon {
            color: #9aa0a6;
            margin-right: 8px;
        }
        
        .search-input {
            flex: 1;
            border: none;
            background: none;
            outline: none;
            font-size: 16px;
        }
        
        .search-buttons {
            display: flex;
            gap: 12px;
            margin-top: 24px;
        }
        
        .search-btn {
            background-color: #f8f9fa;
            border: 1px solid #f8f9fa;
            border-radius: 4px;
            color: #3c4043;
            font-family: arial, sans-serif;
            font-size: 14px;
            margin: 11px 4px;
            padding: 0 16px;
            line-height: 27px;
            height: 36px;
            min-width: 54px;
            text-align: center;
            cursor: pointer;
            user-select: bgr;
        }
        
        .search-btn:hover {
            box-shadow: 0 1px 1px rgba(0, 0, 0, 0.1);
            background-color: #f8f9fa;
            border: 1px solid #dadce0;
            color: #202124;
        }
        
        .signal-section {
            margin-top: 40px;
            width: 100%;
            max-width: 800px;
        }
        
        .signal-card {
            background: #fff;
            border: 1px solid #dadce0;
            border-radius: 8px;
            padding: 20px;
            margin-bottom: 16px;
            box-shadow: 0 1px 2px rgba(0, 0, 0, 0.1);
        }
        
        .signal-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 16px;
        }
        
        .signal-title {
            font-size: 16px;
            font-weight: 400;
        }
        
        .signal-refresh {
            color: #1a73e8;
            cursor: pointer;
            font-size: 14px;
        }
        
        .signal-refresh:hover {
            text-decoration: underline;
        }
        
        .signal-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 16px;
        }
        
        .signal-item {
            text-align: left;
        }
        
        .signal-label {
            font-size: 12px;
            color: #5f6368;
            margin-bottom: 4px;
        }
        
        .signal-value {
            font-size: 18px;
            font-weight: 400;
        }
        
        .pulse-display {
            text-align: center;
            margin: 20px 0;
            padding: 16px;
            background: #f8f9fa;
            border-radius: 8px;
        }
        
        .pulse-visual {
            font-size: 24px;
            font-weight: bold;
            letter-spacing: 4px;
            margin-bottom: 8px;
        }
        
        .pulse-text {
            font-size: 14px;
            color: #5f6368;
        }
        
        .recommendation {
            background: #e8f0fe;
            border: 1px solid #d2e3fc;
            border-radius: 8px;
            padding: 16px;
            margin-top: 16px;
        }
        
        .recommendation-title {
            font-size: 14px;
            font-weight: 500;
            margin-bottom: 8px;
        }
        
        .recommendation-text {
            font-size: 16px;
        }
        
        .loading {
            display: none;
            text-align: center;
            padding: 20px;
        }
        
        .spinner {
            border: 4px solid #f3f3f3;
            border-top: 4px solid #1a73e8;
            border-radius: 50%;
            width: 20px;
            height: 20px;
            animation: spin 1s linear infinite;
            display: inline-block;
            margin: 0 8px;
        }
        
        @keyframes spin {
            0% { transform: rotate(0deg); }
            100% { transform: rotate(360deg); }
        }
        
        .footer {
            margin-top: 40px;
            padding: 16px 16px 0;
            width: 100%;
            max-width: 580px;
            text-align: center;
        }
        
        .footer a {
            text-decoration: none;
            color: #70757a;
            font-size: 12px;
            margin: 0 12px;
        }
        
        .footer a:hover {
            text-decoration: underline;
        }
    </style>
</head>
<body>
    <div class="header">
        <div>
            <a href="#">Gmail</a>
            <a href="#">Images</a>
        </div>
        <div>
            <a href="#">Sign in</a>
        </div>
    </div>
    
    <div class="main-content">
        <div class="logo">Pulsation System</div>
        
        <div class="input-container">
            <div class="search-box">
                <span class="search-icon">🎯</span>
                <input type="text" class="search-input" placeholder="Market Fear Pulsation System" readonly>
            </div>
        </div>
        
        <div class="search-buttons">
            <button class="search-btn" onclick="updateSignal()">Google Search</button>
            <button class="search-btn" onclick="updateSignal()">I'm Feeling Lucky</button>
        </div>
        
        <div id="loading" class="loading">
            <span class="spinner"></span>
            <span>Loading market data...</span>
        </div>
        
        <div id="content">
            <div class="signal-card">
                <div class="signal-header">
                    <div class="signal-title">Market Fear Pulsation System</div>
                    <div class="signal-refresh" onclick="updateSignal()">↻ Refresh</div>
                </div>
                
                <div class="pulse-display">
                    <div class="pulse-visual" id="pulse-visual">█████</div>
                    <div class="pulse-text" id="pulse-text">Loading signal...</div>
                </div>
                
                <div class="signal-grid">
                    <div class="signal-item">
                        <div class="signal-label">Fear Index</div>
                        <div class="signal-value" id="fear-index">--</div>
                    </div>
                    
                    <div class="signal-item">
                        <div class="signal-label">BTC Price</div>
                        <div class="signal-value" id="btc-price">--</div>
                    </div>
                    
                    <div class="signal-item">
                        <div class="signal-label">Signal Type</div>
                        <div class="signal-value" id="signal-type">--</div>
                    </div>
                    
                    <div class="signal-item">
                        <div class="signal-label">Confidence</div>
                        <div class="signal-value" id="confidence">--</div>
                    </div>
                </div>
                
                <div class="recommendation">
                    <div class="recommendation-title">💡 Recommendation</div>
                    <div class="recommendation-text" id="recommendation">Loading...</div>
                </div>
            </div>
        </div>
        
        <div class="footer">
            <div style="margin-bottom: 16px;">
                <a href="#">About</a>
                <a href="#">Privacy</a>
                <a href="#">Terms</a>
                <a href="#">Settings</a>
            </div>
            <div>
                <a href="#">Switch to HTML view</a>
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
                    document.getElementById('confidence').textContent = data.confidence;
                    document.getElementById('pulse-visual').textContent = data.pulse_visual;
                    document.getElementById('pulse-text').textContent = data.signal_text;
                    document.getElementById('recommendation').textContent = data.recommendation;
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
            errorDiv.style.cssText = `
                background: #fce8e6;
                border: 1px solid #fa7664;
                border-radius: 8px;
                padding: 16px;
                margin-top: 16px;
                color: #d93025;
            `;
            errorDiv.innerHTML = '<strong>❌ Error:</strong> ' + message;
            content.appendChild(errorDiv);
        }
        
        // Auto-refresh every 60 seconds
        setInterval(updateSignal, 60000);
        
        // Initial load
        updateSignal();
    </script>
</body>
</html>
"""

@app.route('/')
def home():
    """Google-style main web interface"""
    return render_template_string(google_template)

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
    print("🚀 Starting Google-style Market Fear Pulsation System")
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