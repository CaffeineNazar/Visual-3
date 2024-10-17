import PySimpleGUI as sg

sg.theme("DarkGreen4")
sg.theme_text_color("#FFFF00")
window = sg.Window(title="Profile",
                    layout=[[sg.Text("FTI UNISKA ", font=("Helvetica", 24))],  #mengganti font dengan helvetica dan size 24
                            [sg.Text("FAKULTAS TEKNOLOGI  INFORMASI ", font=("Courier", 18, "italic", "bold", "underline"))],
                            [sg.Text("UNISKA MAB BANJARMASIN ", text_color="#FFCC00")]],
                    size=(450,200),     #size dari window yang akan ri run
                    font=("Times", 18))

window()
window.close()