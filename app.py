from llama_index import GPTSimpleVectorIndex, Document, download_loader
import openai
import os

os.environ['OPENAI_API_KEY'] = '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'

# GoogleDriveReader = download_loader("GoogleDriveReader")
SimpleDirectoryReader = download_loader("SimpleDirectoryReader")
question = ' '

if __name__ == "__main__":
    question = input("Do you want to recreate the index ? (y/n)")
    if question == 'y':
        loader = SimpleDirectoryReader('./Files')
        documents = loader.load_data()
        for doc in documents:
          print(doc.text)
        # print(documents)
        index = GPTSimpleVectorIndex(documents)
        index.save_to_disk('index.json')
    else:
        index = GPTSimpleVectorIndex.load_from_disk('index.json')
    while question:
        question = input("Type a question :")
        if question != '':
            response = index.query(question)
            print(response)
        else:
            break