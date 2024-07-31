# About
Hello, This is my solo submission for Windy City Hacks, Schumburg. I wanted to make an educational program that allows people with disabilities to be better able to comunicate and interact with the learning enviornment in schools (in this case ASL to Text). As schools around the world have slowly drifted towards using more technology, it opens up an opertunity to allow more students to utilize cool and new technologies that are easily intagratable into the classroom enviornment. This concept is still, well, a concept so it only supports ASL letters A-G, but nevertheless it is still a usefull program to use in the classroom.

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
            - **DO NOT TEST YOUR MODEL AS IT WILL BE INACCURATE DUE TO THE DOTS AND LINES NOT BEING PROJECTED ON YOUR HAND**
    - Put replace everything in the `Model` folder to import your new model **(Only A-G Supported as of Currently)**

## Known Problems
- Keras Tensorflow Classifier (main part of the program) doesn't even work

### Sources:
- Sign Language Alphabet (Shapes)
    - https://www.ai-media.tv/knowledge-hub/insights/sign-language-alphabets/

- Media Pipe
    - https://www.youtube.com/watch?v=TACu8y2T2ps

- CVZone (MediaPipe Fork)
    - https://www.youtube.com/watch?v=ieXQTtQgyo0

- Pillow (Image Library) Docs:
    - https://pillow.readthedocs.io/en/stable/
