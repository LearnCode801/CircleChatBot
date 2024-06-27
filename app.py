from flask import Flask, render_template, jsonify, request
from langchain_core.documents import Document
from langchain_core.prompts import PromptTemplate
# from langchain import LLMChain

# from langchain.prompts import PromptTemplate

from dotenv import load_dotenv
from circlebot.helper import load_AI21Lab_llm, returning_pre_created_vector_store_obj
from circlebot.prompt import *
import os

app = Flask(__name__)
load_dotenv()


llm=load_AI21Lab_llm()
pre_created_vector_store=returning_pre_created_vector_store_obj()


def processing_fun(query,llm,pre_created_vector_store):

    results = pre_created_vector_store.similarity_search(query, k=2)
    cxt=""
    for res in results:
        cxt =cxt + f" ==> {res.page_content} [{res.metadata}] \n "

    print(f"===============>>>>> Context: {cxt}")
    


    # PROMPT=PromptTemplate(template=prompt_template, input_variables=["context", "question"])
    # chain = LLMChain(llm=llm, prompt=PROMPT)
    # result = chain.run({"context": cxt, "question":query})
    

    prompt = PromptTemplate.from_template(prompt_template)
    chain = prompt | llm
    result=chain.invoke({"context": cxt, "question":query})

    return result


@app.route("/")
def index():
    return render_template('chat.html')



@app.route("/get", methods=["GET", "POST"])
def chat():
    msg = request.form["msg"]
    query = msg
    result=processing_fun(query, llm, pre_created_vector_store)
    print(f"Result--->{result}")
    return str(result)



if __name__ == '__main__':
    app.run(host="0.0.0.0", port= 8080, debug= True)




