from ollama import chat
import json

print("=" * 60)
print("             AI TOOL-USING AGENT")
print("=" * 60)


# ============================================================
# TOOL 1 — CALCULATOR
# ============================================================

def calculator(expression):
    try:
        result = eval(expression, {"__builtins__": {}}, {})
        return str(result)
    except:
        return "Unable to calculate the expression."


# ============================================================
# TOOL 2 — COMPANY INFORMATION
# ============================================================

def get_company_info():
    return {
        "company": "Find Web Studios",
        "services": [
            "Web Development",
            "Logo Design",
            "Social Media Marketing",
            "Business Branding"
        ],
        "business_model": "Digital agency"
    }


# ============================================================
# TOOL DEFINITIONS
# ============================================================

tools = [
    {
        "type": "function",
        "function": {
            "name": "calculator",
            "description": "Calculate a mathematical expression.",
            "parameters": {
                "type": "object",
                "properties": {
                    "expression": {
                        "type": "string",
                        "description": "Mathematical expression such as 25 * 4"
                    }
                },
                "required": ["expression"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_company_info",
            "description": "Get information about the company.",
            "parameters": {
                "type": "object",
                "properties": {},
                "required": []
            }
        }
    }
]


# ============================================================
# USER INPUT
# ============================================================

user_message = input("\nWhat would you like me to do?\n> ")


# ============================================================
# FIRST AI CALL
# ============================================================

response = chat(
    model="qwen3:1.7b",
    messages=[
        {
            "role": "user",
            "content": user_message
        }
    ],
    tools=tools
)


# ============================================================
# CHECK WHETHER AI WANTS TO USE A TOOL
# ============================================================

message = response["message"]

if message.get("tool_calls"):

    for tool_call in message["tool_calls"]:

        function_name = tool_call["function"]["name"]
        arguments = tool_call["function"]["arguments"]

        print("\nAI selected tool:", function_name)
        print("Arguments:", arguments)

        # ----------------------------------------------------
        # EXECUTE CALCULATOR
        # ----------------------------------------------------

        if function_name == "calculator":

            expression = arguments["expression"]

            tool_result = calculator(expression)

        # ----------------------------------------------------
        # EXECUTE COMPANY INFORMATION TOOL
        # ----------------------------------------------------

        elif function_name == "get_company_info":

            tool_result = get_company_info()

        else:

            tool_result = "Unknown tool."

        print("Tool result:", tool_result)

else:

    print("\nAI response:")
    print(message["content"])


print("\n" + "=" * 60)
print("                    END")
print("=" * 60)