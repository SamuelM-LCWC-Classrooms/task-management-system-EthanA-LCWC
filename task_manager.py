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
            return f"No item in list with the title: {title_to_find}"
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
        task_list = []
        for task in self.tasks:
            task_list.append(task)
        if sort_by == "priority":
            priority = lambda x : x["priority"]
            task_list.sort(key=priority)
        elif sort_by == "status":
            status = lambda x : x["status"]
            task_list.sort(key=status)
        return task_list
    def search_tasks(self, title):
        for task in self.tasks:
            if task["title"] == title:
                return task
        return f"No item in list with the title {title}"
