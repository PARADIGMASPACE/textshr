from app.config import settings
from typing import Dict

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

class TextService:
    def __init__(self):
        self.llm = ChatOpenAI(
            model=settings.openai_model,
            api_key=settings.openai_api_key,
            temperature=0.0, 
        )
        self._build_chains()

    def _build_chains(self):
        correction_prompt = ChatPromptTemplate.from_template(
            "Fix grammar, spelling, punctuation, and improve clarity. "
            "Return only the corrected text, no explanations:\n\n{text}"
        )
        self.correction_chain = correction_prompt | self.llm | StrOutputParser()

        summarization_prompt = ChatPromptTemplate.from_template(
            "Summarize the following text in 2-3 clear, concise sentences:\n\n{text}"
        )
        self.summarization_chain = summarization_prompt | self.llm | StrOutputParser()


    async def text_correction(self, text: str) -> Dict[str, str]:
        corrected = await self.correction_chain.ainvoke({"text": text})
        return {"result": corrected}

    async def text_summarization(self, text: str) -> Dict[str, str]:
        summary = await self.summarization_chain.ainvoke({"text": text})
        return {"result": summary}