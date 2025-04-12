import os
import time
import logging
import pytesseract
import pyperclip
from PIL import Image
import rumps

WATCH_FOLDER = os.path.expanduser("~/Desktop")
PROCESSED_FILES = set()

logger = logging.getLogger("SnapTextFileWatcher")
logger.setLevel(logging.INFO)
console = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(message)s')
console.setFormatter(formatter)
logger.addHandler(console)

class SnapTextWatcher(rumps.App):
    def __init__(self):
        super(SnapTextWatcher, self).__init__("📸 SnapText")
        self.menu = ["Show Last Text"]
        self.last_text = ""
        rumps.Timer(self.watch_for_screenshots, 1).start()
        logger.info("📸 SnapText file watcher started.")

    def watch_for_screenshots(self, _):
        try:
            files = [f for f in os.listdir(WATCH_FOLDER) if f.startswith("Screenshot") and f.endswith(".png")]
            for file in sorted(files, key=lambda x: os.path.getctime(os.path.join(WATCH_FOLDER, x))):
                full_path = os.path.join(WATCH_FOLDER, file)
                if full_path in PROCESSED_FILES:
                    continue
                time.sleep(0.5)  # give time for screenshot to finish saving
                logger.info(f"🖼️ New screenshot detected: {file}")
                text = self.extract_text(full_path)
                if text:
                    self.last_text = text
                    pyperclip.copy(text)
                    logger.info(f"✅ Text extracted and copied:\n{text}\n")
                    rumps.notification("SnapText", "Text copied from screenshot!", text[:100])
                else:
                    logger.info("🧐 No text detected in screenshot.")
                PROCESSED_FILES.add(full_path)
                os.remove(full_path)
                logger.info(f"🗑️ Screenshot deleted: {file}")
        except Exception as e:
            logger.error(f"💥 Error: {e}", exc_info=True)

    def extract_text(self, filepath):
        try:
            image = Image.open(filepath)
            return pytesseract.image_to_string(image).strip()
        except Exception as e:
            logger.error(f"⚠️ Failed to OCR image {filepath}: {e}")
            return ""

    @rumps.clicked("Show Last Text")
    def show_last_text(self, _):
        if self.last_text:
            rumps.alert("Last Extracted Text", self.last_text[:2000])
        else:
            rumps.alert("No text extracted yet.")

    @rumps.clicked("Quit")
    def quit_app(self, _):
        logger.info("👋 SnapText quitting.")
        rumps.quit_application()

if __name__ == "__main__":
    SnapTextWatcher().run()
