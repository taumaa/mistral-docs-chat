from smolagents import ToolCallingAgent, DuckDuckGoSearchTool, LiteLLMModel, GradioUI
from tools.Mistral import MistralTool
from const import MISTRAL_API_KEY

def main():
    model = LiteLLMModel(
        model_id="mistral/mistral-large-latest",
        api_key=MISTRAL_API_KEY
    )
    
    agent = ToolCallingAgent(tools=[MistralTool()], model=model)

    ui = GradioUI(agent)
    ui.launch()

if __name__ == "__main__":
    main()