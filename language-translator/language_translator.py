import customtkinter as ctk
from PIL import Image
from googletrans import Translator
from tkinter import messagebox
import pyperclip as pc
from gtts import gTTS
import os
import speech_recognition as spr
from svglib.svglib import svg2rlg
from reportlab.graphics import renderPM
import io

# Setup CustomTkinter - Dark Mode with a Green/Emerald Theme for a unique look
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

root = ctk.CTk()
root.title('Language Translator')
root.geometry('1100x700')
root.resizable(True, True)
root.after(0, lambda: root.state('zoomed'))

# Advanced SVG loader that explicitly forces a clean background and scales properly
def load_svg_image(path, size):
    try:
        drawing = svg2rlg(path)
        img = renderPM.drawToPIL(drawing, bg=0x000000, configPM={'line_cap':0}) # bg is ignored when transparent, but helps init Reportlab
        img = img.convert("RGBA")
        
        # Invert colors if needed (since dark mode backgrounds make black SVGs invisible)
        # Assuming the SVGs drawn with Stroke="#FFFFFF", they should be white. 
        # But Reportlab might not render stroke properly if CSS is missing.
        
        # Let's just resize it directly
        img = img.resize(size, Image.Resampling.LANCZOS)
        return ctk.CTkImage(light_image=img, dark_image=img, size=size)
    except Exception as e:
        print(f"Error loading {path}: {e}")
        return None

# Load Icons
icon_size = (28, 28)
translate_icon = load_svg_image("resources/icons/documents.svg", icon_size)
clear_icon = load_svg_image("resources/icons/eraser.svg", icon_size)
copy_icon = load_svg_image("resources/icons/copy.svg", icon_size)
read_aloud_icon = load_svg_image("resources/icons/text_to_speech.svg", icon_size)
voice_input_icon = load_svg_image("resources/icons/voice_recognition.svg", icon_size)
title_icon = load_svg_image("resources/icons/translation.svg", (40, 40))

try:
    drawing = svg2rlg("resources/icons/translation.svg")
    icon_img = renderPM.drawToPIL(drawing)
    from PIL import ImageTk
    icon_photo = ImageTk.PhotoImage(icon_img)
    root.iconphoto(False, icon_photo)
except:
    pass

cl = ''
output = ''

languages_list = [
    'Afrikaans', 'Albanian', 'Arabic', 'Armenian', 'Azerbaijani', 'Basque', 'Belarusian', 'Bengali', 'Bosnian',
    'Bulgarian', 'Catalan', 'Cebuano', 'Chichewa', 'Chinese', 'Corsican', 'Croatian', 'Czech', 'Danish', 'Dutch',
    'English', 'Esperanto', 'Estonian', 'Filipino', 'Finnish', 'French', 'Frisian', 'Galician', 'Georgian', 'German',
    'Greek', 'Gujarati', 'Haitian Creole', 'Hausa', 'Hawaiian', 'Hebrew', 'Hindi', 'Hmong', 'Hungarian', 'Icelandic',
    'Igbo', 'Indonesian', 'Irish', 'Italian', 'Japanese', 'Javanese', 'Kannada', 'Kazakh', 'Khmer', 'Kinyarwanda',
    'Korean', 'Kurdish', 'Kyrgyz', 'Lao', 'Latin', 'Latvian', 'Lithuanian', 'Luxembourgish', 'Macedonian', 'Malagasy',
    'Malay', 'Malayalam', 'Maltese', 'Maori', 'Marathi', 'Mongolian', 'Myanmar', 'Nepali', 'Norwegian', 'Odia',
    'Pashto', 'Persian', 'Polish', 'Portuguese', 'Punjabi', 'Romanian', 'Russian', 'Samoan', 'Scots Gaelic', 'Serbian',
    'Sesotho', 'Shona', 'Sindhi', 'Sinhala', 'Slovak', 'Slovenian', 'Somali', 'Spanish', 'Sundanese', 'Swahili',
    'Swedish', 'Tajik', 'Tamil', 'Tatar', 'Telugu', 'Thai', 'Turkish', 'Turkmen', 'Ukrainian', 'Urdu', 'Uyghur',
    'Uzbek', 'Vietnamese', 'Welsh', 'Xhosa', 'Yiddish', 'Yoruba', 'Zulu'
]

def translate():
    language_1 = t1.get("1.0", "end-1c")
    global cl
    cl = choose_language_var.get()

    if language_1.strip() == '':
        messagebox.showerror('Language Translator', 'Please fill the Text Box for Translation')
    else:
        t2.delete("1.0", 'end')
        translator = Translator()
        global output
        try:
            output_obj = translator.translate(language_1, dest=cl)
            output = output_obj.text
            t2.insert('end', output)
        except Exception as e:
             messagebox.showerror('Error', f'Translation failed: {e}')

def clear():
    t1.delete("1.0", 'end')
    t2.delete("1.0", 'end')
    status_label.configure(text="Workspace Cleared", text_color="grey")

def copy():
    pc.copy(str(output))
    status_label.configure(text="Copied to Clipboard!", text_color="#10b981")

def get_lang_code(lang_name):
    mapping = {
        'English': 'en', 'Afrikaans': 'af', 'Albanian': 'sq', 'Arabic': 'ar', 'Armenian': 'hy', 'Azerbaijani': 'az',
        'Basque': 'eu', 'Belarusian': 'be', 'Bengali': 'bn', 'Bosnian': 'bs', 'Bulgarian': 'bg', 'Catalan': 'ca',
        'Cebuano': 'ceb', 'Chinese': 'zh-cn', 'Corsican': 'co', 'Croatian': 'hr', 'Czech': 'cs', 'Danish': 'da',
        'Dutch': 'nl', 'Esperanto': 'eo', 'Estonian': 'et', 'Finnish': 'fi', 'French': 'fr', 'Frisian': 'fy',
        'Galician': 'gl', 'Georgian': 'ka', 'German': 'de', 'Greek': 'el', 'Gujarati': 'gu', 'Haitian Creole': 'ht',
        'Hausa': 'ha', 'Hawaiian': 'haw', 'Hebrew': 'he', 'Hindi': 'hi', 'Hmong': 'hmn', 'Hungarian': 'hu',
        'Icelandic': 'is', 'Igbo': 'ig', 'Indonesian': 'id', 'Irish': 'ga', 'Italian': 'it', 'Japanese': 'ja',
        'Javanese': 'jv', 'Kannada': 'kn', 'Kazakh': 'kk', 'Khmer': 'km', 'Kinyarwanda': 'rw', 'Korean': 'ko',
        'Kurdish': 'ku', 'Kyrgyz': 'ky', 'Lao': 'lo', 'Latin': 'la', 'Latvian': 'lv', 'Lithuanian': 'lt',
        'Luxembourgish': 'lb', 'Macedonian': 'mk', 'Malagasy': 'mg', 'Malay': 'ms', 'Malayalam': 'ml', 'Maltese': 'mt',
        'Maori': 'mi', 'Marathi': 'mr', 'Mongolian': 'mn', 'Myanmar': 'my', 'Nepali': 'ne', 'Norwegian': 'no',
        'Odia': 'or', 'Pashto': 'ps', 'Persian': 'fa', 'Polish': 'pl', 'Portuguese': 'pt', 'Punjabi': 'pa',
        'Romanian': 'ro', 'Russian': 'ru', 'Samoan': 'sm', 'Scots Gaelic': 'gd', 'Serbian': 'sr', 'Sesotho': 'st',
        'Shona': 'sn', 'Sindhi': 'sd', 'Sinhala': 'si', 'Slovak': 'sk', 'Slovenian': 'sl', 'Somali': 'so',
        'Spanish': 'es', 'Sundanese': 'su', 'Swahili': 'sw', 'Swedish': 'sv', 'Tajik': 'tg', 'Tamil': 'ta',
        'Tatar': 'tt', 'Telugu': 'te', 'Thai': 'th', 'Turkish': 'tr', 'Turkmen': 'tk', 'Ukrainian': 'uk', 'Urdu': 'ur',
        'Uyghur': 'ug', 'Uzbek': 'uz', 'Vietnamese': 'vi', 'Welsh': 'cy', 'Xhosa': 'xh', 'Yiddish': 'yi',
        'Yoruba': 'yo', 'Zulu': 'zu'
    }
    return mapping.get(lang_name, 'en')

def texttospeech():
    global cl
    cl = choose_language_var.get()
    if os.path.exists("text_to_speech.mp3"):
        try:
            os.remove("text_to_speech.mp3")
        except:
            pass
    mytext = output
    if not mytext:
        messagebox.showerror('Error','Please translate something first before reading aloud.')
        return
        
    language = get_lang_code(cl)
    
    try:
        status_label.configure(text="Generating Audio...", text_color="#f59e0b")
        root.update()
        myobj = gTTS(text=mytext, lang=language, slow=False)
        myobj.save("text_to_speech.mp3")
        os.system("start text_to_speech.mp3" if os.name == 'nt' else "text_to_speech.mp3")
        status_label.configure(text="Playing Audio!", text_color="#10b981")
    except ValueError:
        messagebox.showerror('Error', cl + ' is currently not supported for Read Aloud')
    except AssertionError:
        messagebox.showerror('Error','Please enter data.')

def speechtotext():
    cl = choose_language_var.get()
    to_lang = get_lang_code(cl)
    from_lang = "en"

    recog1 = spr.Recognizer()
    mc = spr.Microphone()

    status_label.configure(text="Listening... Speak now", text_color="#8b5cf6")
    root.update()

    with mc as source:
        recog1.adjust_for_ambient_noise(source, duration=0.9)
        try:
            audio = recog1.listen(source, timeout=5)
            status_label.configure(text="Recognizing...", text_color="#f59e0b")
            root.update()
            
            get_sentence = recog1.recognize_google(audio)
            
            t1.delete("1.0", 'end')
            t1.insert("end", get_sentence)
            
            translator = Translator()
            text_to_translate = translator.translate(get_sentence, src=from_lang, dest=to_lang)
            
            global output
            output = text_to_translate.text
            t2.delete("1.0", 'end')
            t2.insert("end", output)
            
            status_label.configure(text="Done! Playing feedback...", text_color="#10b981")
            root.update()

            speak = gTTS(text=output, lang=to_lang, slow=False)
            speak.save("text_to_speech_temp.mp3")
            os.system("start text_to_speech_temp.mp3" if os.name == 'nt' else "text_to_speech_temp.mp3")
            
        except spr.UnknownValueError:
            messagebox.showwarning("Voice Input", "Unable to Understand the Input")
            status_label.configure(text="Ready")
        except spr.RequestError as e:
            messagebox.showerror("Voice Input", f"Could not request results; {e}")
            status_label.configure(text="Ready")
        except Exception as e:
            messagebox.showerror("Voice Input", f"Error: {e}")
            status_label.configure(text="Ready")

# ----------------- UI LAYOUT REDESIGN -----------------
# We will create a modern "split-panel" layout. 
# Left Sidebar = Controls & Settings
# Right Content = Editor areas

sidebar = ctk.CTkFrame(root, width=250, corner_radius=0)
sidebar.pack(side="left", fill="y")
sidebar.pack_propagate(False)

content = ctk.CTkFrame(root, fg_color="transparent")
content.pack(side="right", fill="both", expand=True)

# SIDEBAR COMPONENTS
title_label = ctk.CTkLabel(sidebar, text=" NeuraTrans", image=title_icon, compound="left", font=ctk.CTkFont(size=24, weight="bold"))
title_label.pack(pady=(30, 10))

subtitle_label = ctk.CTkLabel(sidebar, text="Premium Translator Suite", font=ctk.CTkFont(size=12), text_color="gray")
subtitle_label.pack(pady=(0, 30))

btn_kwargs = {"height": 50, "font": ctk.CTkFont(size=15, weight="bold"), "corner_radius": 12, "anchor": "w", "image": translate_icon, "compound": "left"}

translate_btn = ctk.CTkButton(sidebar, text="Translate", command=translate, **btn_kwargs)
translate_btn.configure(image=translate_icon)
translate_btn.pack(pady=10, padx=20, fill="x")

read_aloud_btn = ctk.CTkButton(sidebar, text="Read Aloud", command=texttospeech, fg_color="#ea580c", hover_color="#c2410c", **btn_kwargs)
read_aloud_btn.configure(image=read_aloud_icon)
read_aloud_btn.pack(pady=10, padx=20, fill="x")

voice_input_btn = ctk.CTkButton(sidebar, text="Voice Dictation", command=speechtotext, fg_color="#7c3aed", hover_color="#6d28d9", **btn_kwargs)
voice_input_btn.configure(image=voice_input_icon)
voice_input_btn.pack(pady=10, padx=20, fill="x")

copy_btn = ctk.CTkButton(sidebar, text="Copy to Clipboard", command=copy, fg_color="#059669", hover_color="#047857", **btn_kwargs)
copy_btn.configure(image=copy_icon)
copy_btn.pack(pady=10, padx=20, fill="x")

clear_btn = ctk.CTkButton(sidebar, text="Clear Workspace", command=clear, fg_color="#dc2626", hover_color="#b91c1c", **btn_kwargs)
clear_btn.configure(image=clear_icon)
clear_btn.pack(pady=10, padx=20, fill="x")

# Status Label at the bottom of the sidebar
status_label = ctk.CTkLabel(sidebar, text="Ready", font=ctk.CTkFont(size=14, weight="bold"), text_color="gray")
status_label.pack(side="bottom", pady=20)

# CONTENT COMPONENTS
top_content = ctk.CTkFrame(content, fg_color="transparent")
top_content.pack(fill="x", pady=20, padx=30)

auto_detect_var = ctk.StringVar(value="Auto Detect")
auto_detect = ctk.CTkOptionMenu(top_content, variable=auto_detect_var, values=["Auto Detect"] + languages_list, width=250, height=40, font=ctk.CTkFont(size=16), corner_radius=10)
auto_detect.pack(side="left")

arrow_label = ctk.CTkLabel(top_content, text="➔", font=ctk.CTkFont(size=30, weight="bold"), text_color="#10b981")
arrow_label.pack(side="left", expand=True)

choose_language_var = ctk.StringVar(value="Spanish")
choose_language = ctk.CTkOptionMenu(top_content, variable=choose_language_var, values=languages_list, width=250, height=40, font=ctk.CTkFont(size=16), corner_radius=10)
choose_language.pack(side="right")

# Text Areas Box
text_container = ctk.CTkFrame(content, fg_color="transparent")
text_container.pack(fill="both", expand=True, padx=30, pady=(0, 30))

t1_frame = ctk.CTkFrame(text_container, corner_radius=15, fg_color="#2b2b2b")
t1_frame.pack(side="left", fill="both", expand=True, padx=(0, 15))

t1_lbl = ctk.CTkLabel(t1_frame, text="Source Text", font=ctk.CTkFont(size=16, weight="bold"), text_color="gray")
t1_lbl.pack(anchor="w", pady=(15, 5), padx=20)

t1 = ctk.CTkTextbox(t1_frame, font=ctk.CTkFont(size=20), fg_color="transparent", text_color="#ffffff", border_width=0, wrap="word")
t1.pack(fill="both", expand=True, padx=20, pady=(0, 20))


t2_frame = ctk.CTkFrame(text_container, corner_radius=15, fg_color="#1d2e28") # slight green tint frame 
t2_frame.pack(side="right", fill="both", expand=True, padx=(15, 0))

t2_lbl = ctk.CTkLabel(t2_frame, text="Translation", font=ctk.CTkFont(size=16, weight="bold"), text_color="#10b981")
t2_lbl.pack(anchor="w", pady=(15, 5), padx=20)

t2 = ctk.CTkTextbox(t2_frame, font=ctk.CTkFont(size=20), fg_color="transparent", text_color="#ffffff", border_width=0, wrap="word")
t2.pack(fill="both", expand=True, padx=20, pady=(0, 20))

root.mainloop()
