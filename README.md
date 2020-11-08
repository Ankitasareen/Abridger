# Learnex
##### A ML curated study tool that helps the students to prepare with their tests and assignments at the last moment.😎
This project is built during HackCBS.
&NewLine;
### What on earth is this?
“LEARNEX” aims to provide solutions to various problems we as students face reguarly in this digital age of eduvcation..
A)In this, we provide an easy interface where students can either provide an image of their books or notes, links to pages of interests or can directly provide an paragraph and our program will provide an summary of the text (with the option of the length of the summary)
Which will highly benefit them for reading and last minute revision
B)Based on the images or links or paragraphs provided by the user, we provide with a quiz generated upon the topic given in the texts provided by them and also check the correctness of the answers  

### Tech Stack and Dataset used
* Python Base Programming Language 
* OpenCv and Pytesseract for OCR implementation
* BeautifulSoup4 as a text parser
* NLTK for text summarization
* Transformer Networks for Q/A Generation 
* Cosine similarity for Answer Verification
* Streamlit for web app deployment
The glove twitter dataset used  [link]https://drive.google.com/file/d/17j_PqnNXRAAzo060ooud3qmvzvCjA317/view?usp=sharing/.
(Since this was large enough, we couldnot upload it in github)


### Installation
To run the jupyter notebooks, make sure you have anaconda already set up, then.
* Clone this repository `git clone https://github.com/Ankitasareen/Learnex-
* Activate conda environment in cmd 

To run the interactive UI for data visualisation deployed in streamlit,
* streamlit run app_summarize.py in conda env.



### Functionalities
Basically, this app allows the student to input a photo, url or text and our model extracts text from it and provides it's summary. Morever it has a feature for generating questions from the text extracted. The students can enter their answers and using our text similarity model we inform them about how correct they are.








