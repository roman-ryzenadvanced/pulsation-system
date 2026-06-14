# Pulsation System

A rhythmic visualization and animation system built with Python.

## Features

- 🎨 **Multiple pulsation rings** with gradient colors
- ⚡ **Real-time animation** at 60 FPS
- 🎮 **Interactive controls** via keyboard
- 📊 **Configurable parameters** (speed, radius, rings)
- 🖥️ **Cross-platform** console-based visualization

## Installation

```bash
cd pulsation-system
pip install -r requirements.txt
```

## Usage

```bash
python main.py
```

## Controls

| Key | Action |
|-----|--------|
| `SPACE` | Pause/Resume animation |
| `UP` | Increase pulse speed |
| `DOWN` | Decrease pulse speed |
| `Q` | Quit application |

## Features

- **Dynamic Pulse**: Each ring oscillates with sine waves for smooth, organic motion
- **Color Gradient**: Rings transition from cyan to purple
- **Real-time Updates**: Adjust speed on the fly
- **Status Display**: Shows current state (paused/speed)

## Configuration

You can modify these parameters in `main.py`:

```python
self.radius = 100          # Base ring radius
self.num_rings = 5         # Number of rings
self.pulse_speed = 1.0     # Base animation speed
```

## Project Structure

```
pulsation-system/
├── main.py           # Main application
├── requirements.txt  # Python dependencies
└── README.md         # This file
```

## Requirements

- Python 3.8+
- numpy (mathematical operations)
- colorama (cross-platform terminal colors)

## License

MIT License - Feel free to use and modify!

## Future Enhancements

- [ ] GUI version with PySide6/PyQt
- [ ] Audio synchronization
- [ ] Save/Load configurations
- [ ] Multiple visualization modes
- [ ] Export animations as video

---

**Enjoy the pulsation!** 🌊✨
