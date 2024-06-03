from pyscript import document

def your_name(event):
    input_text = document.querySelector("#name")
    name = input_text.value
    
    output_div = document.querySelector("#output")

    if name == "":
        output_div.innerText = ""
    else:
        output_div.innerText = f"Привет, {name}!"
        
