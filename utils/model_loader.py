import os
from dotenv import load_dotenv
from typing import Literal, Optional, Any
from pydantic import BaseModel, Field
from utils.config_loader import load_config
from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI




class ConfigLoader:

    def __init__(self):
        print("Loading config...")
        self.config = load_config()
        load_dotenv()
        
    def __getitem__(self, key):
        return self.config.get(key)

class ModelLoader(BaseModel):
    
    model_provider: Literal["openai", "groq"] = "groq"
    config: Optional[ConfigLoader] = Field(default=None, exclude=True)

    def model_post_init(self, _context: Any) -> None:
        self.config = ConfigLoader()

    class Config:
        arbitrary_types_allowed = True

    def load_llm(self):
        """
        Load and return the LLM model
        """

        print("LLM loading...")
        print(f"Loading model from provider: {self.model_provider}")

        if self.model_provider == "groq":
            print("Loading LLM from Groq...")
            
            groq_api_key = os.getenv("GROQ_API_KEY")
            
            # --- DEBUG STEP 1: Check API Key ---
            if not groq_api_key:
                 raise ValueError("CRITICAL ERROR: GROQ_API_KEY is missing from environment.")
            print("GROQ_API_KEY found. Attempting to load model name...")
            
            # --- DEBUG STEP 2: Handle Config KeyError ---
            try:
                model_name = self.config["llm"]["groq"]["model"]
                print(f"Config path found. Model name: {model_name}")
            except KeyError as e:
                # This will raise a visible error if the config path is wrong
                raise KeyError(f"CRITICAL ERROR: Missing configuration key in config.yaml: {e}")
                
            # --- EXECUTION ---
            print("Initializing ChatGroq...")
            llm = ChatGroq(model=model_name, api_key=groq_api_key)
            print("ChatGroq initialized successfully.")
        elif self.model_provider == "openai":
            print("Loading LLM from OpenAI..............")
            openai_api_key = os.getenv("OPENAI_API_KEY")
            model_name = self.config["llm"]["openai"]["model_name"]
            llm = ChatOpenAI(model_name="o4-mini", api_key=openai_api_key)
        
        return llm