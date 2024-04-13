# Prompt Engineering with Streamlit

This repository contains a Streamlit application that helps generate prompts for large language models using various prompt engineering techniques, including:

- Few-Shot Prompting
- COSTAR Prompting
- Chain of Thought Prompting

## Features

- Provides a user-friendly interface for generating prompts
- Supports multiple examples for Few-Shot Prompting
- Allows customization of context, objective, style, audience, and response for COSTAR Prompting
- Supports Chain of Thought Prompting with customizable steps
- Generates a prompt based on the selected techniques and user input

## Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/prompt-engineering-streamlit.git
cd prompt-engineering-streamlit
```

2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

To run the Streamlit application, execute the following command:

```bash
streamlit run app.py
```

This will start the application, and you can access it through your web browser at `http://localhost:8501`.

## Technologies Used

- Python
- Streamlit
- dataclasses

## Customization

You can customize the default values for the COSTAR Prompting fields by modifying the following variables in the `app.py` file:

- `default_context`
- `default_objective`
- `default_style`
- `default_audience`
- `default_response`

## Contributing

Feel free to submit issues or pull requests if you have any suggestions or improvements for the application.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.

## Contact

For any questions or inquiries, please contact [your email address].