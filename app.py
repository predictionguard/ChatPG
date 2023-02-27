import gradio as gr
import predictionguard as pg


# Prediction Guard proxy endpoint names.
chatGen = "chatpg-gen"

# Prompt reference.
prefix = "The following is a conversation with an AI assistant. The assistant is"
prefix += " helpful, creative, clever, and very friendly.\n"


def add_text(state, text):

    # Construct prompt.
    prompt = prefix
    if len(state) > 0:
        for exchange in state:
            prompt += "\nHuman: " + exchange[0] + "\nAI: " + exchange[1]
        prompt += "\nHuman: " + text + "\nAI: "
    else:
        prompt += "\nHuman: " + text + "\nAI: "

    # Get the completion from Prediction Guard.
    client = pg.Client()
    completion = client.predict(name=chatGen, data={"prompt": prompt})['text']
    completion = completion.split("\nHuman:")[0]

    state = state + [(text, completion)]
    return state, state


with gr.Blocks() as demo:
    chatbot = gr.Chatbot(elem_id="chatbot")
    state = gr.State([])
    
    with gr.Row():
        txt = gr.Textbox(show_label=False, placeholder="Enter text and press enter").style(container=False)
            
    txt.submit(add_text, [state, txt], [state, chatbot])

            
demo.launch()