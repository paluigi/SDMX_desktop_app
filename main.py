import pandas as pd
import PySimpleGUI as sg
import sdmx


sources_list = sdmx.list_sources()

layout_start  = (
    [[sg.Text(f"{s}"), sg.Button(key=f"source_{s}")] for s in sources_list] + 
    [[sg.Button('Exit')]]
)

window = sg.Window('SDMX Sources', layout_start)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit': # if user closes window or clicks cancel
        break
    if event.startswith("source_"):
        source_str = event.split("_")[-1]
        source = sdmx.Client(str)
        datasets = sdmx.to_pandas(source.dataflow().dataflow)
        layout = (
            [[sg.Text(f"{i}"), sg.Text(f"{k}"), sg.Button("Get", key=f"flow_{i}")] for i, k in datasets.items()] + 
            [[sg.Button('Exit')]]
        )
        window.close()

        window = sg.Window(f'Data flow for {source}', layout)

window.close()

#source = sdmx.Client("ECB")
#datasets = sdmx.to_pandas(flow_msg.dataflow)
