from model.budget import Budget

class Budget_Ctrl:
    def __init__(self) -> None:
        self.budgets = []
    
    def create_budget(self, budget_title, budget_total_price, budget_products, budget_services):
        self.budget = Budget(budget_title, budget_total_price, budget_products, budget_services)
        self.budgets.append(self.budget)

    def update_budget(self, index, datatype, data):
        if datatype == "Name":
            self.budgets[index].set_name(data)
        elif datatype == "Email":
            self.budgets[index].set_email(data)
        else:
            print("Error")
        return self.budgets

    def delete_budget(self, id):
        del self.budgets[id]
        return self.budgets