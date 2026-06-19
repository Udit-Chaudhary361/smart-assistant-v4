from storage import load_data , save_data
from logger import logger

class Assistant:
    def set_name(self ,name):
        self.name = name
        data = load_data()
        data["name"] = self.name
        save_data(data)
        logger(f"Set Name - {name}")

    def get_name(self):
        data = load_data()
        logger("Viewed Name")
        return data["name"]

    def add_note(self , note):
        self.note = note
        data = load_data()
        data["notes"].append(self.note) 
        save_data(data)
        logger(f"Added Note - {note}")

    def view_notes(self):
        data = load_data()
        notes = data["notes"]
        output = ""
        for note in notes:
            output+=f"- {note}\n"
        logger("Viewed Notes")
        return output.strip()


    def add_task(self ,task):
        data = load_data()
        tsk = { "task" : task,
               "completed" : False}
        data["tasks"].append(tsk)
        save_data(data)
        logger(f"Added Task - {task}")

    def view_tasks(self):
        data = load_data()
        output = ""
        tasks = data["tasks"]
        for i , task in enumerate(tasks , start=1):
            if task["completed"]:
                tick = "[✓]"
            else:
                tick = "[ ]"
            output += f"{i}. {task['task']}  {tick}\n"
        logger("Viewed Tasks")
        return output.strip()
    def history_viewer(self):
        try:
            with open("History.txt", "r") as f:
                return f.read().strip()
        except FileNotFoundError:
            return "No history found."

    def delete_note(self , dele):
        data = load_data()
        if dele < 1 or dele > len(data["notes"]):
            print("Invalid Note Number!")
        else:
            data["notes"].pop(dele-1)
            save_data(data)
            logger(f"Deleted Note")
        

    def complete_task(self , comp):
        data = load_data()
        tasks = data["tasks"]
        if comp < 1 or comp > len(tasks):
            print("Invalid Task Number!")
            return
        tasks[comp-1]["completed"] = True
        save_data(data)
        logger("Task Completed") 

    def delete_task(self , tsk):
        data = load_data()
        if tsk < 1 or tsk > len(data["tasks"]):
            print("Invalid Task Number!")
        else:
            data["tasks"].pop(tsk-1)
            save_data(data)
            logger(f"Deleted Task")

    def task_stats(self):
        data = load_data()
        tasks = data["tasks"]
        total = len(tasks)
        completed = 0
        for task in tasks:
            if task["completed"]:
                completed += 1
        pending = total - completed
        output = (
            f"===== TASK STATS =====\n"
            f"Total Tasks: {total}\n"
            f"Completed Tasks: {completed}\n"
            f"Pending Tasks: {pending}"
        )
        logger("Viewed Task Stats")
        return output