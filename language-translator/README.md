<h1 align="center" id="title">Language Translator - Premium Edition</h1>

The Premium Language Translator project is a stunning, modern desktop application designed to empower seamless communication across more than 100 languages. Utilizing the power of Python, `googletrans`, and a completely revitalized UI via `CustomTkinter`, our project allows you to effortlessly translate text in real-time, breaking down language barriers with a highly polished aesthetic.

With its intelligent auto-detect function, the project can instantly recognize the language of the input text, eliminating the need for manual identification. Once the source language is determined, you have the freedom to select your desired target language from our extensive database of 100+ worldwide languages.

This project goes far beyond text-to-text translation! My project offers additional features such as:
- **Text-to-Speech (Read Aloud)**: Enabling you to smoothly hear the translated text.
- **Speech-to-Text (Voice Input)**: Providing a convenient, hands-free method for entering English text that converts automatically into the target language.
- **Clipboard Integration**: Easily copy the translated text for use in any external application or platform.
- **Quick Clear**: Swiftly remove previous translations to start fresh with zero clutter.

## 🚀 What's New? (Recent Redesign)

- **Total UI Overhaul**: Moved from standard, legacy `tkinter` to a highly customizable, dark-mode-first framework using **CustomTkinter**.
- **Vector Graphics (.SVG)**: All legacy `.png` raster images have been completely removed and replaced with dynamically rendered **SVG vector graphics** via `svglib` and `reportlab`. This ensures crisp, infinitely scalable icons regardless of your monitor resolution.
- **Glassmorphic Layouts**: Clean spacing, rounded corners, flat elegant theme palettes, and a unified dark color scheme mapping perfectly to a premium digital product experience.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/ashin-coder/language-translator.git
   ```
2. Navigate into the folder:
   ```bash
   cd language-translator
   ```
3. Install Python (version 3.10 recommended, though newer versions are usually perfectly fine).
4. Install all the newly required Python backend and frontend dependencies:
   ```bash
   pip install customtkinter svglib reportlab googletrans==3.1.0a0 gTTS SpeechRecognition pyperclip
   ```
   *(Note: You might also need `PyAudio` depending on your OS, which is required by SpeechRecognition for microphone access.)*
5. Run the Application directly from your terminal or IDE:
   ```bash
   python language_translator.py
   ```

**Please Note**: An active Internet Connection is required for the live external libraries (Google Translate API, Google Text-to-Speech, SpeechRecognition) to function.

## Features at a Glance

1. 🌍 **Translate Text**: Translate data instantly spanning over 100 languages.
2. 🔊 **Read Aloud**: Listen dynamically to the translated text.
3. 🎤 **Voice Input**: Speech-to-Text capability for hands-free dictation.
4. 📋 **Copy**: Send translated text to your system clipboard instantly.
5. 🧹 **Clear**: Instantly reset your workspace.
6. 🎨 **Modern GUI**: A beautiful, meticulously crafted Graphical User Interface with deep dark-mode and custom SVGs.

## Implementation Details

The core functionality of the project revolves around translating text from one language to another using the `googletrans` library. The intelligent auto-detect function automatically identifies the language of the input text entirely without user interaction.

The new graphical user interface (GUI) of the project is securely implemented using the `customtkinter` library, paired gracefully with `svglib` which programmatically loads SVG vector assets as memory-mapped images to feed the front-facing UI components (`CTkButton`, `CTkLabel`). We specifically removed static, hardcoded `.png` images and custom-generated high-quality SVG equivalents for UI icons (Translator, Trash, Copy, Microphone, Document).

Other libraries include:
- `gTTS`: Google Text-to-Speech integration logic, automatically managing temporary `.mp3` cache generation and OS-level audio triggering.
- `speech_recognition`: Handling microphone listening instances, ambient noise filtering, and parsing input into string streams.
- `pyperclip`: Bridging internal strings with system OS clipboards.

## Acknowledgments

I would like to thank the developers and contributors of Python, as well as the robust frameworks (`customtkinter`, `gTTS`, `svglib`) used in this project. All vector pathways and `.svg` layouts generated independently or sourced openly.

## Project Disclaimer: For Demonstration Purposes Only

**Please Note**: The project provided here is for demonstration purposes only and may contain bugs or glitches. The intention behind sharing this project is to provide a solid GUI/API integration boilerplate and showcase the immense value of Python-based modern frontend design. It is encouraged for users to further enhance and improve the project based on their specific edge-case requirements!
