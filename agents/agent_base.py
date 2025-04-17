import os
from abc import ABC, abstractmethod
from openai import OpenAI
from loguru import logger


class AgentBase(ABC):
    def __init__(self, name, max_retries=2, verbose=True):
        self.name = name
        self.max_retries = max_retries
        self.verbose = verbose

        
        self.client = OpenAI(
            api_key=os.getenv("GROQ_API_KEY"),
            base_url="https://api.groq.com/openai/v1"
        )

    @abstractmethod
    def execute(self, *args, **kwargs):
        pass

    def call_llama(self, messages, temperature=0.7, max_tokens=150):
        retries = 0
        while retries < self.max_retries:
            try:
                if self.verbose:
                    logger.info(f"[{self.name}] Sending messages to Groq:")
                    for msg in messages:
                        logger.debug(f"  {msg['role']}: {msg['content']}")

                response = self.client.chat.completions.create(
                    model="llama3-8b-8192",
                    messages=messages,
                    temperature=temperature,
                    max_tokens=max_tokens
                )

                reply = response.choices[0].message.content

                if self.verbose:
                    logger.info(f"[{self.name}] Received response: {reply}")

                return reply

            except Exception as e:
                retries += 1
                logger.error(f"[{self.name}] Error during Groq call: {e}. Retry {retries}/{self.max_retries}")

        raise Exception(f"[{self.name}] Failed to get response from Groq after {self.max_retries} retries.")
