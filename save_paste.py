"""
Auto-save paste tool - saves everything to file immediately
"""

import os
from datetime import datetime

def save_paste(content, label=""):
    """Save pasted content to file with timestamp"""
    os.makedirs('data/pastes', exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"data/pastes/paste_{timestamp}_{label}.txt"

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"[OK] Saved to: {filename}")
    return filename

if __name__ == "__main__":
    print("Paste content (Ctrl+Z then Enter when done):")
    lines = []
    try:
        while True:
            lines.append(input())
    except EOFError:
        pass

    content = '\n'.join(lines)
    label = input("\nLabel (town_season, e.g., FOX_Fall2025): ").strip()
    save_paste(content, label)
