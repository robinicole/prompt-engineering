import streamlit as st
from dataclasses import dataclass
from typing import List

@dataclass
class Example:
    text: str
    output: str

@dataclass
class FewShotPrompt:
    examples: List[Example]

    def show(self) -> str:
        example_template = """
<example>
Text: {text}
Output: {output}
</example>"""
        examples_str = ""
        for example in self.examples:
            examples_str += example_template.format(
                text=example.text,
                output=example.output
            )
        return examples_str

@dataclass
class COSTARPrompt:
    context: str
    objective: str
    style: str
    audience: str
    response: str

    def show(self) -> str:
        costar_template = f"""
<CONTEXT>
{self.context}
</CONTEXT>
<OBJECTIVE>
{self.objective}
</OBJECTIVE>
<STYLE>
{self.style}
</STYLE>
<AUDIENCE>
{self.audience}
</AUDIENCE>
<RESPONSE>
{self.response}
</RESPONSE>
"""
        return costar_template

@dataclass
class ChainOfThoughtPrompt:
    steps: List[str]

    def show(self) -> str:
        if not self.steps:
            return "Think step by step"
        else:
            return '\n'.join([f"{ix}. {step}" for ix, step in enumerate(self.steps, start=1)])