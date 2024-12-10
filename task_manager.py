class TaskManager:
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
    def view_tasks(self):
        for task in self.tasks:
            the_title = task["title"]
            the_priority = task["priority"]
            the_status = task["status"]
            print(f"{the_title} (Priority: {the_priority}, Status: {the_status})")
    def search_task(title):
        pass