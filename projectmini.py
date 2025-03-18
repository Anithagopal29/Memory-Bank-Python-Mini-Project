from datetime import datetime
class memory_bank:
    def __init__(self):
        self.memories=[]

    def adding_memory(self):
        stop = True
        while stop:
            ask = input("Do You Want to Add Memory ?\n  Type \"YES\" To Add Memory Else Type \"NO\": ").lower()
            if ask == "yes":
                date=(input("Enter a date (YYYY-MM-DD):"))
                try:
                   datetime.strptime(date, "%Y-%m-%d")
                except ValueError:
                   print("Invalid date format. Please try again.")
                   return
                title=input("Enter the memory title: ")
                description = input("Enter the memory description: ")
                category = input("Enter a category like (TRAVEL OR ANY OTHER): ")
                memory_add = {
                      "date": date,
                      "title": title,
                      "description": description,
                      "category": category,
                   }
                self.memories.append(memory_add)

                print(f"Memory '{title}' added successfully!")


            else:
                stop=False
    def view_memory(self):
        if not self.memories:
            print("No memories to display.")
            return
        else:
            print("----\"ALL MEMORIES SAVED IN MEMORY BANK\"----")
            for event in self.memories:
                print(f"Date: {event['date']}")
                print(f"Title: {event['title']}")
                print(f"Description: {event['description']}")
                print(f"Category: {event['category']}")
                print("----------------")
    def delete_memory(self):
        title = input("Enter the title of the memory to delete: ")
        for topic in self.memories:
            if topic['title'].lower() == title.lower():
                self.memories.remove(topic)
                print(f"Memory titled '{title}' deleted successfully!")
                return
        print(f"No memory found with the title '{title}'.")
    def search_memory(self):
        a=input("Search Using \"DATE\" or \"TITLE\":").lower()
        if a=="date":
            Date=input("Enter a Date to Search (YYYY-MM-DD):")
            try:
                datetime.strptime(Date, "%Y-%m-%d")
            except ValueError:
                print("Invalid date format. Please try again.")
                return
            results=[]
            for memory in self.memories:
                if memory['date']==Date:
                    results.append(memory)
            if results:
                print("\nSearch Results:")
                for memory in results:
                    print(f"Title: {memory['title']}")
                    print(f"Description: {memory['description']}")
                    print(f"Category: {memory['category']}")
                    print("----------------")
            else:
                print(f"No memories found matching '{Date}'.")
        elif a=="title":
            title=input("Enter a Title to Search:").lower()
            results=[]
            for memory in self.memories:
                if memory['title'].lower() == title:
                    results.append(memory)
            if results:
                print("\nSearch Results:")
                for memory in results:
                    print(f"Date: {memory['date']}")
                    print(f"Description: {memory['description']}")
                    print(f"Category: {memory['category']}")
                    print("----------------")
            else:
                print(f"No memories found matching '{title}'.")
        else:
            print("Invalid search option. Please use 'DATE' or 'TITLE'.")
def main():
    memory = memory_bank()
    while True:
        print("\nMemory Bank Menu")
        print("1. Add Your Beautiful Memory")
        print("2. View Your Beautiful Memories")
        print("3. Delete Your Unwanted Memory")
        print("4. Search Your Favourite Memories")
        print("5. Exit")
        choice = input("Choose an option: ")
        if choice=="1":
            memory.adding_memory()
        elif choice=="2":
            memory.view_memory()
        elif choice=="3":
            memory.delete_memory()
        elif choice=="4":
            memory.search_memory()
        elif choice=="5":
            print("Bye Bye!!!")
            break
        else:
            print("Invalid choice. Please try again.")
main()

