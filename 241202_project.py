#%%
# 
import cv2
import pytesseract
from datetime import datetime, timedelta
import json
import os

# Example inventory database
inventory_db = "inventory.json"

# Load or initialize inventory database
def load_inventory():
    if os.path.exists(inventory_db):
        with open(inventory_db, "r") as file:
            return json.load(file)
    return {}

def save_inventory(inventory):
    with open(inventory_db, "w") as file:
        json.dump(inventory, file, indent=4)

# Initialize inventory
inventory = load_inventory()

# Function to process image from camera and update inventory
def process_image(image_path):
    # Image recognition to detect food items
    image = cv2.imread(image_path)
    detected_text = pytesseract.image_to_string(image)
    
    # Mock recognition logic (could use a trained ML model for actual use)
    items = detected_text.split("\n")
    for item in items:
        if item.strip():
            name, exp_date = item.split(":") if ":" in item else (item.strip(), None)
            exp_date = datetime.strptime(exp_date.strip(), "%Y-%m-%d") if exp_date else datetime.now() + timedelta(days=7)
            inventory[name.strip()] = {"expiration_date": exp_date.strftime("%Y-%m-%d")}
    save_inventory(inventory)

# Function to alert about expiring items
def check_expiration():
    today = datetime.now().date()
    for item, details in inventory.items():
        exp_date = datetime.strptime(details["expiration_date"], "%Y-%m-%d").date()
        if exp_date <= today:
            print(f"ALERT: {item} has expired or is expiring today!")
        elif (exp_date - today).days <= 2:
            print(f"WARNING: {item} will expire in {(exp_date - today).days} day(s).")

# Function to recommend recipes
def recommend_recipes():
    available_items = inventory.keys()
    print("Based on your inventory, try these recipes:")
    # Mock logic for recipe recommendation
    print(f"1. {', '.join(available_items)} Salad")
    print(f"2. {', '.join(available_items)} Stir Fry")

# Example Usage
process_image("fridge_camera_image.jpg")  # Replace with actual camera feed
check_expiration()
recommend_recipes()

# %%
