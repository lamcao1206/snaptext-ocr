# SnapText

📸 **SnapText** is a macOS menu bar application that automatically extracts text from screenshots saved on your desktop using Optical Character Recognition (OCR). The extracted text is copied to your clipboard for easy use.

## Features

- Automatically detects new screenshots saved on your desktop.
- Extracts text from screenshots using [Tesseract OCR](https://github.com/tesseract-ocr/tesseract).
- Copies the extracted text to your clipboard.
- Displays notifications for successful text extraction.
- Allows you to view the last extracted text via the menu bar.
- Deletes processed screenshots to keep your desktop clean.

## Why SnapText?

I came up with this tool while vibing to the **Lofi Girl** YouTube stream and constantly missing the song titles. SnapText lets you screenshot the title, extracts the text, and copies it to your clipboard—so you can stay in the zone without missing a beat.

## Requirements

- Python 3.7 or higher
- macOS
- The following Python packages (specified in `requirements.txt`):
  - `packaging==24.2`
  - `pillow==11.1.0`
  - `pyobjc-core==11.0`
  - `pyobjc-framework-cocoa==11.0`
  - `pyobjc-framework-quartz==11.0`
  - `pyperclip==1.9.0`
  - `pytesseract==0.3.13`
  - `rumps==0.4.0`

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/lamcao1206/snaptext-ocr.git
   cd snaptext
   ```
2. Run the application:
   ```bash
   python main.py
   ```
   SnapText will appear in your macOS menu bar with the icon 📸.
