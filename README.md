# 🏨 Hotel Room Reservation System

A sophisticated hotel room booking system built for the **Unstop SDE-3 Assessment**. This interactive web application demonstrates advanced algorithms for optimal room allocation while providing an intuitive user interface.

## ✨ Features

- **Smart Room Allocation**: Advanced algorithms that minimize travel time between rooms
- **Multi-Floor Support**: 10 floors with intelligent cross-floor booking strategies
- **Real-time Updates**: Dynamic room status updates with visual feedback
- **Responsive Design**: Beautiful glassmorphism UI that works on all devices
- **Interactive Controls**: Random occupancy generation and system reset functionality

## 🏗️ Architecture

### Hotel Structure
- **Floors 1-9**: 10 rooms each (101-109, 201-209, etc.)
- **Floor 10**: 7 rooms (1001-1007)
- **Total Capacity**: 97 rooms

### Booking Algorithm
1. **Same-Floor Priority**: Attempts to book rooms on the same floor first
2. **Cross-Floor Optimization**: If same-floor booking isn't possible, finds the optimal combination across multiple floors
3. **Travel Time Calculation**: Considers stairs/lift positioning and room distances

## 🚀 Live Demo

**Visit the live application**: [Hotel Reservation System](https://hritwiza13.github.io/python_ml_practice/)

## 🛠️ Technology Stack

- **Frontend**: React 18, Tailwind CSS
- **Styling**: Custom CSS with glassmorphism effects
- **Deployment**: GitHub Pages
- **No Build Process**: Pure HTML/CSS/JavaScript for instant deployment

## 📱 How to Use

1. **Set Room Count**: Choose 1-5 rooms to book
2. **Generate Random Occupancy**: Click "🎲 Random Occupancy" to simulate hotel usage
3. **Book Optimally**: Click "✨ Book Optimally" to find the best room combination
4. **Reset System**: Use "🔄 Reset" to clear all bookings

## 🎯 Key Algorithms

### `bestSameFloorBooking()`
- Finds optimal room combinations on a single floor
- Minimizes room span for better accessibility

### `bestCrossFloorBooking()`
- Searches for optimal combinations across multiple floors
- Uses floor bands and index thresholds for efficiency

### `setDiameter()`
- Calculates maximum travel time between any two rooms in a set
- Considers both horizontal and vertical movement

## 🎨 UI Features

- **Glassmorphism Design**: Modern, translucent card-based interface
- **Responsive Grid**: Adapts to different screen sizes
- **Interactive Elements**: Hover effects and smooth transitions
- **Color Coding**: Clear visual indicators for room status
- **Dark Mode Support**: Automatic theme detection

## 📊 Room Status Indicators

- **White**: Available rooms
- **Yellow**: Currently booked rooms
- **Gray**: Occupied rooms

## 🔧 Development

### Local Development
1. Clone the repository
2. Open `index.html` in a web browser
3. No build process required

### Deployment
- Automatically deployed via GitHub Pages
- Updates automatically on push to main branch

## 📝 Assessment Details

This project was created for the **Unstop SDE-3 Assessment** and demonstrates:

- **Problem-Solving**: Complex algorithmic thinking for room optimization
- **Frontend Development**: Modern web technologies and responsive design
- **User Experience**: Intuitive interface with clear visual feedback
- **Code Quality**: Clean, maintainable JavaScript code
- **Performance**: Efficient algorithms for real-time room allocation

## 🤝 Contributing

Feel free to submit issues, feature requests, or pull requests to improve this project.

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

**Built with ❤️ for the Unstop SDE-3 Assessment**


