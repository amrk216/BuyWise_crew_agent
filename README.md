






The generated project has the following structure. The starter embedded crew uses the classic Python/YAML layout, and in Step 4 we will replace the content crew with a JSONC crew.

ai-agent-project/
├── .gitignore
├── requirements.txt
├── README.md
├── .env
└── src/
    └── BuyWise_agent/
        ├── __init__.py
        ├── main.py
        ├── crews/
        │   └── buywise_crew/
        │       ├── config/
        │       │   ├── agents.py
        │       │   └── tasks.py
        │       └── buywise_crew.py
        └── tools/
            └── custom_tool.py


            PYTHONPATH=src python -m BuyWise_agent.crews.buywise_crew.buywise_crew