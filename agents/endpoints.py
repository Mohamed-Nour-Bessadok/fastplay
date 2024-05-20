from utils import extract_competition_results
from fastapi import FastAPI
import requests

app = FastAPI()


@app.get("/parse_departmental_awards/{input}")
def parse_departmental_awards(input: str):
    """Parses the departmental awards section to extract rankings."""
    
    section = extract_competition_results("./docs/competition_result.txt", "2. Awaited competition results:", "Individual Achievements:")
    lines = section.split('\n')
    awards = {}

    for line in lines:
        if "1st Place - " in line:
            awards["1st Place"] = line.split("1st Place - ")[1].strip(":")
        elif "2nd Place - " in line:
            awards["2nd Place"] = line.split("2nd Place - ")[1].strip(":")
        elif "3rd Place - " in line:
            awards["3rd Place"] = line.split("3rd Place - ")[1].strip(":")

    if input in ["1st Place", "2nd Place", "3rd Place"]:
        return awards[input]
    else:
        None

@app.get("/parse_employee_awards/{input}")
def parse_employee_awards(input: str):
    """Parses the employee awards section to extract rankings."""
    section = extract_competition_results("./docs/competition_result.txt","Individual Achievements:", "Conclusion:")

    lines = section.split('\n')
    awards = {}

    for line in lines:
        if "1st Place - " in line:
            awards["1st Place"] = line.split("1st Place - ")[1].strip(":")
        elif "2nd Place - " in line:
            awards["2nd Place"] = line.split("2nd Place - ")[1].strip(":")
        elif "3rd Place - " in line:
            awards["3rd Place"] = line.split("3rd Place - ")[1].strip(":")

    if input in ["1st Place", "2nd Place", "3rd Place"]:
        return awards[input]
    else:
        None


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)