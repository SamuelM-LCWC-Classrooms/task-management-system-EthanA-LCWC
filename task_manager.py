class Task_manager:
    def __init__(self) -> None:
        self.tasks = []
    def add_task(self, title, description, priority):
        self.status = "Incomplete"
        self.tasks.append({
            "title": title,
            "description": description,
            "priority": priority,
            "status": self.status
        })
    def remove_task(self, title_to_find):
        found_task = False
        for task in self.tasks:
            if task["title"] == title_to_find:
                self.tasks.remove(task)
                found_task = True
                break
        if found_task == False:
            print("AAAAA")
            print("ERROR: This task does not exist")
    def mark_complete(self, title_to_find):
        found_task = False
        number_of_task = 0
        for task in self.tasks:
            if task["title"] == title_to_find:
                new_task = task
                new_task["status"] = "Complete"
                self.tasks[number_of_task] = new_task
                found_task = True
                break
            number_of_task += 1
        if found_task == False:
            print("ERROR: This task does not exist")
    def view_tasks(self, sort_by="priority"):
        for task in self.tasks:
            the_title = task["title"]
            the_priority = task["priority"]
            the_status = task["status"]
            print(f"{the_title} (Priority: {the_priority}, Status: {the_status})")
    def search_tasks(self, title):
        pass

'''
manager = Task_manager()

manager.add_task("Buy groceries", "Milk, eggs, bread", 2)
manager.add_task("Clean room", "Tidy up and vacuum", 3)
manager.add_task("Finish Project", "Complete Python assignment", 1)

print(manager.view_tasks())
# [{'title': 'Finish Project', 'description': 'Complete Python assignment', 'priority': 1, 'status': 'Incomplete'}, {'title': 'Buy groceries', 'description': 'Milk, eggs, bread', 'priority': 2, 'status': 'Incomplete'}, {'title': 'Clean room', 'description': 'Tidy up and vacuum', 'priority': 3, 'status': 'Incomplete'}]   

manager.mark_complete("Buy Groceries")
print(manager.view_tasks())
# [{'title': 'Finish Project', 'description': 'Complete Python assignment', 'priority': 1, 'status': 'Incomplete'}, {'title': 'Buy groceries', 'description': 'Milk, eggs, bread', 'priority': 2, 'status': 'Incomplete'}, {'title': 'Clean room', 'description': 'Tidy up and vacuum', 'priority': 3, 'status': 'Incomplete'}]

print(manager.search_tasks("Clean room"))

# Title: Clean room
# Description: Tidy up and vacuum
# Priority: 3
# Status: Incomplete

manager.remove_task("Clean room")

print(manager.view_tasks())
# [{'title': 'Finish Project', 'description': 'Complete Python assignment', 'priority': 1, 'status': 'Incomplete'}, {'title': 'Buy groceries', 'description': 'Milk, eggs, bread', 'priority': 2, 'status': 'Incomplete'}]

print(manager.search_tasks("Clean room"))
# No task found with title Clean room
'''