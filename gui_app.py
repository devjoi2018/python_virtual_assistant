import PySimpleGUI as sg
import salida as op
import virtual_assistant_app as asistente

sg.theme('Dark Black')

# Imagen de un microfono en formato base64
mic = b'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'

# Columnas que construyen la interfaz
layout = [
    [sg.Button('Cancel')],
    [sg.Image(data= op.Circle2, key='_IMAGE_')], # gif animado
    [],
    [sg.Button(
        '',
        image_data= mic, # Carga la imagen del microfono en el boton
        button_color= (sg.theme_background_color(), sg.theme_background_color()), # Elimina el color negro de fondo del gif
        border_width=0,
        key='_MIC_'
        )
     ]
]

window = sg.Window(
    title= '',
    layout= layout,
    no_titlebar= True,
    grab_anywhere= True,
    transparent_color= '#000000' # Transparenta el color de fondo de la ventana
)

while True:
    event, values = window.read(timeout=10)
    
    if event == '_MIC_':
        asistente.run()
    elif event == sg.WINDOW_CLOSED or event == 'Cancel':
        break
    window.Element('_IMAGE_').UpdateAnimation(op.Circle2,  time_between_frames=50)
    
window.close()