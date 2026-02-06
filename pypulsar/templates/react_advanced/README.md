# Advanced React Template for PyPulsar

This template provides a more advanced React application integrated with PyPulsar, featuring:

- React Router for navigation
- Multiple pages: Home, Counter, Settings, Files
- State management between Python backend and React frontend
- File system operations
- Settings persistence

## Features

- **Counter**: Increment, decrement, and reset counter with custom steps
- **Settings**: Change theme and language (persisted in Python state)
- **Files**: Browse directories and read file contents
- **Real-time updates**: Changes in Python are reflected in React via events

## Usage

1. Install dependencies: `cd web && npm install`
2. Build the React app: `cd web && npm run build`
3. Run the Python app: `python main.py`
4. The app will open with the built React application

## Development

For development with hot reloading:

1. Install dependencies: `cd web && npm install`
2. Start Vite dev server: `cd web && npm run dev`
3. Update `main.py` to point to the Vite dev server (e.g., change webroot or use a different approach)
4. Run the Python app: `python main.py`

## API Endpoints

- `get_app_state`: Get current app state
- `update_counter`: Update counter (increment/decrement)
- `reset_counter`: Reset counter to 0
- `save_settings`: Save settings
- `load_files`: Load files from directory
- `read_file`: Read file content

## Structure

- `main.py`: Python backend with PyPulsar Engine
- `web/`: React frontend
  - `src/App.jsx`: Main app with routing
  - `src/components/`: React components
  - `src/utils/api.js`: API communication utility