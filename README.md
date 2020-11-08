# Abridger
##### A ML curated study tool that helps the students to prepare with their tests and assignments at the last moment.😎
This project is built during HackCBS.
&NewLine;
### What on earth is this?
“LEARNEX” aims to provide solutions to various problems we as students face reguarly in this digital age of eduvcation..
A)In this, we provide an easy interface where students can either provide an image of their books or notes, links to pages of interests or can directly provide an paragraph and our program will provide an summary of the text (with the option of the length of the summary)
Which will highly benefit them for reading and last minute revision
B)Based on the images or links or paragraphs provided by the user, we provide with a quiz generated upon the topic given in the texts provided by them and also check the correctness of the answers  

### Tech Stack and Algorithms used
1)Python Base Programming Language 
2)OpenCv and Pytesseract for OCR implementation
3)BeautifulSoup4 as a text parser
4)NLTK for text summarization
5)Transformer Networks for Q/A Generation 
7)Cosine similarity for Answer Verification
6)Streamlit for web app deployment

### Installation
To run the jupyter notebooks, make sure you have anaconda already set up, then.
* Clone this repository `git clone https://github.com/Ankitasareen/Learnex-
* Activate conda environment in cmd 

To run the interactive UI for data visualisation deployed in streamlit,
* streamlit run app2.py in conda envt.



### Functionalities
Basically, this app allows the student to input a photo, url or text and our model extracts text from it and provides it's summary. Morever it has a feature for generating questions from the text extracted. The students can enter their answers and using our text similarity model we inform them about how correct they are.








