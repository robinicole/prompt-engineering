import streamlit as st
from dataclasses import dataclass
from typing import List
from prompt_classes import Example, FewShotPrompt, COSTARPrompt, ChainOfThoughtPrompt

default_context="I want to share our company's new product feature for serving open source large language models at the lowest cost and lowest latency. The product feature is Anyscale Endpoints, which serves all Llama series models and the Mistral series too."
default_objective="Create a LinkedIn post for me, which aims at Gen AI application developers to click the blog link at the end of the post that explains the features, a handful of how-to-start guides and tutorials, and how to register to use it, at no cost."
default_style="Follow the simple writing style common in communications aimed at developers such as one practised and advocated by Stripe. Be persuasive yet maintain a neutral tone. Avoid sounding too much like sales or marketing pitch."
default_audience="Tailor the post toward developers seeking to look at an alternative to closed and expensive LLM models for inference, where transparency, security, control, and cost are all imperatives for their use cases."
default_response="Be concise and succinct in your response yet impactful. Where appropriate, use appropriate emojis."

def main():
    st.title("Prompt Generator")
    # Few-shot prompting
    st.header("Question:")
    question = st.text_input("The prompt of the model")
    st.header("Few-Shot Prompting")
    st.markdown("Provide few example of input/output for the model to learn what you expect")
    num_examples = st.number_input("Number of Examples", min_value=0, value=1, step=1)
    examples = []
    for i in range(num_examples):
        st.subheader(f"Example {i+1}")
        text = st.text_area(f"Text {i+1}")
        output = st.text_area(f"Output {i+1}")
        examples.append(Example(text=text, output=output))
    few_shot_prompt = FewShotPrompt(examples=examples)

    # COSTAR prompting
    use_costar = st.checkbox("Use COSTAR Prompting")
    st.markdown("Use the CoSTAR method to provide context, objective, style, audience, and response for the model to generate a response.")
    if use_costar:
        st.header("COSTAR Prompting")
        context = st.text_area("Context", default_context)
        objective = st.text_area("Objective", default_objective)
        style = st.text_area("Style", default_style)
        audience = st.text_area("Audience", default_audience)
        response = st.text_area("Response", default_response)
        costar_prompt = COSTARPrompt(
            context=context,
            objective=objective,
            style=style,
            audience=audience,
            response=response
        )

    # Chain of Thought prompting
    st.header("Chain of Thought Prompting")
    st.markdown("Provide a series of steps to guide the model in generating a response.")
    num_steps = st.number_input("Number of Steps", min_value=0, value=0, step=1)
    steps = []
    for i in range(num_steps):
        step = st.text_input(f"Step {i+1}")
        steps.append(step)
    chain_of_thought_prompt = ChainOfThoughtPrompt(steps=steps)

    # Generate prompt
    if st.button("Generate Prompt"):
        st.header("Generated Prompt")
        prompt = few_shot_prompt.show()
        if use_costar:
            prompt += "\n" + costar_prompt.show()
        prompt += "\n" + chain_of_thought_prompt.show()
        prompt += f"""\nText: {question}
Output:"""
        st.code(prompt)

if __name__ == "__main__":
    main()