class Category:
  def __init__(self, category): 
        self.accumulator =[]
        self.amount=0
        self.category = category 


  def check_funds(self,amount):
    if self.amount< amount:
      return False
    else:
      return True


  def deposit(self,amount, description=""):
    self.accumulator.append({"amount":amount,"description":description})
    self.amount += amount


  def withdraw(self,amount,description=""):
    if self.check_funds(amount) ==True:
      self.amount -=amount
      self.accumulator.append({"amount":-amount,"description":description})
      return True
    else:
      return False

  # return balanace of budget 
  def get_balance(self):
    return self.amount

  def __str__(self):
    result=""
    result+="*************Food*************"+"\n"
    for transaction in self.accumulator:
      amount=0
      description=""
      for key,value in transaction.items():
          if key=="amount":
            amount = value
          elif key=="description":
            description=value
      if len(description)>23:
        description=description[:23]
      amount = str(format(float(amount),'.2f'))
      if len(amount)>7:
        amount= amount[:7] 
      result+= description + str(amount).rjust(30-len(description))+"\n"
    result+="Total: "+str(format(float(self.amount),'.2f'))
    return result



  def transfer(self,amount,category):
    if self.check_funds(amount)==True:
      self.amount-=amount
      self.accumulator.append({"amount": -amount,"description":"Transfer to "+category.category})
      category.accumulator.append({"amount": amount,"description": "Transfer from "+self.category})
      return True
    else:
      return False


food = Category("Food")
food.deposit(100, "initial deposit")
food.withdraw(10, "groceries")
food.withdraw(15, "restaurant and more food for dessert")
print(food.get_balance())
clothing = Category("Clothing")
food.transfer(50, clothing)
clothing.withdraw(20)
clothing.withdraw(100)
auto = Category("Auto")
auto.deposit(1000, "initial deposit")
auto.withdraw(15)

print(food)
print(clothing)
