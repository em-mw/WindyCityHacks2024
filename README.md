# Hello, this is my SOLO submition for Windy City Hacks, Schumburg

## Dependencies:
just run the req.txt through pip
`pip install -r req.txt` ***Note:*** *if this does not work try putting in the `req.txt` directory/path or try installing pip*

## How To Run:
- Training your hand
    - `cvtrain.py` allows you to take photos of the sign that you want to use (just press s to take the photo of the ML hands)
    - `cvcon.py` takes the images that you took with `cvtrain.py` and makes themm all the same resolution for the next step
    - got to (Teachable Machines)[https://teachablemachine.withgoogle.com/] and train your images as images
        - you will be fine with the default settings but if you want to change them then feel free to do so
        - to **export**, export the `Kearas` Model from the `Tensor Flow` Tab of the export
            - **DO NOT TEST YOUR MODEL AS IT WILL BE INACCURATE DUE TO THE DOTS AND LINES NOT BEING PROJECCTED ON YOUR HAND**
    - Put replace everything in the `Model` folder to import your new model **(Only A-G Supported as of Currently)**

### Sources:
- Sign Language Alphabet (Shapes)
    - https://www.ai-media.tv/knowledge-hub/insights/sign-language-alphabets/

- Media Pipe
    - https://www.youtube.com/watch?v=TACu8y2T2ps

- CVZone (MediaPipe Fork)
    - https://www.youtube.com/watch?v=ieXQTtQgyo0

- Pillow (Image Library) Docs:
    - https://pillow.readthedocs.io/en/stable/