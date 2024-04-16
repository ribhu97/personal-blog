from langchain_core.messages import AIMessage, HumanMessage
"""Callback Handler that prints to std out."""
import threading
import tiktoken
from typing import Any, Dict, List

from langchain_core.callbacks import BaseCallbackHandler
from langchain_core.outputs import LLMResult

MODEL_COST_PER_1K_TOKENS = {
    # Anthropic Models
    # Claude
    "claude-instant-1.2": 0.0008,
    "claude-2":0.008,
    "claude-2.1":0.008,

    # Claude output
    "claude-instant-1.2-completion": 0.0024,
    "claude-2-completion":0.024,
    "claude-2.1-completion":0.024,


    # OpenAI Models
    # GPT-4 input
    "gpt-4": 0.03,
    "gpt-4-0314": 0.03,
    "gpt-4-0613": 0.03,
    "gpt-4-32k": 0.06,
    "gpt-4-32k-0314": 0.06,
    "gpt-4-32k-0613": 0.06,
    "gpt-4-vision-preview": 0.01,
    "gpt-4-1106-preview": 0.01,
    "gpt-4-0125-preview": 0.01,
    "gpt-4-turbo-preview": 0.01,
    # GPT-4 output
    "gpt-4-completion": 0.06,
    "gpt-4-0314-completion": 0.06,
    "gpt-4-0613-completion": 0.06,
    "gpt-4-32k-completion": 0.12,
    "gpt-4-32k-0314-completion": 0.12,
    "gpt-4-32k-0613-completion": 0.12,
    "gpt-4-vision-preview-completion": 0.03,
    "gpt-4-1106-preview-completion": 0.03,
    "gpt-4-0125-preview-completion": 0.03,
    "gpt-4-turbo-preview-completion": 0.03,

    # GPT-3.5 input
    # gpt-3.5-turbo points at gpt-3.5-turbo-0613 until Feb 16, 2024.
    # Switches to gpt-3.5-turbo-0125 after.
    "gpt-3.5-turbo": 0.0015,
    "gpt-3.5-turbo-0125": 0.0005,
    "gpt-3.5-turbo-0301": 0.0015,
    "gpt-3.5-turbo-0613": 0.0015,
    "gpt-3.5-turbo-1106": 0.001,
    "gpt-3.5-turbo-instruct": 0.0015,
    "gpt-3.5-turbo-16k": 0.003,
    "gpt-3.5-turbo-16k-0613": 0.003,
    # GPT-3.5 output
    # gpt-3.5-turbo points at gpt-3.5-turbo-0613 until Feb 16, 2024.
    # Switches to gpt-3.5-turbo-0125 after.
    "gpt-3.5-turbo-completion": 0.002,
    "gpt-3.5-turbo-0125-completion": 0.0015,
    "gpt-3.5-turbo-0301-completion": 0.002,
    "gpt-3.5-turbo-0613-completion": 0.002,
    "gpt-3.5-turbo-1106-completion": 0.002,
    "gpt-3.5-turbo-instruct-completion": 0.002,
    "gpt-3.5-turbo-16k-completion": 0.004,
    "gpt-3.5-turbo-16k-0613-completion": 0.004,
}

def parse_chat_history(chat_history, message_format):
    lines = chat_history.split("\n")
    messages_formatted = []
    messages_dict = []
    current_speaker = None

    for line in lines:
        if line.startswith("User:"):
            current_speaker = "User"
            content = line[len("User:"):].strip()
            messages_formatted.append(HumanMessage(content=content))
            messages_dict.append({"input": content})

        elif line.startswith("Assistant:"):
            current_speaker = "Assistant"
            content = line[len("Assistant:"):].strip()
            messages_formatted.append(AIMessage(content=content))
            messages_dict.append({"output": content})

        elif current_speaker:
            # continue appending lines for the current speaker
            if current_speaker == "User":
                messages_formatted[-1] = HumanMessage(content=messages_formatted[-1].content + " " + line.strip())
                messages_dict[-1] = {"input": messages_dict[-1]["input"] + " " + line.strip()}
            else:
                messages_formatted[-1] = AIMessage(content=messages_formatted[-1].content + " " + line.strip())
                messages_dict[-1] = {"output": messages_dict[-1]["output"] + " " + line.strip()}

    if not message_format:
       messages = []
       for i in range(0,len(messages_dict)-1,2):
          messages.append((messages_dict[i],messages_dict[i+1]))
       return messages
    else: return messages_formatted

def standardize_model_name(
    model_name: str,
    is_completion: bool = False,
) -> str:
    """
    Standardize the model name to a format that can be used in the OpenAI API.

    Args:
        model_name: Model name to standardize.
        is_completion: Whether the model is used for completion or not.
            Defaults to False.

    Returns:
        Standardized model name.

    """
    model_name = model_name.lower()
    if ".ft-" in model_name:
        model_name = model_name.split(".ft-")[0] + "-azure-finetuned"
    if ":ft-" in model_name:
        model_name = model_name.split(":")[0] + "-finetuned-legacy"
    if "ft:" in model_name:
        model_name = model_name.split(":")[1] + "-finetuned"
    if is_completion and (
        model_name.startswith("gpt-4")
        or model_name.startswith("gpt-3.5")
        or model_name.startswith("gpt-35")
        or model_name.startswith("claude")
        or ("finetuned" in model_name and "legacy" not in model_name)
    ):
        return model_name + "-completion"
    else:
        return model_name


def token_cost_for_model(
    model_name: str, num_tokens: int, is_completion: bool = False
) -> float:
    """
    Get the cost in USD for a given model and number of tokens.

    Args:
        model_name: Name of the model
        num_tokens: Number of tokens.
        is_completion: Whether the model is used for completion or not.
            Defaults to False.

    Returns:
        Cost in USD.
    """
    model_name = standardize_model_name(model_name, is_completion=is_completion)
    if model_name not in MODEL_COST_PER_1K_TOKENS:
        raise ValueError(
            f"Unknown model: {model_name}. Please provide a valid model name."
            "Known models are: " + ", ".join(MODEL_COST_PER_1K_TOKENS.keys())
        )
    return MODEL_COST_PER_1K_TOKENS[model_name] * (num_tokens / 1000)


class TokenCallbackHandler(BaseCallbackHandler):
    """Callback Handler that tracksinfo."""

    total_tokens: int = 0
    prompt_tokens: int = 0
    completion_tokens: int = 0
    successful_requests: int = 0
    total_cost: float = 0.0

    def __init__(self) -> None:
        super().__init__()
        self._lock = threading.Lock()

    def __repr__(self) -> str:
        return (
            f"Tokens Used: {self.total_tokens}\n"
            f"\tPrompt Tokens: {self.prompt_tokens}\n"
            f"\tCompletion Tokens: {self.completion_tokens}\n"
            f"Successful Requests: {self.successful_requests}\n"
            f"Total Cost (USD): ${self.total_cost}"
        )

    @property
    def always_verbose(self) -> bool:
        """Whether to call verbose callbacks even if verbose is False."""
        return True

    def on_llm_start(
        self, serialized: Dict[str, Any], prompts: List[str], **kwargs: Any
    ) -> None:
        """Print out the prompts."""
        print(serialized)
        enc = tiktoken.encoding_for_model("gpt-3.5-turbo-instruct")
        self.prompt_tokens += len(enc.encode(prompts[0]))

    def on_llm_new_token(self, token: str, **kwargs: Any) -> None:
        """Print out the token."""
        print("shit's working")
        self.completion_tokens += 1

    def on_llm_end(self, response: LLMResult, **kwargs: Any) -> None:
        """Collect token usage."""
        if response.llm_output is None:
            return None

        if "token_usage" not in response.llm_output:
            with self._lock:
                self.successful_requests += 1
            return None

        # compute tokens and cost for this request
        token_usage = response.llm_output["token_usage"]
        completion_tokens = token_usage.get("completion_tokens", 0)
        prompt_tokens = token_usage.get("prompt_tokens", 0)
        model_name = standardize_model_name(response.llm_output.get("model_name", ""))
        if model_name in MODEL_COST_PER_1K_TOKENS:
            completion_cost = token_cost_for_model(
                model_name, completion_tokens, is_completion=True
            )
            prompt_cost = token_cost_for_model(model_name, prompt_tokens)
        else:
            completion_cost = 0
            prompt_cost = 0

        # update shared state behind lock
        with self._lock:
            self.total_cost += prompt_cost + completion_cost
            self.total_tokens += token_usage.get("total_tokens", 0)
            self.prompt_tokens += prompt_tokens
            self.completion_tokens += completion_tokens
            self.successful_requests += 1

    def __copy__(self) -> "TokenCallbackHandler":
        """Return a copy of the callback handler."""
        return self

    def __deepcopy__(self, memo: Any) -> "TokenCallbackHandler":
        """Return a deep copy of the callback handler."""
        return self