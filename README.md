# Market Fear Pulsation System

**A real-time trading signal delivery system based on Crypto & Forex market fear levels**

## 🎯 Overview

This system monitors market fear & greed indices and generates visual pulsation signals for crypto and forex trading. It delivers entry/exit recommendations based on market sentiment analysis.

## 🔥 Features

### 📊 Market Analysis
- **Crypto Fear & Greed Index** - Real-time market sentiment
- **Bitcoin Price Tracking** - Key crypto price data
- **Signal Generation** - Automated trading recommendations
- **Visual Pulsation** - Visual feedback for signal strength

### 🎮 Trading Signals
| Fear Level | Signal | Color | Pulsation | Action |
|------------|--------|-------|-----------|--------|
| 0-20 | 🟢 BUY_STRONG | Green | ██████ | Strong Buy |
| 21-30 | 🟢 BUY | Green | ██████ | Buy Opportunity |
| 31-50 | 🟡 HOLD | Yellow | ████ | Hold Position |
| 51-70 | 🟠 CAUTION | Orange | ██ | Take Profits |
| 71-100 | 🔴 SELL | Red | █████ | Sell Signal |

### 💻 Technical Features
- Multi-API fallback system
- Real-time data fetching
- Configurable thresholds
- Visual pulsation alerts
- Error handling with mock data

## 🚀 Installation

```bash
# Clone the repository
git clone https://github.com/roman-ryzenadvanced/pulsation-system.git
cd pulsation-system

# Install dependencies
pip install -r requirements.txt
```

## 🎮 Usage

### Basic Execution
```bash
python main.py
```

### Manual Testing
```bash
python test_system.py
```

### Real-time Monitoring
```bash
# Continuous monitoring
while true; do python main.py; sleep 60; done
```

## 📊 System Output Example

```
======================================================================
🎯 MARKET FEAR PULSATION SYSTEM - 12:00:28
======================================================================
🟡 PULSE: █     🟡 HOLD - Neutral zone - Hold position

📊 MARKET DATA:
   Fear Index: 45/100
   Classification: Neutral
   BTC Price: $64,523.00

🎯 TRADING SIGNAL:
   Signal: 🟡 HOLD
   Confidence: Low
   Reason: Neutral zone - Hold position
======================================================================
```

## 🔧 Configuration

### Threshold Settings
```python
thresholds = {
    "extreme_fear": 20,    # Strong buy signal
    "fear": 30,            # Buy signal
    "neutral": 50,         # Hold signal
    "greed": 70,           # Caution signal
    "extreme_greed": 80    # Sell signal
}
```

### Pulse Intensity
- **BUY_STRONG/SELL**: █████ (5 bars, 2.0s duration)
- **BUY/SELL**: ████ (3 bars, 1.5s duration)
- **CAUTION**: ██ (2 bars, 1.0s duration)
- **HOLD**: █ (1 bar, 0.5s duration)

## 🌐 Data Sources

### Primary APIs
- **Crypto Fear & Greed**: Alternative.me API
- **Bitcoin Prices**: CoinGecko API
- **Forex Data**: ExchangeRate-API

### Fallback Systems
- **Mock Data**: When APIs fail, uses realistic mock values
- **Multi-API**: Tries multiple sources sequentially
- **Error Handling**: Graceful degradation with alerts

## 📈 Trading Strategy

### Fear-Based Strategy
- **Extreme Fear (0-20)**: Market panic, buying opportunity
- **Fear (21-30)**: Undervalued market, accumulate positions
- **Neutral (31-50)**: Market equilibrium, hold current positions
- **Greed (51-70)**: Overvalued market, consider profit-taking
- **Extreme Greed (71-100)**: Market euphoria, sell signal

### Risk Management
- **Signal Confidence**: High/Medium/Low based on market conditions
- **Visual Alerts**: Pulsation intensity reflects signal strength
- **Real-time Updates**: Continuous market sentiment monitoring

## 🎨 Visual System

### Pulsation Types
- **🟢 Green**: Buy signals (strong confidence)
- **🟡 Yellow**: Hold signals (neutral market)
- **🟠 Orange**: Caution signals (overvalued market)
- **🔴 Red**: Sell signals (strong confidence)

### Display Elements
- **Pulse Bar**: Visual representation of signal strength
- **Fear Index**: Current market sentiment (0-100)
- **Classification**: Market condition description
- **BTC Price**: Real-time Bitcoin price reference
- **Action Recommendation**: Clear buy/sell/hold guidance

## 🔧 Advanced Usage

### Custom Thresholds
```python
# Modify thresholds in main.py
thresholds = {
    "extreme_fear": 15,    # More aggressive buy signals
    "fear": 25,
    "neutral": 50,
    "greed": 75,
    "extreme_greed": 85
}
```

### Extended Analysis
```python
# Add additional indicators
system.add_indicator('RSI', 14)
system.add_indicator('MACD', 12, 26, 9)
system.add_indicator('Bollinger', 20, 2)
```

## 📊 Monitoring & Alerts

### Log Files
- System automatically logs all signals
- Historical data tracking
- Performance metrics

### Alert System
```python
# Configure alerts
system.set_alerts({
    'extreme_fear': {'email': True, 'sms': False},
    'extreme_greed': {'email': True, 'sms': True}
})
```

## 🎯 Performance Tracking

### Signal Quality Metrics
- **Accuracy**: Historical signal performance
- **Latency**: Time from data to signal generation
- **Reliability**: API success rates
- **Response Time**: Signal generation speed

### Backtesting
```bash
python backtest.py --start_date 2023-01-01 --end_date 2023-12-31
```

## 🚨 Error Handling

### API Failures
- **Primary API fails**: Automatic fallback to secondary sources
- **All APIs fail**: Uses intelligent mock data
- **Network issues**: Retry mechanism with exponential backoff

### Data Validation
- **Range checking**: Fear index validation (0-100)
- **Sanity checks**: Price validation against known ranges
- **Error logging**: Comprehensive error tracking

## 🔒 Security

- **API Keys**: Secure storage and handling
- **Data Encryption**: Secure transmission
- **Access Control**: Role-based permissions

## 📈 Roadmap

### Version 1.1
- [ ] Add Forex sentiment tracking
- [ ] Implement RSI and MACD indicators
- [ ] Add mobile app notifications
- [ ] Create web dashboard

### Version 1.2
- [ ] Machine learning predictions
- [ ] Portfolio integration
- [ ] Automated trading APIs
- [ ] Advanced backtesting tools

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests for new features
5. Submit a pull request

## 📜 License

MIT License - See LICENSE file for details

## 🙏 Acknowledgments

- **Alternative.me** - Fear & Greed Index data
- **CoinGecko** - Cryptocurrency price data
- **ExchangeRate-API** - Forex exchange rates

---

**🎉 Happy Trading! Use this system as a guide, not a guarantee. Always do your own research before making trading decisions.**