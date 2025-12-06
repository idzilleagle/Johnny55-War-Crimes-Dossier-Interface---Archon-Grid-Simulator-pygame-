"""
Save Manager Module
Handles game state persistence via JSON file I/O.
Decoupled from main game logic for clean separation of concerns.

IMPORTANT: Save file is stored in the same directory as this script,
NOT in the current working directory. This ensures saves work correctly
when the game is launched from different locations (e.g., double-clicking
the .py file vs running from command line).
"""

import json
import os


class SaveManager:
    """Static utility class for managing game state save/load operations."""
    
    # Get the directory where THIS script file is located
    # This ensures the save file is always in the same folder as the game files
    _SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    SAVE_FILE = os.path.join(_SCRIPT_DIR, 'state_record.json')
    
    @staticmethod
    def save_game(data: dict):
        """
        Save game state to JSON file.
        
        Args:
            data: Dictionary containing game state data to save
        """
        try:
            with open(SaveManager.SAVE_FILE, 'w') as file:
                json.dump(data, file, indent=4)
            print(f"Saved to: {SaveManager.SAVE_FILE}")  # Debug: show where file was saved
        except Exception as e:
            print(f"Error saving game state: {e}")
            print(f"Attempted save path: {SaveManager.SAVE_FILE}")
            import traceback
            traceback.print_exc()
    
    @staticmethod
    def load_game():
        """
        Load game state from JSON file.
        
        Returns:
            Dictionary containing game state data, or None if file doesn't exist or error occurs
        """
        if not os.path.exists(SaveManager.SAVE_FILE):
            print(f"No save file found at: {SaveManager.SAVE_FILE}")
            return None
        
        try:
            with open(SaveManager.SAVE_FILE, 'r') as file:
                print(f"Loading save from: {SaveManager.SAVE_FILE}")  # Debug: show where file was loaded from
                return json.load(file)
        except json.JSONDecodeError as e:
            print(f"Error: Invalid JSON in save file: {e}")
            return None
        except Exception as e:
            print(f"Error loading game state: {e}")
            import traceback
            traceback.print_exc()
            return None

