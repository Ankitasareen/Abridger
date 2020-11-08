FROM python:3.7




COPY . /home/abhrant/Projects/education_app
COPY requirements.txt ./requirements.txt
RUN pip install -r requirements.txt
EXPOSE  8501
ENTRYPOINT ["streamlit","run"] 
CMD ["app_summarize.py"]
   

