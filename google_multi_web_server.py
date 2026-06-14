#!/usr/bin/env python3
"""
Google-style Web Server for Multi-Instrument Market Fear Pulsation System
"""

from flask import Flask, jsonify, render_template_string, request
import json
import sys
import os
from datetime import datetime
from main_multi import MarketFearPulsationSystem

app = Flask(__name__)

# Google-style HTML template
GOOGLE_STYLE_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Market Fear Pulsation System - Multi-Instrument</title>
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
            padding: 0;
            background: #fff;
            border-bottom: 1px solid #dadce0;
            height: 60px;
            display: flex;
            align-items: center;
            justify-content: space-between;
        }
        
        .header a {
            color: #1a0dab;
            text-decoration: none;
            padding: 0 15px;
            font-size: 13px;
            line-height: 40px;
            height: 48px;
            display: inline-block;
        }
        
        .header a:hover {
            text-decoration: underline;
        }
        
        .main {
            padding: 0 40px;
            padding-top: 20px;
            max-width: 784px;
            margin: 0 auto;
        }
        
        .logo {
            text-align: center;
            margin: 40px 0;
        }
        
        .logo h1 {
            font-size: 32px;
            font-weight: 400;
            color: #222;
            margin-bottom: 10px;
        }
        
        .logo p {
            font-size: 16px;
            color: #5f6368;
        }
        
        .search-container {
            display: flex;
            flex-direction: column;
            align-items: center;
            margin: 20px 0 40px;
        }
        
        .search-box {
            width: 100%;
            max-width: 580px;
            border: 1px solid #dfe1e5;
            border-radius: 24px;
            display: flex;
            align-items: center;
            padding: 0 15px;
            font-size: 16px;
            margin-bottom: 20px;
        }
        
        .search-box input {
            flex: 1;
            border: none;
            outline: none;
            padding: 10px 0;
            font-size: 16px;
        }
        
        .search-icon {
            color: #9aa0a6;
            margin-right: 10px;
        }
        
        .search-buttons {
            display: flex;
            gap: 10px;
        }
        
        .search-btn {
            background: #f8f9fa;
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
            user-select: none;
        }
        
        .search-btn:hover {
            box-shadow: 0 1px 1px rgba(0,0,0,0.1);
            background: #f8f9fa;
            border: 1px solid #dadce0;
            color: #202124;
        }
        
        .results {
            margin: 40px 0;
        }
        
        .card {
            background: #fff;
            border-radius: 8px;
            box-shadow: 0 1px 2px rgba(0,0,0,0.1);
            padding: 24px;
            margin-bottom: 16px;
        }
        
        .instrument-selector {
            display: flex;
            gap: 8px;
            margin-bottom: 20px;
            flex-wrap: wrap;
        }
        
        .instrument-btn {
            background: #f8f9fa;
            border: 1px solid #f8f9fa;
            border-radius: 16px;
            padding: 8px 16px;
            cursor: pointer;
            font-size: 14px;
            transition: all 0.2s;
        }
        
        .instrument-btn.active {
            background: #1a73e8;
            color: white;
            border-color: #1a73e8;
        }
        
        .instrument-btn:hover {
            background: #e8f0fe;
            border-color: #1a73e8;
        }
        
        .instrument-btn.active:hover {
            background: #1a73e8;
        }
        
        .signal-display {
            text-align: center;
            margin: 30px 0;
        }
        
        .signal-type {
            font-size: 36px;
            font-weight: bold;
            margin-bottom: 10px;
        }
        
        .signal-text {
            font-size: 18px;
            margin-bottom: 20px;
        }
        
        .pulsation {
            font-size: 48px;
            font-family: monospace;
            margin: 20px 0;
            animation: pulse 1s ease-in-out infinite;
        }
        
        @keyframes pulse {
            0%, 100% { opacity: 1; }
            50% { opacity: 0.5; }
        }
        
        .market-data {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 20px;
            margin: 30px 0;
        }
        
        .data-card {
            background: #f8f9fa;
            padding: 20px;
            border-radius: 8px;
            text-align: center;
        }
        
        .data-label {
            font-size: 14px;
            color: #5f6368;
            margin-bottom: 8px;
        }
        
        .data-value {
            font-size: 24px;
            font-weight: bold;
            color: #202124;
        }
        
        .instruments-overview {
            margin: 40px 0;
        }
        
        .instruments-table {
            width: 100%;
            border-collapse: collapse;
            margin-top: 20px;
        }
        
        .instruments-table th,
        .instruments-table td {
            padding: 12px;
            text-align: left;
            border-bottom: 1px solid #dadce0;
        }
        
        .instruments-table th {
            background: #f8f9fa;
            font-weight: 600;
        }
        
        .intensity-bar {
            font-family: monospace;
            font-size: 14px;
        }
        
        .refresh-btn {
            background: #f8f9fa;
            border: 1px solid #f8f9fa;
            border-radius: 4px;
            color: #3c4043;
            padding: 0 16px;
            font-size: 14px;
            cursor: pointer;
            margin: 20px 0;
        }
        
        .refresh-btn:hover {
            background: #e8f0fe;
            border-color: #1a73e8;
            color: #1a73e8;
        }
        
        .footer {
            text-align: center;
            padding: 30px 0;
            color: #5f6368;
            font-size: 12px;
        }
        
        .refresh-container {
            display: flex;
            justify-content: center;
            align-items: center;
            margin: 20px 0;
        }
        
        .loading {
            display: none;
            margin-left: 10px;
        }
        
        .spinner {
            border: 2px solid #f3f3f3;
            border-top: 2px solid #1a73e8;
            border-radius: 50%;
            width: 16px;
            height: 16px;
            animation: spin 1s linear infinite;
        }
        
        @keyframes spin {
            0% { transform: rotate(0deg); }
            100% { transform: rotate(360deg); }
        }
    </style>
</head>
<body>
    <div class="header">
        <div style="display: flex;">
            <a href="#">Gmail</a>
            <a href="#">Images</a>
        </div>
        <div style="display: flex;">
            <a href="#">Sign in</a>
        </div>
    </div>
    
    <div class="main">
        <div class="logo">
            <h1>Market Fear Pulsation System</h1>
            <p>Multi-Instrument Crypto Trading Signals</p>
        </div>
        
        <div class="search-container">
            <div class="search-box">
                <span class="search-icon">🎯</span>
                <input type="text" placeholder="Select instrument below to view trading signals..." readonly>
            </div>
            <div class="search-buttons">
                <button class="search-btn">🎯 View Signals</button>
                <button class="search-btn">🚀 I'm Feeling Lucky</button>
            </div>
        </div>
        
        <div class="results">
            <div class="card">
                <h3>Select Instrument</h3>
                <div class="instrument-selector" id="instrumentSelector">
                    <!-- Instrument buttons will be populated here -->
                </div>
                
                <div class="refresh-container">
                    <button class="refresh-btn" onclick="refreshData()">
                        🔄 Refresh Data
                    </button>
                    <div class="loading" id="loading">
                        <div class="spinner"></div>
                    </div>
                </div>
                
                <div id="instrumentContent">
                    <div class="signal-display">
                        <div class="signal-type">🎯</div>
                        <div class="signal-text">Select an instrument above to view trading signals</div>
                        <div class="pulsation">─────</div>
                    </div>
                </div>
            </div>
            
            <div class="card instruments-overview">
                <h3>All Instruments Overview</h3>
                <table class="instruments-table">
                    <thead>
                        <tr>
                            <th>Instrument</th>
                            <th>Price</th>
                            <th>Signal</th>
                            <th>Intensity</th>
                            <th>Fear Index</th>
                        </tr>
                    </thead>
                    <tbody id="instrumentsTable">
                        <!-- Table rows will be populated here -->
                    </tbody>
                </table>
            </div>
        </div>
    </div>
    
    <div class="footer">
        <p>&copy; 2026 Market Fear Pulsation System | Real-time Crypto Trading Signals</p>
    </div>
    
    <script>
        let currentInstrument = 'BTC';
        let refreshInterval;
        
        function initializeApp() {
            loadInstruments();
            loadAllInstruments();
            startAutoRefresh();
        }
        
        function loadInstruments() {
            fetch('/api/instruments')
                .then(response => response.json())
                .then(data => {
                    const selector = document.getElementById('instrumentSelector');
                    selector.innerHTML = '';
                    
                    data.instruments.forEach(instrument => {
                        const btn = document.createElement('button');
                        btn.className = `instrument-btn ${instrument === currentInstrument ? 'active' : ''}`;
                        btn.textContent = instrument;
                        btn.onclick = () => selectInstrument(instrument);
                        selector.appendChild(btn);
                    });
                });
        }
        
        function loadAllInstruments() {
            fetch('/api/all-instruments')
                .then(response => response.json())
                .then(data => {
                    const table = document.getElementById('instrumentsTable');
                    table.innerHTML = '';
                    
                    Object.entries(data).forEach(([instrument, result]) => {
                        if (result.error) return;
                        
                        const row = document.createElement('tr');
                        row.innerHTML = `
                            <td><strong>${instrument}</strong></td>
                            <td>$${result.raw_data.instrument_price.toLocaleString()}</td>
                            <td>${result.pulsation.color} ${result.pulsation.signal_type}</td>
                            <td><span class="intensity-bar">${result.pulsation.visual}</span></td>
                            <td>${result.raw_data.fear_index}/100</td>
                        `;
                        table.appendChild(row);
                    });
                });
        }
        
        function selectInstrument(instrument) {
            currentInstrument = instrument;
            document.querySelectorAll('.instrument-btn').forEach(btn => {
                btn.classList.remove('active');
            });
            event.target.classList.add('active');
            
            loadInstrumentData(instrument);
        }
        
        function loadInstrumentData(instrument) {
            showLoading(true);
            
            fetch(`/api/instrument/${instrument}`)
                .then(response => response.json())
                .then(data => {
                    displayInstrumentData(data);
                    showLoading(false);
                })
                .catch(error => {
                    console.error('Error loading data:', error);
                    showLoading(false);
                });
        }
        
        function displayInstrumentData(data) {
            const content = document.getElementById('instrumentContent');
            
            if (data.error) {
                content.innerHTML = `
                    <div class="signal-display">
                        <div class="signal-type">❌</div>
                        <div class="signal-text">Error: ${data.error}</div>
                    </div>
                `;
                return;
            }
            
            const signal = data.signal;
            const pulsation = data.pulsation;
            const rawData = data.raw_data;
            
            content.innerHTML = `
                <div class="signal-display">
                    <div class="signal-type">${signal.color}</div>
                    <div class="signal-text">${signal.signal_type} - ${signal.recommendation}</div>
                    <div class="pulsation">${pulsation.visual}</div>
                </div>
                
                <div class="market-data">
                    <div class="data-card">
                        <div class="data-label">Current Price</div>
                        <div class="data-value">$${rawData.instrument_price.toLocaleString()}</div>
                    </div>
                    <div class="data-card">
                        <div class="data-label">Fear Index</div>
                        <div class="data-value">${rawData.fear_index}/100</div>
                    </div>
                    <div class="data-card">
                        <div class="data-label">Market Cap Weight</div>
                        <div class="data-value">${(rawData.market_cap_weight * 100).toFixed(1)}%</div>
                    </div>
                    <div class="data-card">
                        <div class="data-label">Volatility Factor</div>
                        <div class="data-value">${rawData.volatility_factor}x</div>
                    </div>
                </div>
            `;
        }
        
        function refreshData() {
            loadAllInstruments();
            loadInstrumentData(currentInstrument);
        }
        
        function showLoading(show) {
            document.getElementById('loading').style.display = show ? 'block' : 'none';
        }
        
        function startAutoRefresh() {
            refreshInterval = setInterval(() => {
                loadAllInstruments();
            }, 60000); // Refresh every 60 seconds
        }
        
        // Initialize the app when the page loads
        document.addEventListener('DOMContentLoaded', initializeApp);
    </script>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(GOOGLE_STYLE_TEMPLATE)

@app.route('/api/health')
def health():
    return jsonify({
        'service': 'Market Fear Pulsation System',
        'status': 'healthy',
        'timestamp': datetime.now().isoformat(),
        'version': '2.0',
        'feature': 'Multi-Instrument Support'
    })

@app.route('/api/instruments')
def instruments():
    system = MarketFearPulsationSystem()
    return jsonify({
        'instruments': system.get_supported_instruments(),
        'timestamp': datetime.now().isoformat()
    })

@app.route('/api/instrument/<instrument>')
def get_instrument_data(instrument):
    try:
        system = MarketFearPulsationSystem(instrument)
        data = system.get_market_data()
        return jsonify(data)
    except Exception as e:
        return jsonify({
            'error': str(e),
            'instrument': instrument,
            'timestamp': datetime.now().isoformat()
        })

@app.route('/api/all-instruments')
def get_all_instruments_data():
    system = MarketFearPulsationSystem()
    data = system.get_all_instruments_data()
    return jsonify(data)

@app.route('/api/<instrument>/pairs')
def get_trading_pairs(instrument):
    try:
        system = MarketFearPulsationSystem(instrument)
        pairs = system.get_trading_pairs(instrument)
        return jsonify({
            'instrument': instrument,
            'trading_pairs': pairs,
            'timestamp': datetime.now().isoformat()
        })
    except Exception as e:
        return jsonify({
            'error': str(e),
            'instrument': instrument,
            'timestamp': datetime.now().isoformat()
        })

@app.route('/api/<instrument>/info')
def get_instrument_info(instrument):
    try:
        system = MarketFearPulsationSystem(instrument)
        info = system.get_instrument_info(instrument)
        if info:
            return jsonify({
                'instrument': instrument,
                'info': info,
                'timestamp': datetime.now().isoformat()
            })
        else:
            return jsonify({
                'error': 'Instrument not found',
                'instrument': instrument,
                'timestamp': datetime.now().isoformat()
            })
    except Exception as e:
        return jsonify({
            'error': str(e),
            'instrument': instrument,
            'timestamp': datetime.now().isoformat()
        })

@app.route('/api/test')
def test():
    """Test endpoint to verify all APIs are working"""
    try:
        system = MarketFearPulsationSystem()
        all_data = system.get_all_instruments_data()
        
        results = {}
        for instrument, data in all_data.items():
            if 'error' not in data:
                results[instrument] = {
                    'status': 'ok',
                    'signal': data.get('pulsation', {}).get('signal_type', 'UNKNOWN'),
                    'price': data.get('raw_data', {}).get('instrument_price', 0),
                    'fear_index': data.get('raw_data', {}).get('fear_index', 0)
                }
            else:
                results[instrument] = {
                    'status': 'error',
                    'error': data.get('error', 'Unknown error')
                }
        
        return jsonify({
            'test_results': results,
            'timestamp': datetime.now().isoformat(),
            'total_instruments': len(results),
            'working_instruments': len([r for r in results.values() if r['status'] == 'ok'])
        })
    except Exception as e:
        return jsonify({
            'error': str(e),
            'timestamp': datetime.now().isoformat()
        })

def main():
    print("🚀 Starting Google-style Multi-Instrument Market Fear Pulsation System")
    print("=" * 80)
    print(f"🌐 Public URL: http://95.216.124.247:5000")
    print(f"📊 API Endpoint: http://95.216.124.247:5000/api/instrument/<instrument>")
    print(f"🩺 Health Check: http://95.216.124.247:5000/api/health")
    print(f"🌍 All Instruments: http://95.216.124.247:5000/api/all-instruments")
    print("=" * 80)
    print("Press Ctrl+C to stop the server")
    print("=" * 80)
    
    # Test the system
    system = MarketFearPulsationSystem()
    test_data = system.get_market_data()
    print(f"✅ System test passed - Instrument: {test_data.get('instrument', 'UNKNOWN')}")
    
    app.run(host='0.0.0.0', port=5000, debug=False)

if __name__ == '__main__':
    main()