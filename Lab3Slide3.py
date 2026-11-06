import json
import os

CONFIG_FILE = "config.json"


def get_default_config() -> dict:
    """Returns a reasonable default configuration dictionary if the file is missing."""
    return {
        "app_name": "StudentGradebookManager",
        "version": "1.0.0",
        "settings": {
            "theme": "dark",
            "max_login_attempts": 3,
            "enable_notifications": True,
            "backup": {
                "auto_save": True,
                "interval_minutes": 15
            }
        }
    }


def load_configuration() -> dict:
    """Loads configuration when the program starts.

    Handles missing configuration file with a reasonable default.
    """
    print("--- 1. Program Starting: Loading Configuration ---")
    if not os.path.exists(CONFIG_FILE):
        print(f"[INFO] '{CONFIG_FILE}' not found. Initializing with default settings...")
        default_config = get_default_config()
        # Save defaults immediately so the file exists next time
        save_configuration(default_config)
        return default_config

    try:
        with open(CONFIG_FILE, "r", encoding="utf-8") as file:
            config_data = json.load(file)
            print("[SUCCESS] Configuration file loaded successfully.")
            return config_data
    except json.JSONDecodeError:
        print("[ERROR] 'config.json' is corrupted. Falling back to safe defaults.")
        return get_default_config()


def save_configuration(config_data: dict):
    """Writes the configuration dictionary back to disk with clean indentation."""
    with open(CONFIG_FILE, "w", encoding="utf-8") as file:
        # indent=4 adds readability whitespace formatting matching submission criteria
        json.dump(config_data, file, indent=4)
    print(f"[SAVED] Updated configuration structural changes written back to '{CONFIG_FILE}'.")


# --- Execution Flow ---
if __name__ == "__main__":
    # Simulate fresh startup (clean previous files if they exist for demo validation)
    if os.path.exists(CONFIG_FILE):
        os.remove(CONFIG_FILE)

    # First Start: File missing, should safely handle with default initialization values
    config = load_configuration()

    print("\n--- 2. Reading Nested Settings ---")
    # Access regular settings and multi-layered nested dictionary options
    app_theme = config["settings"]["theme"]
    backup_status = config["settings"]["backup"]["auto_save"]
    save_interval = config["settings"]["backup"]["interval_minutes"]

    print(f"• Application Name : {config['app_name']}")
    print(f"• Target Theme     : {app_theme}")
    print(f"• Auto-Save Active : {backup_status}")
    print(f"• Backup Window    : Every {save_interval} minutes")

    print("\n--- 3. Modifying Setting In-Memory ---")
    # Mutating values inside nested dictionary arrays
    print(f"Old Theme Value: {config['settings']['theme']}")
    config["settings"]["theme"] = "light"
    print(f"New Theme Value: {config['settings']['theme']}")

    print("\n--- 4. Writing Changes Back to Disk ---")
    save_configuration(config)

    print("\n--- 5. Verifying Second Startup Lifecycle Load ---")
    # Reload from file to prove modification saved successfully
    reloaded_config = load_configuration()
    print(f"Verified Theme state from file: {reloaded_config['settings']['theme']}")
