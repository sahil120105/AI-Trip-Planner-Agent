from fastapi import FastAPI
from pydantic import BaseModel
from agent.agentic_workflow import GraphBuilder
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import os
from utils.save_to_document import save_document
from dotenv import load_dotenv
load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # set specific origins in prod
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


os.environ["LANGSMITH_API_KEY"] = os.getenv("LANGSMITH_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"

class QueryRequest(BaseModel):
    question: str

@app.post("/query")
async def query_travel_agent(query: QueryRequest):

    try:
        print(f"Query received: {query}")
        graph = GraphBuilder(model_provider="groq")
        react_app = graph()

        png_graph = react_app.get_graph().draw_mermaid_png()
        with open("my_graph.png", "wb") as f:
            f.write(png_graph)

        print(f"Graph PNG saved as my_graph.png in {os.getcwd()}")

        messages = {"messages": [query.question]}
        output = react_app.invoke(messages)

        if isinstance(output, dict) and "messages" in output:
            final_output = output["messages"][-1].content  # Last AI response
            # Save to markdown document
            save_document(final_output)
        else:
            final_output = str(output)

        return {"answer": final_output}
    
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})