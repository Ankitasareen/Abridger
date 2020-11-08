
def Question_Generation(text):
    from pipelines import pipeline
    nlp = pipeline("question-generation")
    return(nlp(text))


