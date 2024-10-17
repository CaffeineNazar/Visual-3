import PySimpleGUI as sg

window = sg.Window(title="profile", layout=[[sg.Text("NPM \t: 2210010269")],
                                                    [sg.Text("Nama \t: Muhammad Nazarul Iman")],
                                                    [sg.Text("Kelas \t: 5M RegPagi BJM")],
                                                    [sg.Text("nMatkul \t: Pemrograman Visual 3")]], size=(400,200))
window()
window.close()