import openai
import turtle


def drawTextBox(turtle, x_increment, y_increment):
    turtle.penup()
    turtle.goto(turtle.xcor()+x_increment, turtle.ycor()+y_increment)
    turtle.fillcolor("white")
    turtle.begin_fill()
    turtle.ht()
    for _ in range(4):
        turtle.right(90)
        turtle.forward(150)
    turtle.end_fill()

def writeInTextBox(turtle, message, xcor, ycor):
    turtle.ht()
    turtle.penup()
    turtle.clear()
    turtle.goto(xcor, ycor)
    turtle.write(message)
       


openai.api_key = 'Your API Key'
request = [{'role':'system', 'content': 'You are bugs bunny.'}]
wn = turtle.Screen()
wn.bgpic('bgimage.gif')
wn.addshape('bugs.gif') #picture of bugs bunny from https://www.animatedimages.org/cat-bugs-bunny-1026.htm

bugs = turtle.Turtle()
bugs.shape('bugs.gif')
bugs.penup()
bugs.goto(bugs.xcor()-10, bugs.ycor()+15)

textBox1 = turtle.Turtle()
drawTextBox(textBox1, 150, 200)
text = turtle.Turtle()

openingSequence = [
    "Eh... what's up doc?", 
    "I am Tani's favourite cartoon!", 
    "A young Tani always \nwanted to talk to me",
    "Go to the console \n and ask me a question"
]

for message in openingSequence:
    wn.ontimer(writeInTextBox(text, message, 10, 150), 3000)

user_question = input("Ask bugs a question: ")
request.append({'role': 'user', 'content': 'Pretend you are bugs bunny '+user_question+ ' Answer in 10 words or less per sentence.'})
chat = openai.ChatCompletion.create(
    model = 'gpt-3.5-turbo', 
    messages = request
)
answer = chat.choices[0].message.content
print(answer)
answer_list = answer.split('.')
for message in answer_list:
    wn.ontimer(writeInTextBox(text, message, 10, 150), 3000)
wn.mainloop()

  