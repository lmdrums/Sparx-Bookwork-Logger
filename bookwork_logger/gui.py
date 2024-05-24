from customtkinter import (CTk, CTkLabel, CTkEntry, CTkButton, CTkToplevel,
                           CTkImage, CTkFrame, StringVar, CTkSwitch,
                           set_appearance_mode, set_default_color_theme, END)
from PIL import Image
from selenium.common.exceptions import InvalidArgumentException
from tkinter import messagebox
from threading import Thread

import bookwork_logger.constants as c
import bookwork_logger.helpers as h
from bookwork_logger.main import main as script
from utils.path import get_resource_path
from utils.settings import get_setting, edit_setting

set_default_color_theme(get_resource_path(c.THEME_PATH))
set_appearance_mode("system")

get_pillow_image = lambda relative_path: Image.open(get_resource_path(relative_path))

find_image = CTkImage(light_image=get_pillow_image(c.FIND_IMAGE["dark"]),
                          dark_image=get_pillow_image(c.FIND_IMAGE["light"]))
run_image = CTkImage(light_image=get_pillow_image(c.RUN_IMAGE["dark"]),
                          dark_image=get_pillow_image(c.RUN_IMAGE["light"]))
save_image = CTkImage(light_image=get_pillow_image(c.SAVE_IMAGE["dark"]),
                          dark_image=get_pillow_image(c.SAVE_IMAGE["light"]))
settings_image = CTkImage(light_image=get_pillow_image(c.SETTINGS_IMAGE["dark"]),
                          dark_image=get_pillow_image(c.SETTINGS_IMAGE["light"]))

class App(CTk):
    def __init__(self):
        super().__init__()
        
        self.title(c.MAIN_TITLE)
        self.geometry(c.MAIN_GEOMETRY)
        self.iconbitmap(get_resource_path(c.WINDOW_ICON_PATH))
        
        self.frame = CTkFrame(self)
        self.frame.pack(pady=20, padx=20, fill="both", expand=True)

        self.run_button = CTkButton(self.frame, text="Launch Sparx", image=run_image,
                                    width=240, height=40, command=self.run_sparx)
        self.run_button.pack(pady=(20,0))

        self.settings_button = CTkButton(self.frame, text="Settings", image=settings_image,
                                         width=240, height=40, command=self.settings_function)
        self.settings_button.pack(pady=(10,0))

        self.bookwork_search = CTkEntry(self.frame, placeholder_text="Search for bookwork", width=160,
                                        justify="center")
        self.bookwork_search.pack(pady=(15,0))
        self.bookwork_search.bind("<Return>", lambda _: self.search_for_bookwork())

        self.search_button = CTkButton(self.frame, text="Find", width=100, 
                                       command=self.search_for_bookwork, image=find_image)
        self.search_button.pack(pady=(7,0))

        self.dark_mode_val = StringVar(value="off")
        self.mode = CTkSwitch(self.frame, text="Dark Theme", variable=self.dark_mode_val,
                              onvalue="on", offvalue="off", command=self.dark_mode)
        self.mode.pack(side="left", anchor="sw", padx=10, pady=10)

        self.clear_hw_session = CTkButton(self.frame, text="Clear Homework Session",
                                          fg_color="#c92020", hover_color="#9c1919", command=self.clear_session)
        self.clear_hw_session.pack(side="right", anchor="se", padx=10, pady=10)

        self.image_frame = CTkFrame(self.frame, fg_color="grey85")
        self.image_frame.pack(pady=20, padx=(20,10), fill="both", expand=True, side="bottom", anchor="n")

        self.image_label = CTkLabel(self.image_frame, text="")
        self.image_label.pack()
        self.image_label.place(anchor="center", relx=0.5, rely=0.5)
  
    def bookwork_check(self, image, bookwork):
        h.send_notification("Bookwork Check",
                            f"Bookwork Check! Bookwork code {bookwork} found and displayed.",
                            get_resource_path(c.NOTIFICATION_ICON_PATH),
                            get_resource_path(c.NOTIFICATION_SOUND_PATH))

        self.state("zoomed")
        self.image_frame.configure(fg_color="#EEF4FE")
        self.image_label.configure(image=image)
        
    def run_sparx(self):
        def run_script():
            self.run_button.configure(text="Running...", fg_color=("#325882", "#254260"), state="disabled")

            try:
                script(self)
            except InvalidArgumentException:
                messagebox.showerror("Invalid Settings", "Make sure you have valid settings.")
            finally:
                self.run_button.configure(text="Launch Sparx", fg_color=("#3a7ebf", "#1f538d"), state="normal")

        Thread(target=run_script).start()
    
    def clear_session(self):
        if messagebox.askyesnocancel("Continue?",
                                  "All bookwork codes from this session will be cleared.\nContinue?", 
                                  icon="warning"):
            h.end_hw_session()
            messagebox.showinfo("Success", "This homework session has successfully been deleted")

    def dark_mode(self):
        value = self.dark_mode_val.get()
        if value == "off":
            set_appearance_mode("light")
        elif value == "on":
            set_appearance_mode("dark")

    def search_for_bookwork(self):
        try:
            bookwork = self.bookwork_search.get()
            image = h.get_bookwork_image(bookwork.upper())
            if image:
                self.state("zoomed")
                
                self.image_frame.configure(fg_color="#EEF4FE")
                self.image_label.configure(image=image)
            else:
                messagebox.showerror("Error", "This bookwork code could not be located.")
        except UserWarning:
            pass

    def settings_function(self):
        settings = Settings()
        settings.mainloop()

class Settings(CTkToplevel):
    def __init__(self):
        super().__init__()

        self.title(c.SETTINGS_TITLE)
        self.geometry(c.SETTINGS_GEOMETRY)
        self.after(250, lambda: self.iconbitmap(get_resource_path(c.WINDOW_ICON_PATH)))

        self.frame = CTkFrame(self)
        self.frame.pack(pady=20, padx=20, fill="both", expand=True)

        self.username_label = CTkLabel(self.frame, text="Username")
        self.username_label.grid(column=0, row=0, padx=10, pady=(10,0), sticky="w")

        self.username_entry = CTkEntry(self.frame, placeholder_text="Enter username",
                                       width=200)
        self.username_entry.grid(column=1, row=0, pady=(10,0), sticky="w")

        self.password_label = CTkLabel(self.frame, text="Password")
        self.password_label.grid(column=0, row=1, padx=10, pady=(10,0), sticky="w")

        self.password_entry = CTkEntry(self.frame, placeholder_text="Enter password",
                                       width=200, show="●")
        self.password_entry.grid(column=1, row=1, pady=(10,0), sticky="w")

        self.url_label = CTkLabel(self.frame, text="URL")
        self.url_label.grid(column=0, row=2, padx=10, pady=(10,0), sticky="w")

        self.url_entry = CTkEntry(self.frame, placeholder_text="Enter URL",
                                       width=400)
        self.url_entry.grid(column=1, row=2, pady=(10,0), sticky="w")

        self.save_button = CTkButton(self.frame, text="Save", 
                                     command=self.save_function, image=save_image)
        self.save_button.grid(column=0, row=3, padx=10, pady=(10,0), sticky="w")


        self.username_entry.bind("<Return>", lambda _: self.save_function())
        self.password_entry.bind("<Return>", lambda _: self.save_function())
        self.url_entry.bind("<Return>", lambda _: self.save_function())

        self.after(200, self.lift)
        self.get_info()

    def get_info(self):
        self.username_entry.delete(0, END)
        self.username_entry.insert(END, get_setting(*c.USERNAME_SETTING_LOCATOR))
        
        self.password_entry.delete(0, END)
        self.password_entry.insert(END, get_setting(*c.PASSWORD_SETTING_LOCATOR))

        self.url_entry.delete(0, END)
        self.url_entry.insert(END, get_setting(*c.URL_SETTING_LOCATOR))

    def save_function(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        url = self.url_entry.get()

        if not username:
            messagebox.showerror("Error", "Please enter a valid username")
            self.lift()
        elif not password:
            messagebox.showerror("Error", "Please enter a valid password")
            self.lift()
        elif not url:
            messagebox.showerror("Error", "Please enter a valid URL")
            self.lift()
        else:
            edit_setting(*c.USERNAME_SETTING_LOCATOR, username)
            edit_setting(*c.PASSWORD_SETTING_LOCATOR, password)
            edit_setting(*c.URL_SETTING_LOCATOR, url)

            messagebox.showinfo("Success", "Settings saved successfully")
            self.lift()

def main():
    App().mainloop()