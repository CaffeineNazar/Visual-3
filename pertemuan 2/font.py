import PySimpleGUI as sg

sg.theme("DarkBlue10")
sg.theme_text_color("#E3CF57")

window = sg.Window(title="profile", layout=[[sg.Text("SELAMAT DATANG DIKELAS", font=("Arial", 18, "italic", "bold", "underline"))],
                                                    [sg.Text("NPM \t: 2210010269")],
                                                    [sg.Text("Nama \t: Muhammad Nazarul Iman")],
                                                    [sg.Text("Kelas \t: 5M RegPagi BJM")],
                                                    [sg.Text("Matkul \t: Pemrograman Visual 3")]], 
                                                size=(510,200),
                                                font=("Times, 18"))
window()                
window.close()