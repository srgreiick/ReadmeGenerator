print("---------------------Good morning, let's make a readme---------------------")
import os
import inquirer


questions = [
    inquirer.Text("user", message="Please enter your github username", validate=lambda _, x: x != ".")
]
answers = inquirer.prompt(questions)


print(answers)
print(answers["user"])

readmeContent = (
  f'''asdf
  {answers["user"]}
  ASdf'''
)
print(readmeContent)

if os.path.exists("README.md"):
  os.remove("README.md")
else:
  print("The file does not exist")
readme = open("README.md", "x")

readme.write(f"{readmeContent}")