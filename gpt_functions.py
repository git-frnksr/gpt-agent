import json

def write_file(file_name, content):
    sure = input(f"Do you want to write to {file_name} YES/NO")
    print(sure)
    if sure == "YES":
        with open(file_name, "w") as f:
            f.write(content)
        return f"Successfully written to file {file_name}"
    else:
        return "ERROR: You are not allowed to this file"

def get_jokes(number_of_jokes):
    return json.dumps([
        "Why don't scientists trust atoms? Because they make up everything!", 
        "Did you hear about the mathematician who's afraid of negative numbers? He'll stop at nothing to avoid them!", 
        "Why don't skeletons fight each other? They do not have the guts!"])

definitions = [
        {
            "name": "get_jokes",
            "description": "Gets jokes from the joke database",
            "parameters": {
                "type": "object",
                "properties": {
                    "number_of_jokes": {
                        "types": "number",
                        "description": "Get the specified number of jokes"
                    }
                }
            },
            "required": ["number_of_jokes"]
        },
        {
            "name": "write_file",
            "description": "Writes content to a file",
            "parameters": {
                "type": "object",
                "properties": {
                    "file_name": {
                        "types": "string",
                        "description": "File name to write to"
                    },
                    "content": {
                        "types": "string",
                        "description": "Content to write to file"
                    },
                }
            },
            "required": ["file_name", "content"]
        }
    ]

